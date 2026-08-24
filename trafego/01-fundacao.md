# 01, Fundação técnica (FASE 1)

Checklist executável. Checado em 22/08/2026, direto no Gerenciador de
Eventos e nas Configurações do Negócio (`business.facebook.com`), com
login do Jonas via navegador. Cada item tem status e a ação que falta.

**Legenda:** ✅ feito · ⚠️ parcial, precisa de ajuste · ❌ falta · 🔒 preciso
da sua decisão antes de mexer

---

## 1. Business Manager

| Item | Status | Detalhe |
|---|---|---|
| Conta de anúncios certa identificada | ✅ | `708536560751820`, confirmada |
| Página do Facebook certa vinculada | ✅ | Geburger, `103681477971070` |
| 2 páginas soltas sem relação aparente | 🔒 | `esthereilish`, `Manaus em Dobro`. Você disse "investigar depois", continua pendente |
| Administrador secundário (backup) | ✅ | Confirmado no Central de Segurança: "você tem pelo menos um outro administrador" |
| Autenticação de dois fatores (2FA) | ❌ | Política exige 2FA de "somente administradores", mas **0 de 4 pessoas ativaram**. É risco real: erro #13 da lista de "erros que eu não posso cometer" do `CLAUDE.md` |
| Verificação da empresa (Business Verification) | ❌ | Status "Não verificada", mas "qualificada para verificação". Não verificada limita acesso a alguns recursos da Meta |
| Catálogo de produtos | ❌ | Confirmado: zero catálogos na conta. Decisão de criar ou não fica pra FASE 4 (depende se vamos usar anúncio dinâmico) |

## 2. Domínio

| Domínio | Status |
|---|---|
| `geburger.com.br` | ✅ Verificado, "pertence a Gê Burger" |
| `geburger.saipos.com` | ❌ **Não verificado** |

**Achado importante:** o domínio real do cardápio próprio (canal "Site
Delivery SAIPOS" nas vendas) é `geburger.saipos.com`, hospedado pelo
próprio Saipos. Isso resolve a pendência do item 10 do `briefing.md`. Mas
é justamente esse domínio, o que recebe o clique do anúncio e onde o
pixel dispara, que **não está verificado**. Verificação de domínio afeta a
prioridade dos 8 eventos configurados na Agregação de Eventos (obrigatório
desde a atualização de privacidade do iOS), então isso precisa ser
corrigido antes de confiar 100% na otimização de conversão.

**Ação:** verificar `geburger.saipos.com` nas Configurações do Negócio >
Fontes de dados > Domínios, e então configurar a prioridade dos 8 eventos
na Agregação de Eventos.

**Achado à parte, fora do escopo de tráfego:** o endereço físico da loja
aparece **diferente em três lugares**:
- `CLAUDE.md` da raiz: R. Alexandre Magno, nº 497, CEP 69054-723
- iFood (cadastro da loja): Rua Perimetral, 495, CEP 69054-726
- Meta Business (razão social Ge Burger LTDA): Rua Arquiteto Renato Braga, 415, CEP 69054-699

**Resolvido em 22/08/2026:** o Jonas confirmou que **R. Alexandre Magno, nº
497** é o endereço físico real da loja. Os outros dois (iFood, Meta
Business) são só vínculo de cadastro de CNPJ usado pra direcionar
campanha, não representam a loja física.

## 3. Mapa de eventos do cardápio

| Evento | Status |
|---|---|
| PageView | ✅ Disparando |
| ViewContent | ✅ Disparando |
| AddToCart | ✅ Disparando |
| InitiateCheckout | ✅ Disparando |
| AddPaymentInfo | ✅ Disparando |
| Purchase (com value e currency) | ⚠️ Disparando, mas com problema de qualidade |

**Achado direto do Gerenciador (aba Ações, alta prioridade):** 17% dos
dados de preço recebidos dos eventos Purchase do site contêm **problema de
formatação ou valor ausente**. Isso afeta direto o cálculo de ROAS que a
Meta mostra: 1 em cada 6 compras conta errado ou não conta valor nenhum. É
prioridade técnica alta, provavelmente um ajuste no código de disparo do
evento (o value não está sendo passado certo em parte dos casos).

## 4. Rastreamento: pixel e CAPI

| Item | Status |
|---|---|
| Pixel do site | ✅ Ativo, disparando |
| API de Conversões (CAPI) | ✅ **Ativa**, via parceiro **Signals Gateway** (produto oficial da Meta), "recebido pela última vez há 1 hora" |
| Configuração do Signals Gateway completa | ⚠️ Falta adicionar o "Signals Gateway Pixel". A própria Meta estima **até 23% de custo por resultado mais baixo** só com isso |
| Qualidade de correspondência (EMQ) | ❌ Nota 3, só por `user_agent`. Sem email nem telefone hasheado no evento |

**Correção do que eu tinha registrado antes:** em `00-descoberta.md` eu
tinha marcado CAPI como "não confirmado". Está errado, CAPI está ativa.
O problema real não é a CAPI estar desligada, é ela não estar mandando
identificador de cliente (email, telefone) junto do evento, por isso o
EMQ continua baixo mesmo com CAPI rodando. É ajuste de payload, não de
ativação.

**Confirmado também do lado do Saipos** (22/08/2026, aba "Acesso e
Conversão" do canal Site Delivery): o token de API de Conversão Meta está
preenchido lá, mesmo pixel `746769616981227` configurado nos dois lados.
**Achado novo, sem causa confirmada ainda:** o Oka Guaraná, na mesma
plataforma Saipos, encontrou um bug real de CAPI disparando `Purchase`
duas vezes por pedido, sem deduplicação. É a hipótese mais forte pro pico
de 39 compras numa hora só (seção 1 de `00-auditoria.md`). Plano de
verificação e correção detalhado em `02-migracao-cardapio-web.md`.

## 5. UTM

❌ **Ainda não verificado.** Preciso abrir uma amostra de criativos ativos
e conferir se o link de destino carrega
`utm_source=meta&utm_medium=paid&utm_campaign=...` etc. Isso é o que
permite bater o relatório do Meta com o relatório de vendas do Saipos por
campanha, não só no total. Fica pra próxima sessão.

## 6. Públicos personalizados

| Item | Status |
|---|---|
| Visitantes do site (30/60/90/180 dias) | ✅ Existem |
| Compradores (30/60/90/180 dias, "2x") | ✅ Existem |
| Engajamento Instagram e Facebook (60/365 dias) | ✅ Existem |
| Lista de clientes do PDV (first-party) | ✅ Existe (`Repediu - Todos os clientes`) |
| Lookalike 1% e 3% de compradores | ❌ **Todos os lookalikes da conta estão INACTIVE.** Zero prospecção por semelhança rodando hoje |

**Ação:** recriar pelo menos um lookalike 1% a partir do público de
compradores ativo (30 ou 90 dias), depois de confirmar que a base tem
volume suficiente. Público morto não serve pra nova campanha.

## 7. WhatsApp

🔒 **Contradição a esclarecer antes de decidir.** Você me disse que o
WhatsApp do Geburger é "app comum, sem API oficial nem automação". Mas nas
Configurações do Negócio existe uma conta cadastrada como **"Geburger,
Aplicativo WhatsApp Business"**, vinculada ao Business Manager. Isso pode
ser só o vínculo básico usado pra anúncio de clique-pra-WhatsApp (não
precisa de API oficial pra isso), ou pode já ter mais estrutura do que
você lembra. **Preciso que você confirme**: esse WhatsApp cadastrado no
Meta é o mesmo número de atendimento? É só o vínculo de anúncio ou tem
API/BSP por trás? Isso decide se a recomendação do Opportunity Score
("compartilhar evento de compra via WhatsApp", até 24% menor custo por
compra) é viável agora ou depende de migrar pra API oficial primeiro.

## 8. Nomenclatura de campanha

✅ Já definida em `CLAUDE.md`: `GEB_[Unidade]_[Objetivo]_[Oferta]_[MMDD]`.
Nenhuma campanha ativa hoje segue esse padrão ainda (nomes atuais usam
colchete tipo `[MP][Conversão]`), aplicar a partir da próxima campanha
nova.

---

## Resumo: o que trava o sprint de 50 pedidos até corrigir

Ordenado por impacto, não por ordem da lista acima:

1. **17% dos eventos Purchase com preço malformado** — corrige antes de
   confiar no ROAS que vai medir o sprint
2. **Lookalike zerado** — sem isso, toda campanha nova de prospecção parte
   de público genérico, não de semelhança com quem já compra
3. **Domínio do cardápio (`geburger.saipos.com`) não verificado** — afeta
   a prioridade de evento na Agregação, o que pode limitar o volume de
   sinal que chega pro leilão
4. **Signals Gateway Pixel incompleto** — 23% de custo por resultado é
   estimativa da própria Meta, ganho relevante de baixo esforço
5. **2FA em zero admin** — não afeta performance, mas é risco de perder a
   conta inteira. Baixo esforço, resolve em minutos

## O que ainda falta checar (não deu tempo nesta sessão)

- UTM nos criativos ativos
- Prioridade dos 8 eventos na Agregação de Eventos
- Dedup exato do CAPI por `event_id` (Signals Gateway costuma cuidar
  disso automaticamente, mas não confirmei o detalhe)
- Detalhe completo da verificação de negócio (o que exatamente falta pra
  completar)
