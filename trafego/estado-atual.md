# Estado atual

**Atualizado em 22/08/2026 (terceira sessão do dia).** FASE 0 rodada
(`00-auditoria.md`) e FASE 1 auditada (`01-fundacao.md`), essa última com
achado direto no Gerenciador de Eventos e nas Configurações do Negócio via
login do Jonas. Meta: estrutura de tráfego pronta e campanha ativada até
31/08/2026 (9 dias a partir de hoje).

## O que está rodando agora (22/08/2026)

| Campanha | Objetivo | Gasto histórico |
|---|---|---|
| `[MP][Engajamento] - WhatsApp [05.06]` | OUTCOME_ENGAGEMENT | R$ 1.948,35 |
| `[MP][Conversão] - ADV [20.05] + Adicional Reels` | OUTCOME_SALES | R$ 1.911,67 |
| `Post do Instagram: Ge Classic chega conquistando...` | LINK_CLICKS | R$ 41,74 |
| `[MP][Conversão] - Teste de Criativo [21.08] [Imã 2]` | OUTCOME_SALES | R$ 17,27 |

**Não mexi em nada.** Nenhuma campanha foi criada, pausada, ativada ou teve
orçamento alterado nesta sessão. Só leitura.

## Achados desta sessão que pedem decisão do Jonas

1. Campanha de **engajamento** ativa (`[MP][Engajamento] - WhatsApp`).
   Histórico de R$ 25 mil em objetivo de engajamento na conta toda, sem
   contar venda. Decidir se mantém ou pausa
2. `Post do Instagram: Ge Classic chega conquistando...` parece post
   impulsionado direto do Instagram, não campanha do Gerenciador. Confirmar
3. Pixel com Event Match Quality nota 3, só correspondência por
   `user_agent`. Sem email/telefone configurado, o que enfraquece a
   otimização de qualquer campanha de conversão
4. 2 páginas do Facebook associadas à conta de anúncios sem relação aparente
   com o negócio (`esthereilish`, `Manaus em Dobro`). Confirmar se é lixo de
   vínculo antigo
5. **DRE do Saipos não está confiável** (91 de 97 categorias sem vínculo de
   seção). Antes de calcular CAC máximo ou margem de contribuição, esse
   trabalho de vinculação financeira precisa acontecer (ver
   `../operacao/02-plano-de-contas.md`)
6. 44% do estoque com saldo negativo pode estar distorcendo o custo do
   prato usado pra qualquer conta de margem (ver
   `../operacao/06-estoque-ingredientes-e-fichas.md`)

## FASE 0 rodada: achados novos desta sessão

Ver `00-auditoria.md` para o detalhe completo. Resumo:

- Opportunity Score da conta: **74/100**. Maior alavanca disponível é
  fragmentação de público (+19 pontos só de consolidar conjuntos)
- Catálogo de produtos: **confirmado que não existe** (zero catálogos)
- 6 erros de entrega ativos bloqueando anúncios específicos (formato
  incompatível, música licenciada, anúncio não entregando, mídia arquivada)
- Raio de mídia confirmado: 5 km ao redor da loja (Rua Alexandre Magno, 497)
  em todos os conjuntos ativos analisados
- Criativos ativos mostram repetição alta de título genérico ("Peça Agora"
  e variações, +10 versões), sinal de baixa diversidade de ângulo
- Pico de 39 Purchase em uma hora só (18/08 16h) precisa confirmação: é
  venda real ou disparo duplicado no pixel?
- Testei a Biblioteca de Anúncios da Meta como ferramenta de inteligência
  competitiva: funciona, mas não filtra por cidade, só por país

## Decisões do Jonas (22/08/2026)

1. Campanha `[MP][Engajamento] - WhatsApp [05.06]`: **manter até ele decidir**,
   não pausar sozinho. Perguntar o motivo dela existir antes de mexer.
2. Post impulsionado `Ge Classic chega conquistando...`: **deixar terminar o
   ciclo**. Não impulsionar post do Instagram de novo assim (regra fixa).
3. Páginas soltas (`esthereilish`, `Manaus em Dobro`): **não sabe, investigar
   depois**. Não bloqueia o lançamento de 31/08, mas fica pendência.
4. WhatsApp de atendimento: **app comum do WhatsApp Business, sem API oficial
   nem automação**, segundo o Jonas. **Achado que pede confirmação:** existe
   uma conta "Geburger" cadastrada como Aplicativo WhatsApp Business dentro
   do Business Manager (ver `01-fundacao.md`, seção 7). Pode ser só o
   vínculo básico de anúncio clique-pra-WhatsApp, não necessariamente API
   oficial. Fica pendente confirmar antes de decidir sobre compartilhar
   evento de compra via WhatsApp.

## FASE 1 auditada: achados desta sessão

Ver `01-fundacao.md` para o detalhe completo. Resumo:

- CAPI está **ativa** (correção do que constava antes como "não
  confirmado"), via Signals Gateway, mas com configuração incompleta
  (falta Signals Gateway Pixel, até 23% menor custo por resultado)
- Domínio do cardápio (`geburger.saipos.com`) identificado, mas **não
  verificado** no Meta. O domínio institucional (`geburger.com.br`) está
  verificado
- 17% dos eventos Purchase chegam com preço malformado ou ausente,
  achado direto do Gerenciador de Eventos, prioridade alta
- Todos os públicos lookalike da conta estão inativos, zero prospecção
  por semelhança rodando
- 2FA: 0 de 4 pessoas ativaram, mesmo com política exigindo de admin
- **Endereço da loja diverge em três sistemas** (`CLAUDE.md`, iFood, Meta
  Business): R. Alexandre Magno 497, Rua Perimetral 495, Rua Arquiteto
  Renato Braga 415. Precisa confirmação do Jonas antes de configurar
  geolocalização com segurança

## Migração pro Cardápio Web (23/08/2026)

O site de delivery vai trocar do Site Delivery (SAIPOS) pro **Cardápio
Web** (`cardapioweb.com`, plataforma separada, não é produto do Saipos,
mesmo padrão já usado no Oka Guaraná). Site novo já no ar em
`app.cardapioweb.com/geburger`, painel de gestão em
`portal.cardapioweb.com`. Endereço confirmado pelo Jonas: **R. Alexandre
Magno, nº 497** (os outros dois que apareceram são só vínculo de CNPJ).

Achei que o painel do Cardápio Web já tem card dedicado pra Facebook
Pixel, CAPI, Domínio Próprio e Catálogo do Facebook — mais simples que
configurar via Saipos puro. Nada disso está preenchido ainda. Domínio
`geburger.com.br` sendo configurado essa semana. Roteiro completo em
`02-migracao-cardapio-web.md`.

## Fundação técnica do Cardápio Web: pixel, CAPI e GTM prontos (23/08/2026)

Feito e confirmado ao vivo no site (`window.fbq` e `window.gtag` ativos):
- Pixel `746769616981227` colado (mesmo de sempre, não criei um novo)
- Token de CAPI gerado no Gerenciador de Eventos e colado no Cardápio Web
- GTM `GTM-WXPT39J5` (confirmado pelo Jonas) colado no lugar do container
  genérico que estava lá de fábrica

**Pedido de teste real completado às 18h51** (loja abriu 17h30): 4x Água
Mineral, R$20, retirada, cliente "TESTE PIXEL NAO REAL". Pedido `#263139086`
criado e já cancelado no painel com motivo registrado. **Verificação do
lado do Meta ficou inconclusiva**: a Visão Geral do Gerenciador ainda
mostrava timestamp velho (PageView "há 7 horas", Compra "há 4 dias") logo
depois do teste, não dá pra saber ainda se é delay de agregação normal ou
se o evento não está chegando. Precisa conferir de novo mais tarde.

## FASE 3 iniciada: inteligência criativa (23/08/2026)

Jonas priorizou criativo agora porque depende da Tifany, social mídia que
atende Geburger **e** Oka Guaraná ao mesmo tempo, e quer material pronto
pra gravar antes do início de setembro.

Testei a Biblioteca de Anúncios da Meta por nome de concorrente: não filtra
bem por cidade (busca por "Dome's Burgers" ou "Burgers e Burgers" devolve
milhares de resultados nacionais sem relação com Manaus). Único achado
específico: JSK Burgers tem só 8 anúncios ativos no total na conta deles.
Não vou insistir nessa ferramenta pra concorrente local pequeno, a fonte
real que temos é o dossiê do iFood (`dossie-ifood-concorrentes-manaus.md`),
que já tem preço, cardápio e review de verdade.

Entregue: `03-inteligencia-criativa.md` (6 ângulos com origem no dado,
matriz de 12 combinações Ângulo x Formato x Oferta) e `swipe-file.md`
(4 roteiros prioritários, prontos pra Tifany gravar, segundo a segundo,
com texto principal, título e CTA).

**Pergunta em aberto que trava o volume semanal:** quantos dias/horas por
semana a Tifany dedica ao Geburger (ela divide com o Oka), e se ela grava
sozinha ou precisa de alguém segurando câmera. Sem isso não dá pra prometer
quantos criativos saem por semana.

## Plano de rotação de criativos (23/08/2026)

Jonas sentiu falta de uma estratégia de uso do acervo mês a mês (quando
entra criativo novo, quando ativa/desativa, com que frequência analiso).
Entregue `plano-rotacao-criativos.md`: 3 estados de criativo (testando,
escalando, parado), cadência diária (só monitora, não decide) vs semanal
(decide de verdade, toda segunda) vs mensal (fecha DRE de mídia e
replaneja), gatilhos claros pra entrada de criativo novo no meio do mês
(fadiga do que já roda, validação do que estava em teste, orgânico que
performou bem) e um calendário modelo de 4 semanas aplicado ao lote de
setembro.

## FASE 2 adiantada: arquitetura de campanhas de setembro (23/08/2026)

Jonas pediu o planejamento detalhado de setembro: que campanha criar,
que vídeo/estático usar, semana a semana. Entregue `02-arquitetura.md`:
2 campanhas (Prospecção 60% da verba, Retargeting/Fidelização 40%),
mapa de criativo por semana cruzando o acervo existente com
`swipe-file.md`, e lista de estáticos a criar.

**Achado que precisa de resposta sua:** você pediu estático de "cupom de
10% no primeiro pedido", mas esse mecanismo só apareceu documentado no
Oka Guaraná (cupom OKA10), não achei nada equivalente pro Geburger em
nenhum arquivo do repo. Não criei esse estático até você confirmar se
existe cupom assim no Geburger (percentual, pedido mínimo, canal,
validade) ou se é pra criar um novo do zero.

Outros bloqueios listados em `02-arquitetura.md` antes de eu poder
ativar qualquer campanha: verificação do pixel/CAPI do Cardápio Web
ainda inconclusiva, preço/produto a confirmar em 4 criativos (GE BOX
PRIME R$96, combos casal/família, milkshake no vídeo Split Screen,
programa de ímãs ainda ativo), verba mensal e capacidade da Tifany.

## Próximo passo

1. **Jonas responde os bloqueios do `02-arquitetura.md`**: cupom existe
   ou não, confirmação de preço/produto dos 4 criativos sinalizados,
   verba mensal, capacidade da Tifany, e se pausa a campanha
   `[MP][Conversão] - ADV [20.05]` em favor da estrutura nova
2. Tifany grava os 4 roteiros prioritários do `swipe-file.md`
3. **Conferir de novo o Gerenciador de Eventos** — ver se "recebido pela
   última vez" avançou pra hoje (pixel/CAPI do Cardápio Web). Se não
   avançar, é problema real, não só delay
4. Domínio próprio (`geburger.com.br`) — Jonas disse que fica pronto essa
   semana, depois disso: verificação no Meta e Agregação de Eventos
5. Revisitar cálculo de CAC máximo: `operacao/CLAUDE.md` mudou, DRE agora
   com 61 de 100 categorias vinculadas (era 6 de 97), pode já dar pra
   calcular com mais segurança
6. Verba mensal de mídia ainda sem valor final confirmado

## Como manter este arquivo

Atualize no fim de toda sessão. Este é o arquivo que a próxima sessão lê
para saber onde parou: campanha ativa, orçamento, criativo no ar, teste em
andamento e próximo passo.
