#!/bin/sh
# T-108 e T-109 — roda o pipeline do gerador v1.11 (pacote.json com a limpeza das tabelas e o campo `interno`, pacote_estudante.json, adendo 3 do registro, edição .md, registro de
# alterações por id, conferências e testes de mutação), na ordem do MANIFESTO.md, a partir de qualquer pasta.
# Todo script roda com python -I -B por meio de _run.py (o modo isolado não põe a pasta do script no sys.path; _run.py põe só a pasta do gerador).
# Apaga e recria out/; só grava em out/, em ensaio/ (passo 0, só ENSAIO) e, no passo 10, no MANIFESTO.md desta pasta. Nada vai a saida/ fora desta pasta: a promoção é ato separado, depois
# do gatilho A da GBQ. Para na primeira falha (set -e). Chaves da ocorrência em config_v111.py (FINAL só com as condições de entrada E1 a E5 cumpridas).
# Os scripts herdados da v1.10 que regeneram o pacote a partir das fontes ficam na pasta como registro e NÃO são executados.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
if python3 -c "" >/dev/null 2>&1; then PY=python3; else PY=python; fi
rm -rf "$D/out"
mkdir -p "$D/out"
cd "$D"
if grep -q "^FINAL = False" config_v111.py; then
  "$PY" -I -B _run.py ensaio/gera_tabelas_ensaio.py > out/ensaio_stdout.txt
fi
"$PY" -I -B _run.py build_v111.py > out/gen_stdout.txt
"$PY" -I -B _run.py estudante_json_v111.py > out/estudante_json_stdout.txt
"$PY" -I -B _run.py registro_adendo_v111.py > out/registro_stdout.txt
"$PY" -I -B _run.py estudante_md_v111.py > out/estudante_md_stdout.txt
"$PY" -I -B _run.py registro_alteracoes_v111.py > out/registro_alteracoes_stdout.txt
"$PY" -I -B _run.py validate_v111.py > out/validate_stdout.txt
"$PY" -I -B _run.py conferencias_v111.py > out/conferencias_stdout.txt
"$PY" -I -B _run.py inventario_v111.py out/pacote.json out/pacote_estudante.json out/estudante out/inventario.csv out/inventario.json > out/inventario_stdout.txt
"$PY" -I -B _run.py fidelidade_mutacao_v111.py > out/fidelidade_mutacao_stdout.txt
"$PY" -I -B _run.py manifesto_v1_11.py >&2
echo "pipeline completo: out/ regerado em $D/out (modo em config_v111.py; promoção é ato separado da geração final)" >&2
