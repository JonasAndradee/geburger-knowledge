# Padronizar categorias financeiras da Geburger no molde do Oka Guaraná

Data: 2026-08-22

Status: vigente (estrutura proposta, ainda **não executada no Saipos**)

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
│   └── Motoboy [P]                              já existe id 939315, MANTÉM (ver PENDÊNCIA 1)
└── Fornecedores [P]                             já existe id 939307, hoje vazia, VIRA PAI de baixo
    ├── 1.2.01 Insumos                           id 945362 [R$ -67.417,04] MOVER (era filha de "Custos com produtos")
    │   └── 1.2.01.01 Pão                        id 1665263 [R$ -1.114,00] MOVER, mantém aninhado
    ├── 1.2.02 Embalagens                        id 945366 [R$ -9.602,71] MOVER
    ├── 1.2.03 Bebidas                           id 945363 [R$ -14.312,89] MOVER
    ├── 1.2.04 Salgados                          NOVA (padronização, Geburger pode nunca usar)
    ├── 1.2.05 Congelados                        id 945361 [R$ -4.846,80] MOVER (posição específica Geburger)
    ├── 1.2.06 Hortifruti                        id 945364 [R$ -2.216,07] MOVER (posição específica Geburger)
    └── 1.2.07 Descartáveis (embalagem de pedido) id 945367 [R$ -1.972,22] MOVER, ver PENDÊNCIA 2

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
│   └── Garçom [P]                                já existe id 939316, sem uso hoje, ver PENDÊNCIA 7
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
│   ├── 2.2.10 Reformas                          NOVA (padronização)
│   ├── 2.2.11 Gás                               id 968777 [R$ -2.014,49] MOVER (posição específica Geburger)
│   ├── 2.2.12 IPTU                              id 945270 [R$ -662,98] MOVER (posição específica Geburger)
│   ├── 2.2.13 Seguro                            id 945345 [R$0] MOVER (posição específica Geburger)
│   ├── 2.2.14 Celular                           id 945265 [R$ -286,14] MOVER (posição específica Geburger)
│   ├── 2.2.15 Manutenção ar condicionado        id 945331 [R$ -1.150,00] MOVER (posição específica Geburger)
│   └── 2.2.16 Manutenção elétrica               id 1040044 [R$ -230,00] MOVER (era "Manutenção de Rede Elétrica", raiz solta)
├── 2.3 Logística
│   ├── 2.3.01 Fretes                            NOVA, ver PENDÊNCIA 1 (pode receber "Delivery compras")
│   └── 2.3.02 Transporte
│       ├── 2.3.02.01 Gasolina                   NOVA (padronização)
│       └── 2.3.02.02 Uber/99                    NOVA (padronização)
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
│   └── 3.2.03 Consultorias                      NOVA, ver PENDÊNCIA 3 (pode receber "Recursos Humanos")
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
├── 6.1 Pró-labore                               id 945320 [R$0] RENOMEAR, ver PENDÊNCIA 4
├── 6.2 Distribuição de lucros                   id 945355 [R$ -5.355,00] RENOMEAR
├── 6.3 Retirada extraordinária                  NOVA, ver PENDÊNCIA 6 (pode receber "Pagamento de dívidas passadas")
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

### O que exclui (vazio, sem risco de lançamento)

| Categoria | id | Motivo |
|---|---|---|
| Social Meida | 1074976 | Duplicata de digitação de "Social Midia", zero lançamento |
| Vale transporte | 945318 | Zero lançamento, redundante com "Transporte Funcionários" |
| Estrutura | 998256 | Zero lançamento, escopo vago |
| Mídias | 945340 | Zero lançamento, virou redundante com as categorias específicas por plataforma |

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

## Pendências, decisão do Jonas antes de eu executar

1. **Comissão entregadores (R$ -13.456,22) + Entregadores (R$ -6.310,00) +
   Delivery compras (R$ -3.923,03).** Três categorias diferentes de custo
   de entrega, R$ 23.689,25 no total. Preciso saber o que cada uma
   representa pra decidir se viram uma coisa só dentro de "Motoboy" [P]
   (que hoje existe e está vazia) ou se ficam separadas: por exemplo,
   comissão por entrega variável vs. salário fixo de entregador CLT vs.
   outra coisa em "Delivery compras". Isso também decide se precisa mover
   lançamento na mão (fundir) ou só mover a categoria (reposicionar).
2. **Descartáveis (R$ -1.972,22).** É embalagem que vai no pedido do
   cliente (aí é `1.2.07`, custo de venda, entra no CMV) ou é copo e
   guardanapo de uso interno da equipe (aí é `3.1.01 Consumo`, e nunca
   deveria ter sido lançado como custo de produto)? Isso muda a seção do
   DRE também, então melhor decidir agora.
3. **Recursos Humanos (R$ -107,27).** Valor pequeno, mas quero confirmar se
   é taxa de serviço de RH/recrutamento antes de jogar em `3.2.03
   Consultorias`.
4. **Pró-labore está com R$ 0,00 lançado no período inteiro.** Estranho pra
   um negócio rodando há meses. O sócio retira por fora do Saipos
   (transferência direta sem lançamento) ou isso não foi lançado ainda?
5. **Receita de Vendas e as 5 subcategorias** (Ifood Online, crédito,
   dinheiro, débito, pix) têm só R$ 7,00 de lançamento no período inteiro.
   A receita real está no relatório "Vendas por período", não em
   lançamento financeiro. Posso excluir essa árvore inteira, ou você usa
   isso pra algum controle manual que eu não vi?
6. **Pagamento de dívidas passadas (R$ 0,00).** Dívida de quê? Se for
   empréstimo, entra em `5.2.03 Empréstimos`. Se for outra coisa (fornecedor
   em atraso, por exemplo), crio uma posição própria em `6.3 Retirada
   extraordinária` ou mantenho separada.
7. **Garçom [P] existe mas nunca recebeu lançamento.** A Geburger tem
   atendimento de salão com garçom, ou essa categoria pode ficar sem uso
   mesmo (ela é padrão do sistema, não dá pra excluir)?

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

Depois que o Jonas responder as 7 pendências acima. Só então a estrutura
proposta vira execução real no Saipos (Fase 1 do
`../operacao/08-roadmap-implantacao.md`). Vinculação de DRE é decisão
separada, fica pra depois desta estrutura estar fechada.
