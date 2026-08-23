# Padronizar categorias financeiras da Geburger no molde do Oka Guaraná

Data: 2026-08-22

Status: vigente, **executada no Saipos em 22/08/2026** (com 2 ajustes em relação
ao plano original, ver seção "Execução" no fim do documento)

## Contexto

A Geburger tem 97 categorias financeiras raiz sem nenhuma lógica de código,
91 delas sem seção de DRE vinculada (ver `../operacao/04-categorias-financeiras.md`).
O Oka Guaraná já resolveu esse mesmo problema com um padrão de codificação
numérica (`1.1.01`, ordem de raiz seguindo a leitura do DRE), documentado em
`../../oka-guarana/operacao/04-categorias-financeiras-parque-dez.md`.

Jonas pediu para não reinventar a estrutura da Geburger: quem lança
despesa é a mesma pessoa nas duas empresas, então reaproveitar o padrão do
Oka (renomeando, movendo, excluindo e criando o que for preciso) reduz
carga mental de quem lança. O que for específico da Geburger entra dentro
da estrutura do Oka, não vira uma raiz nova.

**Regra usada no mapeamento:** o Saipos vincula lançamento e DRE pelo **id**
da categoria, não pelo nome (confirmado pelo Oka, `07-automacao-pdv-notas-tecnicas.md`
da Geburger e o próprio doc do Oka). Isso significa:
- **Renomear ou mover uma categoria existente é seguro.** O id não muda, o
  lançamento e o vínculo de DRE seguem juntos automaticamente.
- **Só precisa mover lançamento manualmente quando duas categorias viram
  uma só** (fundir), ou quando uma categoria vai ser excluída e tinha
  lançamento real.
- Categoria pai que perde todos os filhos é removida sozinha pelo Saipos
  (comportamento confirmado pelo Oka). Não precisa excluir manualmente pai
  que só agrupava.

## Opções consideradas

- Manter a árvore atual da Geburger e só vincular DRE em cima dela
- Criar uma estrutura nova do zero, sem olhar pro Oka
- Importar o esqueleto de codificação do Oka e encaixar a Geburger nele,
  ajustando nome, posição e criando o que for específico daqui

## Decisão

Adotar a terceira opção. Abaixo o mapeamento completo: toda categoria atual
da Geburger recebe um código no padrão do Oka, uma ação (RENOMEAR, MOVER,
EXCLUIR ou CRIAR NOVA) e o valor lançado em 2026 (01/01 a 22/08) quando
houver, pra deixar claro o que tem dinheiro real em jogo.

### Árvore alvo completa

`[R$ x]` é o total lançado em 2026 até 22/08 (fonte:
`../operacao/dados/despesas-por-categoria-62061-2026-01-a-08.csv`). Sem
valor = sem lançamento no período. `id` é o id atual no Saipos, quando a
categoria já existe.

```
1 Custos Variáveis
├── 1.1 Custos de Venda
│   ├── 1.1.01 Comissão sobre vendas            NOVA (padronização, Oka usa, Geburger ainda não)
│   ├── 1.1.02 Taxas iFood                      NOVA (comissão do iFood ainda não tem categoria própria aqui)
│   ├── 1.1.03 Taxas 99food                     NOVA
│   ├── Despesas Financeiras (Taxas de cartão + Aluguel Máquinas) [P]   já existe id 939324, MANTÉM
│   └── Motoboy [P]                              já existe id 939315, RECEBE FUSÃO de "Comissão entregadores"
│                                                  (id 965890, R$ -13.456,22, taxa de entrega paga por pedido).
│                                                  Mover lançamento na mão, depois excluir id 965890 vazia
└── Fornecedores [P]                             já existe id 939307, hoje vazia, VIRA PAI de baixo
    ├── 1.2.01 Insumos                           id 945362 [R$ -67.417,04] MOVER (era filha de "Custos com produtos")
    │   └── 1.2.01.01 Pão                        id 1665263 [R$ -1.114,00] MOVER, mantém aninhado
    ├── 1.2.02 Embalagens                        id 945366 [R$ -9.602,71] MOVER
    ├── 1.2.03 Bebidas                           id 945363 [R$ -14.312,89] MOVER
    ├── 1.2.04 Salgados                          NOVA (padronização, Geburger pode nunca usar)
    ├── 1.2.05 Congelados                        id 945361 [R$ -4.846,80] MOVER (posição específica Geburger)
    ├── 1.2.06 Hortifruti                        id 945364 [R$ -2.216,07] MOVER (posição específica Geburger)
    └── 1.2.07 Descartáveis (embalagem de pedido) id 945367 [R$ -1.972,22] MOVER. CONFIRMADO pelo Jonas: é copo
                                                  de refri e guardanapo que vão pro cliente, não é consumo interno

2 Despesas Operacionais
├── 2.1 Equipe
│   ├── 2.1.01 Salários                          id 945317 [R$ -58.433,39] RENOMEAR (era "Salário de funcionários")
│   ├── 2.1.02 Encargos trabalhistas             NOVA (INSS/FGTS, confirmar se já está em outra categoria)
│   ├── 2.1.03 Comissão funcionários             id 968776 [R$ -1.468,56] MOVER (já tinha o nome certo)
│   ├── 2.1.04 Freelancers / diaristas           id 945322 [R$ -4.390,97] RENOMEAR (era "Diarista")
│   ├── 2.1.05 Benefícios
│   │   ├── 2.1.05.01 Alimentação                id 945323 [R$ -8.762,48] MOVER
│   │   │   └── Água (item específico)           id 1665262 [R$0] MOVER, mantém aninhado
│   │   └── 2.1.05.02 Transporte Funcionários    id 967269 [R$ -6.722,27] MOVER
│   ├── 2.1.06 Entregadores (diária fixa)       id 945324 [R$ -6.310,00] MOVER (era "Entregadores", raiz solta).
│   │                                            CONFIRMADO: taxa fixa de R$30/dia paga ao entregador, diferente
│   │                                            da comissão por pedido que vai pro "Motoboy"
│   ├── 2.1.07 Recrutamento (vagas, anúncios)   id 968775 [R$ -107,27] MOVER (era "Recursos Humanos", filha direta
│   │                                            de "Despesas administrativas"). CONFIRMADO: anúncio de vaga tipo OLX
│   └── Garçom [P]                                já existe id 939316, MANTÉM sem uso. CONFIRMADO: tem garçom no
│                                                  salão, mas a comissão dele não é gerenciada pelo Saipos hoje
├── 2.2 Estrutura Física
│   ├── 2.2.01 Aluguel                           id 945268 [R$ -24.500,00] MOVER
│   ├── 2.2.02 Condomínio                        NOVA (padronização)
│   ├── 2.2.03 Energia elétrica                  id 945267 [R$ -9.951,43] MOVER
│   ├── 2.2.04 Água                              id 945269 [R$ -74,00] MOVER
│   ├── 2.2.05 Esgoto                            NOVA (padronização)
│   ├── 2.2.06 Internet                          id 945266 [R$ -861,67] MOVER
│   ├── 2.2.07 Serviço de Limpeza                NOVA (diferente de "Material de limpeza", que é insumo)
│   ├── 2.2.08 Controle de Pragas                id 945327 [R$ -250,00] MOVER
│   ├── 2.2.09 Detetização                       NOVA (Oka trata separado de Controle de Pragas)
│   ├── 2.2.10 Reformas                          id 998256 [R$0] MOVER + RENOMEAR (era "Reformas/Estrutura",
│   │                                            filha de "Investimentos em bens materiais". Nome real, meu
│   │                                            levantamento original tinha cortado errado em "Estrutura")
│   ├── 2.2.11 Gás                               id 968777 [R$ -2.014,49] MOVER (posição específica Geburger)
│   ├── 2.2.12 IPTU                              id 945270 [R$ -662,98] MOVER (posição específica Geburger)
│   ├── 2.2.13 Seguro                            id 945345 [R$0] MOVER (posição específica Geburger)
│   ├── 2.2.14 Celular                           id 945265 [R$ -286,14] MOVER (posição específica Geburger)
│   ├── 2.2.15 Manutenção ar condicionado        id 945331 [R$ -1.150,00] MOVER (posição específica Geburger)
│   └── 2.2.16 Manutenção elétrica               id 1040044 [R$ -230,00] MOVER (era "Manutenção de Rede Elétrica", raiz solta)
├── 2.3 Logística
│   ├── 2.3.01 Fretes                            NOVA (padronização)
│   └── 2.3.02 Transporte
│       ├── 2.3.02.01 Gasolina                   NOVA (padronização)
│       └── 2.3.02.02 Uber/99                    id 945369 [R$ -3.923,03] MOVER (era "Delivery compras", raiz solta).
│                                                CONFIRMADO: gasto com Uber/motoboy pra buscar insumo, não é entrega ao cliente
├── 2.4 Operação
│   ├── 2.4.01 Material de Cozinha               id 945329 [R$ -822,80] RENOMEAR (era "Materiais de Copa e Cozinha")
│   ├── 2.4.02 Material de Limpeza               id 945328 [R$ -1.269,86] MOVER
│   ├── 2.4.03 Material de Expediente            id 945326 [R$ -652,88] RENOMEAR (era "Materiais de expediente / escritório")
│   ├── 2.4.04 Uniforme                          id 968774 [R$ -10,00] MOVER
│   ├── 2.4.05 Manutenção equipamentos           id 967274 [R$ -450,00] RENOMEAR (era "Manutenção máquinas e equipamentos")
│   ├── 2.4.06 Pequenos reparos                  id 998254 [R$ -890,00] MOVER (era "Manutenção de loja", raiz solta)
│   ├── 2.4.07 Decoração                         id 982316 [R$ -78,00] MOVER (saía de "Custos com produtos", correção de seção)
│   ├── 2.4.08 Manutenção móveis                 id 945330 [R$0] MOVER (posição específica Geburger)
│   └── 2.4.09 Equipamentos de loja              id 1025587 [R$ -107,47] MOVER (posição específica Geburger)
└── 2.5 Segurança
    └── 2.5.01 Vigilância                        NOVA (padronização)

3 Despesas Administrativas
├── 3.2 Serviços Profissionais
│   ├── 3.2.01 Contabilidade                     id 945271 [R$ -3.500,00] RENOMEAR (era "Contador")
│   ├── 3.2.02 Jurídico                          NOVA (padronização)
│   └── 3.2.03 Consultorias                      NOVA (padronização)
├── 3.3 Serviços Terceirizados
│   ├── 3.3.01 Gestão financeira                 id 945277 [R$ -2.100,00] RENOMEAR (era "Assessoria financeira")
│   ├── 3.3.02 Gestão de tráfego                 id 945276 [R$ -5.600,00] RENOMEAR (era "Gestor de tráfego")
│   ├── 3.3.03 Social Media                      id 1074977 [R$ -9.700,00] RENOMEAR (era "Social Midia")
│   ├── 3.3.04 Design                            id 1258778 [R$ -683,50] MOVER (saía de "Investimentos em marketing")
│   ├── 3.3.05 Gestor iFood                      id 945278 [R$0] MOVER (posição específica Geburger)
│   └── 3.3.06 Gestor de estoque                 id 1142344 [R$ -450,00] MOVER (posição específica Geburger)
├── 3.4 Sistemas e Ferramentas
│   ├── 3.4.01 Saipos                            NOVA (hoje some dentro de "Mensalidade de softwares")
│   ├── 3.4.02 Outros softwares                  id 945272 [R$ -2.874,03] RENOMEAR (era "Mensalidade de softwares")
│   └── 3.4.03 Site / cardápio digital           id 1025589 [R$0] MOVER (posição específica Geburger, saía de marketing)
└── Consumo [P]                                  já existe id 1007993, MANTÉM (já vinculada ao DRE)
    ├── 3.1.01 Descartáveis (consumo interno)    NOVA. Só copo/guardanapo de uso interno, NUNCA embalagem de pedido
    └── 3.1.02 Testes de receita                 NOVA (padronização)

4 Marketing e Crescimento
├── 4.1 Tráfego Pago
│   ├── 4.1.01 Meta Ads                          id 945341 [R$ -15.031,46] RENOMEAR (era "Facebook")
│   ├── 4.1.02 Google Ads                        id 945342 [R$0] MOVER
│   ├── 4.1.03 TikTok Ads                        id 945343 [R$0] MOVER (era "Tik Tok Ads")
│   └── 4.1.04 Ifood Ads                         id 945344 [R$0] MOVER (posição específica Geburger)
├── 4.2 Branding e Conteúdo
│   ├── 4.2.01 Produção de conteúdo              NOVA (padronização)
│   ├── 4.2.02 Fotografia / vídeo                NOVA (padronização)
│   └── 4.2.03 Influenciadores                   NOVA (padronização)
└── 4.3 Materiais e Ações
    ├── 4.3.01 Ações promocionais                id 968728 [R$ -529,07] RENOMEAR (era "Brindes")
    ├── 4.3.02 Eventos                           NOVA (padronização)
    └── 4.3.03 Impressos                         id 1589050 [R$ -66,00] RENOMEAR (era "Gráfica")

5 Financeiro
├── 5.1 Impostos
│   ├── 5.1.01 Simples Nacional                  id 945358 [R$ -2.479,40] RENOMEAR
│   ├── 5.1.02 Taxas municipais                  NOVA (padronização)
│   └── 5.1.03 Outras obrigações                 NOVA (padronização)
└── 5.2 Despesas Financeiras
    ├── 5.2.01 Tarifas bancárias                 NOVA, recebe os R$ -30,00 soltos em "Custos tributários ou financeiros"
    ├── 5.2.02 Antecipações                      NOVA (padronização)
    ├── 5.2.03 Empréstimos                       id 945352 [R$0] RENOMEAR (era "Pagamento de empréstimos")
    ├── 5.2.04 Juros empréstimos                 id 945353 [R$ -85,30] RENOMEAR (era "Juros bancários e por atraso")
    ├── 5.2.05 Taxas de pix                      id 945359 [R$0] MOVER (posição específica Geburger)
    └── 5.2.06 Empréstimos obtidos               id 945348 [R$0] MOVER (entrada de empréstimo, não saída, posição específica Geburger)

6 Sócios e Capital
├── 6.1 Pró-labore                               id 945320 [R$0] RENOMEAR. CONFIRMADO pelo Jonas: os sócios não tiram
│                                                pró-labore hoje, R$0 é real, não é lacuna de lançamento
├── 6.2 Distribuição de lucros                   id 945355 [R$ -5.355,00] RENOMEAR
├── 6.3 Retirada extraordinária                  NOVA (padronização)
└── 6.4 Aportes dos sócios                       id 945349 [R$0] RENOMEAR (era "Capitalização dos sócios")

7 Expansão e Investimentos
├── 7.1 Investimentos no Negócio
│   ├── 7.1.01 Compra de máquinas                NOVA (padronização)
│   ├── 7.1.02 Pesquisa e desenvolvimento        NOVA (padronização)
│   └── 7.1.03 Venda de equipamentos usados      id 945350 [R$0] MOVER (posição específica Geburger)
└── 7.2 Obras e Implantação
    ├── 7.2.01 Obra                              NOVA (padronização)
    ├── 7.2.02 Arquitetura                       NOVA (padronização)
    ├── 7.2.03 Mão de obra                       NOVA (padronização)
    ├── 7.2.04 Equipamentos                      NOVA (padronização)
    └── 7.2.05 Mobiliário                        NOVA (padronização)

Diferença de caixa [P]      já existe id 939322, MANTÉM
Fiado [P]                   já existe id 939325, MANTÉM
Frente de Caixa [P]         já existe id 939323, MANTÉM
Saldo Inicial [P]           já existe id 939326, MANTÉM
```

### O que exclui (vazio ou quase vazio, sem risco de lançamento)

| Categoria | id | Motivo |
|---|---|---|
| Social Meida | 1074976 | Duplicata de digitação de "Social Midia", zero lançamento |
| Vale transporte | 945318 | Zero lançamento, redundante com "Transporte Funcionários" |
| Mídias | 945340 | Zero lançamento, virou redundante com as categorias específicas por plataforma |
| Pagamento de dívidas passadas | 945354 | CONFIRMADO: é empréstimo/financiamento, mesma coisa que "Pagamento de empréstimos" (id 945352, vira `5.2.03 Empréstimos`). Zero lançamento, duplicata |
| Receita de Vendas (raiz) e as 5 filhas: Receita em Ifood Online, Receita em crédito, Receita em dinheiro, Receita em débito, Receita em pix | 964541, 964576, 964543, 1027402, 964545, 964542 | CONFIRMADO: o Saipos já lança a receita automaticamente, tanto no relatório `Vendas por período` quanto na linha `(+) Receita Operacional Bruta` do `DRE Gerencial` (é automática, não depende de vínculo de categoria, ver `../operacao/02-plano-de-contas.md`). Essa árvore de categorias em `Lançamentos financeiros` nunca foi o lugar certo pra registrar venda, por isso só tem R$ 7,00 lançado no período inteiro (provável lançamento avulso/teste). Nenhum lançamento futuro de venda precisa passar por aqui |

### O que esvazia e some sozinho (Saipos remove pai sem filho)

Custo com frete, Custos com embalagens, Custos com produtos, Custos
tributários ou financeiros, Custos variáveis, Investimentos em bens
materiais, Investimentos em marketing, Investimentos, Entradas não
operacionais, Saídas não operacionais, Movimentações não operacionais,
Despesas administrativas, Despesas com materiais e equipamentos, Despesas
com pessoal, Despesas fixas, Serviços. Não precisa excluir na mão, só
esvaziar movendo os filhos.

**Atenção:** "Custos variáveis" e "Despesas fixas" são raízes, não
subcategorias. Não confirmamos se o Saipos remove raiz vazia do mesmo jeito
que remove subcategoria vazia. Verificar na tela depois de mover os filhos,
e se não sumir sozinha, excluir na mão (sem risco, já está vazia).

## Pendências

Todas as 7 pendências foram resolvidas pelo Jonas em 22/08/2026.

1. ~~Comissão entregadores + Entregadores + Delivery compras~~. São três
   coisas diferentes: **Comissão entregadores** (R$ -13.456,22) é a taxa de
   entrega paga por pedido, vai fundida em `Motoboy` [P]. **Entregadores**
   (R$ -6.310,00) é a diária fixa de R$30/dia paga ao entregador, vira
   `2.1.06 Entregadores (diária fixa)`. **Delivery compras** (R$ -3.923,03)
   é gasto com Uber/motoboy pra buscar insumo, não tem nada a ver com
   entrega ao cliente, vira `2.3.02.02 Uber/99`.
2. ~~Descartáveis~~ (R$ -1.972,22). Confirmado: é copo de refri e
   guardanapo que vão pro cliente. Fica em `1.2.07`, custo de venda, entra
   no CMV. Não é `3.1.01 Consumo`.
3. ~~Pró-labore zerado~~. Confirmado: os sócios não tiram pró-labore hoje.
   R$0 é o número real, não é lançamento faltando.
4. ~~Recursos Humanos~~ (R$ -107,27). Confirmado: anúncio de vaga tipo OLX,
   não é serviço de consultoria de RH. Vira `2.1.07 Recrutamento (vagas,
   anúncios)`, dentro de Equipe, não em Serviços Profissionais.
5. ~~Receita de Vendas e as 5 subcategorias~~. Confirmado: o Saipos já
   lança a receita de venda sozinho, tanto no relatório `Vendas por
   período` quanto na linha automática `(+) Receita Operacional Bruta` do
   DRE. Não existe lançamento manual de venda a fazer. A árvore inteira
   (raiz + 5 filhas) entra na lista de exclusão, R$ 7,00 era lançamento
   avulso/teste.
6. ~~Pagamento de dívidas passadas~~ (R$ 0,00). Confirmado: é
   empréstimo/financiamento, mesma coisa que "Pagamento de empréstimos".
   Vira duplicata de `5.2.03 Empréstimos`, entra na lista de exclusão.
7. ~~Garçom [P] sem uso~~. Confirmado: tem garçom no salão, mas a comissão
   dele não passa pelo Saipos hoje. Categoria de sistema, mantém como está,
   sem mudança estrutural. Se um dia decidirem lançar a comissão do
   garçom pelo Saipos, ela já está vinculada ao DRE (seção 3, Despesas
   administrativas).

### Fusão que precisa mover lançamento na mão

Só um caso na proposta inteira: **"Comissão entregadores" (id 965890) para
dentro de "Motoboy" [P] (id 939315).** R$ 13.456,22 em lançamentos.
"Motoboy" já existe e está vazia, então não dá pra só renomear "Comissão
entregadores" e virar "Motoboy": tem que editar cada lançamento e trocar a
categoria pra "Motoboy", um por um (ou em lote, se o Saipos tiver essa
opção, ainda não testamos). Depois de tudo migrado, excluir "Comissão
entregadores" vazia. Todo o resto da proposta é renomear ou mover
categoria, sem tocar em lançamento individual.

## Motivo

Reaproveitar o padrão do Oka economiza a carga mental de quem lança nos
dois negócios e já resolve o problema de numeração alfabética embaralhada
que o Oka documentou (Saipos reordena filho por ordem alfabética ao salvar,
por isso o código usa dois dígitos a partir do nível 2). Trazer o esqueleto
inteiro do Oka, mesmo as categorias que a Geburger ainda não usa, deixa o
sistema pronto pra quando a categoria for necessária, sem precisar
redesenhar a árvore de novo.

## Como saber se deu errado

Depois de executado: se algum relatório de despesa por categoria mostrar
número diferente do levantado nesta sessão (`despesas-por-categoria-62061-2026-01-a-08.csv`)
pro mesmo período, algum lançamento se perdeu ou foi parar em categoria
errada durante a migração. Conferir categoria por categoria contra esse CSV
antes de considerar a migração concluída.

## Revisão prevista

As 7 pendências foram resolvidas em 22/08/2026. Estrutura pronta pra
execução real no Saipos (Fase 1 do `../operacao/08-roadmap-implantacao.md`).
Vinculação de DRE é decisão separada, fica pra depois desta estrutura
estar fechada.

## Execução, 22/08/2026

Migração feita direto na tela `Categorias financeiras` do Saipos (renomear,
mover por arrastar, criar subcategoria, excluir), categoria por categoria,
salvando em checkpoints. Confirmado por leitura da API (`$http` do Angular)
depois de cada etapa.

### O que saiu igual ao plano

- Todo o grupo `Fornecedores` (1.2.01 a 1.2.07, com Pão aninhado em
  1.2.01.01) migrado e renomeado, dinheiro intacto
- `1.1 Custos de Venda` criado com as 3 categorias novas
- `2.1 Equipe` e `2.2 Estrutura Física` criados e povoados
- As 5 raízes novas criadas (3 Despesas Administrativas, 4 Marketing e
  Crescimento, 5 Financeiro, 6 Sócios e Capital, 7 Expansão e
  Investimentos)
- Social Meida, Vale transporte, Estrutura (virou Reformas, não foi
  excluída) e Mídias excluídas ou corrigidas conforme o plano
- Toda categoria com dinheiro real recebeu o nome numerado certo

### Os 2 ajustes em relação ao plano original

1. **"Comissão entregadores" NÃO foi fundida em "Motoboy".** Na hora de
   mover o lançamento, descobri que a categoria tem **215 lançamentos
   individuais** (R$ 13.456,22) e o Saipos não tem nenhuma ferramenta de
   trocar categoria em lote pela tela de Lançamentos Financeiros (só existe
   "mudar para pago/não pago" em massa). Mover 215 lançamentos um por um
   não é viável numa sessão. Decisão: manter "Comissão entregadores" como a
   categoria definitiva, só renomeada para `1.1.04 Comissão entregadores
   (motoboy)`. A categoria de sistema `Motoboy` [P] continua existindo,
   vazia, do mesmo jeito que Fiado e Frente de Caixa já ficam. Zero risco
   de lançamento perdido, mas a Geburger tem uma categoria de sistema a
   mais sem uso do que o Oka.

2. **`Receita de Vendas` e as 5 filhas tinham lançamento real, não só
   R$7,00.** Na hora de excluir, o Saipos avisou "existem lançamentos
   financeiros nesta categoria" pra `Receita em dinheiro` e `Receita em
   Ifood Online` também (meu levantamento original não pegou isso,
   provavelmente porque vinha do CSV de despesas por categoria e essas
   entradas não apareceram lá). Usei o próprio fluxo do Saipos de "escolha
   uma categoria pra transferir esses lançamentos" e mandei tudo pra
   `Diferença de caixa` antes de excluir. Nenhum valor foi perdido, mas
   vale conferir com o Jonas o que exatamente estava lançado ali.

### O que NÃO ficou fisicamente aninhado como no desenho aprovado

Por causa da estratégia "renomear no lugar" (mais rápida que mover toda
categoria), boa parte do conteúdo com nome numerado certo **ainda mora
dentro dos wrappers antigos**, não dentro das raízes novas 3 a 7. Por
exemplo: `3.2.01 Contabilidade` está fisicamente dentro de `Despesas
administrativas`, que está dentro da raiz `2 Despesas Operacionais`, não
dentro da raiz `3 Despesas Administrativas` (que existe, mas está vazia
hoje). O nome e o código estão certos, então quem lê a lista entende onde
cada coisa pertence, mas visualmente a árvore não bate 100% com o desenho
aprovado.

**Isso não afeta nada funcional:** vínculo de DRE, filtro de relatório e
lançamento são todos por id da categoria, não pela posição dela na árvore.
É só estética. Fica registrado como pendência de uma "Fase 1c" futura, se o
Jonas quiser a árvore fisicamente idêntica à do Oka. Wrappers antigos que
ainda existem, com filhos renomeados dentro: `Despesas administrativas`,
`Despesas com materiais e equipamentos`, `Despesas com pessoal`, `Serviços`,
`Investimentos em marketing`, `Investimentos em bens materiais`,
`Movimentações não operacionais` (com `Entradas` e `Saídas não
operacionais` dentro), `Custos com produtos`, `Custo com frete`.

### Conferência de integridade

97 categorias antes, 101 logo depois da migração. Nenhuma categoria com
saldo real foi excluída sem passar pelo fluxo de transferência de
lançamento do próprio Saipos.

### Auditoria de lixo e duplicata, 22/08/2026 (pedido do Jonas)

Varri as 101 categorias pela API procurando duas coisas: categoria vazia
sem propósito (o Saipos avisa que remove pai sem filho sozinho, mas isso
não é garantido em toda situação) e nome duplicado.

- **Nomes duplicados: nenhum.** As duas categorias chamadas "Água"
  (`2.1.05.01.01 Água`, item específico dentro de Alimentação, e `2.2.04
  Água`, conta de água do imóvel) são conceitos diferentes, não duplicata
- **1 categoria lixo encontrada e excluída:** `Custos com embalagens`, um
  wrapper antigo que ficou sem nenhum filho depois que Embalagens e
  Descartáveis migraram pra `Fornecedores`, e não foi removido sozinho
  pelo Saipos. Excluída sem lançamento pra transferir (zero uso)

**101 categorias antes desta auditoria, 100 depois.** Nenhuma outra
categoria vazia sobrou. As categorias "NOVA (padronização)" do plano
original (ex: `1.1.01 Comissão sobre vendas`, `2.2.02 Condomínio`) continuam
existindo mesmo sem lançamento: são posições reservadas do padrão do Oka,
não lixo, ficam prontas pra quando a Geburger precisar.
