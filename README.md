# Geburger

Base de conhecimento e de trabalho do Geburger, hamburgueria em Manaus/AM.

## Como está organizado

- `CLAUDE.md`: instruções gerais sobre o negócio, como o Claude Code deve
  agir e onde cada coisa fica
- `dados/`: dados agregados usados por mais de uma frente
- `decisoes/`: histórico de decisões, um arquivo por decisão
- `operacao/`: financeiro, estoque, cardápio, pessoas, delivery
- `trafego/`: tráfego pago, baseline, campanhas, criativos, relatórios

Cada pasta de frente (`operacao/`, `trafego/`) tem seu próprio `CLAUDE.md`
com as regras específicas daquela área.

## Como usar com o Claude Code

Abra este repositório com `claude` no diretório raiz. O `CLAUDE.md` da raiz
carrega automaticamente. Ao trabalhar dentro de `trafego/` ou `operacao/`, o
CLAUDE.md daquela pasta se soma ao da raiz.

Dado pessoal de cliente não entra neste repositório em hipótese alguma. Veja
a regra completa no `CLAUDE.md` da raiz.

## Estado

Estrutura criada em 21/08/2026, espelhando o repositório `oka-guarana`. O
levantamento de dados ainda não foi feito. Todo campo marcado com
`[preencher]` é lacuna conhecida, não esquecimento.
