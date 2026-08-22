# 04, Categorias financeiras

**Versão 1, 22/08/2026.** Levantado da tela `Categorias financeiras` da loja
Ge Burger (62061) via API do Saipos. Divergência entre o que está aqui e o
que está na tela é bug do documento, corrija o documento.

**Proposta de reestruturação em aberto:** ver
`../decisoes/2026-08-22-padronizar-categorias-financeiras-com-oka.md`, que
reaproveita o padrão de codificação do Oka Guaraná. Ainda não executada no
Saipos, esperando o Jonas responder as pendências listadas lá. Este arquivo
continua sendo a árvore **real** até a migração acontecer.

Fonte bruta: `dados/categorias-financeiras-62061-2026-08-22.csv`.

## Árvore

97 categorias únicas, em 14 raízes. `[DRE:N]` marca a categoria vinculada a
uma seção do DRE (ver `02-plano-de-contas.md` para o que cada número
significa). `[CAIXA]` marca categoria do sistema com `cashier = Y`.

```
- Consumo (#1007993) [DRE:3] [CAIXA]
- Custos variáveis (#945356)
  - Custo com frete (#945368)
    - Comissão entregadores (#965890)
    - Delivery compras (#945369)
  - Custos com embalagens (#945365)
    - Descartáveis (#945367)
    - Embalagens (#945366)
  - Custos com produtos (#945360)
    - Bebidas (#945363)
    - Brindes (#968728)
    - Congelados (#945361)
    - Decoração (#982316)
    - Equipamentos de loja (#1025587)
    - Gráfica (#1589050)
    - Hortifruti (#945364)
    - Insumos (#945362)
      - Pão (#1665263)
  - Custos tributários ou financeiros (#945357)
    - Comissão funcionários (#968776)
    - Simples nacional (#945358)
    - Taxas de pix (#945359)
  - Manutenção de Rede Elétrica (#1040044)
  - Manutenção de loja (#998254)
- Despesas Financeiras (Taxas de cartão + Aluguel Máquinas) (#939324) [DRE:4] [CAIXA]
- Despesas fixas (#945263)
  - Despesas administrativas (#945264)
    - Aluguel (#945268)
    - Celular (#945265)
    - Contador (#945271)
    - Energia elétrica (#945267)
    - Gás (#968777)
    - IPTU (#945270)
    - Internet (#945266)
    - Mensalidade de softwares (#945272)
    - Recursos Humanos (#968775)
    - Seguro (#945345)
    - Serviços (#945275)
      - Assessoria financeira (#945277)
      - Controle de pragas (#945327)
      - Gestor de estoque (#1142344)
      - Gestor de tráfego (#945276)
      - Gestor ifood (#945278)
    - Transporte Funcionários (#967269)
    - Água (#945269)
  - Despesas com materiais e equipamentos (#945325)
    - Materiais de expediente / escritório (#945326)
    - Manutenção ar condicionado (#945331)
    - Manutenção máquinas e equipamentos (#967274)
    - Manutenção móveis (#945330)
    - Materiais de Copa e Cozinha (#945329)
    - Materiais de limpeza (#945328)
  - Despesas com pessoal (#945316)
    - Alimentação (#945323)
      - Água (#1665262)
    - Diarista (#945322)
    - Entregadores (#945324)
    - Pró-labore (#945320)
    - Salário de funcionários (#945317)
    - Uniforme (#968774)
    - Vale transporte (#945318)
- Diferença de caixa (#939322) [DRE:3] [CAIXA]
- Fiado (#939325) [CAIXA]
- Fornecedores (#939307) [CAIXA]
- Frente de Caixa (#939323) [CAIXA]
- Garçom (#939316) [DRE:3] [CAIXA]
- Investimentos (#945338)
  - Investimentos em bens materiais (#998255)
    - Estrutura (#998256)
  - Investimentos em marketing (#945339)
    - Design (#1258778)
    - Facebook (#945341)
    - Google Ads (#945342)
    - Ifood Ads (#945344)
    - Mídias (#945340)
    - Site (#1025589)
    - Social Meida (#1074976)
    - Social Midia (#1074977)
    - Tik Tok Ads (#945343)
- Motoboy (#939315) [DRE:2] [CAIXA]
- Movimentações não operacionais (#945346)
  - Entradas não operacionais (#945347)
    - Capitalização dos sócios (#945349)
    - Empréstimos obtidos (#945348)
    - Venda de equipamentos usados (#945350)
  - Saídas não operacionais (#945351)
    - Distribuição de lucros (#945355)
    - Juros bancários e por atraso (#945353)
    - Pagamento de dívidas passadas (#945354)
    - Pagamento de empréstimos (#945352)
- Receita de Vendas (#964541)
  - Receita em Ifood Online (#964576)
  - Receita em crédito (#964543)
  - Receita em dinheiro (#1027402)
  - Receita em débito (#964545)
  - Receita em pix (#964542)
- Saldo Inicial (#939326) [DRE:5] [CAIXA]
```

## Achado crítico: quase nada está vinculado ao DRE

**Só 6 das 97 categorias raiz têm seção do DRE vinculada.** O próprio Saipos
avisa isso na tela do DRE Gerencial: "Existem 91 categorias financeiras não
vinculadas ao DRE." As 6 vinculadas:

| Categoria | Seção do DRE |
|---|---|
| Consumo | 3, Despesas administrativas |
| Despesas Financeiras (Taxas de cartão + Aluguel Máquinas) | 4, Despesas financeiras |
| Diferença de caixa | 3, Despesas administrativas |
| Garçom | 3, Despesas administrativas |
| Motoboy | 2, Custo com vendas |
| Saldo Inicial | 5, Receita não operacional líquida |

Isso significa que o `DRE Gerencial` de hoje (ver `02-plano-de-contas.md`)
está incompleto: praticamente todo gasto lançado por categoria (Insumos,
Salário de funcionários, Aluguel, Facebook, etc.) não aparece separado por
seção, só entra no bruto se o Saipos tiver alguma regra automática por trás
(a ver, não confirmado). Antes de usar o DRE Gerencial pra decisão, vincular
as categorias que de fato recebem lançamento.

## Categorias que de fato receberam lançamento (01/01 a 22/08/2026)

Das 97 categorias raiz, 49 têm lançamento no período. Total por categoria em
`dados/despesas-por-categoria-62061-2026-01-a-08.csv`. As 15 maiores em
volume (sempre negativo = saída, positivo = entrada):

| Categoria | Total 2026 (jan a 22/08) |
|---|---|
| Insumos | -R$ 67.417,04 |
| Salário de funcionários | -R$ 58.433,39 |
| Aluguel | -R$ 24.500,00 |
| Facebook | -R$ 15.031,46 |
| Bebidas | -R$ 14.312,89 |
| Comissão entregadores | -R$ 13.456,22 |
| Energia elétrica | -R$ 9.951,43 |
| Social Midia | -R$ 9.700,00 |
| Embalagens | -R$ 9.602,71 |
| Alimentação | -R$ 8.762,48 |
| Transporte Funcionários | -R$ 6.722,27 |
| Entregadores | -R$ 6.310,00 |
| Gestor de tráfego | -R$ 5.600,00 |
| Saídas não operacionais | -R$ 5.355,00 |
| Congelados | -R$ 4.846,80 |
| Frente de Caixa (sangria/reforço) | R$ 12.943,33 |

**Achado sobre `Facebook` e `Social Midia`:** juntas somam R$ 24.731,46 em
2026 até aqui, maior que `Comissão entregadores`. Isso é a categoria de
Investimentos em marketing, que hoje não está vinculada ao DRE (fica dentro
de `Investimentos`, que é raiz sem seção). Se a intenção é ler DRE de
verdade, precisa decidir se marketing é despesa operacional ou investimento
separado, e vincular.

**Achado sobre receita:** o relatório `Lançamentos financeiros` não mostra
nenhum valor relevante nas categorias de `Receita de Vendas`. A receita real
está no relatório `Vendas por período` (ver `../dados/vendas-por-periodo-62061-2026-01-a-08.md`),
não nos lançamentos financeiros manuais. Ou seja, o financeiro (contas a
pagar/receber) e o comercial (vendas do PDV) não estão conciliados num único
relatório hoje. Perguntar ao Jonas se existe fechamento manual que junta os
dois.

## Filtro usado nas automações

Nenhuma automação de leitura por categoria configurada ainda (n8n ou
equivalente). Quando existir, documentar aqui o filtro exato, igual o Oka
Guaraná faz.

## Regra de padronização entre unidades

A estrutura de categorias precisa ser idêntica em todas as lojas, senão a
consolidação não fecha. Qualquer categoria nova entra em todas ao mesmo tempo.
Hoje só a loja Ge Burger (62061) foi mapeada, não há confirmação de quantas
unidades existem no total (ver `08-roadmap-implantacao.md`).
