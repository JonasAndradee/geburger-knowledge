# Briefing: números do negócio para tráfego pago

Fonte única de verdade dos números usados nas análises de tráfego.
Consolidado em 22/08/2026 a partir do repo (Saipos, levantado nesta sessão)
e do MCP da Meta Ads. Ver `00-descoberta.md` para o rastro completo.

**Dado velho é avisado como velho.** Se a data de extração for antiga na
hora de usar isso, confira de novo antes de decidir em cima do número.

---

## Status do levantamento

| # | Item | Status | Fonte | Data do dado |
|---|---|---|---|---|
| 1 | Ticket médio por canal | PARCIAL | `../operacao/dados/vendas-por-periodo-62061-2026-01-a-08.md` | 22/08/2026 |
| 2 | CMV e margem por lanche e combo | PARCIAL, custo pode estar distorcido | `../operacao/06-estoque-ingredientes-e-fichas.md` | 22/08/2026 |
| 3 | CAC máximo | FALTANDO, depende do item 2 | | |
| 4 | Faturamento por unidade e sazonalidade | PARCIAL (só total do período, falta quebra por dia/hora) | `../operacao/dados/vendas-por-periodo-62061-2026-01-a-08.md` | 22/08/2026 |
| 5 | Recompra e LTV 90 dias | FALTANDO | | |
| 6 | Verba mensal de mídia | FALTANDO (perguntar ao Jonas) | | |
| 7 | Capacidade da cozinha no pico | FALTANDO | | |
| 8 | Raio de entrega por unidade | FALTANDO | | |
| 9 | Instagram e página do Facebook | ACHADO, com ressalva | `00-descoberta.md` | 22/08/2026 |
| 10 | Domínio e plataforma do cardápio | PARCIAL (canal "Site Delivery (SAIPOS)" confirmado nas vendas, plataforma exata não confirmada) | | |
| 11 | Pixel e eventos | ACHADO | `00-descoberta.md` | 22/08/2026 |
| 12 | CAPI | FALTANDO | | |
| 13 | EMQ por evento | ACHADO: nota 3, só por user_agent | `00-descoberta.md` | 22/08/2026 |
| 14 | Catálogo | FALTANDO | | |
| 15 | Conta de anúncios | ACHADO: `708536560751820` | `00-descoberta.md` | 22/08/2026 |
| 16 | Google Business por unidade | FALTANDO | | |
| 17 | WhatsApp: API oficial ou app | FALTANDO | | |

## Números do negócio

**Vendas, 01/01 a 22/08/2026** (fonte: relatório Vendas por período do
Saipos, ver `../operacao/unidades/ge-burger.md`):
- 4.407 pedidos, R$ 346.518,78 em faturamento
- iFood: 1.134 pedidos, R$ 70.937,61
- Site Delivery (SAIPOS): 822 pedidos, R$ 74.266,70
- Telefone: 285 pedidos, R$ 22.571,11
- 99Food: 66 pedidos, R$ 4.283,92 (só a partir de abril/2026)
- Facebook e WhatsApp como canal de venda: 0 pedidos

**Cardápio:** 183 produtos cadastrados no Saipos (conta itens duplicados
entre canal salão/delivery e promoções do iFood). Ver
`../operacao/dados/cardapio-62061-2026-08-22.csv`.

**Custo de insumo:** 149 ingredientes, 53 fichas técnicas de produto final.
**Atenção:** 44% dos itens de estoque estão com saldo negativo, incluindo
os ingredientes-base de quase todo hambúrguer (queijo cheddar, brioche,
blend). Isso pode estar distorcendo o custo médio calculado pelo Saipos.
Não usar o CMV por prato pra calcular CAC máximo antes de confirmar isso
com a operação. Ver `../operacao/06-estoque-ingredientes-e-fichas.md`.

**DRE:** o DRE Gerencial do Saipos não reflete o resultado real hoje (91 de
97 categorias financeiras sem vínculo de seção). Não usar pra calcular
margem de contribuição ainda. Ver `../operacao/02-plano-de-contas.md`.

## Ativos digitais

Ver `00-descoberta.md`, seções "Rastreamento", "Públicos personalizados" e
"Páginas e Instagram vinculados".
