# 02, Plano de contas

**Versão 1, 22/08/2026.** Levantado da tela `DRE Gerencial > Vincular` da
loja Ge Burger (62061).

## Seções do DRE

O Saipos oferece 7 seções vinculáveis. `Receita Operacional Bruta` e `CMV`
não aparecem na lista porque são automáticas (o sistema calcula direto,
não por vínculo de categoria).

| # | Seção |
|---|---|
| 1 | Impostos |
| 2 | Custo com vendas |
| 3 | Despesas administrativas |
| 4 | Despesas financeiras |
| 5 | Receita não operacional líquida |
| 6 | IR |
| 7 | Pró-labore |

## Tabela de vinculação

Estado real em 22/08/2026: **6 de 97 categorias raiz vinculadas.** As outras
91 aparecem como "Selecione a seção" no modal de configuração. Ver o alerta
completo em `04-categorias-financeiras.md`.

| Categoria | Seção do DRE |
|---|---|
| Consumo | 3, Despesas administrativas |
| Despesas Financeiras (Taxas de cartão + Aluguel Máquinas) | 4, Despesas financeiras |
| Diferença de caixa | 3, Despesas administrativas |
| Garçom | 3, Despesas administrativas |
| Motoboy | 2, Custo com vendas |
| Saldo Inicial | 5, Receita não operacional líquida |

Todo o resto (Insumos, Salário de funcionários, Aluguel, marketing,
embalagens, hortifruti, etc.) está sem seção. Isso não impede o lançamento
financeiro (o dinheiro é registrado normalmente), mas impede o `DRE
Gerencial` de mostrar a estrutura por seção corretamente.

## DRE Gerencial, snapshot de jun a ago/2026

Lido direto da tela em 22/08/2026, sem nenhuma vinculação adicional feita:

| | Junho | Julho | Agosto (parcial) | Total |
|---|---|---|---|---|
| (+) Receita operacional bruta | R$ 41.550,40 | R$ 39.069,89 | R$ 30.968,20 | R$ 111.588,49 |
| (-) Impostos | R$ 0,00 | R$ 0,00 | R$ 0,00 | R$ 0,00 |
| (=) Receita líquida | R$ 41.550,40 | R$ 39.069,89 | R$ 30.968,20 | R$ 111.588,49 |
| (-) CMV | R$ 11.398,02 (27,43%) | R$ 11.192,26 (28,65%) | R$ 8.985,62 (29,02%) | R$ 31.575,90 (28,30%) |
| (=) Lucro operacional bruto | R$ 30.152,38 | R$ 27.877,63 | R$ 21.982,58 | R$ 80.012,59 |
| (-) Despesas administrativas | -R$ 0,03 | -R$ 0,03 | R$ 0,02 | -R$ 0,01 |
| (-) Despesas financeiras | R$ 1.059,79 | R$ 1.127,62 | R$ 694,79 | R$ 2.882,20 |
| (=) Lucro operacional | R$ 29.092,59 | R$ 26.750,04 | R$ 21.287,77 | R$ 77.130,40 |
| (=) Lucro líquido do exercício | R$ 29.092,59 | R$ 26.750,04 | R$ 21.287,77 | R$ 77.130,40 |

**Isto não é o resultado real do negócio.** `Despesas administrativas` deu
quase zero porque só `Consumo`, `Diferença de caixa` e `Garçom` estão
vinculados a ela, e nenhuma das três recebeu lançamento relevante no
período. O gasto real do trimestre com insumo, salário, aluguel e marketing
soma dezenas de milhares de reais (ver `04-categorias-financeiras.md`), mas
não aparece aqui porque a categoria não está vinculada a nenhuma seção.

**Não usar este DRE para decisão até vincular as categorias.** Isso é
trabalho de configuração no Saipos, não de leitura: alguém precisa abrir
`DRE Gerencial > Vincular` e escolher a seção de cada categoria que recebe
lançamento, uma por uma.

## Categorias que ficam sem vínculo de propósito

Ainda não há decisão registrada de quais categorias devem ficar
propositalmente sem seção (equivalente ao Oka, onde `Fiado`, `Frente de
Caixa`, `Fornecedores` e `Saldo Inicial` ficam fora do DRE porque são
movimentação patrimonial, não resultado). Candidatas por analogia de nome,
a confirmar:

- `Fiado`, `Frente de Caixa`, `Fornecedores`: parecem ser categorias padrão
  do sistema, prováveis candidatas a ficar sem vínculo
- `Saldo Inicial`: já está vinculado a `5, Receita não operacional líquida`
  no Geburger, diferente da recomendação do Oka (lá ficou decidido sem
  vínculo, porque saldo de conta é foto patrimonial, não resultado). Vale
  perguntar ao Jonas se isso foi proposital ou herdou configuração padrão
  do Saipos
- `Investimentos` (e as subcategorias de marketing): decisão em aberto se
  entra como despesa operacional ou fica separado
- `Movimentações não operacionais`: por nome, parece corresponder à seção 5
  do DRE (Receita não operacional líquida), mas não está vinculada
