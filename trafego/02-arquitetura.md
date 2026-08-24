# 02, Arquitetura de campanhas (FASE 2) — Planejamento de Setembro/2026

Criado em 23/08/2026. Isso é a saída da FASE 2 do `CLAUDE-TRAFEGO.md`,
adiantada e já aplicada ao mês de setembro porque é o que você pediu.
Cruza o acervo de criativo (`analise-gemini-videos-organicos.md` +
`swipe-file.md`) com estrutura de campanha, semana a semana.

**Isto é uma proposta, não está ativado.** Regra do repo: tudo que crio
nasce pausado, e pra criar ou alterar campanha eu mostro campo a campo e
espero seu OK explícito antes. O que está aqui é o desenho pra você
aprovar ou ajustar.

---

## Bloqueios a resolver antes de eu criar qualquer coisa

Ordenado por impacto. Nenhum destes impede eu montar o plano (fiz o
plano inteiro já), mas todos impedem eu **ativar** com dinheiro de
verdade.

### 1. 🔴 Cupom de 10% na primeira compra: isso existe no Geburger?

Você pediu pra eu avaliar se precisa criar um estático pro "cupom de 10%
no primeiro pedido". **Só achei esse mecanismo especificamente no Oka
Guaraná** (cupom `OKA10`, 10% off, pedido mínimo R$30, só primeira
compra, só site delivery, válido até 08/10/2026, achado na conversa do
Gemini sobre o Oka). Não achei nada parecido documentado pro Geburger em
nenhum arquivo do repo.

Por regra do `CLAUDE.md` da raiz, não posso tratar número ou mecânica do
Oka como se fosse do Geburger sem sua confirmação explícita. **Preciso
que você me diga:**
- O Geburger tem cupom de primeira compra? Se sim: percentual, pedido
  mínimo, canal (site próprio, iFood, os dois?), validade
- Ou você quis dizer usar a mesma mecânica do Oka como referência pro
  Geburger, criando um cupom novo equivalente?

**Enquanto isso não for respondido, não crio o estático do cupom.** O
resto do plano abaixo segue sem depender dessa peça.

### 2. 🟡 Verificação do pixel/CAPI no Cardápio Web ainda inconclusiva

`02-migracao-cardapio-web.md`: o teste real do dia 23/08 ainda não foi
confirmado no Gerenciador de Eventos (timestamp não tinha avançado na
última checagem). **Antes de otimizar campanha por Purchase e escalar
orçamento em cima disso, preciso reconferir.** O plano abaixo já
considera isso: a campanha nasce com evento de otimização em Purchase,
mas com portão de segurança (não escala até confirmar).

### 3. 🟡 Preço e produto a confirmar nos criativos existentes

- **GE BOX PRIME**, R$ 96,00 na arte (Lote 8/10)
- **Combos "Ge Para Dois" e "Ge Família"** (Lote 10), composição exata
- **Vídeo Split Screen com milkshake** (Lote 8): confirmar se milkshake
  ainda está no cardápio, porque o levantamento de concorrência não achou
  essa categoria no Geburger
- **Programa de ímãs**: confirmar se ainda está ativo do jeito que
  aparece no vídeo "Ímãs do Site" (Lote 10) e no "Unboxing" (Lote 8)

### 4. 🟡 Verba mensal ainda sem número fechado

Uso a faixa provisória do `sprint-50-pedidos-7dias.md` (R$ 1.800 a 2.200
por semana, ~R$ 7.200 a 8.800/mês) só de referência de planejamento.
Ajusto a divisão assim que você confirmar o número real.

### 5. 🟡 Capacidade da Tifany ainda sem resposta

Pergunta em aberto desde `03-inteligencia-criativa.md`. O calendário
abaixo assume 1 leva de criativo novo por semana como ritmo confortável,
mas isso muda se ela tiver menos ou mais tempo disponível.

### 6. 🟢 O que já está rodando na conta, não vou tocar sem você mandar

- `[MP][Engajamento] - WhatsApp [05.06]`: você disse manter até decidir
- `[MP][Conversão] - ADV [20.05] + Adicional Reels`: campanha de venda já
  ativa, com histórico. **Decisão que preciso sua: pauso ela em favor da
  estrutura nova abaixo, ou rodo as duas em paralelo por um tempo?**
  Rodar as duas fragmenta orçamento e contraria a regra de não
  fragmentar, então minha recomendação é pausar a antiga quando a nova
  estiver validada, não no dia 1
- `[MP][Conversão] - Teste de Criativo [21.08] [Imã 2]`: começou há 2
  dias, pouco gasto ainda. Parece que você já estava testando o ângulo
  de ímã por conta própria. Vou tratar isso como o embrião da Campanha 2
  abaixo, mas não mexo nela sem seu OK

---

## Arquitetura proposta: 2 campanhas, não mais que isso

Geburger é loja única, raio de mídia já confirmado em 5km ao redor da
loja. Não tem por que separar por unidade. Sigo a regra do
`CLAUDE-TRAFEGO.md` de consolidar em vez de fragmentar: 2 campanhas com
1 conjunto cada, criativos suficientes dentro de cada uma pra dar volume
de aprendizado (a matemática de "~50 conversões/semana por conjunto pra
sair do aprendizado" é regra geral do leilão, vou confirmar contra o
volume real assim que a campanha rodar).

### Campanha 1 — Prospecção (topo de funil, quem nunca comprou)

| Campo | Valor proposto |
|---|---|
| Nome | `GEB_GeBurger_Prospeccao_Cardapio_0901` |
| Objetivo | OUTCOME_SALES |
| Evento de otimização | Purchase, com portão de segurança (ver bloqueio 2). Se Purchase não estiver confirmado até a data de ativação, otimizar por InitiateCheckout como evento intermediário até resolver, e trocar assim que confirmar |
| Público | Raio 5km ao redor da loja (R. Alexandre Magno, 497), idade e interesse amplos (não fragmentar por interesse específico, regra do repo) |
| Posicionamentos | Automático (Advantage+), deixando o Meta otimizar onde entrega melhor, revisar depois de 1 semana |
| Orçamento sugerido | 60% do total semanal (é a campanha que traz cliente novo, onde a verba rende mais volume) |
| Criativos mínimos | 3 no lançamento, subindo pra 5-6 ao longo do mês |
| Critério de sucesso | CPA dentro da meta (a fechar quando o CAC máximo for calculado, ver `estado-atual.md`) depois de 3 dias / 1.000 impressões |
| Critério de morte | CPA 3x acima da meta sem conversão, ou frequência acima de 2,5-3 com CTR caindo |

### Campanha 2 — Retargeting e fidelização (quem já visitou ou já é cliente)

| Campo | Valor proposto |
|---|---|
| Nome | `GEB_GeBurger_Retargeting_Fidelizacao_0901` |
| Objetivo | OUTCOME_SALES |
| Evento de otimização | Purchase (mesmo portão de segurança da Campanha 1) |
| Público | Visitantes do site 30 dias, quem deu AddToCart/InitiateCheckout sem comprar, lista de clientes do PDV (Repediu, já existe). Lookalike fica de fora por enquanto porque todos estão inativos (achado do `01-fundacao.md`), recriar é tarefa separada |
| Posicionamentos | Automático |
| Orçamento sugerido | 40% do total semanal (público mais quente, custo por resultado tende a ser menor, não precisa da fatia maior) |
| Criativos mínimos | 2 no lançamento, focados em fechar venda (oferta, prova, fidelização), não em atrair atenção |
| Critério de sucesso | CPA abaixo da meta e menor que o da Campanha 1 (retarget deveria ser mais barato) |
| Critério de morte | Mesmo critério da Campanha 1 |

---

## Mapa de criativo por campanha, semana a semana

### Semana 1 (01/09 a 07/09): lançamento com o que já existe

**Campanha 1 (Prospecção):**
| Criativo | Formato | Ângulo | Status |
|---|---|---|---|
| Tour Parque 10 (Lote 7) | Vídeo | Bairro/proximidade | Pronto, código do arquivo truncado, achar o .mp4 original na pasta antes de subir |
| Fritas Melted (Lote 8) | Vídeo | Produto | Pronto, mesma ressalva de código truncado |
| Montagem na Chapa (Lote 9) | Vídeo | Produto | Pronto, `Db_wJU3ztha.mp4` |
| **Novo: estático "Ultra Burger R$ 27,90"** | Estático | Preço de entrada | **Preciso criar**, não depende de vídeo nem da Tifany, dá pra ter pronto em 1 dia (ver seção "Estáticos a criar") |

**Campanha 2 (Retargeting):**
| Criativo | Formato | Ângulo | Status |
|---|---|---|---|
| Vídeo Ímãs do Site (Lote 10) | Vídeo | Fidelização | Pronto, mas confirmar bloqueio 3 (programa ainda ativo?) |
| GE BOX PRIME (Lote 8/10) | Estático | Oferta/combo | Pronto, mas confirmar preço (bloqueio 3) antes de subir |

Se o bloqueio 3 não for resolvido a tempo, a Campanha 2 sobe só com o
vídeo de ímãs na semana 1, e o estático de oferta entra na semana 2.

### Semana 2 (08/09 a 14/09): primeira leitura + primeiro lote da Tifany

- Leitura semanal dos criativos da semana 1 (ver `plano-rotacao-criativos.md`):
  mata o que não performou, escala o que validou
- **Entra o roteiro 2 do `swipe-file.md`** ("Pedido certo, entrega no
  prazo"), prioridade máxima porque é o único ângulo sem nenhum material
  existente
- Se a Tifany já tiver os outros 3 roteiros prioritários prontos
  (queijo derretendo, preço de entrada, bairro), entram também, mas o
  roteiro 2 é o que não pode ficar de fora
- Campanha 2: se o cupom (bloqueio 1) for confirmado até aqui, esse é o
  momento de subir o estático de cupom, é um criativo de fechamento
  clássico pra público que já demonstrou interesse

### Semana 3 (15/09 a 21/09): segunda leitura + reforço

- Leitura semanal, mesma lógica
- Entra o roteiro 3 do `swipe-file.md` (preço de entrada, se ainda não
  tiver entrado) e o carrossel Trend "Achamos Chique" (Lote 9, já
  existe, ângulo de prova social/desejo) na Campanha 2, como reforço de
  fechamento
- Considerar criar 1 carrossel estático de cardápio (3-4 itens com
  preço) se a Campanha 1 estiver precisando de mais volume de criativo

### Semana 4 (22/09 a 30/09): terceira leitura + fechamento do mês

- Leitura semanal
- Fechamento mensal: DRE de mídia, CAC real contra o que o Gerenciador
  atribuiu, quais ângulos ainda não foram testados (fica pra outubro)
- Não entra criativo novo nessa semana a não ser que algo tenha morrido
  e precise de substituto imediato

---

## Estáticos a criar

| # | Peça | Depende de | Quando fica pronto |
|---|---|---|---|
| 1 | Cupom 10% primeira compra | **Bloqueio 1**, sua confirmação | Só depois de saber se existe |
| 2 | "Ultra Burger R$ 27,90" (preço de entrada) | Nada, pode fazer já | Antes da semana 1 |
| 3 | GE BOX PRIME (reaproveitar o que já existe) | Confirmar preço R$ 96,00 vigente | Antes da semana 1, se confirmado |
| 4 | Combos "Ge Para Dois"/"Ge Família" (reaproveitar) | Confirmar composição/preço | Semana 2 ou 3 |
| 5 | Carrossel de cardápio (3-4 itens com preço) | Nada específico, é reforço se faltar volume | Semana 3, só se precisar |

**Por que estático além de vídeo:** o `CLAUDE-TRAFEGO.md` pede número
mínimo de criativos variados por campanha, e estático é mais barato e
rápido de produzir que vídeo. Enquanto a capacidade de vídeo da Tifany
não estiver confirmada, estático é o jeito de manter o pipeline de
criativo novo andando sem depender só dela.

---

## Orçamento (provisório, ajustar quando a verba mensal fechar)

Usando a faixa de referência do `sprint-50-pedidos-7dias.md`
(R$ 1.800 a 2.200/semana):

| Campanha | % do orçamento | Faixa semanal estimada |
|---|---|---|
| Campanha 1, Prospecção | 60% | R$ 1.080 a 1.320 |
| Campanha 2, Retargeting | 40% | R$ 720 a 880 |

Isso é só a divisão proporcional. **O número absoluto ainda não está
confirmado com você**, então trate como estrutura, não como orçamento
fechado.

---

## Checklist antes de eu ativar qualquer coisa

- [ ] Bloqueio 1 respondido (cupom existe ou não no Geburger)
- [ ] Bloqueio 2 resolvido (pixel/CAPI confirmado recebendo Purchase)
- [ ] Bloqueio 3 resolvido (preços e produtos confirmados nos criativos
  sinalizados)
- [ ] Verba mensal confirmada
- [ ] Decisão sobre a campanha `[MP][Conversão] - ADV [20.05]` (pausar
  depois de validar a nova, ou rodar em paralelo)
- [ ] Eu te mostro campo a campo antes de criar qualquer campanha/conjunto/
  anúncio, e tudo nasce pausado

## Próximo passo

1. Você responde os bloqueios 1, 3, 4 e 5 acima
2. Eu reconfiro o Gerenciador de Eventos (bloqueio 2, já é ação pendente
   de antes)
3. Com isso resolvido, monto campo a campo as duas campanhas pra sua
   aprovação final antes de criar
