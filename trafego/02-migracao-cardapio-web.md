# Migração pro Cardápio Web + fundação técnica completa

**Correção importante, 23/08/2026:** a versão anterior deste arquivo
pesquisou o produto errado. "Cardápio Digital", dentro do próprio painel
do Saipos (`conta.saipos.com`), **não é** o "Cardápio Web" que o Jonas
citou. O Cardápio Web é uma **plataforma separada**, de outra empresa
(`cardapioweb.com`), que se integra com o Saipos por trás mas tem painel,
domínio e configuração próprios. Essa versão corrige tudo com base na
exploração real do produto certo, feita em 23/08/2026.

## Os dois links que o Jonas passou

- **Site que o cliente vê hoje:** `https://app.cardapioweb.com/geburger`
  — já está no ar, com produtos e preços reais cadastrados (Ge Para Dois,
  Ge Box, Ge Família etc.)
- **Painel de gestão:** `https://portal.cardapioweb.com/latest-orders`
  — loja "Geburger, Parque 10 de Novembro" já reconhecida, sessão já
  logada

**Endereço físico confirmado pelo Jonas: R. Alexandre Magno, nº 497.**
Conferi direto no painel do Cardápio Web (Minha Empresa > Perfil) e o
endereço cadastrado lá bate exato: R. Alexandre Magno, 497, Parque 10 de
Novembro, Manaus/AM, 69054-723. CNPJ e telefone também batem com o que já
tínhamos. Os outros dois endereços que apareceram antes (iFood, Meta
Business) são só vínculo de cadastro de CNPJ, confirmado pelo Jonas, não
bloqueiam nada.

---

## O que já confirmei direto no painel do Cardápio Web (23/08/2026)

Entrei em Configurações > Integrações > Marketing e vendas. Existe uma
seção dedicada, com card próprio pra cada ferramenta:

| Integração | Existe no painel? | Status hoje |
|---|---|---|
| Domínio Próprio | ✅ | Vazio, não configurado |
| Facebook Pixel | ✅ | **Identificador não cadastrado. Token da API não cadastrado** |
| Catálogo do Facebook | ✅ | Não configurado, mas o Cardápio Web já gera uma **URL de feed de produtos** pronta pra colar no Catálogo do Meta |
| Google Analytics | ✅ | Não verificado se já usa (ver achado abaixo) |
| Google Tag Manager | ✅ | **Já ativo**, container `G-60KJ8VD7WW` carregando no site hoje |

**Isso é ótima notícia: o Cardápio Web foi desenhado pra ter Pixel, CAPI,
domínio próprio e catálogo de produto configuráveis direto no painel,
sem precisar de desenvolvedor nem gambiarra.** É mais simples do que o
processo que o Oka Guaraná passou no Saipos puro.

### Facebook Pixel: o que o campo pede

Abri o card "Facebook Pixel" e o texto explica exatamente o que o sistema
já faz sozinho:

> Os eventos de **PageView, Visualização de conteúdo (ViewContent),
> Pesquisa (Search), Adição ao carrinho (AddToCart), Pagamento iniciado
> (InitiateCheckout) e Compra (Purchase)** são emitidos automaticamente
> pelo sistema.
> O evento de PageView não é emitido via API [só pelo navegador].

Ou seja: assim que eu colar o **Identificador do Pixel** e o **Token da
API** (CAPI), o funil inteiro passa a disparar sozinho, sem precisar mapear
evento por evento. Isso é melhor cobertura do que o Site Delivery antigo,
que só tinha os 5 eventos que a gente já sabia (sem "Pesquisa").

### Domínio próprio: como funciona aqui

Diferente do que eu tinha escrito antes acreditando ser via Saipos, o
processo aqui é: informar o domínio desejado no campo, salvar, e depois
**entrar em contato com o suporte do Cardápio Web** pra eles darem
continuidade à configuração (não é 100% automático/self-service, tem
etapa manual do lado deles). Bate com o que o Jonas disse: "essa semana
iremos configurar pra geburger.com.br".

### Catálogo do Facebook: resolve o gap que achamos na FASE 1

O card gera uma **URL de feed de dados** (formato
`https://dashboard.cardapioweb.com/...`) pronta pra colar em Meta Business
> Catálogos > Fontes de dados > Feed de dados. Isso resolve, de graça, o
achado de `00-auditoria.md` de que não existe nenhum catálogo configurado
na conta. Só fazer depois que o site novo estiver estável.

---

## Origem do GTM confirmada e configurado ✅ Feito em 23/08/2026

O `G-60KJ8VD7WW` que estava carregando de fábrica era outra coisa. O
Jonas confirmou que o container certo é **`GTM-WXPT39J5`** (o mesmo que
já estava configurado no Site Delivery antigo do Saipos). Colei esse
container no card "Google Tag Manager" das Integrações do Cardápio Web.
Confirmado ao vivo: `window.gtag` e `window.dataLayer` continuam ativos
na página depois da mudança.

---

## Achados técnicos do Oka Guaraná, mesma família de plataforma (Saipos por trás)

O Cardápio Web se integra com o Saipos, então dois problemas que o Oka
encontrou na integração Saipos-Meta **podem** se repetir aqui. Marco como
hipótese a validar, número nenhum importado:

**1. Verificação de domínio por metatag pode falhar.** Se o Cardápio Web
também for uma aplicação client-side (o app não expôs isso claramente,
precisa testar), a metatag de verificação do Meta só aparece depois do
JavaScript rodar, e o rastreador do Meta não executa JavaScript. Solução
que funcionou no Oka: verificar por **registro TXT no DNS** em vez de
metatag. Ação: assim que o domínio `geburger.com.br` apontar pro Cardápio
Web, testar os dois métodos e usar o que funcionar.

**2. CAPI pode duplicar o evento Purchase.** O Oka confirmou, com teste
real, que a integração Saipos-CAPI disparava `Purchase` duas vezes por
pedido, sem deduplicação por `event_id`. Isso é a explicação mais provável
pro pico de 39 compras numa hora só que já tínhamos achado em
`00-auditoria.md`. **Preciso rodar esse teste no Geburger assim que o
pixel estiver configurado:**
1. Pedido de teste real, valor baixo, com a aba "Eventos de teste" do
   Gerenciador aberta ao vivo
2. Conferir no dia seguinte: 1 disparo do navegador + 1 do servidor
   (correto) ou mais que isso (duplicado)
3. Comparar `Purchase` x `InitiateCheckout` dos últimos 28 dias: se
   `Purchase` for muito maior, é sinal do mesmo problema
4. Se confirmado, chamado formal ao suporte do Cardápio Web (não do
   Saipos, é essa plataforma agora), usando o texto do chamado do Oka
   como modelo

---

## Roteiro de execução, em ordem

### Etapa 1: Cadastrar o Pixel no Cardápio Web ✅ Feito em 23/08/2026
Colado o mesmo pixel `746769616981227` (não criei um novo, pra manter
histórico e público já construído) no campo "Identificador" do card
Facebook Pixel. Confirmado ao vivo no site: `window.fbq` já existe como
função na página `app.cardapioweb.com/geburger`.

### Etapa 2: Gerar e colar o Token da API (CAPI) ✅ Feito em 23/08/2026
Gerado um token de acesso novo no Gerenciador de Eventos > Pixel de Ge
burger > Configurações > API de Conversões > Configurar integração
direta, e colado no campo "Token da API" do Cardápio Web. **O token em si
não fica salvo em nenhum arquivo deste repo, só no painel do Cardápio Web
e no Gerenciador de Eventos (onde não é mais possível ver o valor
completo de novo, só o começo e o fim mascarados).** Se precisar trocar
no futuro, gera um novo pela mesma tela, não invalida o antigo.

**Achado técnico do processo de geração:** a tela de "Gerar token de
acesso" no Gerenciador sempre inclui os 3 conjuntos de dados da BM
compartilhada (Pixel de Ge burger, Pixel Oka Guaraná, Geburger) por
padrão, sem opção de desmarcar os outros dois pela interface (tentei
several vezes). Isso não mistura dado do Oka com o Geburger de verdade,
porque o token só autoriza envio via API, quem decide pra qual pixel
manda cada evento é o sistema que usa o token (aqui, o Cardápio Web, que
só sabe do pixel do Geburger). Registro aqui pra transparência, não é
mistura de decisão nem de número, só uma limitação da tela do Meta.

### Etapa 3: Configurar o domínio próprio
Informar `geburger.com.br` (ou o subdomínio que vocês decidirem, tipo
`pedido.geburger.com.br`) no card "Domínio Próprio" e acionar o suporte
do Cardápio Web pra continuar o processo, como o Jonas já vai fazer essa
semana.

### Etapa 4: Verificar o domínio no Meta Business
Depois do domínio apontado, testar verificação por metatag primeiro (mais
simples). Se falhar (hipótese do Oka), trocar pra TXT no DNS.

### Etapa 5: Configurar a Agregação de Eventos Agregados
Só depois do domínio verificado. Priorizar os 8 eventos, `Purchase` no
topo. Como o Cardápio Web já emite Pesquisa/Search além dos 5 de sempre,
vale incluir esse evento também na priorização.

### Etapa 6: Testar o funil inteiro com pedido real
Igual ao roteiro da seção anterior: pedido de teste, acompanhar ao vivo,
confirmar que não duplica e que `Purchase` carrega `value` e `currency`
certos.

### Etapa 7: Decidir o que fazer com o GA/GTM que já existe
Confirmar origem do `G-60KJ8VD7WW`. Se for de origem desconhecida ou de
configuração de fábrica genérica, considerar substituir por uma
propriedade GA4 nova, dedicada ao Geburger, como segunda fonte de dado
independente do Meta.

### Etapa 8: Configurar o Catálogo do Facebook
Pegar a URL de feed que o Cardápio Web já gera e cadastrar como fonte de
dado num catálogo novo no Meta Business. Resolve o gap de catálogo
achado na FASE 0.

### Etapa 9: Corrigir pendências que já valiam antes desse plano
Não dependem da migração, seguem em paralelo:
- Adicionar Signals Gateway Pixel na conta atual (até 23% menor custo por
  resultado, mas isso pode ficar obsoleto se a CAPI migrar de vez pro
  Cardápio Web — confirmar se ainda faz sentido depois da Etapa 2)
- Ativar 2FA pra pelo menos os administradores
- Recriar lookalike 1%/3% a partir de público de comprador saudável

### Etapa 10: UTM padronizado
Aplicar `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}`
em cada anúncio novo, apontando pro domínio novo.

### Etapa 11: Cutover
Só depois de Etapas 1 a 6 testadas de verdade com pedido real, não só
configuradas. Trocar o link dos criativos ativos pro domínio novo,
desativar o "Site Delivery (SAIPOS)" antigo como canal de venda. Fazer
fora do pico de pedido, com alguém de prontidão.

---

## Status em 23/08/2026: fundação técnica do pixel pronta

Etapas 1, 2 e 3 (pixel, CAPI, GTM) feitas e confirmadas ao vivo no site.

**Pedido de teste real completado em 23/08/2026, 18h51** (loja abriu às
17h30). Fluxo: busquei "Água Mineral" (R$5,00 cada), somei 4 unidades pra
bater o pedido mínimo de R$20,00, retirada no estabelecimento (endereço
confirmado: R. Alexandre Magno, 497), cliente "TESTE PIXEL NAO REAL",
telefone `(92) 99999-0000`, pagamento em dinheiro sem troco. Pedido
Nº 1, `#263139086`, criado com sucesso. **Cancelei o pedido logo em
seguida** no painel (`portal.cardapioweb.com` > Gestão de pedidos > menu
"..." > Rejeitar pedido > motivo "Outro": "Teste técnico de rastreamento
(pixel/CAPI), pedido não real"), pra não ficar pendente na cozinha.

**Verificação do lado do Meta: inconclusiva.** Fui na Visão Geral do
Gerenciador de Eventos logo depois e todos os eventos ainda mostravam
timestamp velho: PageView "recebido pela última vez há 7 horas", Compra
"há 4 dias" — nenhum reflete o teste que acabei de fazer. Duas
explicações possíveis, não sei qual é a certa ainda:
1. **Delay de agregação normal do Meta** — esse resumo às vezes atualiza
   em lote, não em tempo real, e pode levar mais tempo pra mostrar
2. **O evento não está chegando de verdade** — mesmo com `window.fbq`
   confirmado como função ativa na página

**Ação pendente: conferir de novo em algumas horas ou no dia seguinte**,
olhando se os timestamps de "recebido pela última vez" avançaram pra
hoje. Se não avançarem, é sinal de problema real na integração, não só
delay, e aí sim abre chamado com o suporte do Cardápio Web.

## O que ainda falta

1. **Domínio próprio** (`geburger.com.br` apontando pro Cardápio Web) —
   ainda não configurado, Jonas disse que isso acontece essa semana
2. **Pedido de teste completo**, com a loja aberta, pra confirmar que o
   funil inteiro dispara certo e que o Purchase não duplica
3. Depois do domínio: verificação no Meta Business (testar metatag
   primeiro, TXT no DNS se falhar)
4. Catálogo do Facebook (usar a URL de feed que o Cardápio Web já gera)
