# operacao/

Controle financeiro e operacional do Geburger.

Se você é um agente lendo isso, comece pelo `CLAUDE.md` desta pasta.

## Mapa dos arquivos

| Arquivo | Pergunta que ele responde |
|---|---|
| `CLAUDE.md` | Como trabalhar aqui, regras invioláveis, o que está em aberto |
| `01-manual-financeiro-geburger.md` | Por que o modelo é assim. Baldes, CMV, DRE, rotinas |
| `02-plano-de-contas.md` | Quais são as seções do DRE e o que vincular em cada uma |
| `03-processos-e-fluxos.md` | Como lançar cada coisa e onde ela aparece depois |
| `04-categorias-financeiras.md` | Qual é a árvore real de categorias |
| `05-guia-de-telas-pdv.md` | Onde fica cada tela e cada campo do sistema |
| `06-estoque-ingredientes-e-fichas.md` | Quais insumos existem, quanto custam, o que tem em cada ficha |
| `07-automacao-pdv-notas-tecnicas.md` | Como automatizar o sistema sem quebrar nada |
| `08-roadmap-implantacao.md` | Em que fase estamos e o que falta |
| `pdf/` | PDFs prontos para mandar pro contador. O `.md` ao lado de cada um é a fonte, e `md2pdf.py` regera |
| `unidades/` | Estado de configuração de cada loja, um arquivo por unidade |
| `prompts/` | Prompts prontos de auditoria, para rodar no Claude in Chrome |
| `dados/` | Exports crus do sistema, OFX, planilhas. Ver `dados/README.md` |
| `conferencias/` | Relatório de cada conferência física de estoque |

## Ordem de leitura para quem chega agora

1. `CLAUDE.md`, para as regras
2. `01-manual-financeiro-geburger.md`, para o modelo
3. `08-roadmap-implantacao.md`, para saber onde parou
4. O resto conforme a necessidade

## Convenções

- Arquivo numerado é doutrina, muda pouco e sempre com nota de versão no topo
- Decisão que muda arquitetura vira um arquivo em `../decisoes/`, com data no
  nome. Aqui dentro fica só o estado atual, não o histórico da discussão
- Nome de tela, menu e campo do sistema sempre em crase, escrito exatamente
  como aparece na tela
- Nada de travessão nos textos
