# Análise do Gemini: acervo de vídeos orgânicos do Instagram

Extraído em 23/08/2026 direto da conversa do Gemini do Jonas
("Análise de Vídeos Geburger Ads", `gemini.google.com/app/1817afbf32311ea7`),
via Claude in Chrome. Objetivo: ter o conteúdo consolidado aqui no repo,
sem duplicar, pra cruzar com `03-inteligencia-criativa.md` e decidir o que
vira anúncio pago.

## Cobertura real (leia isso antes de usar o resto do arquivo)

**Só 5 lotes foram analisados (Lote 6 a 10), num total de 34 mídias.**
Jonas mandou originalmente ~65 vídeos + pasta `posts` (imagens/carrossel).
Não existe Lote 1 a 5 em nenhuma conversa do Gemini da conta do Jonas: eu
verifiquei todas as outras conversas com nome parecido na lateral do
Gemini ("Análise de Vídeos para Anúncios" x2, "Análise de Vídeos para
Anúncios Meta Ads", "Análise de Vídeos para Meta Ads", "Análise de Vídeo:
Roteiro, Visual e Estratégias", "Análise Profissional de Instagram") e
nenhuma delas é sobre Geburger: são todas sobre **Oka Guaraná** (shake de
guaraná, `okaguarana.com`) ou são referência genérica de marcas de
smoothie/whey de fora (Smoov, We Protein, Evenly, Amazonas Shopping), ou
ficaram sem resposta. Não misturei nada disso aqui, só registro que
existem pra você saber que não é conteúdo perdido do Geburger, é
material de outro negócio.

**O que fica faltando, então:**
- Boa parte do acervo mais antigo ainda não foi analisada: o próprio
  Gemini, ao tentar ler o CSV, listou vídeos de 2023, outubro/2025,
  fevereiro/2026, abril e maio/2026 que **não aparecem em nenhum dos
  Lotes 6 a 10** (que começam em junho/2026). Ver seção "Vídeos que o
  CSV mostra mas ainda não foram analisados" abaixo
- O arquivo `geburgeroficial.json` não foi encontrado pelo Gemini
  (achou só o `.csv`). Precisa confirmar se ele está mesmo na pasta
- O Gemini nunca cruzou as métricas do CSV (visualizações, curtidas,
  comentários) com cada vídeo individualmente, mesmo o prompt original
  pedindo isso. As notas "Nota Ads" que aparecem abaixo são leitura
  visual/estratégica do Gemini, não são baseadas em métrica real de
  performance
- O link do Google Drive nunca foi acessado de fato pelo Gemini (ele
  disse explicitamente que não consegue abrir link externo). Toda a
  análise abaixo veio de vídeos que o Jonas anexou direto no chat, em
  lotes, não da pasta do Drive

## Como o Gemini confirmou o padrão de URL

Direto da resposta dele: o código entre colchetes no nome do arquivo
(ex: `[DP2HebUkWlh]`) é a coluna `code` do CSV, e a URL é
`https://www.instagram.com/reel/CODIGO/` (ou `/p/CODIGO/` pra post que
não é reel). Confirmado com exemplos reais do CSV, não é achismo.

**Estrutura de colunas do `geburgeroficial.csv`** (segundo o Gemini):
`type` (post/carousel), `media` (video/photo), `code` (shortcode do
Instagram), `id` (ID numérico), `date`, `file` (caminho, ex:
`posts/2026-08-13_17-56-00_[Db_wJU3ztha].mp4`), `slide`, `highlight`,
`likes`, `comments`, `views` (maioria vazio, segundo o Gemini), `caption`,
`liked`.

## Vídeos que o CSV mostra mas ainda não foram analisados

Lista que o próprio Gemini extraiu do CSV como amostra (ele disse "cerca
de 30 a 35 publicações em vídeo constam no CSV", isso aqui não é a lista
completa, é só o que ele mostrou como exemplo). Nenhum destes tem ficha
técnica ainda, porque são de antes de junho/2026 (fora do intervalo dos
Lotes 6-10):

| Arquivo | Data | Assunto (pelo nome do arquivo) |
|---|---|---|
| `posts/2023-07-15_18-00-52_[Cuu9ZtWgmTN].mp4` | 15/07/2023 | Smash burger / ambiente |
| `posts/2025-02-18_18-37-27_[DGOygZfvwSE].mp4` | 18/02/2025 | Ge Amazônico |
| `posts/2025-10-15_17-52-14_[DP2HebUkWlh].mp4` | 15/10/2025 | Ge Amazônico / Bastidor |
| `posts/2026-04-25_17-48-45_[DXkf1MCzAx3].mp4` | 25/04/2026 | Humor / Pagar a conta |
| `posts/2026-04-29_15-48-15_[DXukl_LE3XI].mp4` | 29/04/2026 | GE WEEK / Ge Tropical |
| `posts/2026-05-13_17-36-15_[DYS0eO1z9xv].mp4` | 13/05/2026 | GE WEEK / Ge Classic |
| `posts/2026-05-20_17-48-33_[DYk3emOTmzi].mp4` | 20/05/2026 | Programa de Fidelidade Ímã |

Isso é anterior aos Lotes 6-10, que começam em `DZYP...` (03/06/2026).
**Se você quiser cobrir os 65 vídeos de verdade, falta anexar esse trecho
mais antigo pro Gemini analisar** (ou usar o `prompt-analise-videos-gemini.md`
que já preparei, que resolve isso de um jeito mais completo, cruzando
com CSV e métrica de verdade).

---

## Lote 6 (03/06/2026 a 29/06/2026)

| # | Vídeo/mídia | Ângulo principal | Nota Ads | Por quê |
|---|---|---|---|---|
| 1 | Stop Motion Opções de Hambúrguer (`DZYP...`) | Variedade de Cardápio | 4.2/5 | Retenção boa nos primeiros segundos |
| 2 | Simulação de Ligação FaceTime (`DZbb...`) | Gancho Curioso / Food Porn | 4.9/5 | Quebra de padrão forte, alto thumbstop |
| 3 | Card Dia dos Namorados "Ge Para Dois" (`DZbEXWrz_FP.jpg`) | Combo Casal / Data Sazonal | 4.7/5 | Preço R$ 89,00 na peça, oferta clara |
| 4 | Foto casal no salão (`DZduZVxTA9Q.jpg`) | Casal / Experiência no Salão | 3.8/5 | Bom pra retargeting, não pra topo de funil |
| 5 | Encontro de Casal no Salão (`DZg...`) | Prova Social / Experiência no Salão | 3.5/5 | Bom pra tráfego local |
| 6 | POV Baixar Gastos (`DZt...`) | Humor | 2.2/5 | Só engajamento orgânico |
| 7 | Carrossel GE KIDS (`DZ3VlIplB7U`) | Produto Infantil / Público Família | 4.5/5 | Segmentação pra pais |
| 8 | Apresentação GE BOX, unboxing (`DZ9...`) | Unboxing / Produto / Compartilhamento | 4.8/5 | Demonstra bem o produto |
| 9 | Trend Before/After carne crua → pronta (`EAE...`) | Appetite Appeal / Food Porn | 4.9/5 | Alta retenção, formato clássico |

**Detalhe dos 3 mais fortes:**

- **Simulação de Ligação FaceTime** (~25s): abre simulando tela de
  chamada do iPhone ("GEBURGER Está chamando..."), atende e corta pra
  Food Porn de chapa e montagem. Produto não aparece nos 2s iniciais
  (a tela de chamada segura o gancho), mas o gancho é o ponto forte.
- **Trend Before/After** (~10s): "BEFORE" mostra carne crua na chapa,
  "AFTER" mostra hambúrguer pronto com molho caindo. Produto aparece
  nos 2s iniciais. Formato clássico de transformação.
- **Apresentação GE BOX** (~42s): atendente entrega a GE BOX no salão,
  unboxing, amigas provando os mini-hambúrgueres com narração
  explicativa. Rosto aparece.

---

## Lote 7 (01/07/2026 a 28/07/2026)

| # | Vídeo/mídia | Duração | Ângulo | Nota Ads |
|---|---|---|---|---|
| 1 | Lançamento Queijo Coalho Empanado (`DaRJwnyFLXO`, vídeo) | ~5s | Lançamento / Appetite Appeal / Entrada | 4.8/5 |
| 2 | Carrossel Raio-X Queijo Coalho (`DaRJwnyFLXO_02.jpg`) | — | Raio-X de Produto / Entrada | 4.6/5 |
| 3 | Carrossel Sabor e Experiência (`DaWNZCpFE5E_01 e 02.jpg`) | — | Appetite Appeal / Experiência Completa | 4.3/5 |
| 4 | Burger de Milhões (código truncado pelo Gemini, `Da...`) | ~8s | Meme / Trend / Oportunismo (Copa) | 3.0/5 |
| 5 | Meme da Dívida e Hamburgueria (`Da...`) | ~12s | Humor Relacionável / Meme | 3.5/5 |
| 6 | Meme Inscrição na Academia (`Da...`) | ~16s | Humor de Atuação / Apresentação do Cardápio | 3.9/5 |
| 7 | Tour de Localização Parque 10 (`Da...`) | ~25s | Geo-localização / Tour pelo Salão / Consideração | **4.9/5** |
| 8 | Lançamento Hotdog na Chapa (`Da...`) | ~45s | Novo Produto / Bastidores / Food Porn | 4.4/5 |
| 9 | Pensamentos Intrusivos (`Da...`) | ~8s | Humor de Atuação / Relacionável | 2.5/5 |

URL confirmada pelo Gemini só pros itens 1 e 3 (posts com imagem):
`instagram.com/p/DaRJwnyFLXO/` e `instagram.com/p/DaWNZCpFE5E/`. Os
itens 4 a 9 são vídeo puro e o Gemini nunca escreveu o código completo
(ficou truncado com "..."), então a URL desses **não está confirmada**.

**Cena a cena dos 3 mais fortes (o resto está resumido, ver acima):**

- **Tour de Localização Parque 10** (nota mais alta do lote, 4.9/5):
  0-5s takes noturnos da rua e fachada ("No Parque 10 tem um lugar que
  você precisa conhecer... Rua Alexandre Magno, 497"); 6-10s tour pelo
  ambiente interno instagramável; 11-20s preparo das carnes na chapa e
  unboxing da Ge Box; 21-25s close do lanche fechado com molho.
  Locução em off, sem rosto aparecendo. **Esse é o vídeo que mais bate
  com o ângulo "bairro/proximidade" que já defini em
  `03-inteligencia-criativa.md`** e já existe pronto, não precisa
  gravar de novo.
- **Lançamento Hotdog na Chapa** (~45s): apresentadora anuncia o
  lançamento (rosto aparece, produto não nos 2s iniciais), depois
  processo completo do hotdog prensado na chapa (salsicha, molho,
  maionese, bacon crocante, batata palha, prensagem).
- **Lançamento Queijo Coalho Empanado** (~5s, nota 4.8): mão mergulhando
  o queijo coalho empanado na geleia de cupuaçu, texto "EXPERIMENTE
  NOVIDADE NO CARDÁPIO". Produto aparece de cara.

---

## Lote 8 (31/07/2026 a 08/08/2026)

| # | Vídeo/mídia | Duração | Ângulo | Nota Ads |
|---|---|---|---|---|
| 1 | Fritas Melted com Cheddar e Bacon (`Dbe...`) | ~32s | Appetite Appeal / Food Porn / Acompanhamento | **5.0/5** |
| 2 | Unboxing de Delivery (`Dbg...`) | ~27s | Delivery / Prova Social / Fidelização (ímãs) | 4.8/5 |
| 3 | Nivelação de Fome, pequena/média/grande (`Dbg...`) | ~14s | Ancoragem de Opções / Ticket Médio | 4.7/5 |
| 4 | Print do WhatsApp / Bloqueio (`Dbg...`) | ~11s | Meme / Humor Nativo / WhatsApp | 4.5/5 |
| 5 | Compilation Food Porn (`Dbg...`) | ~47s | Product Appeal / Bastidores / Retenção | 4.9/5 |
| 6 | Carrossel Raio-X de Ingredientes (`Dbg8TTSFOJB`) | — | Raio-X de Produto / Detalhamento | 4.4/5 |
| 7 | Foto Lançamento GE BOX PRIME (`Dboi0FjzCMj.jpg`) | — | Lançamento de Combo / Ancoragem de Preço | **5.0/5** |
| 8 | Split Screen 3 Cenas (`Dby...`) | ~15s | Experiência Completa / Multi-tela | **5.0/5** |

URL confirmada: item 6 `instagram.com/p/Dbg8TTSFOJB/`, item 7
`instagram.com/p/Dboi0FjzCMj/`. Os demais vídeos (1 a 5, 8) ficaram com
código truncado, sem URL confirmada.

**Cena a cena dos 3 com nota 5.0/5:**

- **Fritas Melted**: 0-5s batatas fritas caindo no prato de metal; 5-15s
  cobertura de creme de cheddar em cascata; 15-25s chuva de bacon em
  cubos; 25-32s close final com selo de encerramento da marca. Sem
  legenda queimada (ponto fraco pra rodar no mudo).
- **Foto GE BOX PRIME**: banner oficial "2 Burgers + Ge Fritas + Ge
  Balls POR R$ 96,00 - NOVIDADE IMPERDÍVEL". Preço na peça, pronto pra
  anúncio de combo. **Atenção: confirmar se R$ 96,00 ainda é o preço
  vigente antes de reaproveitar essa peça em anúncio novo** (regra do
  `swipe-file.md`, nunca prometer preço desatualizado).
- **Split Screen 3 Cenas** (~15s): tela dividida em 3 simultâneas,
  "PARA COMEÇAR" (queijo coalho na geleia), "PARA SE REFRESCAR"
  (milkshake), "PARA SE DELICIAR" (mordida no hambúrguer). **Atenção:
  esse vídeo mostra um milkshake**, mas o levantamento de concorrência
  (`dossie-ifood-concorrentes-manaus.md`) registrou que o Geburger não
  tem milkshake no cardápio ainda. Confirmar se esse milkshake é um
  produto real vigente ou se é conteúdo antigo/descontinuado antes de
  usar como anúncio, senão promete produto que não existe mais.

**Unboxing de Delivery**, que também é forte (4.8/5): cliente abre o
pacote, tira a batata, desembala o burger, mostra o ímã colecionável
("Acumulando 10 ímãs você troca por 1 GE SALAD"). Rosto aparece.
Ângulo de fidelização, bate direto com o "Vídeo Ímãs do Site" do Lote 10
(ver abaixo), são conceitos irmãos.

---

## Lote 9 (09/08/2026 a 14/08/2026)

| # | Vídeo/mídia | Data | Ângulo | Nota Ads |
|---|---|---|---|---|
| 1 | Carrossel Dia dos Pais (`Db1VD2CFB3B`) | 09/08 | Data Sazonal / Família / Branding Emocional | 3.2/5 |
| 2 | Carrossel Trend "Achamos Chique" (`Db9KxS-lJnY`) | 12/08 | Meme Trend / Desejo / Prova Social | 4.8/5 |
| 3 | Montagem na Chapa (`Db_wJU3ztha.mp4`) | 13/08 | Appetite Appeal / Food Porn / Processo Artesanal | 4.9/5 |
| 4 | Carrossel Conceito de Ingredientes (`DcCSEdfD3_u_01 e 02`) | 14/08 | Conceito / Ingredientes Frescos | 3.0/5 |

URL confirmada pra todos os 4: `instagram.com/p/Db1VD2CFB3B/`,
`instagram.com/p/Db9KxS-lJnY/`, e `DcCSEdfD3_u/`. O vídeo "Montagem na
Chapa" teve o código completo revelado no nome do arquivo
(`Db_wJU3ztha.mp4`), mas sem URL explicitamente confirmada pelo Gemini
nessa passagem.

**Detalhe:**

- **Trend "Achamos Chique"** (carrossel 4 imagens, nota 4.8): mesa
  farta ("COISAS QUE ACHAMOS CHIQUE") → GE TROPICAL com cardápio digital
  no celular ("Achamos chique quem pede GE BURGER") → casal abraçado no
  salão → mãos com dois hambúrgueres ("Achamos chique... pedir outro").
  Passeia por delivery, salão e variedade num formato leve.
- **Montagem na Chapa** (~32s, nota 4.9): 0-3s selagem dos pães; 4-11s
  smash das carnes com prensador e sal; 12-22s montagem com cheddar
  derretido, bacon, cebola caramelizada; 23-32s molho especial e
  fechamento. Sem legenda queimada, sem rosto. Clássico de retenção por
  apetite.
- **Conceito de Ingredientes** (nota mais baixa do lote, 3.0): cebola
  roxa e tomate em macro, "A vida nos deu CEBOLA ROXA" / "A vida nos deu
  TOMATE". O Gemini marcou como fraco sozinho, sem a revelação do
  produto final. **Esse carrossel continua no Lote 10** (mesmo código
  `DcCSEdfD3_u`, slides 3 a 6), ver abaixo.

---

## Lote 10 (14/08/2026 a 20/08/2026)

| # | Vídeo/mídia | Data | Ângulo | Nota Ads |
|---|---|---|---|---|
| 1 | Carrossel Ingredientes → GE SALAD, slides 3-6 (`DcCSEdfD3_u`, continuação) | 14/08 | Raio-X de Ingredientes / Revelação de Produto | 4.5/5 |
| 2 | Foto Infográfico GE BOX PRIME (`DcHehkuzoQQ.jpg`) | 16/08 | Ancoragem de Valor / Componentes de Combo | 4.9/5 |
| 3 | Carrossel Combos Casal e Família (`DcPTEublL97`) | 19/08 | Combos Estruturados / Ticket Médio | **5.0/5** |
| 4 | Vídeo Fidelidade / Ímãs do Site (`DcR73X-TTuO.mp4`) | 20/08 | Programa de Fidelidade / Tráfego pro Site | **5.0/5** |

**Este lote fecha o carrossel iniciado no Lote 9**: os slides 3 a 6 de
`DcCSEdfD3_u` mostram alface, molho rosé, cheddar, até a entrega final
do GE SALAD nas mãos ("Nós fizemos o GE SALAD"). Junto com os slides 1-2
do Lote 9, formam um carrossel único de 6 imagens, não são dois
criativos separados. **Ao contar candidatos a anúncio, tratar como 1
peça só, não 2** (evita duplicar na contagem final).

**Os dois mais fortes do lote:**

- **Combos Casal e Família** (carrossel, nota 5.0): slide 1 "Ge Para
  Dois" (2 burgers + fritas + refri 1L), slide 2 "Ge Família" (2 Ge
  Salads + 2 Ge Burgers + 2 Batatas + refri 1.5L), slide 3 hambúrgueres
  em destaque ("ESCOLHA A MELHOR OPÇÃO PRA VOCÊ"). **Confirmar preço e
  composição atual desses combos antes de usar**, mesma regra de sempre.
- **Vídeo Ímãs do Site** (~32s, nota 5.0): gancho direto "Pedir pelo
  nosso site pode te dar hambúrguer grátis?", bastidores do pedido,
  entrega do ímã, cliente colando na geladeira cheia de colecionáveis.
  Rosto aparece, locução clara. **Esse é o criativo que o próprio
  Gemini apontou como melhor peça pra migrar cliente de marketplace pro
  canal próprio** (ver Top Criativos abaixo). Ângulo de fidelização
  combina direto com o programa de ímãs que também aparece no
  Unboxing de Delivery do Lote 8.

---

## Top Criativos Recomendados pelo Gemini (síntese dele, não minha)

Isso é a leitura final que o próprio Gemini deu depois de ver os Lotes
7 a 10 (não incluiu o Lote 6 nessa síntese, atenção):

1. **Vídeo Ímãs do Site** (`DcR73X-TTuO.mp4`, Lote 10) — nota 5.0/5:
   melhor peça pra campanha de conversão no site próprio, reduz
   dependência de marketplace
2. **Foto GE BOX PRIME** (`Dboi0FjzCMj.jpg` do Lote 8 e
   `DcHehkuzoQQ.jpg` do Lote 10) — nota 5.0/5: alta conversão pra
   ticket mais alto no delivery
3. **Vídeo Fritas Melted** (Lote 8) — nota 5.0/5: melhor criativo pra
   atração de novo cliente, topo de funil
4. **Tour Parque 10** (Lote 7) — nota 4.9/5: essencial pra campanha de
   tráfego local pra loja física

## Minha leitura em cima disso (cruzando com `03-inteligencia-criativa.md`)

- **Já existe material pronto (ou quase) pra 3 dos 6 ângulos que
  defini**: produto (Montagem na Chapa, Fritas Melted, Trend
  Before/After), bairro/proximidade (Tour Parque 10) e prova
  social/timing leve (Trend "Achamos Chique"). Isso muda a prioridade
  do `swipe-file.md`: talvez não precise gravar os 4 roteiros do zero,
  dá pra testar esse material existente primeiro enquanto a Tifany grava
  o resto
- **Ângulo "pedido certo / entrega no prazo" (roteiro 2 do
  swipe-file) continua sem nenhum vídeo correspondente** em nenhum dos
  5 lotes. Esse aqui precisa ser gravado do zero mesmo
- **Risco real, não hipotético**: pelo menos 2 peças (Split Screen com
  milkshake, combos "Ge Para Dois"/"Ge Família") citam produto ou preço
  que precisam de confirmação antes de qualquer uma virar anúncio.
  Isso vale a regra 14 do `CLAUDE-TRAFEGO.md` (nunca prometer preço
  diferente do cardápio)
- **Nenhuma nota do Gemini usou métrica real de performance** (views,
  curtidas). São notas de leitura visual/estratégica. Antes de escalar
  verba em cima de qualquer um desses, vale cruzar com o que o CSV
  realmente mostra de engajamento, que é justamente o que
  `prompt-analise-videos-gemini.md` pede e essa rodada do Gemini não
  fez

## Próximo passo

1. Decidir se vale completar a lacuna dos Lotes 1-5 (vídeos de
   2023/2025 e abril-maio/2026) ou se o material de junho em diante já
   é suficiente pra fechar o lote de setembro
2. Rodar o `prompt-analise-videos-gemini.md` (ou uma versão adaptada
   dele nessa mesma conversa do Gemini) pra cruzar os vídeos já
   analisados aqui com as métricas reais do CSV
3. Confirmar preço/produto vigente das peças sinalizadas acima (Split
   Screen milkshake, GE BOX PRIME R$ 96,00, combos casal/família) antes
   de aprovar qualquer uma pra virar anúncio
4. Cruzar o Top 4 do Gemini + os achados fortes do Lote 6 e 9 com a
   matriz de 12 combinações do `03-inteligencia-criativa.md`
