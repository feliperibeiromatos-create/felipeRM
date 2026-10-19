# T108_reconciliacao_v1_11_2026-10-18.md — T-108 e T-109 — reconciliação do pacote v1.11 após a fidelidade — 2026-10-18 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (D1; rito 3 da seção 4 de `saida/pacote/T108_D1_pacote_M2_2026-10-18.md`).
DESTINATÁRIO: orquestrador (comandos git das seções 2 e 6; commit é dele), gbq-csc (v1.12), presidencia (gatilho A em PARA_PRESIDENCIA.md).
Base: fidelidade `saida/pacote/fidelidade_v1_11_gbq-cqe.md` (gbq-cqe, opus, rodada 1: ACEITO COM RESSALVAS); nota FINAL `saida/pacote/T108_FINAL_gerador_v1_11_2026-10-18.md`; MANIFESTO `saida/pacote/gerador_v1_11/MANIFESTO.md`. Não editei DECISOES.md, estados de TAREFAS.md, o gerador, `out/` nem as tabelas; sem commit. Gravei: este arquivo; a errata de forma da seção 3 (`regras/pacote_contrato.md`, uma frase; `saida/pacote/T108_D1_pacote_M2_2026-10-18.md`, seção 1.5, uma frase; registro em `saida/pacote/contrato_v1_2_8_2026-10-18.md`, seção 5); o gatilho A em PARA_PRESIDENCIA.md.

## 1. Decisão (D1)

O conteúdo da v1.11 está aceito pela fidelidade: reconstrução independente igual byte a byte (`pacote.json` `1b5657c7…9517`), reversão à v1.10 byte a byte, 560 itens com id, enunciado, gabarito, comando e itemEdital intactos (salvo L2-R16 → P2-3.1, D-T109-L2R16-ACEITE), 0 PROCESSO nos campos da ordem C, conferências 24 OK / 0 PENDENTE / 0 FALHA, mutação 25/25. Não há segunda rodada da gbq-cqe: nenhum achado muda dado nem texto entregue. A GBQ emite o gatilho A da v1.11 como canônica, **condicionado** à conferência da seção 2.3 (reprodutibilidade em clone limpo). Sem a conferência OK, nada é promovido.

| Achado | Disposição |
|---|---|
| 1 (reprodutibilidade) | Corrigir antes do commit: `.gitattributes` com `-text` e recommit byte a byte (seção 2). Condição do gatilho A. |
| 2 (arquivos de teste) | Resolvido pela mesma correção (o exemplo da D-T59-04 entra no `-text`); se ainda divergir, os 3 arquivos ficam fora do conjunto de SHA esperado (não são entregáveis). |
| 3 (ordem de reversão) | Errata de forma da GBQ agora (D1 1.5 e contrato, ponto 2); rótulo do C-5 na v1.12 (seção 3). |
| 4 e 5 (resíduos fora dos campos da ordem) | Leitura A: v1.11 conforme; nada entra agora; destino por resíduo na seção 4. |
| 6 (forma GCE-0128, GCE-0243) | Sem perda de sentido; vai à GCE para a v1.12 (mérito de conteúdo é dela). |
| 7 (`parecer_qa` da T109-0001 sem diretório) | Registrado: o arquivo é `saida/gce/QA_T109_R1_2026-10-18_gce-cqfp.md`; a linha é corrigida no registro da v1.12 (`registro_alteracoes_v111.py` → v1.12). Não muda o registro da v1.11, que é entregável com SHA fixado. |

## 2. Achado 1 — reprodutibilidade em clone limpo

### 2.1 Escolha

Opção (a) da fidelidade: `.gitattributes` com `-text` nos arquivos cujos bytes o gerador lê do disco e confere por SHA-256, e recommit desses arquivos com os bytes do disco. Fundamento: os SHA aceitos pela Presidência (D-T108-GCE-TABELA, D-T108-GCB-TABELA: "SHA-256 dos bytes em disco") são dos bytes em disco; com `-text` o blob passa a ser exatamente esses bytes e qualquer checkout (autocrlf true ou false) os devolve. A opção (b) (ler pelo blob) mudaria o gerador e os SHA fixados no `config_v111.py`, o MANIFESTO e a fidelidade, sem ganho. Lista fechada (6):

| Arquivo | Bytes em disco (= blob depois do recommit) | SHA-256 esperado | Estado no git hoje |
|---|---|---|---|
| `saida/gce/T108_substituicoes_GCE_v3.csv` | CRLF por registro, LF dentro de campo | `77ad3ac331ec120c6fb086c0b3f7c05cb77776c1e06b3dcaa6df2ab1d52fc599` | `i/lf w/mixed` |
| `saida/gcb/T108_substituicoes_GCB.csv` | idem | `10d9e5588753bc9ad273a529b56148b20e1f643bb4f312751a8fbd371b8751ef` | `i/lf w/mixed` |
| `saida/pacote/T108_ocorrencias.csv` | idem | `471aeec59ba26f17548ea2597298bec429aa8d9a78838fd646b7fa7936bde5c6` | `i/lf w/mixed` |
| `saida/pacote/T108_substituicoes_GBQ.csv` | só LF | `528eb620dc6c95e1e27390fe90774acb861e391a467ff969932cd12f97a323dd` | não rastreado (com autocrlf=true sairia CRLF no checkout) |
| `saida/gce/T109_reconciliacao_2026-10-18.md` | só LF | `bb95046b0783eecf24b64814b2a2294ad65ace1050f0258d92df401f31a3eb84` | `i/lf w/lf` (com autocrlf=true sai CRLF no checkout) |
| `saida/pacote/exemplo_erros_v1.json` | CRLF (achado 2) | `9676b0f3032aeb94fb6e3d30972547793550b10f793b7b2a3eefa51391f4f8a0` | `i/lf w/crlf` |

A BASE (`pacote.json` v1.10) continua lida do blob de `cacd606` e não entra na lista. Os entregáveis da seção 5 não têm `\r` (conferido: nenhum byte CR em `pacote.json`, `pacote_estudante.json`, nos 35 .md, no adendo 3 e no registro por id), então o blob deles é igual aos bytes com ou sem `-text`.

### 2.2 Comandos do orquestrador (Git Bash, antes do commit do ciclo)

```sh
cd /c/Users/Felipe/felipeRM_push
L="saida/gce/T108_substituicoes_GCE_v3.csv saida/gcb/T108_substituicoes_GCB.csv saida/pacote/T108_ocorrencias.csv saida/pacote/T108_substituicoes_GBQ.csv saida/gce/T109_reconciliacao_2026-10-18.md saida/pacote/exemplo_erros_v1.json"
{ echo '# Bytes fixados por SHA-256 no gerador_v1_11 (T-108/T-109; saida/pacote/T108_reconciliacao_v1_11_2026-10-18.md, seção 2): sem conversão de fim de linha'
  for f in $L; do echo "$f -text"; done; } > .gitattributes
git add .gitattributes
git add --renormalize -- saida/gce/T108_substituicoes_GCE_v3.csv saida/gcb/T108_substituicoes_GCB.csv saida/pacote/T108_ocorrencias.csv saida/gce/T109_reconciliacao_2026-10-18.md saida/pacote/exemplo_erros_v1.json
git add -- saida/pacote/T108_substituicoes_GBQ.csv
git ls-files --eol -- $L                       # esperado: attr/-text nas 6; i/ igual a w/ (mixed, mixed, mixed, lf, lf, crlf)
for f in $L; do echo "$(git cat-file -p ":$f" | sha256sum | cut -c1-64)  $f"; done   # esperado: os 6 SHA da tabela 2.1
```

Depois disso, o commit do ciclo (do orquestrador) leva `.gitattributes`, os 6 arquivos e o restante do ciclo. Se algum SHA da última linha diferir da tabela 2.1, pare: não commite e devolva à GBQ. A errata da seção 3 (`regras/pacote_contrato.md`) vai no mesmo commit.

### 2.3 Conferência que comprova (depois do commit; clones descartáveis)

```sh
T=$(mktemp -d)
git clone -q --no-local /c/Users/Felipe/felipeRM_push "$T/c1"                         # autocrlf do sistema (true)
git clone -q --no-local -c core.autocrlf=false /c/Users/Felipe/felipeRM_push "$T/c2"
for c in c1 c2; do sh "$T/$c/saida/pacote/gerador_v1_11/rodar_tudo.sh"; echo "$c: código $?"; done
E="pacote.json pacote_estudante.json registro_adendo3.md registro_alteracoes_v1_11.csv registro_alteracoes_v1_11_manter.csv registro_alteracoes_v1_11_resumo.md stats_v1_11.json folhas_v1_11.json estudante/*.md"
R=/c/Users/Felipe/felipeRM_push/saida/pacote/gerador_v1_11/out
for c in c1 c2; do O="$T/$c/saida/pacote/gerador_v1_11/out"
  (cd "$O" && sha256sum $E) | diff - <(cd "$R" && sha256sum $E) && echo "$c: 43/43 entregáveis iguais"
  tail -1 "$O/conferencias_stdout.txt"
  (cd "$O" && find . -type f | LC_ALL=C sort | xargs sha256sum) | diff - <(cd "$R" && find . -type f | LC_ALL=C sort | xargs sha256sum) | grep '^>' ; done
rm -rf "$T"
```

Critério (os dois clones): `rodar_tudo.sh` com código 0; última linha de `conferencias_stdout.txt` "24 OK, 0 PENDENTE, 0 FALHA (modo FINAL)"; e os 43 arquivos de `$E` (os 41 entregáveis da seção 5 (6 arquivos e 35 .md) mais `stats_v1_11.json` e `folhas_v1_11.json`) com o mesmo SHA-256 de `out/` (seção 5). Diferenças admitidas na última listagem, e só estas: `conferencias_stdout.txt` e `conferencias_v1_11.json`, porque a C-G2 imprime o `git status` de `regras/` (hoje "M regras/pacote_contrato.md"; no clone do commit, vazio) — não é entregável e passa em FINAL; e, se o `-text` do exemplo não bastar, os 3 arquivos do achado 2. Qualquer outra diferença reprova. Se c1 falhar e c2 passar, falta arquivo na lista do `-text`: a GBQ o acrescenta por esta mesma regra, sem mudar o gerador. O resultado (dois códigos, duas linhas "43/43" e a lista das diferenças) vai à Presidência antes da decisão do gatilho A.

## 3. Achado 3 — ordem de reversão (errata de forma da GBQ)

Os dados estão certos: `limpeza_v111.reverte` aplica `reversed(o['interno'])`, e o C-5 compara byte a byte com a v1.10. O erro é só de redação: "ordem decrescente de `pos`" não fecha nos dois empates (4C-09, GCB-A0176/A0177, pos 726; 5C-08, GCB-C0074/C0075, pos 437).

| Onde | Antes | Depois | Quando |
|---|---|---|---|
| `saida/pacote/T108_D1_pacote_M2_2026-10-18.md`, seção 1.5, "Reversibilidade" | "em ordem decrescente de `pos`" | "na ordem inversa da lista (o último primeiro; empates de `pos` pela ordem inversa da lista; errata de forma de 18/10/2026, …)" | agora (gravado) |
| `regras/pacote_contrato.md`, v1.2.8, ponto 2 | "aplicando o `interno` ao contrário." | "aplicando os registros do `interno` na ordem inversa da lista (o último primeiro, inclusive quando dois registros do mesmo campo têm o mesmo `pos`), cada um trocando `texto[pos:pos+len(depois)]` por `antes`." | agora (gravado; registro em `saida/pacote/contrato_v1_2_8_2026-10-18.md`, seção 5) |
| `conferencias_v111.py`, rótulo do C-5 | "aplicado em ordem decrescente de pos" | "aplicado na ordem inversa da lista" | v1.12 (no gerador_v1_12). Não agora: mudaria `out/conferencias_*` e o MANIFESTO da v1.11 já conferidos, sem efeito em dado. |

Contrato: errata de forma da D1 da GBQ (D-V15-C-M2), dentro da v1.2.8; não muda campo, tipo, obrigatoriedade, `versao` nem `versaoFormato`. SHA-256 LF `5e3d1fde…15a0` → `5e894c668638032c4081b172a1cc1b509889d026d47c48b835dff1f0e2dfb36f` (48 339 bytes LF, 211 linhas); em disco CRLF `4ee173af…40c2`. A regra do C-14 refeita sobre o arquivo novo dá os mesmos opcodes (`replace 0–1`, `replace 2–3`, `insert 195–206`; verdadeiro), então a saída do C-14 no clone é a mesma.

## 4. Achados 4 e 5 — arbitragem (ordem C: o que a candidata lê)

Fundamento: a ordem C, alínea (a), define o objeto como o texto que a candidata lê **em curso, resumo, pegadinhas e justificativas**; a alínea (c) dá as categorias desse texto; a regra 5 protege enunciado, gabarito e itemEdital (e a D1 tratou comando e textoBase como invariantes, C-4). Por isso a **leitura A** vale para a v1.11: os campos abaixo estão fora do objeto, a v1.11 está conforme, e nenhum entra agora. Entrar agora exigiria tabela nova (da GBQ ou das Gerências), nova rodada FINAL e nova fidelidade, para campos que a ordem não listou. Como a candidata vê esses campos na tela, cada resíduo fica registrado com destino:

| Resíduo | Onde a candidata vê | Decisão | Destino |
|---|---|---|---|
| `lotes[].nome` "Lote N — RF-…/TID-…/TI-… (…)" (7 no -E, 10 no `pacote.json`, e cabeçalhos dos .md) | título do lote | fica na v1.11 | v1.12: linha da tabela da GBQ (metadado do pacote, domínio GBQ) trocando o código de produção pelo nome do tópico do edital; com a ORDEM A (`topicos`), o lote deixa de ser a unidade exibida, e o nome passa a seguir o tópico. QA da gbq-cqe. |
| `simulados[SIM-0].nome` "(v0.2)" (C09) | nome do simulado | fica na v1.11 | v1.12: linha da tabela da GBQ (simulado é domínio GBQ), sem mudar composição nem id. |
| `legendaMecanismo` (6 lotes no `pacote.json`, 4 no -E, gabaritos .md) | legenda nos gabaritos | fica na v1.11 | v1.12: o campo sai dos lotes (opcional desde a v1.2.1), porque nenhuma justificativa usa mais TC/IC/GI/AT (C06 = 0); sem errata de contrato. |
| `comandoOriginal` "julgue os itens de 4C-01 a 4C-10" e equivalentes (140) | comando do bloco | fica | Não vai à v1.12 pela T-108: é comando (regra 5; C-4). Se o Fundador quiser o comando sem ids, é matéria nova, por gatilho, fora da ordem C. |
| "NÃO VERIFICADO/A" em `lotes[L2].resumo` (2) e ~10 "não verificado(s)/a" nos cursos L1–L5 (achado 5) | resumo e curso | fica (leitura A: aviso de conteúdo à candidata — o dado não foi confirmado e não deve ser cobrado como certo; não está em nenhuma das 10 categorias, e REVERIFICAR, que é instrução ao produtor, já está em 0) | ORDEM A (resumos por tópico, "sem referências de produção"): a GCE e a GCB redigem o aviso em frase de leitora, sem caixa alta, com QA. A reescrita é de mérito delas; a GBQ não a redige. |

## 5. Promoção depois do aceite (byte a byte; ato separado, depois da decisão da Presidência e da conferência 2.3)

| Origem (`saida/pacote/gerador_v1_11/`) | Destino canônico | SHA-256 | Bytes |
|---|---|---|---|
| `out/pacote.json` | `saida/pacote/pacote.json` | `1b5657c726b5852885fe0e69e7835d6ec331e6d43dd19191cf451ff4ac069517` | 1 123 649 |
| `out/pacote_estudante.json` | `saida/pacote/pacote_estudante.json` | `8533b0c085594a42dd066b3e7a6161f0ea94f4f60bb2ad2cfbafc969369f6bd7` | 880 435 |
| `out/registro_adendo3.md` | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo3_2026-10-18.md` | `b9f8e2837ef28ad9632464557dcb85990086fe579c5652cf426a6eafd72f611e` | 3 817 |
| `out/registro_alteracoes_v1_11.csv` | `saida/pacote/registro_alteracoes_v1_11.csv` | `faf9007df6760c1f6223efe0966fa10f2697241aec42e00425f744d9441f36fb` | 464 765 |
| `out/registro_alteracoes_v1_11_manter.csv` | `saida/pacote/registro_alteracoes_v1_11_manter.csv` | `d210cb87546cbf0341cb646ab6a42f420b18ce2ba981401a78464f7eb7ba0805` | 563 |
| `out/registro_alteracoes_v1_11_resumo.md` | `saida/pacote/registro_alteracoes_v1_11_resumo.md` | `9ea415b85553a03fbe037181c5e8de7d579ec3a51bacca7d235c4293b2d8b67e` | 5 712 |
| `out/estudante/` (35 arquivos, mesmos nomes de `saida/estudante/`) | `saida/estudante/` (substitui os 35) | por arquivo, abaixo; `sha256sum *` dos 35, em ordem de nome, tem SHA-256 `2d179f8770dba2e6f918b6ebe607ae4a082d205ef1a8fad146107434f6fca6ba` | — |

SHA-256 dos 35 .md: BANCO_gabarito `f7d9bb47…`, BANCO_itens `879e1769…`, DISCURSIVAS `7777c52c…`, DISCURSIVAS_padrao `4d5a4e6e…`, L1_estudo `a43a55df…`, L1_gabarito `57cc505f…`, L1_itens `f1efb027…`, L2_estudo `5e09d1e5…`, L2_gabarito `2438f956…`, L2_itens `9e0e3b11…`, L3_estudo `f2132f27…`, L3_gabarito `7e410a86…`, L3_itens `0364d5f6…`, L4_estudo `160b63ae…`, L4_gabarito `2b7493a1…`, L4_itens `6bac0124…`, L5_estudo `9804c6f7…`, L5_gabarito `cd36b245…`, L5_itens `a51ca726…`, L6A_estudo `3a7515c5…`, L6A_gabarito `fd4b9095…`, L6A_itens `56d6fad5…`, L6B_estudo `653d6836…`, L6B_gabarito `eb5a045a…`, L6B_itens `e8e4baf9…`, NUCLEO `a61f095d…`, README `bdb05cbe…`, SIM-0-P2_folha `f69efe60…`, SIM-0-P2_gabarito `cdd8a658…`, SIM-0_folha `50d509be…`, SIM-0_gabarito `780a8f30…`, SIM-1_folha `e0e21ea3…`, SIM-1_gabarito `535287fa…`, SIM-2_folha `d576cc3f…`, SIM-2_gabarito `2113d4a7…` (valores completos no MANIFESTO e em `sha256sum out/estudante/*`).

Não são promovidos (ficam em `out/` como registro e contraprova): `stats_v1_11.json` (`9fe957e4…`), `folhas_v1_11.json` (`8791434d…`; insumo da cobertura `saida/pacote/cobertura_v1_11.md`, que é da secretaria, T-95), conferências, validação, inventário, mutação, `casos_erros/` e os stdout.

Comandos da promoção (orquestrador, depois do sim da Presidência e da conferência 2.3 OK):

```sh
cd /c/Users/Felipe/felipeRM_push; G=saida/pacote/gerador_v1_11/out
cp "$G/pacote.json" "$G/pacote_estudante.json" saida/pacote/
cp "$G/registro_alteracoes_v1_11.csv" "$G/registro_alteracoes_v1_11_manter.csv" "$G/registro_alteracoes_v1_11_resumo.md" saida/pacote/
cp "$G/registro_adendo3.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo3_2026-10-18.md
cp "$G"/estudante/*.md saida/estudante/
cmp "$G/pacote.json" saida/pacote/pacote.json && cmp "$G/pacote_estudante.json" saida/pacote/pacote_estudante.json && cmp "$G/registro_adendo3.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo3_2026-10-18.md && for f in "$G"/estudante/*.md; do cmp "$f" "saida/estudante/$(basename "$f")" || exit 1; done && echo promocao-ok
git add saida/pacote/pacote.json saida/pacote/pacote_estudante.json saida/pacote/registro_alteracoes_v1_11*.* saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo3_2026-10-18.md saida/estudante/
git cat-file -p :saida/pacote/pacote.json | sha256sum; git cat-file -p :saida/pacote/pacote_estudante.json | sha256sum   # esperado 1b5657c7… e 8533b0c0…
```

Promover não é publicar: nada vai à plataforma da candidata (https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC) nem à prévia sem o sim do Fundador (D-V15-PLATAFORMA); a publicação segue nos itens RESERVADA abertos (D-PLATAFORMA-V110-FUNDADOR, D-V19-PUBLICACAO-REGISTRO). A skill do painel roda quando o pacote for carregado.

## 6. Gatilho

GATILHO A da GBQ, em PARA_PRESIDENCIA.md (ciclo 2026-10-18 s14c2): aceite da v1.11 como canônica, condicionado à conferência 2.3, com a errata de forma da seção 3 registrada.
