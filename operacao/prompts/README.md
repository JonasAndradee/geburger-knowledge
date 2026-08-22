# operacao/prompts/

Prompts prontos de auditoria, para rodar no Claude in Chrome com a sessão do
dono autenticada no sistema.

## Regras

- Todo prompt de auditoria é **somente leitura**. Diga isso dentro do próprio
  prompt, não só no nome do arquivo
- O prompt carrega o contexto do Geburger: unidade, ingredientes, fichas e
  categorias. Ao reaproveitar em outra unidade, ajuste o contexto
- Saída do prompt vira arquivo em `../conferencias/` ou em `../dados/`,
  nunca só resposta em tela
