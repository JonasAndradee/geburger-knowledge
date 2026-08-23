# Vincular categorias financeiras ao DRE Gerencial

Data: 2026-08-23

Status: vigente

## Contexto

A migração de 22/08 (ver
`2026-08-22-padronizar-categorias-financeiras-com-oka.md`) trouxe a árvore de
categorias do Geburger pro mesmo padrão numérico do Oka Guaraná, mas não
mexeu no vínculo com o DRE. Antes desta decisão, só 6 das 100 categorias
tinham seção do DRE escolhida (Consumo, Despesas Financeiras, Diferença de
caixa, Garçom, Motoboy, Saldo Inicial). O `DRE Gerencial` mostrava lucro
operacional de R$ 77.130,40 no trimestre jun-ago, número que não descontava
quase nenhum custo fixo ou variável real, porque a categoria que recebe o
lançamento não estava dizendo ao Saipos em qual linha do DRE entrar.

Jonas pediu pra fazer essa vinculação logo depois da reorganização
estrutural, antes de olhar pro DRE de verdade: "Fazemos primeiro isso e só
depois que vamos olhar para o DRE."

## Opções consideradas

- Vincular cada categoria individualmente, olhando o nome uma por uma
- Reaproveitar o critério que o Oka Guaraná já usa (raiz da árvore decide a
  seção), adaptado à árvore que já existe no Geburger
- Vincular só as categorias que já têm lançamento no período, deixar o
  resto pra depois

## Decisão

Reaproveitar o critério do Oka Guaraná (raiz da árvore decide a seção do
DRE), vinculando todas as 78 categorias-folha da árvore de uma vez, não só
as que já têm lançamento. Tabela completa de mapeamento em
`../operacao/02-plano-de-contas.md`.

**Regra central:** categoria-pai nunca recebe vínculo direto. No Saipos,
vincular uma categoria-pai cascateia a seção pra todos os filhos e trava a
edição individual deles. Como a árvore do Geburger ainda tem o gap da "Fase
1c" (categoria com código de uma raiz morando fisicamente dentro de um
wrapper de outra raiz, porque a reorganização física ainda não foi feita),
cascatear pelo pai erraria a seção de vários filhos que não têm nada a ver
com aquele pai. Por isso só as 58 folhas-alvo foram vinculadas, mais 2
raízes vazias sem filho nenhum ainda (`3 Despesas Administrativas`, `4
Marketing e Crescimento`), e 1 categoria foi desvinculada (`Saldo Inicial`,
ver abaixo). As 39 categorias que ficaram sem vínculo estão listadas com o
motivo em `../operacao/04-categorias-financeiras.md`.

**Duas correções em cima do que já estava configurado:**

1. `Despesas Financeiras (Taxas de cartão + Aluguel Máquinas)` estava
   vinculada a `4, Despesas financeiras`. Mudou pra `2, Custo com vendas`,
   porque apesar do nome é taxa de cartão, custo variável de venda. Mesma
   pegadinha que o Oka já documentou.
2. `Garçom` estava vinculada a `3, Despesas administrativas`. Mudou pra `2,
   Custo com vendas`, seguindo a mesma lógica do Motoboy: comissão de
   atendimento só existe se houver venda.
3. `Saldo Inicial` estava vinculada a `5, Receita não operacional líquida`.
   Foi desvinculada, seguindo a recomendação que o próprio Oka registrou
   (mas nunca aplicou lá): saldo de conta bancária é foto patrimonial, não
   resultado do período. Vinculado, ele infla o lucro do mês em que o
   saldo foi lançado.

## Motivo

Fazer tudo de uma vez, com o critério do Oka, evita vincular errado
categoria por categoria e mantém o padrão entre as duas empresas (mesma
pessoa lança nas duas). Não vincular categoria-pai é a única forma segura
de vincular sem arriscar que uma categoria-folha misturada dentro do pai
errado herde a seção errada.

## Como saber se deu errado

- Se o `DRE Gerencial` continuar mostrando "Despesas administrativas" ou
  "Custo com vendas" perto de zero num mês com movimento real, teve
  vínculo que não pegou ou categoria nova sem vínculo
- Se o lucro operacional de um mês fechado bater muito diferente do que o
  extrato bancário mostra, conferir se alguma categoria com lançamento
  real ficou fora do vínculo (ex: categoria nova criada depois desta data)
- Se a leitura em camadas (resultado da unidade vs camada central) não
  fizer sentido, checar se a raiz `3 Despesas Administrativas` está
  realmente recebendo só serviço central e não bagunçou com despesa de
  ponto

## Revisão prevista

Quando a "Fase 1c" (reorganizar fisicamente as categorias que hoje moram no
wrapper errado) acontecer: nesse momento dá pra reavaliar se as
categorias-pai que ficaram sem vínculo (`5 Financeiro`, `6 Sócios e
Capital`, os wrappers antigos) podem ganhar vínculo próprio sem risco de
cascata errada. Também revisar depois que agosto/2026 fechar por completo,
pra confirmar se a queda de "Despesas administrativas" nesse mês foi falta
de lançamento ou erro de vínculo.
