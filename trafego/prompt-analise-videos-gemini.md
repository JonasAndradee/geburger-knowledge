# Prompt para o Gemini: análise da biblioteca de vídeos do Geburger

Criado em 23/08/2026. Uso: colar no Gemini junto com o link da pasta do
Google Drive (`geburgeroficial`, 65 vídeos, subpasta `posts`,
`geburgeroficial.csv` com métricas e `geburgeroficial.json` com textos).
Objetivo: transformar o histórico de conteúdo orgânico do Instagram numa
lista priorizada de candidatos a virar anúncio pago, encaixados nos
ângulos já definidos em `trafego/03-inteligencia-criativa.md`.

Depois que o Gemini responder, cole o resultado de volta aqui que eu
reviso e já monto o próximo lote de criativos pra testar.

---

## PROMPT (copiar tudo abaixo)

```
Você vai analisar uma biblioteca de vídeos de uma hamburgueria (Geburger,
Manaus/AM) pra eu decidir quais viram anúncio pago no Meta Ads (Instagram
e Facebook). Não é análise de "vídeo bonito", é análise de potencial de
performance como anúncio.

## Materiais na pasta do Google Drive (link vou colar abaixo)

- Cerca de 65 arquivos de vídeo (Reels/posts do Instagram)
- Uma subpasta "posts" (provavelmente imagens ou posts estáticos)
- Um arquivo `geburgeroficial.csv` com métricas dos posts
- Um arquivo `geburgeroficial.json` com os textos/legendas dos posts

Antes de analisar qualquer vídeo, faça isto primeiro:
1. Liste TODO o conteúdo da pasta (nome de arquivo, tipo, tamanho se
   der, subpastas) pra eu confirmar que você enxergou tudo.
2. Abra o CSV e o JSON e me diga: quais colunas/campos existem, qual é a
   chave que liga cada linha do CSV/JSON a um vídeo específico (nome de
   arquivo, ID do post, data, ou outra coisa), e se algum vídeo não tem
   par correspondente no CSV/JSON (ou vice-versa).
3. Se algum vídeo não abrir, estiver corrompido, ou o link de acesso
   falhar, me diga exatamente quais e continue com o resto. Não pule
   isso em silêncio.

Não invente número, métrica ou informação que não está nos arquivos. Se
faltar dado pra responder algum campo abaixo, escreva "sem dado" nesse
campo, não estime.

## O que analisar em CADA vídeo

Monte uma ficha por vídeo com os campos abaixo:

**Identificação**
- Nome do arquivo
- Duração (segundos)
- Data de publicação (se houver no CSV/JSON)
- Legenda original do post (puxar do JSON)
- URL do post no Instagram: o nome do arquivo provavelmente contém o
  código do post (o shortcode que aparece na URL, tipo
  `instagram.com/p/CODIGO/` ou `instagram.com/reel/CODIGO/`). Antes de
  montar a URL pra todos, confirme esse padrão: pegue 3 ou 4 nomes de
  arquivo, veja se o JSON ou o CSV já tem um campo de URL, permalink ou
  ID de post pra esses mesmos itens, e compare se bate com o trecho do
  nome do arquivo. Só depois de confirmar o padrão (ou achar o campo de
  URL já pronto no JSON/CSV), preencha a URL de todos os vídeos. Se não
  der pra confirmar com segurança, não invente a URL: deixe o campo como
  "não confirmado" e explique o que tentou

**Conteúdo, cena a cena**
- Descreva a sequência de cenas do vídeo do início ao fim, com o tempo
  aproximado de cada corte (ex: "0-2s: chapa com blend, 2-5s: montagem do
  sanduíche, 5-9s: mordida, 9-15s: logo e texto final")
- O produto aparece nos primeiros 2 segundos? Sim/não
- Aparece rosto de cliente ou funcionário? Se sim, é alguém falando pra
  câmera (depoimento) ou só aparece de passagem?

**Gancho e estrutura**
- Qual é o gancho dos primeiros 3 segundos (o que prende antes de rolar
  o dedo)? Descreva especificamente, não só "chama atenção"
- Tem CTA (chamada pra ação, tipo "peça agora", "clique no link", "manda
  mensagem")? Se sim, em que segundo aparece e qual é o texto exato. Se
  não tem CTA nenhum, diga explicitamente "sem CTA"
- Tem preço mostrado na tela ou na legenda? Qual valor?
- Tem oferta/promoção mencionada (combo, desconto, "leve 2 pague 1")?

**Ângulo (classifique em um ou mais destes, com base no que o vídeo
realmente mostra, não force encaixe)**
1. Produto (comida em destaque, textura, montagem, queijo derretendo)
2. Pedido certo / entrega no prazo (conferência, embalagem, entrega)
3. Preço de entrada / oferta (foco em valor baixo ou promoção)
4. Bairro / proximidade (fachada da loja, "seu vizinho", localização)
5. Prova social (depoimento real de cliente, reação, comentário)
6. Timing / clima (sexta à noite, fim de semana, "vontade de comer")
7. Nenhum dos acima claramente / bastidor institucional / outro (descreva)

**Checklist técnico pra virar anúncio**
- Formato: vertical 9:16, quadrado, ou horizontal?
- Tem legenda queimada na tela (funciona sem som)? Sim/não
- Tem marca d'água de outro app (TikTok, CapCut, Reels com @ de terceiro)
  visível no vídeo? Isso desqualifica pra anúncio até remover
- A trilha sonora parece ser música comercial protegida (não é som
  ambiente nem trilha de banco livre)? Se sim, marque como risco de
  direito autoral pra anúncio pago (mesmo que funcione como post orgânico)
- Qualidade de imagem: nítida ou com problema visível de foco/luz/
  compressão?
- É conteúdo gravado pela própria loja ou parece repost de terceiro
  (marca d'água, watermark de outro perfil, vídeo que não bate com o
  ambiente da loja)? Marcar como risco se for repost

**Métricas (do CSV, cruzando pelo campo identificado no passo 2)**
- Visualizações, curtidas, comentários, compartilhamentos, salvos (o que
  existir no CSV)
- Taxa de engajamento se der pra calcular com o que existe (ex:
  (curtidas+comentários+compartilhamentos+salvos) / visualizações)
- Se o CSV tiver retenção ou tempo médio assistido, incluir também

## Depois de analisar todos os vídeos, monte 3 saídas

### 1. Tabela-resumo (uma linha por vídeo)
Colunas: nome do arquivo | URL do post no Instagram (ou "não confirmado")
| duração | ângulo(s) | tem CTA (sim/não + qual) | preço mostrado |
formato (9:16 etc) | legenda queimada (sim/não) | risco de direito
autoral (sim/não) | risco de repost de terceiro (sim/não) |
visualizações | engajamento | nota geral pra virar anúncio (1 a 5, com o
motivo em 1 frase)

### 2. Top 15 candidatos a anúncio pago
Ordenados por potencial, não só por métrica orgânica alta (um vídeo pode
ter poucas views só porque foi pouco impulsionado organicamente e ainda
assim ter gancho forte pra anúncio pago, e vice-versa). Para cada um dos
15, justifique em 2-3 frases por que entra na lista e em qual ângulo da
lista acima ele se encaixa melhor. Se dois vídeos forem quase idênticos
(mesma cena, mesmo produto, mesmo gancho), sinalize a duplicidade e
recomende só o melhor dos dois.

### 3. Lacunas encontradas
Depois de ver os 65, me diga: que ângulo da lista de 6 tem pouco ou
nenhum vídeo bom disponível (ou seja, o que eu preciso gravar de novo
porque não existe material aproveitável), e quantos vídeos no total você
classificaria como "prontos pra virar anúncio hoje sem edição" versus
"precisa de edição" (cortar, remover marca d'água, tirar música
protegida) versus "não aproveitável".

## Formato de resposta

Português direto, sem enrolação. Markdown com tabelas de verdade
(renderizáveis), não texto corrido. Se a resposta ficar muito grande pra
caber numa mensagem só, divida em partes e me avise que vai continuar na
próxima.
```

---

## Depois que o Gemini responder

Cole a saída de volta nesta conversa. Eu vou:
1. Cruzar o Top 15 com a matriz de `03-inteligencia-criativa.md` (ver
   quais ângulos já ficam cobertos por conteúdo existente e quais ainda
   dependem só do `swipe-file.md`, gravação nova)
2. Conferir preço de qualquer vídeo candidato contra o cardápio ativo
   antes de aprovar pra anúncio
3. Separar o que precisa só de corte/edição do que precisa gravação nova
