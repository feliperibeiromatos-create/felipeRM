# GCE_erratas_reconciliacao_2026-10-10.md — T-08 e T-28 — 2026-10-10 — gerado por gce-gerencia

Objeto: reconciliação de duas erratas de forma de P2 (cadeia gce-cpp → gce-cqfp → gce-gerencia), com as decisões D1 da GCE sobre as observações do QA. Base: DECISOES.md (D-DEREP, D-CANONICOS, D-REVERIFICACAO-JAN, D-FUNDADOR-AGORA-1); TAREFAS.md, linhas T-08 e T-28; relatórios saida/gce/lote3_errata_2026-10-10.md e saida/gce/lote2_errata_2026-10-10.md (produção + QA). A GCE não produziu nem revisou conteúdo: aplicou só erratas mecânicas de cabeçalho, marca e quebra de linha, sem mudar item, gabarito, fonte ou marca V.

## 1. Conferência por script (somente leitura: git show HEAD / git diff; scripts em scratchpad, python3 -I)
Método: (i) diff HEAD × arquivo no estado entregue ao QA; (ii) reconstrução do estado aprovado = HEAD + texto literal dos relatórios (sec. 3 do L3; "DEPOIS" do L2) e comparação com o arquivo: as únicas diferenças restantes são as erratas D1 desta Gerência (seção 3), o que confirma que o QA aprovou exatamente o texto que está no arquivo.

| Verificação | T-08 (GCE_Lote3_v2_CPP.md) | T-28 (GCE_Lote2_v2_CPP.md) |
|---|---|---|
| Operações no diff HEAD → entregue ao QA | 1 inserção de 23 linhas após HEAD:114, dentro de (a) CURSO, 3.1; 0 remoções | 1 substituição (HEAD 150–153 → 150–152), dentro de (a) CURSO, 2.1 |
| Texto literal do relatório = arquivo | SIM (23/23 linhas) | SIM (3/3 linhas) |
| De "(c) PARES CONFUNDÍVEIS" ao fim (itens (d), (d-G), (e), (f)) idêntico ao HEAD | SIM | SIM |
| [V (HEAD → entregue) | 1 → 2 (+1 = marca do próprio bloco, esperado) | 18 → 18 |
| NORMATIVO — QA | 35 → 35 | 7 → 7 |
| [TS] / VOLÁTIL / REVERIFICAR | 19/4/4 → 19/4/4 | 20/4/0 → 20/4/0 |
| QA PENDENTE / SEM FONTE | 0/0 → 0/0 | 0/0 → 0/0 |
| "Derep (antigo DETAQ)" no curso | — | 0 → 1 |

Divergência de contagem não material: o QA da T-08 registrou [TS] 18→18; o script desta Gerência conta 19→19 (a produtora também conta 19). Diferença de padrão de busca; antes = depois em qualquer padrão, nenhum [TS] alterado. Idem "Q<n>" (66 no QA, 68 aqui, por padrão de linha): antes = depois.

## 2. Decisão por tarefa
- T-08 — CONCLUÍDA. QA gce-cqfp APROVADO, 15/15 afirmações conferidas no texto integral oficial (Legin, Publicação Original, verificado em 10/10/2026); mudança única e no lugar declarado; 0 item, 0 gabarito, 0 marca preexistente alterados. Observações tratadas na seção 3.
- T-28 — CONCLUÍDA. QA gce-cqfp APROVADO; forma "Derep (antigo DETAQ)" conforme D-DEREP e E4; 0 item, 0 gabarito, 0 fonte, 0 marca V alterados; demais "DETAQ" estão em notas, fontes e limites (fora do curso) e ficam por E4. Ressalva cosmética tratada na seção 3.
- Nenhuma das duas bloqueia a T-27 (o pacote lê o curso dos arquivos; a T-27 já prevê incorporar a T-28).
- O estado das linhas T-08 e T-28 em TAREFAS.md não foi alterado por esta Gerência (regra de append único); registro aqui para o orquestrador/Secretaria.

## 3. Observações do QA — decisões D1 (classificação obrigatória)
| # | Origem | Observação | Decisão | Classe |
|---|---|---|---|---|
| O1 | T-08, obs. 1 | Precisão da ligação com "registro oficial" (redação alternativa opcional da CQFP) | Manter o texto aprovado. Não é mecânica (mexe em prosa didática); a CQFP julgou a afirmação CONFERE, e a frase seguinte do bloco já diz que o Ato não trata de registro de sessões. Sem tarefa. | DESCARTADO |
| O2 | T-08, obs. 2 | Ausência da marca [NORMATIVO — QA] no bloco | A convenção do lote (cabeçalho, l. 28 do HEAD) marca dispositivo normativo conferido pela CQFP; a CQFP conferiu arts. 3º, 4º e 6º no texto oficial integral. Marca aplicada após a paráfrase dos arts. 3º e 4º (35 → 36). | AGORA (aplicada) |
| O3 | T-08, obs. 3 | F4 fora da convenção de evidência | F4 acrescentada à CONVENÇÃO DE EVIDÊNCIA, com a URL da [V] do bloco. | AGORA (aplicada) |
| O4 | T-08, obs. 3 | N7 desatualizada | N7 completada: lei específica de IA segue NÃO VERIFICADO; Ato da Mesa 225/2025 (F4) registrado como norma interna, só contexto, sem item. | AGORA (aplicada) |
| O5 | T-08, obs. 4 | Incluir o Ato na reverificação de 4–8/1/2027 | Não é mecânica nem cabe nesta janela; a linha da T-11 não pode ser alterada aqui. Tarefa nova (seção 5), sem marca REVERIFICAR no lote (contagem de marcas do lote preservada). | PRÓXIMO (tarefa) |
| O6 | T-28, obs. 3 | Linha 152 com 122 caracteres | Quebra de linha aplicada; texto normalizado do curso idêntico ao aprovado. | AGORA (aplicada) |

## 4. Tabela de Correções (erratas D1 da GCE, 10/10/2026; sem mudança de item, gabarito, fonte ou marca V)
| Código | Arquivo | Localização | Antes → depois |
|---|---|---|---|
| T-08 (registro) | GCE_Lote3_v2_CPP.md | TABELA DE CORREÇÕES do cabeçalho | +2 linhas: "T-08 → (a), 3.1, bloco CONTEXTO NORMATIVO INTERNO…" |
| G1-a (O3) | GCE_Lote3_v2_CPP.md | CONVENÇÃO DE EVIDÊNCIA, após F3 | +6 linhas: "F4 Câmara/Legin — Ato da Mesa nº 225, de 15/12/2025, publicação original…" (URL igual à da [V] do bloco) |
| G1-b (O4) | GCE_Lote3_v2_CPP.md | LIMITES, N7 | "…Nenhum item trata de regulação própria de IA." → + "Norma interna da Câmara: Ato da Mesa nº 225/2025 (F4), verificado em 10/10/2026, só como contexto no curso do 3.1 (errata T-08), fora dos objetos de avaliação; não gera item." |
| G1-c (O2) | GCE_Lote3_v2_CPP.md | (a) 3.1, bloco T-08 | "…comitê de ética de uso da IA. Como contexto" → "…comitê de ética de uso da IA. [NORMATIVO — QA]" + "Como contexto" (quebra de linha) |
| G1 (registro) | GCE_Lote3_v2_CPP.md | TABELA DE CORREÇÕES do cabeçalho | +3 linhas: "G1 → convenção de evidência, F4; limites, N7; bloco T-08…" |
| T-28 (registro) + G2 (O6) | GCE_Lote2_v2_CPP.md | TABELA DE CORREÇÕES (+4 linhas) e (a) 2.1, linha 152 do entregue | linha única de 122 caracteres → 2 linhas ("…NORMATIVO — QA]. A prática" / "oficial inclui a revisão e a redação final") |

Conferência por script após as erratas D1 (estado aprovado × atual):
- L3: 4 operações, todas acima; "[V " 2 → 2; NORMATIVO — QA 35 → 36 (só o G1-c; as menções no cabeçalho foram escritas sem a marca para não alterar contagem); [TS] 19, VOLÁTIL 4, REVERIFICAR 4, QA PENDENTE 0, SEM FONTE 0 inalterados; de "(c) PARES" ao fim idêntico ao HEAD (sha256 bf7bd79300b3a3f0…). Linhas: HEAD 985 → aprovado 1008 → atual 1023.
- L2: 2 operações, ambas acima; "[V " 18, NORMATIVO — QA 7, [TS] 20, VOLÁTIL 4 inalterados; curso (a) com espaços normalizados idêntico ao aprovado; de "(c) PARES" ao fim idêntico ao HEAD (sha256 b5c0592426ec99fe…). Linhas: HEAD 967 → aprovado 966 → atual 971. "Derep (antigo DETAQ)": 1 no curso + 1 na Tabela de Correções.

## 5. Tarefa nova (append único em TAREFAS.md)
- Reverificação do Ato da Mesa nº 225/2025 (F4 do Lote 3) na janela de 4–8/1/2027, junto da T-11 — PRÓXIMO (datado); gce-cqfp → gce-gerencia.

## 6. Gatilho (append único em PARA_PRESIDENCIA.md)
- GATILHO E | GCE: os arquivos GCE_Lote2_v2_CPP.md e GCE_Lote3_v2_CPP.md do Projeto no claude.ai seguem sem as erratas; a sincronização é transporte do Fundador (a fábrica não escreve no Projeto), no mesmo molde dos gatilhos E da GCB (T-32, T-17). Pergunta fechada: encaminhar ao Fundador o transporte, SIM/NÃO.

FIM — gce-gerencia, 10/10/2026.
