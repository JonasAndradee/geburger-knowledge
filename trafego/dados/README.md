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
| `meta-campanhas-maximum-2026-08-21.json` | Todas as 121 campanhas da conta, histórico completo (jul/2023 a ago/2026), atributos e métricas agregadas por campanha | MCP da Meta, `ads_get_ad_entities` nível campanha, `date_preset: maximum`, 21/08/2026 |
| `meta-conjuntos-maximum-2026-08-21.json` / `.csv` | 221 conjuntos de anúncio, histórico completo, com segmentação (`targeting`) e métricas | MCP da Meta, nível adset, `date_preset: maximum` |
| `meta-anuncios-maximum-2026-08-21.json` / `.csv` | 300 anúncios (maiores gastadores, limite da ferramenta), com criativo, resultado e métricas de vídeo | MCP da Meta, nível ad, ordenado por gasto decrescente |
| `meta-conta-diario-2023-07-22-a-2026-08-21.csv` | Série diária da conta inteira, 1.115 dias, jul/2023 a ago/2026 | MCP da Meta, nível ad_account, `time_increment: 1`, 2 chamadas concatenadas (limite de tamanho por chamada) |
| `meta-quebra-plataforma-mensal-2026-08-21.csv` | Gasto e resultado por plataforma (Facebook/Instagram/Audience Network/WhatsApp/Threads), mensal | MCP da Meta, breakdown `publisher_platform` |
| `meta-quebra-posicionamento-mensal-2026-08-21.csv` | Idem, por posicionamento (feed, stories, reels, etc.), mensal | MCP da Meta, breakdown `platform_position` |
| `meta-quebra-hora-mensal-2026-08-21.csv` | Idem, por hora do dia, mensal | MCP da Meta, breakdown `hourly_stats_aggregated_by_advertiser_time_zone` |
| `meta-quebra-idade-mensal-2026-08-21.csv` | Idem, por faixa etária, mensal | MCP da Meta, breakdown `age` |
| `meta-quebra-genero-mensal-2026-08-21.csv` | Idem, por gênero, mensal | MCP da Meta, breakdown `gender` |

Achados de rastreamento, públicos, páginas e erros de entrega (não salvos
como arquivo bruto, só lidos e resumidos) estão em `../00-descoberta.md`.
