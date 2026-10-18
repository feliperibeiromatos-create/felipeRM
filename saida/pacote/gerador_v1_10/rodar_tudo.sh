#!/bin/sh
# T-104 — roda o pipeline do gerador v1.10 (pacote.json v1.10, pacote_estudante.json v1.10-E, registro adendo 2 e edição .md), na ordem do MANIFESTO.md, a partir de qualquer pasta.
# Todo script roda com python3 -I -B por meio de _run.py (o modo isolado não põe a pasta do script no sys.path; _run.py põe só a pasta do gerador).
# Apaga e recria out/; no repositório, só grava em out/ e, no passo 8, o MANIFESTO.md desta pasta. ENSAIO: nada é promovido (D-ONDA4-FILA (3)); a promoção é ato da geração final.
# Para na primeira falha (set -e). Chaves da ocorrência em config_v110.py (E_CURSO só com o gatilho A da T-106 aceito; T104_E_CURSO=1 repete o ensaio com a troca).
# Os scripts herdados que regeneram o pacote a partir das fontes (build_pacote.py, validate.py, conferencias_v18.py, build_v19.py, validate_v19.py, conferencias_v19.py etc.)
# ficam na pasta como registro e NÃO são executados na v1.10 (D1 da GBQ, T104_D1_v1_10_2026-10-18.md, seção 6).
set -e
D="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$D/out"
mkdir -p "$D/out"
cd "$D"
python3 -I -B _run.py build_v110.py > out/gen_stdout.txt
python3 -I -B _run.py estudante_json.py > out/estudante_json_stdout.txt
python3 -I -B _run.py registro_adendo_v110.py > out/registro_stdout.txt
python3 -I -B _run.py estudante_md_v110.py > out/estudante_md_stdout.txt
python3 -I -B _run.py validate_v110.py > out/validate_stdout.txt
python3 -I -B _run.py conferencias_v110.py > out/conferencias_stdout.txt
python3 -I -B _run.py validar_erros_teste.py > out/validar_erros_stdout.txt
python3 -I -B _run.py manifesto_v1_10.py >&2
echo "pipeline completo: out/ regerado em $D/out (modo em config_v110.py; promoção é ato separado da geração final)" >&2
