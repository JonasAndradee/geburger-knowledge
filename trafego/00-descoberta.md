# 00, Descoberta

**Levantamento de 22/08/2026.** Varredura do repo (vazio na parte de negócio,
preenchido nesta sessão a partir do Saipos) e do MCP da Meta Ads.

## Conta de anúncios

Confirmada pelo Jonas: `708536560751820`, nome "Gê Burger -> Digital Livre".
Está na Business Manager "Ge burger" (`584310666620290`), a mesma BM que
hospeda a conta do Oka Guaraná. Existem outras contas na mesma BM
(`Habbitu`, `Ge burger (Read-Only)`) e contas de terceiros associadas
(`Gabriel Azevedo`, `Jonas Andrade`, `Geral`), a maioria `CLOSED` ou
read-only. **A conta certa do Geburger é a `708536560751820`, confirme
sempre antes de qualquer leitura ou alteração.**

## Histórico de gasto

38 meses de histórico, desde julho/2023. Total histórico: R$ 98.805,45 em
121 campanhas. Divisão por objetivo:

| Objetivo | Gasto histórico |
|---|---|
| OUTCOME_SALES (conversão/vendas) | R$ 55.733,88 |
| OUTCOME_ENGAGEMENT (engajamento) | R$ 25.077,45 |
| OUTCOME_AWARENESS (reconhecimento) | R$ 13.900,07 |
| LINK_CLICKS | R$ 2.895,60 |
| OUTCOME_TRAFFIC | R$ 1.198,45 |

**Achado a levantar o motivo com o Jonas:** um quarto do investimento
histórico (R$ 25 mil) foi em objetivo de engajamento, não vendas. Padrão
parecido com o que o Oka Guaraná já identificou e decidiu cortar. Ver regra
correspondente em `CLAUDE.md`.

## Campanhas ativas agora (22/08/2026)

4 campanhas ativas:

| Campanha | Objetivo | Gasto histórico |
|---|---|---|
| `[MP][Engajamento] - WhatsApp [05.06]` | OUTCOME_ENGAGEMENT | R$ 1.948,35 |
| `[MP][Conversão] - ADV [20.05] + Adicional Reels` | OUTCOME_SALES | R$ 1.911,67 |
| `Post do Instagram: Ge Classic chega conquistando...` | LINK_CLICKS | R$ 41,74 |
| `[MP][Conversão] - Teste de Criativo [21.08] [Imã 2]` | OUTCOME_SALES | R$ 17,27 |

**Dois achados pra levantar com o Jonas antes de qualquer plano novo:**
1. Uma campanha de **engajamento** está ativa agora (`[MP][Engajamento] -
   WhatsApp`). Pelo padrão observado no Oka, isso costuma ser dinheiro sem
   retorno mensurável de venda
2. `Post do Instagram: Ge Classic chega conquistando...` parece um post
   impulsionado direto pelo Instagram, não uma campanha montada no
   Gerenciador. Confirmar

## Rastreamento (pixel e qualidade de sinal)

- Dataset ativo: "Pixel de Ge burger" (`746769616981227`), criado em
  março/2023, ainda disparando (`last_fired_time` recente)
- Eventos configurados: AddToCart, InitiateCheckout, PageView, Purchase,
  ViewContent, AddPaymentInfo
- **Event Match Quality: nota 3** em AddToCart, PageView e Purchase (escala
  típica é maior, quanto mais alto melhor). Cobertura de correspondência é
  só por `user_agent`, 100%. **Não há email, telefone ou outro identificador
  de correspondência configurado no pixel.** Isso é sinal fraco: o Meta tem
  dificuldade de casar o evento do site com a conta real da pessoa,
  o que piora a otimização de campanha de conversão
- Não foi confirmado ainda se existe CAPI (API de Conversões) ativa

## Erros de entrega na conta

Erros bloqueando campanha, conjunto ou anúncio, achados na varredura:

- Reels com música licenciada não pode ser impulsionado (2 ocorrências)
- Vários anúncios com "This ad is not delivering", pedindo criar conjunto
  novo com configuração diferente (4 ocorrências)
- 1 anúncio com formato de criativo incompatível com os posicionamentos
  selecionados
- 1 anúncio veio de mídia orgânica do Instagram que foi arquivada
  (`Instagram Ads Archived Organic Media`)

## Públicos personalizados

Muitos públicos cadastrados (mais de 50), a maioria de lookalike **inativos**
(`delivery_status: INACTIVE`). Os públicos base ativos incluem: visitantes
do site (30/60/90/180 dias), compradores (30/60/90/180 dias, e "2x" pra
quem comprou 2 vezes), engajamento de Instagram e Facebook (60 e 365 dias),
seguidores do Instagram, e um público de clientes que repediram (upload de
lista, `Repediu - Todos os clientes`). Nenhum lookalike ativo hoje, todos
`INACTIVE`, o que significa que a conta não está usando semelhança de
público pra prospecção agora.

## Páginas e Instagram vinculados

3 páginas do Facebook aparecem associadas à conta de anúncios: `Geburger`
(a principal, ID `103681477971070`), e duas que parecem não ter relação com
o negócio (`esthereilish`, `Manaus em Dobro`). **Confirmar com o Jonas se
essas duas são erro de vínculo antigo ou têm uso legítimo**, porque campanha
apontando pra página errada é o tipo de erro que passa despercebido.

Conta do Instagram vinculada: `@geburgeroficial`.

## O que ainda falta puxar

- CAPI (API de Conversões): status não confirmado
- Catálogo de produtos: não verificado
- Domínio verificado: não verificado
- UTMs usados nos criativos: não verificado
- Instagram Insights (orgânico): não puxado, é extração manual
- Dados do cardápio próprio (pedidos por dia, origem de tráfego): não
  puxado, depende de acesso à plataforma do delivery
