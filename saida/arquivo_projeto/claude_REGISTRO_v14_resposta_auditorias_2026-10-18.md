# Plataforma Câmara 2026 — v14 (prévia) e resposta às auditorias de 18/10/2026

Insumos: AUDITORIA_INDEPENDENTE_GPT_PLATAFORMA_V13 e a revisão complementar que a acompanha. Executor: Claude (parte interessada: autor da v13). Prévia v14 privada: https://claude.ai/artifact/2QxJibWAiNvnU1unBppV5w (versão 1792350452-ee89). URL da candidata continua na v13 (id 1792348644-fc94) até o "sim" do Fundador.

## 1. Conferências feitas antes de corrigir
| Afirmação | Resultado |
|---|---|
| pacote.json publicado ao lado do index.html é v1.7 (286 itens) | CONFIRMADO no arquivo publicado (sha256 f20216c2…). A página não o lê; ela usa o pacote embutido v1.9. |
| Faltam 48 ids no v1.7: L1-R01…18, L2-R01…18, L3-R01…11, L6A-R01 | CONFIRMADO (18 + 18 + 11 + 1). Com o v1.7 carregado à mão, 13 dos 30 ids do D30-P2 somem e o diagnóstico de Fala não aparece; D30-P1 não é afetado. |
| SHA-256 do index.html v13 = 3593120c… | CONFIRMADO: é o hash do arquivo que eu li de volta da URL publicada logo após publicar (registrado no relatório da Fase 2). A identidade remota foi conferida. |
| BQ-0095 = CAMDEP12_CB1_01, item 43, gabarito definitivo C | Conferido pelo GPT no gabarito definitivo oficial; fecha a ressalva que eu tinha deixado. |
| Sobreposição D30-P1 × SIM-0 = 5 itens | CONFIRMADO. |

## 2. Correções na v14 (em cópia)
| Achado | Correção | Teste |
|---|---|---|
| A01 pacote.json v1.7 | Substituído por pacote.json gerado do pacote embutido v1.9 (334 itens; objeto idêntico; sha256 6cace34e…). | igualdade de objeto verificada |
| A03 escolha gravada por módulo | Nova chave S.escolhaDisc por id da disciplina (cd26-c11/p1/ti…), criada na carga a partir de P1/P2; S.escolha por módulo continua sendo escrita para o código legado. | C3, C5 |
| A04 "Mudar meu caminho" abre no topo | Abre a tela de disciplinas posicionada e com foco na disciplina tocada. | C4 |
| A02 três "diagnósticos" misturados | Simulados agrupados: "Diagnóstico de 30 itens" (topo), "Simulados finais", "Diagnósticos anteriores" (SIM-0 e SIM-0-P2, com legenda). Nomes do pacote não alterados. | C6 |
| A05 código morto | vBoas e vEntrada removidos; S.boasVindas mantido (marca a usuária da v12 na migração). | regressões abaixo |
| Versão no arquivo | meta mapaspro:versao = "v14 · 18/10/2026 · pacote F4 v1.9 embutido · diagnóstico de 30 revisado". O hash não pode ficar dentro do próprio arquivo (mudaria o hash); fica aqui: corpo publicado sha256 1190a0bd0c4e…. | C1 |

Inalterados: pacote embutido (byte a byte), chaves c2026.v01.*, seleção dos 60 itens.

## 3. Cenários de migração testados (Chromium headless, estado sintético)
C1 usuária nova → tela do concurso. C2 usuária da v12 sem escolha, só com simulado → entra no estudo, concurso migrado, tentativa preservada, nenhuma escolha inventada. C3 usuária da v12 com escolhas P1/P2, rascunho de discursiva e erro pendente → escolhaDisc criado, legado mantido, rascunho e erro intactos. C4/C5 mudar caminho por disciplina → foco correto, grava nas duas chaves, evento caminho_mudado. C6 simulados agrupados, sem rolagem em 360 px. Mais: estado igual ao da candidata (escolhas "do zero", tentativa DIAG-P2 1/17, 2 erros) e os testes T01–T10 (52/52) e a regressão anterior (67/67). Prova em andamento não é persistida ao recarregar (comportamento igual ao da v12; não é regressão).

## 4. Registro de decisões
- Ocultar os recortes DIAG-P1/P2 da lista e aceitar 5 itens do SIM-0 no D30-P1: recomendados no relatório da Fase 1, constavam da prévia da Fase 2 e foram publicados com o "Sim, publicar" do Fundador em 18/10/2026. Registro aqui como decisão aprovada por esse ato; se o Fundador preferir outra leitura, revertemos.
- ERRATA ao relatório da Fase 1: ele descrevia a escolha gravada por id de disciplina; a v13 gravou por módulo (equivalente com 2 disciplinas, mas fora do plano). A v14 corrige.
- diag30_selecao_para_revisao.json (v1) fica como registro PRÉ-REVISÃO, sem alteração (o GPT citou o hash dele). Seleção vigente: diag30_selecao_v2_vigente.json (sha256 486ab3ea…) e diag30_final.json, iguais ao DIAG30 do código.

## 5. Pontos das revisões que não procedem ou não são deste produtor
- "Plataforma Câmara 2026.md" com só "Abrindo o caderno": não foi gerado por este chat; parece exportação da página (que monta o conteúdo por script). Pode ser descartado.
- prototipo-entrada-camara-cargo11-v01.html: nunca recebido (NÃO ACESSADO desde a Fase 1); a referência visual usada foi a imagem do mockup e a prévia de desenho da Fase 1.
- aria-disabled nas disciplinas "em preparação": não se aplica; são linhas de texto, não controles.
- "Os demais 55 itens precisam de reverificação normativa": a revisão independente do GPT de 18/10 leu os 60 itens (gabarito, aderência, ambiguidade, repetição); certificação contra gabaritos definitivos de todos os itens Cebraspe não foi feita por ninguém e continua como limite declarado.

## 6. Não verificado
Celular real, leitor de tela, teclado completo, download real (a prévia não declara a capacidade de download; a URL da candidata declara).
