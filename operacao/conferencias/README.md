# operacao/conferencias/

Relatório de cada conferência física de estoque, um arquivo por data e por
loja. Compara a contagem física com o estoque que o sistema mostrava na
extração mais recente disponível em `../dados/`.

## Convenção de nome

`[AAAA-MM-DD]-[unidade].md`, unidade pelo nome curto.

O dado bruto da contagem (item, unidade, conversão, físico x sistema) fica em
`../dados/contagem-fisica-[id]-[AAAA-MM-DD].csv`, seguindo a convenção de
`../dados/README.md`. O `.md` aqui é a leitura interpretada: crítico, atenção,
o que bateu, itens não cadastrados e pendências.

## Por que existe

Para dar pra comparar uma conferência com a anterior e ver se o processo está
melhorando, em vez de só saber que faltou coisa.
