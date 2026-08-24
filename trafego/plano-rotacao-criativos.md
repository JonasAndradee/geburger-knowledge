# Plano de rotação de criativos

Criado em 23/08/2026. Resposta à pergunta: como usar o acervo de criativos
mês a mês, quando entra criativo novo, com que frequência eu analiso, e
quando ativo ou desativo. Isso é um recorte da FASE 5
(`trafego/CLAUDE-TRAFEGO.md`, "Operação, leitura e escala") focado só em
criativo, adiantado porque você pediu a estratégia agora, antes da FASE 2
(arquitetura de campanha) estar fechada. Quando a FASE 2 rodar, esse plano
encaixa dentro da estrutura de campanha que for definida, não muda a
lógica de rotação em si.

**Antes de aplicar isso com dinheiro de verdade, falta fechar 2 coisas:**
1. Capacidade da Tifany (pergunta em aberto desde `03-inteligencia-criativa.md`,
   ainda sem resposta): quantos criativos novos por semana ela consegue
   entregar. Esse plano assume um ritmo, mas o ritmo real depende dela
2. Verba mensal de mídia confirmada (`estado-atual.md`), porque orçamento
   baixo muda quantos criativos simultâneos fazem sentido (regra: cada
   conjunto precisa de volume de conversão pra sair do aprendizado, criativo
   demais com pouca verba fragmenta sinal)

## A lógica em uma frase

Criativo não é "põe e esquece" nem "troca toda hora". É um pipeline com 3
estados (testando, escalando, parado), com decisão semanal baseada em
número, nunca em achismo ou cansaço visual seu.

## Os 3 estados de um criativo

| Estado | O que significa | O que fazer |
|---|---|---|
| **Testando** | Entrou essa semana ou ainda não bateu 3 dias / 1.000 impressões | Não mexer em nada, nem orçamento nem público. Só observar (regra 2 e 5 do `CLAUDE-TRAFEGO.md`) |
| **Validado / escalando** | Bateu o mínimo de teste e CPA está dentro ou abaixo da meta | Pode subir orçamento, no máximo 20% a cada 48-72h (regra de escala do `CLAUDE-TRAFEGO.md`). Nunca dobra de uma vez |
| **Parado** | Foi morto por CPA ruim ou por frequência alta com CTR caindo | Pausa, nunca exclui (histórico fica, regra do repo). Volta a ativar só se for reformulado (imagem/gancho novo), não do jeito que estava |

## Regras de corte e escala (já definidas, só reafirmando aqui aplicado a criativo)

- **Nunca julgar com menos de 3 dias OU menos de 1.000 impressões**, o que
  vier depois. Julgar antes disso é achismo, não dado
- **Matar criativo que gastou 3x o CPA alvo sem conversão** (regra de
  escala do `CLAUDE-TRAFEGO.md`)
- **Frequência**: sem histórico de campanha ativa do Geburger ainda pra
  calibrar um número exato, uso como ponto de partida frequência acima de
  **2,5 a 3** no período com CTR caindo junto como sinal de fadiga. Isso é
  hipótese de trabalho, não regra fechada: depois de 2-3 semanas de
  campanha rodando, ajusto esse número pro que os dados reais do Geburger
  mostrarem
- **Uma variável por vez**: se troca criativo, não mexe em público nem
  orçamento no mesmo dia (regra 4 da lista de erros)
- **Nunca mexer em conjunto que está em aprendizado** só porque "already
  tá rodando há uma semana e não decolou". Aprendizado tem prazo próprio

## Cadência de análise: o que olho e quando

| Frequência | O que fazer | Tempo |
|---|---|---|
| **Diária** | Checar se a verba gastou o previsto, se algum anúncio foi rejeitado/travado, CPA de ontem contra a meta. **Não decide nada aqui, só monitora.** Nunca mexe em conjunto em aprendizado só por causa da leitura diária | ~15 min |
| **Semanal** (toda segunda, olhando os últimos 7 dias) | Decisão de verdade: qual criativo já bateu o mínimo de teste e está validado (escala), qual já bateu o teto de CPA (mata), qual entra novo essa semana. **É aqui que entra ou sai criativo, nunca no meio da semana por impulso** | ~1h |
| **Mensal** | Fechar o mês: DRE de mídia, CAC e ROAS contra a receita real do PDV (não só o atribuído pelo Gerenciador), revisão de quais ângulos da matriz (`03-inteligencia-criativa.md`) estão saturados e quais ainda não foram testados, replanejar produção do mês seguinte com a Tifany | ~2h |

**Resposta direta pra "analiso isso constantemente?"**: não. Monitora
todo dia (rápido, sem mexer em nada), decide toda semana. Decisão diária
é o erro mais comum: você mata criativo bom por impaciência ou reage a
ruído de 1 dia que nem é tendência ainda.

## Quando adicionar criativo novo no meio do mês

Sim, adiciona no meio do mês, mas com gatilho, não em data fixa:

1. **Um criativo validado começou a mostrar fadiga** (frequência subindo
   + CTR caindo por 2 leituras semanais seguidas): entra um substituto do
   mesmo ângulo antes do antigo morrer de vez, pra não ter buraco de
   verba sem criativo bom rodando
2. **Terminou o teste de um novo e ele validou**: ele sobe de "testando"
   pra "escalando", e o próximo da fila entra em teste no lugar dele
3. **Vídeo orgânico novo postado pela Tifany performou bem organicamente**
   (curtida, comentário, salvamento acima da média do perfil): candidato
   a entrar em teste pago, é sinal barato de que pode funcionar pago também
4. **Nunca por acaso ou porque "faz tempo que não muda"**. Toda entrada
   de criativo novo substitui ou complementa um estado específico do
   pipeline, não é feita por rotina de calendário

## Quantos criativos simultâneos

Regra do `CLAUDE-TRAFEGO.md`: leilão da Meta é centrado em criativo, não
em segmentação, e conjunto fragmentado destrói sinal. Isso vale também
pra quantidade de criativo dentro de um mesmo conjunto: criativo demais
sem verba pra sustentar todos dilui teste.

**Ponto de partida sugerido** (a confirmar quando a verba mensal fechar):
- 3 a 4 criativos em teste ao mesmo tempo por conjunto ativo, não mais
  que isso enquanto o orçamento for pequeno
- 1 a 2 validados escalando
- Resto do acervo fica de reserva (testado depois ou arquivado)

## Calendário de um mês típico (modelo, ajustar depois do primeiro mês real)

| Semana | O que fazer |
|---|---|
| **Semana 1** | Sobe os criativos já prontos e validados de preço/produto (ver lista abaixo). Tudo nasce pausado, ativa só com meu OK. Não mexe depois de ativar, só monitora diário |
| **Semana 2** | Primeira leitura semanal de verdade (os criativos da semana 1 já bateram o mínimo de 3 dias/1.000 impressões). Mata o que não performou, mantém ou escala o que performou. Entra o primeiro lote novo da Tifany (os 4 roteiros prioritários do `swipe-file.md`, se já estiverem gravados) |
| **Semana 3** | Segunda leitura semanal. Escala o que validou na semana 2, mata o que não passou. Entra o segundo lote (roteiros 5-8 da matriz, se a capacidade da Tifany permitir) |
| **Semana 4** | Terceira leitura semanal + fechamento mensal: DRE de mídia, CAC real, quais ângulos ainda faltam testar, planeja produção do mês seguinte |

## Para o lote de setembro especificamente

Com o que já existe (ver `analise-gemini-videos-organicos.md`), a
Semana 1 não precisa esperar a Tifany gravar nada do zero, desde que eu
confirme antes:

- **Tour Parque 10** (Lote 7): pronto, ângulo bairro/proximidade
- **Fritas Melted** e **Montagem na Chapa** (Lotes 8 e 9): prontos,
  ângulo produto
- **Vídeo Ímãs do Site** (Lote 10): pronto, ângulo fidelização, mas
  confirmar se o programa de ímãs ainda está ativo do jeito que aparece
  no vídeo antes de rodar
- **GE BOX PRIME** e **combos casal/família**: só entram depois de
  confirmar que preço e composição batem com o cardápio vigente

Isso dá 4 a 6 criativos prontos pra Semana 1, sem depender de gravação
nova. Os roteiros do `swipe-file.md` entram na Semana 2 como já previsto,
e cobrem o ângulo "pedido certo/entrega no prazo" que hoje não tem
nenhum material existente.

## O que fica registrado toda semana

Depois de cada leitura semanal, atualizo `estado-atual.md` com: o que
está rodando, o que foi morto (e por quê, com o número), o que entrou
novo. Isso vira o histórico de qual ângulo já foi testado e qual ainda
não, pra não repetir teste que já morreu antes.

## Próximo passo

1. Fechar capacidade da Tifany e verba mensal (as 2 pendências do topo)
   pra transformar esse plano de modelo em cronograma com data real
2. Confirmar preço/produto das peças sinalizadas em
   `analise-gemini-videos-organicos.md` antes da Semana 1
3. Definir a meta de CPA (depende do CAC máximo, que depende do DRE mais
   confiável, ver `estado-atual.md`) pra calibrar o "3x CPA alvo" que
   mata criativo
