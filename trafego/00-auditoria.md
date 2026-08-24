# 00, Auditoria e diagnóstico (FASE 0)

Rodada em 22/08/2026. Fonte: `00-descoberta.md`, `baseline.md`, `briefing.md`,
dado bruto em `dados/`, mais consultas adicionais ao MCP da Meta feitas nesta
sessão (qualidade e volume do dataset, erros de entrega, opportunity score,
tendência de performance, catálogo, criativos ativos, Biblioteca de Anúncios).

**Regra desta página:** todo item abaixo está marcado como FATO (número
extraído, com fonte) ou HIPÓTESE (leitura minha, ainda sem confirmação). Não
misture os dois na hora de decidir.

---

## 1. Rastreamento: o pixel está mentindo um pouco pra você

**FATO.** Dataset `746769616981227` ("Pixel de Ge burger"), ativo desde
03/2023, disparando agora. Eventos configurados: PageView, ViewContent,
AddToCart, InitiateCheckout, AddPaymentInfo, Purchase.

**FATO.** Qualidade de correspondência (EMQ): nota 3 em AddToCart, PageView e
Purchase. A única chave de correspondência usada é `user_agent`, cobertura de
100%. Não há email, telefone, nome ou outro identificador configurado. Isso é
sinal fraco pro leilão: o Meta sabe que um navegador comprou, mas não consegue
ligar isso com segurança a uma conta real de pessoa, o que piora a
otimização de qualquer campanha de conversão.

**FATO.** Volume dos últimos 7 dias (15 a 22/08): funil caindo forte a cada
etapa, como esperado — mas com um pico de **39 Purchase em uma hora só**, dia
18/08 às 16h (horário de Manaus, ver conversão de fuso no dado bruto). Isso é
quase o dobro do total de Purchase do resto da semana somado. **Preciso que
você confirme:** teve promoção, evento ou pico real de vendas nesse
horário? Se não teve, é sinal de disparo duplicado ou teste de evento indo
pro pixel de produção, o que infla artificialmente o ROAS medido.

**FALTANDO.** Status da API de Conversões (CAPI) ainda não confirmado. O MCP
não tem um endpoint direto de "CAPI ligada sim/não" — isso se confirma no
Gerenciador de Eventos > Fontes de dados > `746769616981227` > aba
Configurações. Sem CAPI, todo o rastreamento depende só do navegador, que
perde evento com bloqueador de anúncio, Safari (ITP) e app do delivery em
WebView.

**FALTANDO.** UTM nos criativos: não verificado ainda. Sem padrão de UTM, os
dados do cardápio próprio (Saipos) e o atribuído pela Meta não batem por
campanha, só no total.

## 2. Catálogo de produtos: não existe

**FATO, confirmado nesta sessão.** `ads_catalog_get_catalogs` retornou zero
catálogos associados à conta. Isso significa: nenhum anúncio dinâmico de
produto é possível hoje, nenhum remarketing "viu o combo X e não comprou",
e a recomendação de menor prioridade da Meta (`gen_ai_mvp`, variações de
imagem por IA) tem menos material de origem pra trabalhar.

Não é bloqueio para o lançamento de 31/08 (catálogo é otimização de fase
mais madura), mas entra no roadmap como item da FASE 1.

## 3. Erros de entrega ativos na conta

**FATO**, lista completa retornada pelo Meta agora:

| Onde | Erro | Efeito |
|---|---|---|
| 2 anúncios | "No Valid Formats": criativo incompatível com os posicionamentos escolhidos | Anúncio não roda em parte do inventário comprado |
| 4 anúncios | "This ad is not delivering" | Zero entrega, verba parada sem ninguém perceber |
| 2 anúncios (Reels) | Música licenciada não pode ser impulsionada | Anúncio nunca vai sair do estado pausado assim |
| 1 anúncio | Mídia orgânica do Instagram foi arquivada | Anúncio órfão, sem post de origem |
| 1 anúncio | CTA de "Otimização de Respostas" só funciona com destino Messenger | Configuração incoerente entre objetivo e destino |
| 1 edição | "Invalid usage of ForceRunStatus" ao tentar editar | Falha ao salvar edição, não é bloqueio de veiculação |

Nenhuma alteração foi feita. Isso é achado, não ação.

## 4. Opportunity Score da conta: 74/100

**FATO**, direto do Meta. Recomendações ordenadas pelo ganho de pontos:

| Recomendação | Ganho estimado | O que significa |
|---|---|---|
| **Fragmentação de público** | **+19 pontos**, até 7% menor custo por conversa | Conjuntos com público sobreposto competindo entre si e mostrando o mesmo anúncio demais pra mesma pessoa. Junte-os. Isso bate direto com a regra "não fragmente" do `CLAUDE.md` |
| Compartilhar evento de compra via WhatsApp/parceiro de mensagens | +1 ponto, até 24% menor custo por compra | Anúncio de clique-pra-mensagem hoje não sabe quem comprou depois da conversa |
| Reels em 9:16 vertical cheio com áudio | +1 ponto, até 8% menor custo por resultado | Formato de criativo, ver FASE 3 |
| Fadiga de criativo no conjunto `120246128291470690` | +1 ponto, até 31% mais resultado | Mesma imagem/vídeo mostrado demais pra mesma audiência, hora de trocar |
| Orçamento pode estar limitando o conjunto `120250462200090690` | +1 ponto | Verba baixa travando entrega |
| Música automática em 2 anúncios | +1 ponto, até 44% menor custo por conversa | Baixo esforço, deixar o Meta escolher trilha |
| Variação de imagem por IA (2 anúncios) | +1 ponto, até 10% mais CTR | Baixa prioridade, depende de material de origem melhor primeiro |

**Leitura:** a fragmentação de público é de longe o maior vazamento de
performance disponível pra corrigir agora, e é ação de estrutura, não de
verba nova.

## 5. Estrutura da conta hoje: fragmentada de fato

**FATO.** 221 conjuntos de anúncio no histórico da conta, **147 ainda com
status ACTIVE no atributo do objeto**, mesmo com só 4 campanhas rodando
agora segundo `00-descoberta.md`. Ou esse número inclui conjunto de campanha
pausada com status próprio ainda ativo (comum e inofensivo), ou há mais
coisa "ligada" do que o esperado. **Vale conferir direto no Gerenciador**
antes de reestruturar, pra não duplicar trabalho de limpeza.

**FATO**, raio de anúncio: todos os conjuntos ativos analisados miram
**5 km ao redor de Rua Alexandre Magno, 497** (endereço da loja), com
segmentação por local de casa/recente (`home`, `recent`). Isso responde o
item 8 do briefing pro lado do anúncio: **raio de mídia = 5 km**. Falta
confirmar se esse raio bate com o raio de entrega real configurado na
plataforma do delivery próprio — os dois podem estar desalinhados (anunciar
pra fora do raio que a loja realmente entrega é erro listado no `CLAUDE.md`).

## 6. Criativos ativos: repetição alta de gancho genérico

**FATO**, a partir da lista de criativos ativos (~50 primeiros, mais existem
via paginação). Padrão de nome/título reaparecendo em datas diferentes:

- "PEÇA AGORA!" e variações ("PEÇA AGORA MESMO!", "Clique e Peça Agora"):
  pelo menos 10 criativos diferentes, de jun a ago/2026
- "A fome bateu? Vem de Ge Burger!": 5 criativos, de mai a ago/2026
- "Peça seu GeBurger 🍔": 8 criativos, de mai a jul/2026
- "GeBurger ⭐⭐⭐⭐⭐ 4.9/5": 3 criativos em jun/2026

**Hipótese:** o texto do anúncio (corpo/título) varia pouco, o que sugere
que a variação real está na imagem ou vídeo por trás, não no ângulo ou na
oferta. Isso é compatível com o achado de fadiga de criativo do Opportunity
Score (seção 4) e com o CTR de link baixo da baseline (0,35%, abaixo do
esperado pra food local, que costuma rodar de 0,9% a 1,5% quando o gancho é
forte). Alguns criativos fogem do padrão promocional puro e usam humor/meme
de relacionamento ("Será que eu bloqueio ela? 😓😭", "Levando à sério a meta
desse mês! Hahaha 🤣") — vale checar se esses têm CTR melhor, é candidato a
ângulo pra escalar.

**Achado técnico:** a `ads_insights_performance_trend` mostrou o anúncio
"ADReels - Imã" (teste de criativo mais recente, campanha ativa) com CTR
**+154% de variação, tendência BOA**, dentro do público de retargeting
otimizando pra compra. Esse é o criativo mais promissor rodando agora,
vale registrar o que ele tem de diferente antes de qualquer coisa.

## 7. Inteligência competitiva: ferramenta testada e funcionando

**FATO.** Busca na Biblioteca de Anúncios da Meta por "hamburgueria" no
Brasil (ativos agora) retornou 15.566 resultados. Amostra trouxe
concorrentes food service atuando com anúncio de clique-pra-WhatsApp, Reels
com gancho de produto ("UM DOS MAIS PEDIDOS DA CASA..."), e uso de emoji
pesado no título. **Limite da ferramenta:** a busca não filtra por cidade,
só por país. Pra achar concorrente específico de Manaus, o caminho é buscar
pelo nome da página depois de eu (ou você) identificar quem são, não por
palavra-chave genérica.

## 8. Os 3 maiores vazamentos de dinheiro, em ordem de impacto

1. **Fragmentação de público** (seção 4 e 5). Maior alavanca de custo
   disponível agora, é reestruturação, não corte de verba. Ganho estimado
   pelo próprio Meta: até 7% menor custo por conversa, +19 pontos de score.
2. **Objetivo errado consumindo verba sem meta de venda.** Histórico: R$ 25
   mil (25% do total já gasto) em objetivo de Engajamento. Ativo agora:
   uma campanha `[MP][Engajamento] - WhatsApp` rodando, mais um post
   impulsionado direto do Instagram (`Post do Instagram: Ge Classic...`)
   otimizando pra "visitar perfil do Instagram", não pra pedido, com CTR
   caindo 56% segundo a tendência de performance. Isso é dinheiro saindo
   sem numerador de venda.
3. **Rastreamento fraco distorcendo a decisão do algoritmo.** EMQ nota 3,
   sem CAPI confirmada, sem catálogo. O ROAS de 1,3 medido na baseline
   provavelmente subestima o retorno real, mas o problema maior é que o
   próprio Meta decide pra quem mostrar o anúncio de conversão com esse
   sinal fraco — mais sinal, melhor decisão de quem recebe o anúncio.

## 9. CAC máximo saudável: ainda não dá pra calcular com segurança

**Bloqueio confirmado, não novo.** Depende de margem de contribuição por
lanche, que depende do CMV, que está distorcido: 44% dos itens de estoque
com saldo negativo no Saipos, incluindo insumo-base de quase todo hambúrguer
(queijo cheddar, brioche, blend). E o DRE Gerencial do Saipos não é
confiável pra esse cálculo agora (91 de 97 categorias sem vínculo de seção).
Ver `../operacao/06-estoque-ingredientes-e-fichas.md` e
`../operacao/02-plano-de-contas.md`.

**Isso não trava o lançamento de 31/08**, mas trava decidir com segurança
até onde vale pagar por um pedido novo. Enquanto isso não resolve, uso como
teto provisório o CPA já observado na baseline (R$ 34,29) como referência
de "não piorar", não como CAC ideal.

## 10. O que ainda falta puxar ou confirmar

- CAPI: status exato (manual, Gerenciador de Eventos)
- UTM nos criativos: não verificado
- Domínio verificado nos Negócios: não verificado
- Instagram Insights orgânico: extração manual, não puxado
- Dados do cardápio próprio (pedido por dia, origem, abandono): depende de
  acesso à plataforma do delivery
- Confirmar se o pico de 39 Purchase em uma hora (18/08) é real
- Confirmar se os 147 conjuntos com status ACTIVE são resíduo inofensivo ou
  precisam de limpeza de fato
