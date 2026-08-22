# Ge Burger

**ID no PDV (Saipos):** 62061
**CNPJ:** [preencher]
**Papel:** única unidade confirmada até 22/08/2026
**Endereço:** [preencher]
**Horário:** [preencher]
**WhatsApp:** [preencher]
**Atualizado em:** 22/08/2026

## Login do Saipos

Conta `geburgeroficial@gmail.com`, com autenticação de dois fatores por
e-mail. Sessão é única por usuário: logar em um computador novo pede para
desconectar a sessão anterior. Atenção antes de desconectar: pode derrubar
alguém da equipe usando o sistema (balcão, WhatsApp) na hora.

## Estado de configuração

| Bloco | Estado |
|---|---|
| Categorias financeiras | 97 categorias raiz (252 nós contando subcategoria). PRONTO o cadastro, mas só 6 vinculadas ao DRE. Ver `../04-categorias-financeiras.md` |
| Vinculação de DRE | CRÍTICO: 91 de 97 categorias sem seção. Ver `../02-plano-de-contas.md` |
| Conta bancária | NÃO CONFIRMADO |
| Ingredientes | 149 cadastrados, 92 compõem CMV |
| Beneficiados | 16 (blends, molhos, empanados, sucos) |
| Fichas de produto final | 53 |
| Estoque | 44% dos itens (96 de 218) com saldo negativo. Ver `../06-estoque-ingredientes-e-fichas.md` |
| Cardápio | 183 produtos cadastrados (inclui variações "S -" de salão e "D -" de delivery do mesmo item, e promoções do iFood) |
| Contagem física | Nenhuma registrada no repositório ainda |

## Números do período (01/01 a 22/08/2026)

Fonte: relatório `Vendas por período` do Saipos, 3 consultas de até 3 meses
cada (limite da tela). Ver `../dados/vendas-por-periodo-62061-2026-01-a-08.md`.

- Pedidos: 4.407 (57 cancelados, R$ 1.988,12)
- Faturamento: R$ 346.518,78
- Canal com mais pedidos: iFood, 1.134 pedidos, R$ 70.937,61
- Canal com mais faturamento: Site Delivery (SAIPOS), 822 pedidos, R$ 74.266,70
- Telefone: 285 pedidos, R$ 22.571,11
- 99Food: 66 pedidos, R$ 4.283,92 (só passou a vender a partir de abril/2026)
- Facebook e WhatsApp como canal de venda: 0 pedidos no período inteiro

## Particularidade da leitura do DRE

Diferente do Oka Guaraná (onde o problema era qual unidade paga a camada
central), aqui o problema é estrutural: o DRE Gerencial do Saipos mostra
"Despesas administrativas" perto de zero porque quase nenhuma categoria
financeira está vinculada à seção certa. O lucro líquido que a tela mostra
(R$ 77.130,40 em jun-ago/2026) não desconta o grosso do custo fixo e
variável real da operação. Não usar esse número para decisão sem antes
vincular as categorias.

## Pendências

- CNPJ, endereço e horário de funcionamento
- Confirmar se existe mais de uma unidade Geburger ou se é loja única
- Vincular as 91 categorias financeiras sem seção do DRE
- Entender por que quase metade do estoque está negativo (falta de compra
  com nota lançada? falta de contagem física?)
