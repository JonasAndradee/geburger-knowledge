# operacao/ , Financeiro e operação Geburger

Instruções para qualquer agente ou pessoa trabalhando dentro desta pasta.

**Versão 1, 21/08/2026.** Estrutura criada vazia, espelhando o repositório
`oka-guarana`. Nada aqui foi levantado ainda: todo `[preencher]` é lacuna
conhecida.

---

## Contexto

Geburger, hamburgueria em Manaus. Unidades operando no PDV:

| Unidade | Papel | ID no PDV | CNPJ |
|---|---|---|---|
| [preencher] | matriz | [preencher] | [preencher] |

Regime tributário: [preencher]. Contabilidade: [preencher]. Gerente de
operação: [preencher].

Modelo de compras e estoque: [preencher, centralizado ou por unidade]

---

## Fonte de verdade

Os arquivos numerados desta pasta são a fonte de verdade. Consulte antes de
responder e não contradiga sem avisar explicitamente que está propondo mudança
de decisão.

| Arquivo | O que é |
|---|---|
| `01-manual-financeiro-geburger.md` | Estrutura decidida, baldes de gasto, CMV, DRE, rotinas |
| `02-plano-de-contas.md` | Seções do DRE e a tabela de vinculação |
| `03-processos-e-fluxos.md` | Como cada coisa entra no sistema e onde sai |
| `04-categorias-financeiras.md` | Árvore real de categorias e códigos |
| `05-guia-de-telas-pdv.md` | Caminhos de menu, campos e comportamento verificados |
| `06-estoque-ingredientes-e-fichas.md` | Ingredientes, custos, fichas técnicas dos lanches |
| `07-automacao-pdv-notas-tecnicas.md` | Como automatizar o sistema sem quebrar nada |
| `08-roadmap-implantacao.md` | Fases, onde estamos, o que falta |

Decisão que muda arquitetura vai em `../decisoes/`, usando o `TEMPLATE.md` de
lá. Aqui dentro só entra o estado atual, não o histórico da discussão.

---

## Os baldes de gasto

[preencher: classificação de gasto do Geburger. No Oka são 3 baldes, compra
local, despesa de rede e compra negociada em conjunto. Só replique aqui se o
modelo for de fato o mesmo, depois de confirmar com o Jonas.]

---

## Como o sistema separa as camadas

[preencher: critério que separa custo variável, custo de ponto, despesa
central e imposto. No Oka o critério é o código numérico da categoria.
Definir aqui depois de montar `04-categorias-financeiras.md`.]

---

## Regras invioláveis

Nunca dê orientação que quebre alguma destas.

[preencher a partir do que for confirmado na tela do PDV do Geburger.]

Candidatas herdadas do Oka Guaraná, que valem para qualquer operação de
alimentação com controle de estoque e ficha técnica. **Revalidar cada uma no
sistema do Geburger antes de tratar como regra desta casa:**

1. Compra sem nota também precisa de entrada manual de estoque, não só o
   lançamento da despesa
2. Categoria de nota de compra nunca vinculada a seção do DRE, senão o custo
   conta duas vezes
3. Insumo que compõe CMV precisa estar em ficha técnica, senão entra no
   estoque e nunca sai
4. Transferência entre contas bancárias não é receita nem despesa
5. Cupom e desconto são redutor de receita, não despesa de marketing
6. Taxa de marketplace e de maquininha são custo variável de venda, entram
   antes da margem de contribuição
7. Não se lê o DRE do mês antes de o saldo do fluxo de caixa bater com o
   extrato de cada banco
8. DRE usa data de emissão (competência). Fluxo de caixa usa data de pagamento
9. Produto de cardápio sem vínculo de ficha vende sem baixar estoque e o CMV
   mente sem dar sinal. O filtro de produtos sem vínculo tem que estar zerado

---

## Pontos ainda em aberto

Não trate como decidido. Se a pergunta depender de um destes, diga que está
pendente em vez de assumir uma resposta.

- Qual é o PDV e quais permissões estão liberadas nele
- Quantas unidades existem, com ID e CNPJ de cada uma
- Data de corte para início do controle
- Modelo de compras: cada unidade compra a sua ou existe compra central
- Quem faz a contagem física e com que frequência
- [preencher o resto conforme aparecer]

---

## Como responder

- Português brasileiro direto e casual. Sem construções formais, sem linguagem
  que soe a texto de IA
- **Nunca use travessão.** Use vírgula, dois-pontos ou reescreva a frase
- Não invente nome de tela, menu, campo ou relatório. Use o
  `05-guia-de-telas-pdv.md`. Se não estiver lá, diga que não está documentado
  antes de responder
- Sempre deixe claro a qual unidade a orientação se aplica quando isso mudar
  a resposta
- Questão fiscal e tributária é território do contador. Dê o quadro geral e
  diga o que perguntar, sem cravar resposta fiscal
- Prefira a solução mais simples que funciona hoje. Se propuser algo que
  aumente custo fixo ou trabalho recorrente, diga isso explicitamente e
  compare com a alternativa mais barata
- Aponte quando alguém estiver a ponto de quebrar uma das regras invioláveis,
  mesmo sem ter perguntado
- Não importe número do Oka Guaraná para cá. Modelo de raciocínio pode ser
  aproveitado, número não
