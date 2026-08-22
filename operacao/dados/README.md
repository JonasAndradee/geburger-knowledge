# operacao/dados/

Exports crus tirados direto do sistema. Arquivo aqui é fonte primária, não
interpretação. Interpretação vai nos arquivos numerados.

## Convenção de nome

`[conteúdo]-[unidade]-[AAAA-MM-DD].csv`, unidade pelo ID do PDV.

## Arquivos

| Arquivo | Conteúdo | Como foi extraído |
|---|---|---|
| `ingredientes-fichas-62061-2026-08-22.json` | Lista mestra completa dos 218 itens cadastrados em `Ingredientes e Insumos` da Ge Burger: 149 ingredientes, 16 beneficiados, 53 fichas técnicas (produto final). JSON bruto da API, um objeto por item | API do Saipos (`api.saipos.com/v1/stores/62061/ingredients`), lida pelo Claude in Chrome autenticado na sessão da loja, em 22/08/2026 |
| `ingredientes-62061-2026-08-22.csv` | Mesma lista em CSV, campos essenciais: id, nome, tipo, grupo, categoria financeira, estoque atual, custo médio, controla estoque, compõe CMV | Derivado do JSON acima |
| `fichas-tecnicas-composicao-62061-2026-08-22.jsonl` | Composição das 69 fichas técnicas (53 produto final + 16 beneficiado), uma linha JSON por ficha, com a lista de ingredientes e quantidade | API do Saipos, escopo Angular da tela `Fichas técnicas` (`vm.record.children`), lida ficha por ficha, 22/08/2026 |
| `fichas-tecnicas-composicao-62061-2026-08-22.csv` | Mesma composição em CSV, uma linha por ingrediente de cada ficha | Derivado do JSONL acima |
| `categorias-financeiras-62061-2026-08-22.csv` | Árvore completa das 97 categorias financeiras raiz (252 nós contando subcategorias e duplicação por caminho), com id, id do pai, profundidade, seção do DRE vinculada e se é categoria de caixa | API do Saipos (`vm.categories` da tela `Categorias financeiras`), 22/08/2026 |
| `cardapio-62061-2026-08-22.csv` | Cardápio completo, 183 produtos: id, nome, categoria do cardápio, ativo, canais habilitados (delivery/site/totem), variação e preço, descrição | API do Saipos (`api.saipos.com/v1/stores/62061/items`), tela `Cardápio` (React), 22/08/2026 |
| `despesas-por-categoria-62061-2026-01-a-08.csv` | Total lançado por categoria financeira, agregado de 01/01 a 22/08/2026, 51 categorias | Tela `Lançamentos financeiros`, agregação de 2.756 lançamentos individuais, 22/08/2026 |
| `vendas-por-periodo-62061-2026-01-a-08.md` | Vendas por período em 3 janelas de até 3 meses (limite da tela): jan-mar, abr-jun, jul-22ago/2026. Pedidos, faturamento, ticket médio, cupons, canal de origem | Relatório `Vendas por período`, 22/08/2026. Consolidado no fim do arquivo |

Toda linha desta tabela precisa dizer **como** o arquivo foi extraído: tela,
relatório, API ou digitação. Export sem origem declarada não serve de fonte.

## Achado ao extrair

**91 das 97 categorias financeiras raiz não estão vinculadas ao DRE.** O
próprio Saipos avisa isso na tela do DRE Gerencial. Só 6 estão vinculadas:
`Consumo`, `Despesas Financeiras (Taxas de cartão + Aluguel Máquinas)`,
`Diferença de caixa`, `Garçom`, `Motoboy` e `Saldo Inicial`. Isso significa que
o DRE Gerencial de hoje não reflete o financeiro real, ver
`../04-categorias-financeiras.md` e `../02-plano-de-contas.md`.

O relatório `Lançamentos financeiros` não mostra receita de venda (só
apareceu `Receita em pix: -R$ 7,00`, que é estorno, e `Frente de Caixa`, que é
sangria/reforço de caixa). A receita de venda em si mora no relatório
`Vendas por período` / vendas do PDV, não nos lançamentos financeiros
manuais. Confirmar com o Jonas se isso é esperado ou se falta alguma
integração de repasse automático.

Toda linha desta tabela precisa dizer **como** o arquivo foi extraído: tela,
relatório, API ou digitação. Export sem origem declarada não serve de fonte.

## Regra de dado

Nenhum arquivo aqui pode ter telefone, nome ou endereço de cliente. Nome de
fornecedor pode entrar quando for o texto que aparece no extrato bancário e
o contador precisar dele para classificar. CPF não entra em nenhum arquivo
deste repositório.
