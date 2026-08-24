# 03, Inteligência de mercado e criativos (FASE 3)

**Início: 23/08/2026.** Motivo de priorizar agora: criativo depende da
Tifany (social mídia), que atende Geburger e Oka Guaraná ao mesmo tempo.
Jonas quer o material pronto pra gravar antes do início de setembro, então
essa fase anda em paralelo com a FASE 1 (rastreamento) em vez de esperar
ela fechar 100%.

## O que já tínhamos antes de abrir esta fase

- `concorrentes-manaus.md`: lista dos 10 concorrentes diretos, com nota do
  Jonas sobre cada um
- `referencias-brasil-125.md`: ranking nacional McCain Hambúrguer Perfeito
  2025, JSK Burgers em #25 e Burgers & Burgers em #7
- `dossie-ifood-concorrentes-manaus.md`: cardápio, preço, avaliação e
  sentimento real de review de cada concorrente. **Esse arquivo é a fonte
  mais forte que temos pra ângulo de criativo**, porque tem reclamação e
  elogio real de cliente, não achismo

## Biblioteca de Anúncios da Meta: o que deu pra confirmar hoje

Testei busca por nome de concorrente (JSK Burgers, Dome's Burgers,
Burgers & Burgers, Jota's Burgers), país Brasil, só ativos.

**Confirma o que `concorrentes-manaus.md` já tinha registrado: a busca por
termo não filtra por cidade nem por página específica de forma confiável.**
Buscar "Dome's Burgers" ou "Burgers e Burgers" devolveu milhares de
resultados de hamburguerias de todo o Brasil sem relação nenhuma com Manaus
(a palavra "burger" sozinha já polui a busca). Não dá pra usar assim.

**Único achado real e específico: JSK Burgers.** A página oficial
("JSK Burgers - O Melhor Burger de Manaus", `page_id 558792854137314`) tem
hoje **só 8 anúncios ativos no total** na conta toda (a maior parte sem
texto de criativo capturado pela busca, então não deu pra ler o gancho).
Achado que vale registrar: o nome da própria página já usa a promessa
como identidade ("O Melhor Burger de Manaus"), não só no anúncio. É um
ângulo de posicionamento direto que dá pra copiar a lógica sem copiar a
frase.

**Conclusão prática:** a Biblioteca de Anúncios não vai ser fonte
confiável de inteligência criativa pra concorrente local pequeno/médio de
Manaus com a ferramenta atual. Não vou insistir nela sem um jeito melhor
de filtrar (teria que ser página por página, e a maioria dos concorrentes
não apareceu nem por nome exato). **A fonte real que temos é o dossiê do
iFood**, que já tem produto, preço e a voz do cliente de verdade.

## Ângulos identificados (com origem no dado, não em achismo)

| Ângulo | De onde vem | Por quê funciona |
|---|---|---|
| **Pedido certo, entrega no prazo** | Geralds Burger (mesmo bairro, Parque Dez): nota 3.6 derrubada por 2 reclamações reais de atraso e item errado, não de sabor | É a abertura mais direta que temos: concorrente do mesmo bairro com problema documentado que não é produto, é operação. Criativo pode prometer o que o outro não entrega, sem precisar inventar superioridade de sabor |
| **Prova de qualidade real, não number-flex** | Geburger tem 94 avaliações contra 4.450 do Jota's e 2.014 do JSK | **Não comparar número direto**, perderíamos feio. Em vez disso, usar depoimento real e específico (se existir print ou vídeo de cliente satisfeito) em vez de "nota 4.9" genérico, que todo mundo tem |
| **Produto na tela, queijo derretendo, chapa** | Template padrão do `CLAUDE-TRAFEGO.md`, reforçado pela regra 8 da lista de erros: nunca usar foto de banco de imagem, food local vende com produto real | Gancho mais barato de produzir e o que mais converte em food local segundo o próprio playbook que já definimos |
| **Preço de entrada / ticket baixo pra quem nunca pediu** | Nosso Ultra Burger 100g a R$ 27,90 está na faixa mais barata do levantamento (mercado vai de R$ 19,90 a R$ 68,95) | Ângulo de aquisição, não de fidelização. Serve pra quem nunca comprou decidir testar com risco baixo |
| **Bairro / proximidade** | Loja em R. Alexandre Magno, 497, Parque Dez de Novembro; mídia já roda raio de 5 km | "Seu vizinho fez esse hambúrguer" é mais barato de crer do que promessa genérica de sabor |
| **Sexta e fim de semana à noite** | Regra fixa do `trafego/CLAUDE.md`: hambúrguer concentra demanda à noite, pico sexta a domingo | Timing de veiculação, não só de roteiro: o mesmo criativo rende mais publicado/impulsionado nesses dias e horário |

**Ângulo que decidi não incluir agora:** sobremesa/milkshake (3 concorrentes
têm, Geburger não tem nenhum). É oportunidade real de ticket médio, mas
não existe produto pra filmar ainda. Fica registrado pra FASE 4
(`04-ofertas.md`), não entra no roteiro de setembro.

## Template de análise de criativo (referência fixa, usar em toda leitura futura)

- **Gancho (0-3s):** o que segura o polegar. Produto na tela ou dor real
  (ex: "pediu hambúrguer e demorou 1 hora?")
- **Ângulo:** qual da tabela acima
- **Formato:** vertical 9:16, Reels nativo (não anúncio estático
  redimensionado), legenda queimada na tela (sem depender de áudio)
- **Estrutura por bloco de segundo:** ver roteiros em `swipe-file.md`
- **Elementos técnicos obrigatórios:** produto real aparece nos 2 primeiros
  segundos, formato 9:16, legenda embutida, sem trilha protegida por
  direito autoral sem licença (Meta já rejeitou anúncio da conta por
  música licenciada, ver `00-auditoria.md`)
- **Métrica alvo:** julgar só depois de 3 dias ou 1.000 impressões (regra 5
  da lista de erros). Hook rate e hold rate primeiro, CTR e CPA depois

## Matriz de teste: Ângulo x Formato x Oferta

12 combinações mínimas, cada uma com roteiro completo em `swipe-file.md`.
Produto e preço usados são os que já existem no cardápio real (ver
`dossie-ifood-concorrentes-manaus.md`), nenhum preço foi inventado.

| # | Ângulo | Formato | Produto/oferta usado | Prioridade pra 1ª semana |
|---|---|---|---|---|
| 1 | Produto (queijo derretendo) | Reels making-of, chapa | Ge Classic (já é o produto do post/criativo atual) | ✅ Sim |
| 2 | Pedido certo / entrega no prazo | Reels depoimento ou tela com texto + produto | Genérico, qualquer combo | ✅ Sim |
| 3 | Preço de entrada | Reels produto + texto de preço na tela | Ultra Burger R$ 27,90 | ✅ Sim |
| 4 | Bairro / proximidade | Reels externa da loja + entrega saindo | Genérico | ✅ Sim |
| 5 | Produto (montagem em câmera lenta) | Reels slow motion | Ge Amazônico ou Ge Rib R$ 47,90 | Não |
| 6 | Sexta à noite | Reels clima/ambiente noturno da loja | Genérico | Não |
| 7 | Prova social (depoimento real) | Reels UGC, cliente comendo | Genérico | Depende de ter cliente disponível pra filmar |
| 8 | Preço de entrada | Estático/carrossel cardápio + preço | Ge Fritas R$ 19,90 + Ge Balls R$ 25,90 | Não |
| 9 | Produto (close no corte/recheio) | Reels close-up | Ge Classic | Não |
| 10 | Bairro / proximidade | Stories bastidor cozinha | Genérico | Não |
| 11 | Grupo/compartilhar | Reels produto grande | Ge da Galera R$ 179,90 (serve 5) | Não |
| 12 | Pedido certo / entrega no prazo | Estático, tela com promessa de prazo | Genérico | Não |

**Prioridade pra 1ª semana (itens 1 a 4):** são os 4 roteiros mais simples
de produzir (não dependem de cliente disponível, nem de câmera lenta
técnica) e cobrem os 4 ângulos com mais lastro de dado. Serve de primeiro
lote antes de setembro.

## Volume de produção: pergunta que trava o planejamento

O `CLAUDE-TRAFEGO.md` manda eu dizer quantos criativos novos por semana o
orçamento justifica. **Não consigo calcular isso sem saber quanto tempo a
Tifany dedica ao Geburger especificamente**, já que ela também atende o
Oka Guaraná. Preciso de 1 resposta sua:

- Quantos dias por semana (ou quantas horas) a Tifany reserva pro Geburger?
- Ela grava sozinha (com celular) ou precisa de alguém segurando câmera /
  aparecendo no vídeo?

Sem isso, a matriz de 12 fica no papel, mas não dá pra prometer quantos
saem prontos por semana. **Sugestão de ponto de partida, pra não travar a
Tifany esperando resposta:** os 4 roteiros marcados como prioridade (✅
acima) cabem numa tarde de gravação na loja, todos reaproveitam a mesma
visita.

## Próximo passo

1. Jonas responde a pergunta de capacidade da Tifany acima
2. Tifany grava os 4 roteiros prioritários de `swipe-file.md`
3. Material bruto sobe pra pasta `trafego/criativos/`
4. Eu reviso antes de subir como anúncio: título, texto principal, CTA e
   conferência de preço contra o cardápio real (regra 14 da lista de erros)
