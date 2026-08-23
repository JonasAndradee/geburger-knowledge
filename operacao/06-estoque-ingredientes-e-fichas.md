# 06, Estoque, ingredientes e fichas técnicas

**Versão 1, 22/08/2026.** Levantado da tela `Ingredientes e Insumos` e
`Fichas técnicas` da loja Ge Burger (62061), via API do Saipos.

Fonte bruta: `dados/ingredientes-fichas-62061-2026-08-22.json` (e `.csv`) e
`dados/fichas-tecnicas-composicao-62061-2026-08-22.jsonl` (e `.csv`).

## Visão geral

| Bloco | Quantidade |
|---|---|
| Ingredientes (matéria-prima, embalagem, limpeza) | 149 |
| Beneficiados (preparo interno, molho e blend) | 16 |
| Fichas técnicas (produto final, o que vai pro cardápio) | 53 |
| **Total de itens cadastrados** | **218** |

Dos 149 ingredientes, 92 têm `Compõe CMV` marcado (`Y`) e 57 não (`N`). Item
com `N` normalmente é descartável, produto de limpeza ou insumo de uso
interno que não entra na conta de custo do prato.

## Achado crítico: quase metade dos itens está com estoque negativo

**96 dos 218 itens (44%) estão com saldo de estoque negativo no sistema.**

**Causa confirmada com o Jonas em 23/08/2026: hoje não existe controle de
estoque nenhum.** Não se lança entrada de compra (com ou sem nota) nem se
faz contagem física. O Saipos só baixa estoque na venda, nunca reabastece,
então o saldo fica cada vez mais negativo com o tempo. Não é um bug pontual
nem falta de disciplina ocasional, é ausência total de rotina. Os 15 piores
casos:

| Item | Estoque atual | Tipo |
|---|---|---|
| Queijo Cheddar Vigor | -4.170,1 | ingrediente |
| Brioche 70g | -4.094 | ingrediente |
| Blend 130g | -2.988,5 | beneficiado |
| Blend 40g | -2.327 | beneficiado |
| Brioche 20g | -2.280 | ingrediente |
| Blend 100g | -1.058,5 | beneficiado |
| Caixa Box | -1.051 | ingrediente |
| Costela Desfiada | -499 | beneficiado |
| Coca-Cola Zero 350ml | -471 | ingrediente |
| Coca-Cola 350ml | -437 | ingrediente |
| Batata Palito | -304,7 | ingrediente |
| Coca-Cola 1L | -275 | ingrediente |
| Ovo | -251,6 | ingrediente |
| Ge Balls Receita | -148 | beneficiado |
| Guaraná Antártica 350ml | -143 | ingrediente |

**Isso é grave porque os piores casos são exatamente os ingredientes-base de
quase todo hambúrguer do cardápio** (queijo cheddar, brioche 70g, blend
130g, o próprio pão). Sem entrada de estoque nunca acontecendo, o
`average_cost` que o Saipos calcula fica travado no preço de cadastro
original, não reflete nenhuma compra real feita depois disso. **O CMV que
aparece automaticamente no `DRE Gerencial` (28-29% no trimestre jun-ago,
ver `02-plano-de-contas.md`) não é confiável até existir alguma rotina de
entrada.** Não dá pra saber se está sub ou superestimado sem comparar com o
custo de compra real.

## Fichas técnicas: as 53 do cardápio

Todas as 53 fichas foram lidas com a composição completa (lista de
ingredientes com quantidade). A maior parte usa uma quantidade "base" (`qtt`)
mais variações por tamanho de produto (`variations`), porque o mesmo
hambúrguer pode ter mais de um tamanho/combo vinculado no cardápio.

Estrutura recorrente dos hambúrgueres principais: **Brioche 70g + Queijo
Cheddar Vigor + Blend 130g + molho**, com o diferencial (bacon, cebola
caramelizada, costela desfiada, catupiry empanado, etc.) por cima. Exemplo,
`Ge Burger` (ficha #3825359, custo médio R$ 7,41):

| Ingrediente | Qtd |
|---|---|
| Brioche 70g | 1 |
| Queijo Cheddar Vigor | 2 |
| Blend 130g | 1 |
| Molho Rosé | 0,015 |

Molhos e itens beneficiados (`Molho Rosé`, `Molho Maionese Caseira`,
`Creme de Cheddar`, `Cebola Caramelizada`, `Costela Desfiada`, `FRANGO
EMPANADO`, `Catupiry Empanado`) são preparados internamente e viram
ingrediente de outras fichas, um nível de composição a mais que no Oka
Guaraná (lá as fichas eram diretas, aqui há beneficiado dentro de beneficiado
em alguns casos, como `Ge Balls Receita` usado em `Ge Box Prime` e `Ge
balls-Box Prime`).

Ver a composição completa e o custo médio de cada uma das 53 fichas em
`dados/fichas-tecnicas-composicao-62061-2026-08-22.csv`.

## Beneficiados (preparo interno)

16 itens. Os principais, com rendimento (`yield`, quantas porções a receita
base gera):

| Beneficiado | Rendimento | Custo médio |
|---|---|---|
| Blend 130g | 1 | R$ 4,41 |
| Blend 100g | 1 | R$ 3,40 |
| Blend 40g | 1 | R$ 1,36 |
| Cebola Caramelizada | 1,17 | R$ 12,33 |
| Molho Maionese Caseira | 1,8 | R$ 8,20 |
| Molho Rosé | 1,5 | R$ 12,55 |
| Molho Honey Mustard | 1,21 | R$ 14,38 |
| Creme de Cheddar | 1 | R$ 31,24 |
| Costela Desfiada | 65 | R$ 2,05 |
| Catupiry Empanado | 18 | R$ 5,32 |
| FRANGO EMPANADO | 12 | R$ 2,73 |
| Geleia de Cupuaçu | 1,8 | R$ 14,33 |
| Ge Balls Receita | 36 | R$ 4,05 |
| Suco de Maracujá Receita | 3,6 | R$ 8,92 |
| Suco de Morango Receita | 0,3 | R$ 6,76 |
| Vinagrete de Manga | 1 | R$ 0,25 |

## Itens de revenda

Bebidas compradas prontas (refrigerante, água, suco de caixinha) não têm
ficha técnica, entram como ingrediente comum vinculado direto ao produto do
cardápio. É o mesmo padrão do Oka Guaraná.

## Divergências e pendências

- **Confirmado, 23/08/2026:** não existe rotina de compra lançada (com ou
  sem nota) nem contagem física. `average_cost` do Saipos reflete só o
  cadastro inicial, nunca foi atualizado por compra real. Ver
  `08-roadmap-implantacao.md` pra próximos passos
- `Milk-Shake Sabor` aparece cadastrado 4 vezes com IDs diferentes
  (3831315, 3831330, 4220136, e outro), cada um com composição de sabor
  diferente (chocolate, oreo, biscoff). Provavelmente 1 ficha por sabor de
  milkshake vendido, não duplicidade de cadastro, mas vale confirmar
