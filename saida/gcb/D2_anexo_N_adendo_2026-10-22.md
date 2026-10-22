# D2_anexo_N_adendo_2026-10-22.md — T-116 — 2026-10-22 — gerado por qa-normativo-da

# ADENDO AO ANEXO N DO LOTE D2 — folha P1-DA-4.1 (Fontes e princípios) — CF, art. 5º, caput, LIV e LV — reforço DA, leva 5 (ciclo s16c3)

Base do pedido: ficha saida/gcb/DA_reforco_ficha_2026-10-20.md (SHA-256 52f80184a6eb1ff3c9340c3b32ce15221b64b32b4cdfebf670fd54096ef9c64a), seções 11.4.2 (b) e 11.4.10, item 1; DECISOES.md, D-T116-LEVA4-ACEITE (condições da fila (a) a (d)); D-FONTE-DATA-ANTERIOR; D-COMPLEMENTOS. Acréscimo ao Anexo N do D2 (saida/gcb/D2_anexo_N_mapa_normativo.md, SHA-256 b0a54fff4ddcf21a693e01ba71032efccf72e0a6fdf912221ff05413cc0e340a), que não foi alterado. Escopo fechado: CF, art. 5º, caput, LIV e LV; nada além.

## 1. Fonte, rede, método e data

| Fonte | Norma | URL (Fonte 1 do Anexo N do D2) | Bytes | SHA-256 do HTML | Cópia em cache | SHA-256 da cópia |
|---|---|---|---|---|---|---|
| 1 (cópia de 20/10) | CF/1988, texto compilado | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 1.507.134 | 65255e489e95188558c1c2c152ad2fddbd51367e19888d22c25100cb206d5ae6 (linha 1 da cópia) | saida/gcb/normativo_cache/CF_1988_compilada_2026-10-20.txt | d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d |
| 1 (reabertura de 22/10) | CF/1988, texto compilado | https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm | 1.507.134 | 40142a118722682d0ea2bb88d8ec0dac10ea8bc82fa47e6b33e0b072420394d6 | — (HTML guardado só no scratchpad da sessão; não gravado em saida/) | — |

- Cópia: saida/gcb/normativo_cache/CF_1988_compilada_2026-10-20.txt, SHA-256 conferido em 22/10/2026 = d6580cb327147e1beb69ccd09cd930613c06f39e1791b235729930a01cacb51d (igual ao do despacho, d6580cb3…cb51d). Linha 1 da cópia: URL acima, "verificado em 20/10/2026", "obtido por curl (HTTP 200), texto extraído por script (html.parser, cp1252)", SHA-256 do HTML 65255e489e95188558c1c2c152ad2fddbd51367e19888d22c25100cb206d5ae6, 1507134 bytes. Data verdadeira da cópia: verificado em 20/10/2026 (D-FONTE-DATA-ANTERIOR).
- SHA-256 do HTML no Anexo N do D2 (seção 1, Fonte 1): ae04e89b164b421f9cccacb62e4bfe5b8eb5c9b5bcca1717371ff3a863588ba4, 1.507.134 bytes. Difere do SHA-256 do HTML registrado na cópia (65255e48…d5ae6) e do HTML de 22/10 (40142a11…94d6), com o mesmo tamanho nos três downloads. O adendo do D3 (saida/gcb/D3_anexo_N_adendo_2026-10-20.md, seção 1) registra que o SHA-256 difere a cada download por causa do script de medição que o Planalto troca; aqui não foi feita comparação byte a byte entre os downloads (o HTML do Anexo não está gravado no repositório). Os três textos transcritos são iguais, caractere a caractere, na cópia de 20/10 e na página de 22/10 (seção 3).
- Rede (tentativa única de reabrir a página, conforme o despacho): `curl -sS -m 30 -A "Mozilla/5.0" https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm` em 2026-10-22T21:05:35Z. Resultado literal: `HTTP 200 bytes 1507134`, código de saída 0. A página ABRIU: o bloqueio de rede previsto no despacho não se verificou nesta tentativa. Conteúdo íntegro (título "Constituicao-Compilado"; cp1252; 0 U+FFFD). Pela D-T116-LEVA4-ACEITE, condição (b) ("havendo rede no ciclo, a reabertura tem preferência"), a página reaberta foi usada como conferência da cópia; a cópia de 20/10 segue como a base indicada pelo despacho. Os dois registros de data são verdadeiros: cópia verificada em 20/10/2026; página reaberta e conferida em 22/10/2026.
- URL: não construída de memória; é a da Fonte 1 do Anexo N do D2 (localizada por WebSearch restrita a planalto.gov.br na T-75, seção 1 do Anexo), igual à da linha 1 da cópia. Nenhuma busca nova foi feita.
- Extração (método 1): script python3 -I, html.parser da biblioteca padrão sobre o HTML de 22/10 (cp1252), um registro por parágrafo `<p>`, texto em `<strike>`, `<s>`, `<del>` ou `text-decoration:line-through` separado como tachado, `<sup>o</sup>` → "º". Cada um dos três dispositivos ocorre em 1 parágrafo, sem trecho tachado, na ordem caput → LIV → LV, antes do "Art. 6º". Os textos da seção 2 foram gerados pelo script a partir do texto extraído; nenhum texto de lei foi digitado à mão.
- Conferência (método 2, independente do parser): (i) busca da cadeia exata de cada texto na cópia de 20/10 — 1 ocorrência em todo o arquivo e igualdade com a linha inteira (l. 52, 124 e 125); (ii) expressões regulares sobre o HTML bruto de 22/10 (blocos tachados removidos, tags apagadas, entidades decodificadas, espaços normalizados) — 1 ocorrência de cada texto.
- Notas de redação do compilado: nenhuma. Os três parágrafos não têm "(Redação dada …)", "(Incluído …)", "(Vide …)" nem "(Revogado …)", na cópia e na página; não há trecho tachado. Registro como "redação original", na convenção da seção 4 do Anexo (ausência de nota no compilado). Vigência: promulgação (5.10.1988), na convenção do Anexo; a página traz "Brasília, 5 de outubro de 1988." no fecho. Nenhuma alteração posterior a 2/10/2026 anotada nesses dispositivos. REVERIFICAR: nenhum (sem redação de 2025 ou 2026).
- O SHA-256 deste arquivo não pode constar dele; vai no relato da entrega.

## 2. Texto transcrito (CF/1988, Fonte 1)

| Dispositivo | Texto (transcrição do compilado) | Redação dada por / incluído por | Vigência | Consulta | Observação |
|---|---|---|---|---|---|
| art. 5º (caput) | Art. 5º Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade, nos termos seguintes: | redação original | promulgação (5.10.1988) | 2026-10-20 (cópia, l. 52); 2026-10-22 (página reaberta) | Edital: núcleo 4.1 (contexto dos incisos LIV e LV). O mesmo texto já consta, sem marca, no Anexo N do D2, seção 4.2. |
| art. 5º, inc. LIV | LIV - ninguém será privado da liberdade ou de seus bens sem o devido processo legal; | redação original | promulgação (5.10.1988) | 2026-10-20 (cópia, l. 124); 2026-10-22 (página reaberta) | Edital: núcleo 4.1 (devido processo legal). |
| art. 5º, inc. LV | LV - aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e ampla defesa, com os meios e recursos a ela inerentes; | redação original | promulgação (5.10.1988) | 2026-10-20 (cópia, l. 125); 2026-10-22 (página reaberta) | Edital: núcleo 4.1 (contraditório e ampla defesa, "em processo judicial ou administrativo"). |

Efeito no Anexo N do D2 (registro, sem alterar o Anexo): a nota da 4.1 na seção 3 e o "[SEM FONTE — não afirmar]" da seção 5.1 para a CF, art. 5º, LIV e LV, ficam supridos por este adendo, só para esses dois incisos e o caput. O mapa da seção 3 passa a ler, para a 4.1, núcleo acrescido de "CF, art. 5º, caput, LIV e LV (adendo de 22/10/2026)". A seleção do que entra no curso é da GCB.

## 3. Conferência

| Dispositivo | Linha da cópia | Cadeia exata na cópia (ocorrências) | Igual à linha inteira da cópia | Método 1 (parser, página 22/10) | Método 2 (regex, HTML bruto 22/10) | Caracteres |
|---|---|---|---|---|---|---|
| art. 5º (caput) | 52 | 1 | sim | 1 parágrafo, sem tachado | 1 | 257 |
| art. 5º, inc. LIV | 124 | 1 | sim | 1 parágrafo, sem tachado | 1 | 84 |
| art. 5º, inc. LV | 125 | 1 | sim | 1 parágrafo, sem tachado | 1 | 173 |

Resultado: 3 de 3 conferem literalmente nos dois métodos e nas duas datas.

## 4. Leis alteradoras

CF, art. 5º, caput, LIV e LV: nenhuma (sem nota de alteração no compilado em 20/10/2026 e em 22/10/2026).

## 5. NÃO CONFERIDO e alertas

- NÃO CONFERIDO: nenhum dispositivo do escopo.
- Alerta 1 (rede): o despacho previa planalto bloqueado; a tentativa única de 22/10/2026 retornou HTTP 200. O registro "planalto não reaberto: rede bloqueada" NÃO se aplica a este adendo. A condição (d) da D-T116-LEVA4-ACEITE (reabertura dos três dispositivos na T-120, parte DA) fica, de fato, já atendida por esta conferência; a decisão é da GCB/orquestrador.
- Alerta 2 (SHA-256 do HTML): três valores diferentes para a mesma URL e o mesmo tamanho (Anexo ae04e89b…8ba4; cópia 65255e48…d5ae6; 22/10 40142a11…94d6); explicação registrada no adendo do D3 (script de medição variável), não reconferida aqui.
- Fora do escopo e não transcrito (D-COMPLEMENTOS): qualquer outro inciso do art. 5º e qualquer outro dispositivo.

FIM DO ADENDO
