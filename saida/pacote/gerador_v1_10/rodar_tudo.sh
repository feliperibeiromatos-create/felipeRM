#!/bin/sh
# T-94 — roda o pipeline do gerador v1.9 (pacote.json v1.9 e pacote_estudante.json v1.9-E), na ordem do MANIFESTO.md, a partir de qualquer pasta.
# Todo script roda com python3 -I -B por meio de _run.py (o modo isolado não põe a pasta do script no sys.path; _run.py põe só a pasta do gerador).
# Apaga e recria out/; no repositório, só grava em out/ e, no passo 7, o MANIFESTO.md desta pasta. Para na primeira falha (set -e); os passos 2, 4, 5 e 6 saem com código 1 se houver falha.
# Os scripts herdados da v1_8 que regeneram o pacote e a edição a partir das fontes de hoje (build_pacote.py, estudante_gen.py, estudante_fidelidade.py, sync_check.py, validate.py,
# conferencias_v18.py, fidelidade_mutacao.py, relatorio_v1_8.py, manifesto_v1_8.py) ficam na pasta como registro e NÃO são executados na v1.9 (D1 da GBQ, T94_D1_v1_9_2026-10-18.md, seção 1.3).
set -e
D="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$D/out"
mkdir -p "$D/out"
cd "$D"
python3 -I -B _run.py build_v19.py > out/gen_stdout.txt
python3 -I -B _run.py estudante_json.py > out/estudante_json_stdout.txt
python3 -I -B _run.py registro_adendo_v19.py > out/registro_stdout.txt
python3 -I -B _run.py validate_v19.py > out/validate_stdout.txt
python3 -I -B _run.py conferencias_v19.py > out/conferencias_stdout.txt
python3 -I -B _run.py validar_erros_teste.py > out/validar_erros_stdout.txt
python3 -I -B _run.py manifesto_v1_9.py >&2
echo "pipeline completo: out/ regerado em $D/out" >&2
