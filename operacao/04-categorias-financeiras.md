# 04, Categorias financeiras

**Versão 3, 23/08/2026.** Extrato novo puxado direto da tela `Categorias
financeiras` da loja Ge Burger (62061) via API do Saipos, depois da migração
pro padrão numérico do Oka Guaraná (22/08) e da vinculação ao DRE (23/08).
Esta é a árvore real e atual, não mais um retrato de antes da migração.

Histórico da migração (o que virou o quê, os 2 ajustes feitos em cima do
plano original) está em
`../decisoes/2026-08-22-padronizar-categorias-financeiras-com-oka.md`.
Histórico da vinculação ao DRE está em
`../decisoes/2026-08-23-vincular-categorias-ao-dre.md`.

## Árvore

100 categorias únicas, em 18 raízes. `[DRE:N]` marca a categoria vinculada a
uma seção do DRE (ver `02-plano-de-contas.md` para o que cada número
significa). `[CAIXA]` marca categoria do sistema com `cashier = Y`. `[P]`
marca categoria padrão do Saipos (não pode ser renomeada nem excluída).

```
- 1 Custos Variáveis (#945356)
  - 1.1 Custos de Venda (#1695808)
    - 1.1.01 Comissão sobre vendas (#1695809) [DRE:2]
    - 1.1.02 Taxas iFood (#1695810) [DRE:2]
    - 1.1.03 Taxas 99food (#1695811) [DRE:2]
  - 5.2.01 Tarifas bancárias (#945357)
    - 5.2.05 Taxas de pix (#945359) [DRE:4]
  - Custo com frete (#945368)
    - 1.1.04 Comissão entregadores (motoboy) (#965890) [DRE:2]
    - 2.3.02.02 Uber/99 (#945369) [DRE:3]
  - Custos com produtos (#945360)
    - 2.4.07 Decoração (#982316) [DRE:3]
    - 2.4.09 Equipamentos de loja (#1025587) [DRE:3]
    - 4.3.01 Ações promocionais (#968728) [DRE:3]
    - 4.3.03 Impressos (#1589050) [DRE:3]
- 2 Despesas Operacionais (#945263)
  - 2.1 Equipe (#1695816)
    - 2.1.01 Salários (#945317) [DRE:3]
    - 2.1.02 Encargos trabalhistas (#1695817) [DRE:3]
    - 2.1.04 Freelancers / diaristas (#945322) [DRE:3]
    - 2.1.05 Benefícios (#1695818)
      - 2.1.05.01 Alimentação (#945323)
        - 2.1.05.01.01 Água (#1665262) [DRE:3]
    - 2.1.06 Entregadores (diária fixa) (#945324) [DRE:3]
  - 2.1.03 Comissão funcionários (#968776) [DRE:3]
  - 2.1.07 Recrutamento (vagas, anúncios) (#968775) [DRE:3]
  - 2.2 Estrutura Física (#1695820)
    - 2.2.03 Energia elétrica (#945267) [DRE:3]
    - 2.2.06 Internet (#945266) [DRE:3]
    - 2.2.11 Gás (#968777) [DRE:3]
    - 2.2.12 IPTU (#945270) [DRE:3]
  - 2.2.01 Aluguel (#945268) [DRE:3]
  - 2.2.04 Água (#945269) [DRE:3]
  - 2.2.13 Seguro (#945345) [DRE:3]
  - 2.2.14 Celular (#945265) [DRE:3]
  - 2.2.16 Manutenção elétrica (#1040044) [DRE:3]
  - 2.4.06 Pequenos reparos (#998254) [DRE:3]
  - 5.1.01 Simples Nacional (#945358) [DRE:1]
  - Despesas administrativas (#945264)
    - 2.1.05.02 Transporte Funcionários (#967269) [DRE:3]
    - 3.2.01 Contabilidade (#945271) [DRE:4]
    - 3.4.02 Outros softwares (#945272) [DRE:4]
    - Serviços (#945275)
      - 2.2.08 Controle de Pragas (#945327) [DRE:3]
      - 3.3.01 Gestão financeira (#945277) [DRE:4]
      - 3.3.02 Gestão de tráfego (#945276) [DRE:4]
      - 3.3.05 Gestor iFood (#945278) [DRE:4]
      - 3.3.06 Gestor de estoque (#1142344) [DRE:4]
  - Despesas com materiais e equipamentos (#945325)
    - 2.2.15 Manutenção ar condicionado (#945331) [DRE:3]
    - 2.4.01 Material de Cozinha (#945329) [DRE:3]
    - 2.4.02 Material de Limpeza (#945328) [DRE:3]
    - 2.4.03 Material de Expediente (#945326) [DRE:3]
    - 2.4.05 Manutenção equipamentos (#967274) [DRE:3]
    - 2.4.08 Manutenção móveis (#945330) [DRE:3]
  - Despesas com pessoal (#945316)
    - 2.4.04 Uniforme (#968774) [DRE:3]
    - 6.1 Pró-labore (#945320) [DRE:7]
- 3 Despesas Administrativas (#1695821) [DRE:4]
- 4 Marketing e Crescimento (#1695822) [DRE:3]
- 5 Financeiro (#1695823)
- 6 Sócios e Capital (#1695824)
- 7 Expansão e Investimentos (#1695825)
- Consumo (#1007993) [DRE:3] [CAIXA] [P]
- Despesas Financeiras (Taxas de cartão + Aluguel Máquinas) (#939324) [DRE:2] [CAIXA] [P]
- Diferença de caixa (#939322) [DRE:3] [CAIXA] [P]
- Fiado (#939325) [CAIXA] [P]
- Fornecedores (#939307) [CAIXA] [P]
  - 1.2.01 Insumos (#945362)
    - 1.2.01.01 Pão (#1665263)
  - 1.2.02 Embalagens (#945366)
  - 1.2.03 Bebidas (#945363)
  - 1.2.04 Salgados (#1695815)
  - 1.2.05 Congelados (#945361)
  - 1.2.06 Hortifruti (#945364)
  - 1.2.07 Descartáveis (embalagem de pedido) (#945367)
- Frente de Caixa (#939323) [CAIXA] [P]
- Garçom (#939316) [DRE:2] [CAIXA] [P]
- Investimentos (#945338)
  - Investimentos em bens materiais (#998255)
    - 2.2.10 Reformas (#998256) [DRE:3]
  - Investimentos em marketing (#945339)
    - 3.3.03 Social Media (#1074977) [DRE:4]
    - 3.3.04 Design (#1258778) [DRE:4]
    - 3.4.03 Site / cardápio digital (#1025589) [DRE:4]
    - 4.1.01 Meta Ads (#945341) [DRE:3]
    - 4.1.02 Google Ads (#945342) [DRE:3]
    - 4.1.03 TikTok Ads (#945343) [DRE:3]
    - 4.1.04 Ifood Ads (#945344) [DRE:3]
- Motoboy (#939315) [DRE:2] [CAIXA] [P]
- Movimentações não operacionais (#945346)
  - Entradas não operacionais (#945347)
    - 5.2.06 Empréstimos obtidos (#945348)
    - 6.4 Aportes dos sócios (#945349)
    - 7.1.03 Venda de equipamentos usados (#945350)
  - Saídas não operacionais (#945351)
    - 5.2.03 Empréstimos (#945352) [DRE:4]
    - 5.2.04 Juros empréstimos (#945353) [DRE:4]
    - 6.2 Distribuição de lucros (#945355)
- Saldo Inicial (#939326) [CAIXA] [P]
```

**Gap conhecido, "Fase 1c" no roadmap:** várias categorias com código
numérico (ex: `3.2.01 Contabilidade`, `5.2.01 Tarifas bancárias`) ainda
moram fisicamente dentro de wrappers antigos (`Despesas administrativas`,
`Custo com frete`, `Investimentos`, etc), não dentro das raízes numeradas 1
a 7. Isso é só estética: DRE e relatório usam o `id` da categoria, não a
posição na árvore. Arrastar pra posição final é opcional.

## Vinculação ao DRE

**61 das 100 categorias estão vinculadas a uma seção do DRE.** As outras 39
ficam sem vínculo de propósito, não por lacuna:

| Grupo sem vínculo | Categorias | Por quê |
|---|---|---|
| Compra de mercadoria | `Fornecedores` e as 7 filhas (Insumos, Embalagens, Bebidas, Salgados, Congelados, Hortifruti, Descartáveis, Pão) | CMV já é automático pelo estoque. Vinculado, o custo conta duas vezes |
| Já é receita automática | `Fiado`, `Frente de Caixa` | Já entram em `(+) Receita Operacional Bruta`, vincular duplicaria |
| Capital, não operação | `6.2 Distribuição de lucros`, `6.4 Aportes dos sócios`, `7.1.03 Venda de equipamentos usados`, `5.2.06 Empréstimos obtidos` | Entrada/saída de capital dos sócios, não resultado do negócio |
| Saldo patrimonial | `Saldo Inicial` | Foto de saldo de conta, não é resultado do período. Vinculado, infla o lucro do mês de corte |
| Categoria-pai ambígua | `5 Financeiro`, `6 Sócios e Capital` | A raiz mistura filhas que vão pra seções diferentes (Impostos e Despesas financeiras; Pró-labore e capital), não dá pra escolher uma seção só |
| Categoria-pai/wrapper sem vínculo direto | `1.1 Custos de Venda`, `2.1 Equipe`, `2.1.05 Benefícios`, `2.2 Estrutura Física`, `7 Expansão e Investimentos`, e os 12 wrappers antigos sem código (`Custo com frete`, `Custos com produtos`, `Despesas administrativas`, `Serviços`, `Despesas com materiais e equipamentos`, `Despesas com pessoal`, `Investimentos`, `Investimentos em bens materiais`, `Investimentos em marketing`, `Movimentações não operacionais`, `Entradas não operacionais`, `Saídas não operacionais`) | Vincular uma categoria-pai no Saipos cascateia a seção pra todos os filhos e trava a edição individual deles. Como a árvore ainda tem o gap da Fase 1c (filho com código de uma raiz, morando fisicamente em outra), cascatear pelo pai erraria a seção de vários filhos. Ficam sem vínculo até a reorganização física acontecer |

Critério usado (mesmo do Oka Guaraná, ver
`../decisoes/2026-08-23-vincular-categorias-ao-dre.md`): raiz `1 Custos
Variáveis` (menos a subárvore de compra) vai em `2, Custo com vendas`; raiz
`2 Despesas Operacionais` vai em `3, Despesas administrativas`; raiz `3
Despesas Administrativas` (serviço central) vai em `4, Despesas financeiras`
por convenção; raiz `4 Marketing e Crescimento` vai em `3, Despesas
administrativas`; `5.1.x` (impostos) vai em `1, Impostos`; `5.2.x`
(despesa financeira real) vai em `4, Despesas financeiras`; `6.1 Pró-labore`
vai em `7, Pró-labore`.

**Efeito real no DRE Gerencial**, mesmo período (01 jun a 31 ago/2026):
lucro operacional total caiu de R$ 77.130,40 (quando só 6 categorias
estavam vinculadas) pra R$ 28.750,49 (com as 61 vinculadas). O número
antigo estava inflado porque quase nenhuma despesa real aparecia separada
por seção.

## Categorias que de fato receberam lançamento (01/01 a 22/08/2026)

**Atenção: esta tabela usa os NOMES de antes da migração** (ainda não foi
recalculada com o extrato pós-migração). Total por categoria em
`dados/despesas-por-categoria-62061-2026-01-a-08.csv`. Puxar de novo depois
que a Fase 1c (reorganização física) acontecer, se acontecer. As 15 maiores
em volume (sempre negativo = saída, positivo = entrada):

| Categoria (nome antigo) | Total 2026 (jan a 22/08) |
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

**Achado sobre receita:** o relatório `Lançamentos financeiros` não mostra
nenhum valor relevante nas categorias de receita. A receita real está no
relatório `Vendas por período` (ver
`../dados/vendas-por-periodo-62061-2026-01-a-08.md`), não nos lançamentos
financeiros manuais. O financeiro (contas a pagar/receber) e o comercial
(vendas do PDV) não estão conciliados num único relatório hoje. Perguntar
ao Jonas se existe fechamento manual que junta os dois.

## Filtro usado nas automações

Nenhuma automação de leitura por categoria configurada ainda (n8n ou
equivalente). Quando existir, documentar aqui o filtro exato, igual o Oka
Guaraná faz.

## Regra de padronização entre unidades

A estrutura de categorias precisa ser idêntica em todas as lojas, senão a
consolidação não fecha. Qualquer categoria nova entra em todas ao mesmo tempo.
Hoje só a loja Ge Burger (62061) foi mapeada, não há confirmação de quantas
unidades existem no total (ver `08-roadmap-implantacao.md`).
