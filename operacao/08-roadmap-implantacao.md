# 08, Roadmap de implantação

**Versão 2, 22/08/2026.** Fase 0 100% concluída para a loja Ge Burger (62061).

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
- [ ] **Jonas responder as 7 pendências da proposta** (o que é "Comissão
      entregadores" vs "Entregadores" vs "Delivery compras", o que é
      "Descartáveis", por que Pró-labore está zerado, etc.)
- [ ] **Executar a migração no Saipos** depois das pendências resolvidas:
      renomear, mover, criar e excluir categoria conforme a proposta
- [ ] **Vincular as 91 categorias que faltam ao DRE.** Isso vem depois da
      migração estrutural, é trabalho de tela: entrar em `DRE Gerencial >
      Vincular` e escolher a seção de cada categoria com lançamento
- [ ] Decidir se `Fiado`, `Frente de Caixa`, `Fornecedores` e `Saldo Inicial`
      ficam propositalmente sem vínculo (como no Oka) ou se o Geburger quer
      outro critério

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

- [ ] Bloqueado pela Fase 1 (vinculação de categorias). O `DRE Gerencial`
      de hoje mostra lucro líquido de R$ 77.130,40 em jun-ago/2026, mas esse
      número está incompleto porque quase nenhum custo real está
      classificado numa seção. Não é o resultado real do negócio

## Onde paramos

22/08/2026: primeiro levantamento completo da loja Ge Burger (62061) feito
via API do Saipos. Dados brutos salvos em `dados/`. Documentos 02, 04 e 06
atualizados com número real. Achado mais importante da sessão: **o DRE
Gerencial do Saipos não pode ser usado para decisão ainda**, porque 91 das
97 categorias financeiras não estão vinculadas a nenhuma seção. **Fase 0
fechada**: Jonas confirmou loja única, passou CNPJ/endereço/horário, e
confirmou que os canais de venda batem com a percepção dele. Próximo passo
natural: montar a árvore de categorias numerada (Fase 1, decisão já tomada
de reaproveitar o padrão de codificação do Oka Guaraná adaptado à estrutura
que já existe aqui), e investigar a causa do estoque negativo generalizado
antes de confiar no CMV calculado (Fase 2).
