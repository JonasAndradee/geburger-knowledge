# 08, Roadmap de implantação

**Versão 3, 23/08/2026.** Fase 0 e Fase 1 concluídas para a loja Ge Burger (62061).

Onde estamos e o que falta. Este é o arquivo que responde "por onde eu continuo".

## Fase 0: levantamento

- [x] Confirmar qual PDV: Saipos, mesma plataforma do Oka Guaraná
- [x] Confirmar ao menos uma unidade e ID no PDV: Ge Burger, loja 62061
- [x] Confirmar se existe mais de uma unidade Geburger: não, loja única,
      confirmado com o Jonas
- [x] Confirmar CNPJ, endereço, horário de funcionamento: CNPJ
      41.861.038/0001-36, R. Alexandre Magno nº 497, Parque 10 de Novembro,
      Manaus/AM. Horário em `unidades/ge-burger.md` (segunda-feira fechado)
- [x] Puxar ingredientes e insumos completos (149 ingredientes, 16
      beneficiados, 53 fichas técnicas)
- [x] Puxar composição de todas as 53 fichas técnicas
- [x] Puxar árvore completa de categorias financeiras (97 raízes, 252 nós)
- [x] Puxar cardápio completo (183 produtos)
- [x] Puxar despesas por categoria, jan a 22/08/2026
- [x] Puxar vendas por período, jan a 22/08/2026 (em 3 janelas de 3 meses,
      limite da tela)
- [x] Confirmar canais de venda ativos e a participação de cada um: Jonas
      confirmou que bate com a percepção dele
- [x] Preencher `../CLAUDE.md` e `CLAUDE.md` desta pasta com o que foi
      confirmado (parcial, ainda restam campos de negócio como sócios e
      ticket médio por canal)

## Fase 1: plano de contas

- [x] Levantar as seções do DRE disponíveis no Saipos (7 seções)
- [x] Levantar quais categorias estão de fato vinculadas: só 6 de 97
- [x] Montar a proposta de árvore padronizada com o Oka Guaraná, ver
      `../decisoes/2026-08-22-padronizar-categorias-financeiras-com-oka.md`
- [x] Jonas respondeu as 7 pendências da proposta (Comissão
      entregadores/Entregadores/Delivery compras, Descartáveis, Pró-labore,
      Recursos Humanos, Receita de Vendas, Pagamento de dívidas passadas,
      Garçom). Estrutura fechada, pronta pra execução
- [x] **Migração executada no Saipos em 22/08/2026.** 97 categorias
      viraram 101, renomeadas com o código numérico, `Receita de Vendas`
      excluída (com transferência de lançamento real pro Saipos), 4
      categorias vazias/duplicadas excluídas. Único ajuste em relação ao
      plano: "Comissão entregadores" tinha 215 lançamentos individuais e o
      Saipos não tem troca de categoria em lote, então ficou como categoria
      própria renomeada em vez de fundir em "Motoboy". Detalhe completo em
      `../decisoes/2026-08-22-padronizar-categorias-financeiras-com-oka.md`
- [ ] **Fase 1c, opcional:** boa parte do conteúdo renomeado ainda mora
      fisicamente dentro dos wrappers antigos (ex: `3.2.01 Contabilidade`
      dentro de `Despesas administrativas`, que é filha da raiz `2`, não da
      raiz `3`), não dentro das raízes numeradas novas. Não afeta DRE nem
      relatório (que são por id, não por posição na árvore), é só estética.
      Arrastar pra posição final se o Jonas quiser a árvore idêntica à do
      Oka
- [x] **Puxar novo extrato de `04-categorias-financeiras.md`** pós-migração,
      feito em 23/08/2026 (100 categorias, 18 raízes)
- [x] **Vincular as categorias ao DRE**, feito em 23/08/2026. 61 de 100
      vinculadas, reaproveitando o critério do Oka (raiz decide a seção,
      categoria-pai nunca recebe vínculo direto pra não cascatear seção
      errada). 2 correções em cima do que já estava configurado (`Despesas
      Financeiras` e `Garçom` foram pra `Custo com vendas`, não `Despesas
      administrativas`/`financeiras`) e 1 desvínculo (`Saldo Inicial`, pra
      não inflar o lucro do mês de corte). Detalhe completo em
      `../decisoes/2026-08-23-vincular-categorias-ao-dre.md`. Efeito real:
      lucro operacional do trimestre jun-ago caiu de R$ 77.130,40 (número
      fake, quase nada vinculado) pra R$ 28.750,49 (número real)
- [x] Decidir se `Fiado`, `Frente de Caixa`, `Fornecedores` e `Saldo Inicial`
      ficam propositalmente sem vínculo: sim, mesmo critério do Oka. Ver
      decisão acima

## Fase 2: cadastro de estoque e fichas

- [x] Estoque e fichas já estão cadastrados no Saipos (218 itens, 53 fichas)
- [ ] **Investigar por que 44% dos itens (96 de 218) estão com saldo
      negativo**, incluindo os ingredientes-base de quase todo hambúrguer
      (queijo cheddar, brioche, blend). Ver `06-estoque-ingredientes-e-fichas.md`
- [ ] Confirmar se existe rotina de lançamento de compra com nota e entrada
      manual de estoque sem nota

## Fase 3: conferência física

- [ ] Nenhuma conferência física registrada ainda. Primeira conferência
      destrava a correção do estoque negativo acima

## Fase 4: DRE fechando

- [x] Desbloqueado pela Fase 1. O `DRE Gerencial` já mostra número real:
      lucro operacional de R$ 28.750,49 em jun-ago/2026 (era R$ 77.130,40
      antes da vinculação)
- [ ] **Investigar agosto/2026.** `Despesas administrativas` do mês
      aparece perto de zero, destoando de junho/julho. Provável falta de
      lançamento (aluguel, salário) até a data de corte, não erro de
      vínculo, mas precisa confirmar antes de fechar o mês
- [ ] Ainda falta: conciliar financeiro (lançamentos manuais) com comercial
      (vendas do PDV) num relatório só, e decidir se marketing entra como
      despesa operacional ou fica separado (ver `04-categorias-financeiras.md`)

## Onde paramos

23/08/2026: **Fase 1 fechada.** Categorias migradas pro padrão numérico do
Oka Guaraná (22/08) e vinculadas ao DRE (23/08), 61 de 100. O `DRE
Gerencial` já pode ser lido com número real: lucro operacional de
R$ 28.750,49 no trimestre jun-ago, contra o R$ 77.130,40 fake de antes.
Documentos 02 e 04 atualizados. Pendência aberta em agosto (despesa
administrativa quase zero, provável falta de lançamento) e a Fase 1c
(reorganização física, opcional, só estética) seguem em aberto.

Próximo passo natural: **Fase 2**, investigar por que 44% do estoque está
com saldo negativo, antes de confiar no CMV que o DRE já mostra
automaticamente. Sem isso, o número de CMV do próprio DRE pode estar
distorcido mesmo com a vinculação certa.
