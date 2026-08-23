# 02, Plano de contas

**Versão 2, 23/08/2026.** Categorias vinculadas ao DRE na tela `DRE
Gerencial > Vincular` da loja Ge Burger (62061). Ver
`../decisoes/2026-08-23-vincular-categorias-ao-dre.md` para o critério
completo e `04-categorias-financeiras.md` para a árvore com cada vínculo.

## Seções do DRE

O Saipos oferece 7 seções vinculáveis. `Receita Operacional Bruta` e `CMV`
não aparecem na lista porque são automáticas (o sistema calcula direto,
não por vínculo de categoria).

| # | Seção |
|---|---|
| 1 | Impostos |
| 2 | Custo com vendas |
| 3 | Despesas administrativas |
| 4 | Despesas financeiras |
| 5 | Receita não operacional líquida |
| 6 | IR |
| 7 | Pró-labore |

## Tabela de vinculação

**Estado real em 23/08/2026: 61 das 100 categorias vinculadas.** As outras
39 ficam sem vínculo de propósito (compra de mercadoria que já vira CMV
automático, receita que já entra na Receita Operacional Bruta, movimento de
capital dos sócios, saldo patrimonial, e categoria-pai que cascatearia
seção errada pros filhos). Tabela completa de quem ficou sem vínculo e por
quê em `04-categorias-financeiras.md`, seção "Vinculação ao DRE".

Critério usado, mesmo padrão do Oka Guaraná:

| Seção do DRE | Recebe |
|---|---|
| 1, Impostos | `5.1.x` (Simples Nacional e o resto de impostos) |
| 2, Custo com vendas | Raiz `1 Custos Variáveis`, menos a subárvore de compra de mercadoria (`Fornecedores`); `Garçom` e `Despesas Financeiras (Taxas de cartão + Aluguel Máquinas)`, que apesar do nome são custo variável de venda |
| 3, Despesas administrativas | Raiz `2 Despesas Operacionais` inteira; raiz `4 Marketing e Crescimento`; `Consumo`, `Diferença de caixa` |
| 4, Despesas financeiras | Raiz `3 Despesas Administrativas` (serviço central, por convenção); `5.2.x` (despesa financeira real: tarifa, juros, empréstimo) |
| 5, Receita não operacional líquida | Nenhuma categoria hoje (`Saldo Inicial` fica de propósito sem vínculo, ver abaixo) |
| 6, IR | Nenhuma, não se usa no Simples Nacional |
| 7, Pró-labore | `6.1 Pró-labore` |

**Pegadinha de nome, mesma do Oka:** a categoria `Despesas Financeiras
(Taxas de cartão + Aluguel Máquinas)` não vai na seção "Despesas
financeiras". É taxa de cartão, custo variável de venda, vai em `2, Custo
com vendas`. A seção "Despesas financeiras" fica reservada pra raiz `3
Despesas Administrativas` mais a despesa financeira real do `5.2.x`.

## DRE Gerencial, snapshot de jun a ago/2026

Lido direto da tela em 23/08/2026, depois da vinculação:

| | Junho | Julho | Agosto (parcial) | Total |
|---|---|---|---|---|
| (+) Receita operacional bruta | R$ 41.550,40 | R$ 39.069,89 | R$ 32.594,89 | R$ 113.215,18 |
| (-) Impostos | R$ 341,12 | R$ 360,00 | R$ 0,00 | R$ 701,12 |
| (=) Receita líquida | R$ 41.209,28 | R$ 38.709,89 | R$ 32.594,89 | R$ 112.514,06 |
| (-) CMV | R$ 11.398,02 (27,66%) | R$ 11.192,26 (28,91%) | R$ 9.493,38 (29,13%) | R$ 32.083,66 (28,52%) |
| (-) Custo com vendas | R$ 3.004,18 (7,29%) | R$ 2.757,38 (7,12%) | R$ 943,51 (2,89%) | R$ 6.705,07 (5,96%) |
| (=) Lucro operacional bruto | R$ 26.807,08 (65,05%) | R$ 24.760,25 (63,96%) | R$ 22.158,00 (67,98%) | R$ 73.725,33 (65,53%) |
| (-) Despesas administrativas | R$ 20.506,61 (49,76%) | R$ 17.033,55 (44,00%) | -R$ 0,20 | R$ 37.539,96 (33,36%) |
| (-) Despesas financeiras | R$ 4.108,30 (9,97%) | R$ 3.326,58 (8,59%) | R$ 0,00 | R$ 7.434,88 (6,61%) |
| (=) Lucro operacional | R$ 2.192,17 (5,32%) | R$ 4.400,12 (11,37%) | R$ 22.158,20 (67,98%) | R$ 28.750,49 (25,55%) |
| (=) Lucro líquido do exercício | R$ 2.192,17 | R$ 4.400,12 | R$ 22.158,20 | R$ 28.750,49 |

**Isto já é o resultado real, com ressalva.** O lucro do trimestre caiu de
R$ 77.130,40 (quando só 6 categorias estavam vinculadas) pra R$ 28.750,49,
porque agora `Despesas administrativas` e `Custo com vendas` mostram o
gasto de verdade. A ressalva é agosto: `Despesas administrativas` aparece
quase zero no mês, o que não bate com junho/julho. Prováveis causas:
aluguel, salário e outras despesas fixas de agosto ainda não foram
lançadas no Saipos até a data de corte (22-23/08), não que o gasto não
existiu. Não fechar o resultado de agosto sem checar se falta lançamento.

## Categorias que ficam sem vínculo de propósito

Decisão tomada em 23/08/2026, mesmo critério do Oka Guaraná:

- `Fiado`, `Frente de Caixa`: já entram em `(+) Receita Operacional Bruta`
  automaticamente, vincular duplicaria
- `Fornecedores` e as 7 filhas (Insumos, Embalagens, Bebidas, Salgados,
  Congelados, Hortifruti, Descartáveis, Pão): CMV já é automático pelo
  estoque, vinculado o custo conta duas vezes
- `Saldo Inicial`: **mudou nesta versão.** Estava vinculado a `5, Receita
  não operacional líquida`, foi desvinculado pra bater com a recomendação
  do Oka: saldo de conta é foto patrimonial, não resultado do período.
  Vinculado, ele inflava o lucro do mês de corte
- `6.2 Distribuição de lucros`, `6.4 Aportes dos sócios`, `7.1.03 Venda de
  equipamentos usados`, `5.2.06 Empréstimos obtidos`: movimento de capital
  dos sócios, não é resultado da operação
- `5 Financeiro`, `6 Sócios e Capital`: categoria-pai vazia que mistura
  filhas de seções diferentes, não dá pra escolher uma seção só pra ela
- Categorias-pai/wrapper (`1.1 Custos de Venda`, `2.1 Equipe`, `7 Expansão
  e Investimentos`, e os wrappers antigos ainda sem código numérico):
  vincular categoria-pai no Saipos cascateia a seção pros filhos e trava a
  edição individual deles. Como a árvore ainda tem filho com código de uma
  raiz morando fisicamente em outra (gap da "Fase 1c", ver
  `04-categorias-financeiras.md`), vincular pelo pai erraria a seção de
  vários filhos. Lista completa na mesma seção do arquivo 04
