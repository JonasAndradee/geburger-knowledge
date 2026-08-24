# Raio de entrega e taxas, Ge Burger (62061)

Extraído do Saipos em 22/08/2026, tela **Áreas de entrega** (`#/app/store/area-map`),
modo "Usar taxas por recorte" (ativo). Fonte: automação de navegador (Claude
in Chrome), sessão já autenticada da loja.

## Raio real de entrega configurado no Saipos

| Raio | Taxa de entrega | Taxa do entregador |
|---|---|---|
| 1 km | R$ 5,00 | R$ 5,00 |
| 2 km | R$ 7,00 | R$ 7,00 |
| 3 km | R$ 9,00 | R$ 9,00 |
| 4 km | R$ 10,00 | R$ 10,00 |
| 5 km | R$ 12,00 | R$ 12,00 |
| 6 km | R$ 13,00 | R$ 13,00 |

Raio máximo atendido: **6 km** a partir do ponto geo da loja (Rua Alexandre
Magno, 497, Parque 10 de Novembro).

## Achado: descompasso entre raio do anúncio e raio real de entrega

`00-auditoria.md` já tinha confirmado que todo conjunto ativo no Meta Ads
mira **5 km**. O Saipos entrega de verdade até **6 km**. Ou seja, existe um
anel de 5 a 6 km onde a loja entrega e recebe taxa, mas o anúncio não
alcança. Não é erro grave (é sub-cobertura, não anúncio fora de área, que
seria o erro proibido pelo `CLAUDE.md`), mas é oportunidade de ampliar o
raio de mídia pra bater com o raio real antes de qualquer nova campanha.

## Taxa de entrega como parte da conta de margem

A taxa de entrega (R$ 5 a R$ 13, dependendo da distância) é cobrada do
cliente, então não é custo do Geburger na maior parte dos casos. Mas pode
virar alavanca de oferta ("frete grátis acima de X" ou "frete grátis nas
primeiras Y km") pras campanhas de topo de funil, com a conta de quanto
isso reduz a margem por pedido feita antes de qualquer promessa no criativo.

## O que ainda falta confirmar

- Se essa mesma taxa está espelhada no site delivery próprio (canal "Site
  Delivery (SAIPOS)") ou só no PDV/roteirização interna
- Geo ponto da loja usado como centro (não conferido em detalhe, aba
  "Ajustar geo ponto da loja" não aberta nesta extração)
- Cidades atendidas fora de Manaus (aba "Cidades atendidas" não aberta)
