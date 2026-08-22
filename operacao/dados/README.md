# operacao/dados/

Exports crus tirados direto do sistema. Arquivo aqui é fonte primária, não
interpretação. Interpretação vai nos arquivos numerados.

## Convenção de nome

`[conteúdo]-[unidade]-[AAAA-MM-DD].csv`, unidade pelo ID do PDV.

## Arquivos

| Arquivo | Conteúdo | Como foi extraído |
|---|---|---|
| [vazio até o primeiro levantamento] | | |

Toda linha desta tabela precisa dizer **como** o arquivo foi extraído: tela,
relatório, API ou digitação. Export sem origem declarada não serve de fonte.

## Regra de dado

Nenhum arquivo aqui pode ter telefone, nome ou endereço de cliente. Nome de
fornecedor pode entrar quando for o texto que aparece no extrato bancário e
o contador precisar dele para classificar. CPF não entra em nenhum arquivo
deste repositório.
