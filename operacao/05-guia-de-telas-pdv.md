# 05, Guia de telas do PDV

**Versão 1, 22/08/2026.** Primeiras telas confirmadas na sessão de
levantamento da loja Ge Burger (62061).

Caminho de menu, campo e comportamento **verificados na tela**. Nada aqui pode
ser deduzido por analogia com outro sistema. Se não foi visto, não entra.

Sistema: Saipos (mesmo do Oka Guaraná)

## Formato de cada entrada

```
### [Nome da tela ou funcionalidade]
Fonte: [artigo da central de ajuda, com título exato, ou "verificado na tela"], lido em [data]

Caminho: Menu > ...
Campos: ...
Comportamento confirmado: ...
Armadilha, se houver: ...
```

Marque sempre se é `CONFIRMADO na documentação`, `VERIFICADO na tela` ou
`NÃO ENCONTRADO`. Nunca deixe ambíguo. Registre também o que foi procurado e
não achado: saber que não existe artigo economiza a próxima busca.

## Telas

### Ingredientes e Insumos
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Estoque > `Ingredientes e Insumos`
Campos: Descrição, Grupo, Fornecedor, Controle de Estoque, Beneficiado, Nível
de estoque, e a tabela com Unidade de Consumo, Grupo, Estoque Mínimo, Estoque
Atual, Custo Médio, Controla Estoque, Controla CMV, Beneficiado, Ações
Comportamento confirmado: lista só itens com `kind: ingredient` por padrão.
Fichas técnicas (`kind: datasheet`) e beneficiados (`kind: benefited`) não
aparecem aqui mesmo filtrando por "Beneficiado", ficam em telas separadas
Armadilha: filtrar por nome de ficha técnica nesta tela não encontra nada,
mesmo o item existindo no sistema. É preciso ir na tela `Ficha técnica`

### Ficha técnica
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Estoque > `Ficha técnica`
Campos: Descrição, Grupo, e a tabela com Ficha Técnica, Grupo, Estoque Atual,
Ações (imprimir, editar, excluir)
Comportamento confirmado: lista as 53 fichas de produto final e os 16
beneficiados juntos. Editar abre
`#/app/store/datasheet-record/edit/{id}/datasheet`, com a composição
completa em `record.children`, cada linha podendo ter uma quantidade base
e uma lista de `variations` (uma por variação de produto do cardápio que usa
aquela ficha)

### Categorias financeiras
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Financeiro > `Categorias financeiras`
Comportamento confirmado: árvore com 97 categorias raiz (252 nós contando
subcategoria). Mesmo comportamento do Oka Guaraná: arrastar pela alça pra
mover, `[+] Adicionar subcategoria` pra criar filho, tudo rascunho até
`Salvar`

### DRE Gerencial
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Financeiro > `DRE Gerencial/Financeiro`
Comportamento confirmado: mostra alerta no topo quando existem categorias
financeiras sem seção vinculada ("Existem N categorias financeiras não
vinculadas ao DRE. Vincular"). Clicar em "Vincular" abre o modal
`Configuração do DRE`, uma árvore com select por categoria, 7 seções
disponíveis (`Receita Operacional Bruta` e `CMV` são automáticas, não
aparecem na lista). Na Ge Burger, 91 das 97 categorias raiz estavam sem
vínculo em 22/08/2026, o que deixa o DRE incompleto (ver
`02-plano-de-contas.md`)
Armadilha: o período máximo de navegação parece ser por mês (setas `<` `>`
ao lado da data), não testado forçar um intervalo maior

### Lançamentos Financeiros
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Financeiro > `Lançamentos financeiros`
Campos: Tipo (Contas a pagar/receber/Todas), Situação (Pagas/Não pagas/Todas),
Conta, Método de Pagamento, Categoria, Descrição, Fornecedor ou NF,
Conciliação bancária
Comportamento confirmado: filtro de data por padrão mostra só a semana atual.
Clicar em "PERSONALIZADO" libera os campos de data inicial e final pra
digitar manualmente (aceita digitar sobre o texto selecionado, sem precisar
usar o calendário). Não tem limite de intervalo, uma consulta de 01/01 a
22/08/2026 trouxe 2.756 lançamentos sem erro
Armadilha: este relatório não mostra receita de venda do PDV, só
lançamento financeiro manual (contas a pagar, contas a receber, sangria de
caixa). Pra faturamento de venda, use `Vendas por período`

### Vendas por período
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Relatórios > `Vendas por período`
Campos: Data inicial, Data final, Turno, Entrega/Retirada/Salão/Ficha,
Marcas, Canal/Origem da venda, Cupom de desconto, Status da venda,
Acréscimos/Descontos
Comportamento confirmado: mostra Qtde total de pedidos, cancelados, total em
R$, ticket médio por tipo de atendimento (Entrega/Balcão/Mesa/Ficha), e
quebra por canal (99Food, Facebook, iFood, Site Delivery (SAIPOS), Telefone,
WhatsApp)
Armadilha: **período máximo de 3 meses por consulta.** Pedir um intervalo
maior devolve o erro "Por favor, selecione um período menor do que 3
mês(es) neste filtro". Pra cobrir um ano, são pelo menos 4 consultas
trimestrais. O campo de data é nativo, mais confiável clicar e usar as
setas do calendário popup do que tentar digitar direto

### Cardápio
Fonte: VERIFICADO na tela, 22/08/2026

Caminho: Menu > Cardápio > `Cardápio`
Comportamento confirmado: tela em React (diferente do resto do admin, que é
AngularJS), mas roda dentro do mesmo shell, então `$http` do Angular
continua acessível. 183 produtos cadastrados na Ge Burger, contando
variações "S -" (provavelmente Salão) e "D -" (Delivery) do mesmo item base,
mais promoções específicas de canal (prefixo "Promoções Ifood")
