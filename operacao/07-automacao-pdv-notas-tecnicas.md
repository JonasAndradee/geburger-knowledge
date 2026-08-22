# 07, Automação do Saipos, notas técnicas

**Versão 1, 22/08/2026.** Descoberto na sessão de levantamento completo da
loja Ge Burger (62061), operando o Saipos pela extensão Claude in Chrome.

Leia isto **antes** de mandar qualquer agente ler ou escrever no Saipos.

---

## Regra zero

**Automação lê à vontade, escreve com cuidado.** Igual ao Oka Guaraná: ler é
livre, qualquer coisa que grava exige confirmação explícita antes.

---

## O ambiente

- URL base: `https://conta.saipos.com`
- Admin em **AngularJS**, rotas com hash: `#/app/store/ingredient`,
  `#/app/store/category-financial`, `#/app/report/dre`
- O cardápio é **React**, em `#/app/v2/cardapio`, mas roda dentro do mesmo
  shell Angular. O `angular.element(document.body).injector()` continua
  funcionando mesmo nessa tela
- Login pede autenticação de dois fatores por e-mail, e permite só uma
  sessão por usuário. Logar de um computador novo pede pra desconectar a
  sessão antiga, o que pode derrubar alguém da equipe no meio do
  atendimento. Confirmar com o Jonas antes de desconectar

## Puxar dado em lote: o `$http` interno do Angular

`fetch()` direto do console dá 401, mesmo com `credentials: 'include'`. A
API exige um header de autorização que o `fetch` cru não carrega. A saída é
usar o próprio serviço `$http` do Angular, que já está autenticado:

```js
const injector = angular.element(document.body).injector();
const $http = injector.get('$http');
const r = await $http.get('https://api.saipos.com/v1/stores/62061/ingredients', {params:{limit:500, offset:0}});
r.data // array completo, sem paginação de tela
```

Confirmado funcionando para `ingredients`, `items` (cardápio), e
`store_fin_transactions/find-transactions` (lançamentos financeiros).
Provavelmente funciona pra qualquer endpoint que a tela usa, só trocar o
path.

**Não funciona sempre:** chamar um método de `factory` do controller da
página (ex: `vm.factory.findIngredientToEdit(id)`) trava sem nunca resolver
nem rejeitar, porque a Promise do `$q` do Angular depende de um ciclo de
digest que não roda fora do fluxo normal de evento. `$http.get` direto
funciona porque o XHR dispara o digest sozinho; chamar uma função do
controller não. Se travar assim, não insista tentando `$rootScope.$apply()`
por fora: é mais rápido navegar pra tela de edição do item e ler o dado já
carregado direto do scope (próxima seção).

## Ler dado já carregado: escopo Angular do controller

Pra fichas técnicas (a composição, não só o cadastro do item), o jeito mais
confiável é abrir a tela de edição da ficha e ler o scope depois que a
página carrega:

```js
let target = null;
document.querySelectorAll('*').forEach(el => {
  if (target) return;
  try {
    const s = angular.element(el).scope();
    if (s && s.vm && s.vm.record && s.vm.record.id_store_ingredient) target = s.vm;
  } catch(e) {}
});
target.record.children // array de {id_store_ingred_child, input_child, qtt_consumption, variations}
```

URL da tela: `#/app/store/datasheet-record/edit/{id}/datasheet`. Repita
navegação + leitura pra cada ficha. Em lote (`browser_batch`), navegar e ler
69 fichas (53 produto final + 16 beneficiado) levou 7 lotes de ~10 cada, uns
1,2s de espera entre navegação e leitura por item.

**Achado sobre composição:** cada linha de ingrediente pode ter
`qtt_consumption` na base (às vezes 0) e um array `variations`, uma por
tamanho/variação do produto no cardápio, cada uma com seu próprio
`qtt_consumption`. Ou seja, a mesma ficha pode servir vários produtos do
cardápio com quantidade diferente. Não assumir que o `qtt_consumption` de
topo é a receita real, sempre olhar as `variations`.

## Tirar dado grande de dentro do navegador: limite de tamanho do retorno

O retorno de `javascript_tool` corta em torno de 1.000 a 2.000 caracteres
quando o conteúdo não é texto legível continuo, e strings muito repetitivas
(tipo `'x'.repeat(5000)`) são bloqueadas como se fossem dado codificado.
`Blob` + link de download **não funciona**: automação via CDP não dispara
download real, mesmo simulando clique de mouse de verdade nas coordenadas
do link.

O que funciona: escrever o dado como texto de um elemento `<pre>` no
`document.body` e ler com a ferramenta `get_page_text`, que tem um teto
de 50.000 caracteres por chamada mas devolve o conteúdo integral até esse
teto (e quando o total passa de ~50KB, salva automaticamente num arquivo em
vez de cortar no meio da tela).

```js
document.body.innerHTML = '<pre id="d"></pre>';
document.getElementById('d').textContent = window.__meuDadoGrande;
```

Pra dado maior que 50.000 caracteres, fatiar em pedaços de até 49.999 e
chamar `get_page_text` de novo a cada fatia, sempre sobrescrevendo o
`textContent` do mesmo elemento antes de ler. Depois reconstituir os
pedaços fora do navegador (Python), na ordem certa.

**Cuidado:** sobrescrever `document.body.innerHTML` destrói a aplicação
Angular renderizada. Depois de usar esse truque, navegar pra
`https://conta.saipos.com/` (sem hash) e só então pra rota desejada, senão
a SPA não volta a renderizar (troca de hash sozinha não recarrega o app já
destruído).

## Categorias financeiras: API confirmada

Tela de categorias financeiras carrega a árvore inteira de uma vez no scope
do controller (`vm.categories`), sem paginação. A mesma árvore aparece
duplicada por caminho (a mesma categoria em mais de um ponto se ela é
referenciada por mais de um pai na estrutura de exibição), então ao
processar fora do navegador, deduplicar por `id_store_category_financial`
antes de montar a árvore final.

## Vendas por período: limite de 3 meses por consulta

O relatório `#/app/report/sales-by-period` recusa qualquer intervalo maior
que 3 meses com o erro "Por favor, selecione um período menor do que 3
mês(es) neste filtro". Pra cobrir um ano inteiro, são no mínimo 4 consultas
trimestrais. O campo de data é nativo (não aceita colar texto direto sempre),
mais confiável clicar no campo, usar as setas `<` `>` do calendário pra
mudar de mês, e clicar no dia.

## Protocolo para o agente

1. Antes de escrever qualquer coisa, leia e reporte o estado atual da tela
2. Prefira sempre `$http` direto a chamar função de controller
3. Se for extrair dado grande, use o truque do `<pre>` + `get_page_text`
   desde o início, não tente `JSON.stringify` gigante direto no retorno da
   ferramenta
4. Nunca tente forçar download de arquivo via `Blob`, não funciona neste
   ambiente
5. Depois de destruir o DOM pra extrair texto, sempre recarregue a página
   base antes de continuar navegando
