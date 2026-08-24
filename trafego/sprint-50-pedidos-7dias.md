# Sprint: 50 pedidos em 7 dias

Definido com o Jonas em 22/08/2026. Objetivo: 50 pedidos atribuídos ao
tráfego pago (canal Site Delivery/SAIPOS) em 7 dias corridos. Verba aberta,
"o necessário pra trazer o melhor resultado".

## A conta

Base real, últimos 90 dias (`baseline.md`, extraído do MCP da Meta):
- 210 compras em 90 dias = **2,33 pedidos/dia** de ritmo atual
- CPA medido pelo pixel: **R$ 34,29**
- Investimento médio: R$ 80,01/dia

Meta: 50 pedidos em 7 dias = **7,14 pedidos/dia**, ou seja, **3,06x** o ritmo
atual. Isso não é ajuste fino, é salto de volume, e precisa ser tratado como
tal.

**Capacidade da cozinha não é o limite aqui.** 30 pedidos/hora no pico
suporta 7,14 pedidos/dia com folga enorme. O limite real é o leilão e a
estrutura da conta.

## Por que não dá pra simplesmente multiplicar o CPA atual por 3x

Dois efeitos puxando em direção contrária:

**Pra pior:** aumentar orçamento rápido reinicia fase de aprendizado, e a
conta hoje está fragmentada (147 conjuntos com status ativo no histórico,
ver `00-auditoria.md`). Conjunto fragmentado nunca acumula as ~50
conversões/semana que a Meta pede pra sair do aprendizado, o que historicamente
mantém o CPM e o CPA instáveis.

**Pra melhor:** os principais vazamentos já identificados têm conserto
rápido, não dependem de verba nova:
- Consolidar público fragmentado: o próprio Meta estima até 7% menor custo
  por conversa só nisso (+19 pontos de Opportunity Score)
- Ampliar raio de mídia de 5 km pra 6 km, batendo com o raio real de entrega
  confirmado no Saipos (`dados/saipos-raio-entrega-taxas-2026-08-22.md`)
- Trocar o criativo do conjunto com fadiga confirmada (até 31% mais
  resultado segundo o Meta)
- Corrigir os 6 erros de entrega que hoje travam anúncio sem ninguém notar

## Faixa de orçamento recomendada

Não dá pra cravar um número exato sem rodar e medir, então trabalho com
faixa e ponto de checagem, não promessa fechada.

| Cenário | CPA assumido | Custo pra 50 pedidos | Por dia (7 dias) |
|---|---|---|---|
| Conservador (escala fria, sem arrumar estrutura antes) | R$ 43 | R$ 2.150 | R$ 307 |
| Base (estrutura arrumada antes de escalar) | R$ 34 a 36 | R$ 1.700 a 1.800 | R$ 243 a 257 |
| Otimista (conserto rende o que a Meta estima) | R$ 31 | R$ 1.550 | R$ 221 |

**Recomendação: orçar R$ 1.800 a R$ 2.200 pra semana (R$ 260 a 315/dia)**,
partindo já com a estrutura consolidada (não escalar em cima da bagunça
atual), e conferir no dia 3 se o ritmo bate com 50/7. Se o CPA do dia 3
estiver descolado da faixa base, ajusto o resto da semana em vez de deixar
sangrar até domingo.

**Ressalva de medição:** esse CPA é o que o pixel do Meta mostra, com EMQ
nota 3 (correspondência fraca). O número real de pedido (Saipos) pode ser
maior que o atribuído. Ainda assim, uso o número do pixel como régua de
controle durante a semana, porque é o único que dá pra olhar todo dia. No
fechamento, bato com o relatório de vendas do Saipos pra saber o resultado
de verdade.

## O que precisa estar pronto antes de ligar essa verba

1. Decisão sobre a campanha de Engajamento ainda ativa (Jonas disse que quer
   entender o motivo antes de mexer, ver `estado-atual.md`). Enquanto ela
   roda em paralelo, ela não compete pelo orçamento desse sprint, mas também
   não ajuda a bater os 50 pedidos
2. Consolidação dos conjuntos fragmentados numa campanha de Purchase limpa
3. Correção dos 6 erros de entrega
4. Ajuste do raio de mídia pra 6 km
5. Pelo menos 1 criativo novo pra substituir o que está com fadiga confirmada

## Critério de morte

Se no dia 4 (metade do sprint) o ritmo estiver abaixo de 15 pedidos
acumulados (metade de 25, que seria o ponto médio esperado), paro de
aumentar orçamento e reviso oferta e criativo antes de continuar gastando.
