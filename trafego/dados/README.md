# trafego/dados/

Dado bruto puxado do MCP da Meta, do Gerenciador ou das plataformas, salvo como
veio. Interpretação vai nos arquivos numerados de `../`.

## Convenção de nome

`[conteúdo]-[período, se houver]-[AAAA-MM-DD].[json|csv]`

A data no nome é a data da **extração**, não a do dado. O período do dado vai no
meio do nome ou dentro do arquivo.

## Regras

- Toda extração declara período e janela de atribuição
- Export manual é fallback. Enquanto o MCP responder, o caminho é o MCP
- Nenhum arquivo aqui pode ter telefone, nome ou endereço de cliente

## Arquivos

| Arquivo | Conteúdo | Origem |
|---|---|---|
| [vazio até a primeira extração] | | |
