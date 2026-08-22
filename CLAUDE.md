# Geburger, instruções gerais

## Quem sou eu

Jonas, Manaus/AM. Desenvolvedor frontend e tech lead de dia, dono de negócio
de alimentação. Leigo em tráfego pago e marketing.

Também toco o Oka Guaraná, que tem repositório próprio (`oka-guarana`). São
negócios separados: não misture número, decisão nem campanha de um com o outro.
Quando algo for aprendizado transferível de lá para cá, diga explicitamente que
o dado é do Oka e que precisa ser validado no Geburger antes de virar decisão.

## O negócio

Geburger, hamburgueria em Manaus/AM.

Unidades: 1 confirmada até 22/08/2026, "Ge Burger", ID 62061 no Saipos.
Não confirmado se existe mais alguma unidade.

Endereços: [preencher]

WhatsApp de atendimento: [preencher]. Site de pedido: [preencher, delivery
próprio aparece como canal "Site Delivery (SAIPOS)" nos relatórios]

Canais de venda confirmados (jan a 22/08/2026): iFood (1.134 pedidos,
R$ 70.937,61), site/delivery próprio via Saipos (822 pedidos,
R$ 74.266,70), telefone (285 pedidos, R$ 22.571,11), 99Food (66 pedidos,
R$ 4.283,92, só a partir de abril/2026), além de balcão, mesa e ficha
vendidos direto no PDV. Facebook e WhatsApp como canal de venda registrado:
0 pedidos no período. Ver `operacao/unidades/ge-burger.md`.

Sócios e papéis: [preencher]

Atendimento de WhatsApp: [preencher, quem faz]

Estrutura societária: [preencher: CNPJs, contas bancárias, modelo de compras]

Ticket médio: [preencher por canal. Dado bruto de vendas já está em
`operacao/dados/vendas-por-periodo-62061-2026-01-a-08.md`, falta calcular
por canal especificamente]

Margem de contribuição por lanche: [preencher. Fichas técnicas e custo
médio de insumo já levantados em `operacao/06-estoque-ingredientes-e-fichas.md`,
mas custo médio pode estar distorcido: 44% dos itens de estoque estão com
saldo negativo, ver o mesmo arquivo antes de usar o número]

## Ferramentas

- PDV e financeiro: Saipos (mesmo sistema do Oka Guaraná)
- Plataforma do delivery próprio: aparece como "Site Delivery (SAIPOS)" nos
  relatórios de venda. Não confirmado se é o Cardápio Web do Saipos ou outra
  plataforma integrada
- Fidelidade e CRM: [preencher]
- Marketplaces: iFood e 99Food confirmados
- Automação: [preencher]
- Tráfego pago: Meta Ads, conta de anúncios `708536560751820` ("Gê Burger ->
  Digital Livre"), na mesma BM ("Ge burger") que hospeda a conta do Oka
  Guaraná. Ver `trafego/`

## Como eu quero que você fale

Português brasileiro direto, casual, sem travessão, sem frase de efeito, sem
elogio de cortesia. Número sempre calculado, nunca estimado por impressão.
Se faltar dado, peça o dado específico em vez de responder no genérico.
Explique termo técnico de marketing na primeira vez que usar.

## Como você deve agir

Seja autônomo. Se identificar problema ou oportunidade nos dados, levante a
mão sem eu perguntar. Toda recomendação vem com o que muda, prazo, como medir
e critério de morte.

## Regras de raciocínio que valem para qualquer análise

- Respeite a capacidade da cozinha. Volume acima do que a unidade produz no
  horário de pico gera fila, atraso na entrega e avaliação ruim. Antes de
  propor escala de verba, confirme quantos pedidos por hora a operação aguenta.
- Cada unidade tem raio, público e desempenho próprios. Nunca trate as
  unidades como uma coisa só.
- Hambúrguer tem pico concentrado em noite e fim de semana. Leitura de
  desempenho por dia da semana e por faixa de horário, nunca só a média do mês.
- [preencher: frequência de recompra e janela de LTV usada para avaliar custo
  de aquisição. Definir com dado real antes de usar em conta de CAC]

## Regras de dado

Dado pessoal de cliente (telefone, nome, endereço) não entra neste
repositório em hipótese alguma. Fica no sistema de origem. Aqui só entra
agregado: coorte, taxa de recompra, LTV, contagem.

## Onde as coisas ficam

- `dados/` guarda o que é usado por mais de uma frente
- `decisoes/` guarda o histórico de decisões, um arquivo por decisão
- `operacao/` tem CLAUDE.md próprio com as regras da operação
- `trafego/` tem CLAUDE.md próprio com as regras de tráfego pago

Antes de propor mudança que já foi discutida, leia `decisoes/`. Se a sua
sugestão contraria uma decisão registrada, diga isso explicitamente e
explique o que mudou desde então.

## Estado deste repositório

Criado em 21/08/2026 com a estrutura vazia, espelhando o `oka-guarana`. Os
dados ainda não foram levantados. Enquanto um arquivo estiver marcado com
`[preencher]`, trate o assunto como desconhecido: pergunte ou extraia, não
assuma por analogia com o Oka.
