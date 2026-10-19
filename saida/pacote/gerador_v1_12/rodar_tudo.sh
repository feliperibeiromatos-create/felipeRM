#!/bin/sh
# T-115 — roda o pipeline do gerador v1.12 (pacote.json com os 189 itens novos, as pegadinhas de pares e os `topicos`; pacote_estudante.json; adendo 4 do registro; edição .md; registro de alterações por id;
# conferências e testes de mutação), na ordem do MANIFESTO.md, a partir de qualquer pasta (D1 da GBQ, seção 3.2).
# Todo script roda com python -I -B por meio de _run.py (o modo isolado não põe a pasta do script no sys.path; _run.py põe só a pasta do gerador).
# Apaga e recria out/; só grava em out/ e, no passo 10, no MANIFESTO.md desta pasta. Nada vai a saida/ fora desta pasta: a promoção é ato separado, depois do aceite da fidelidade (gbq-cqe) e do gatilho A da GBQ.
# Para na primeira falha (set -e). O modo (ENSAIO ou FINAL) vem de config_v112.py. Os scripts herdados que regeneram o pacote a partir de outras fontes ficam na pasta como registro e NÃO são executados.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
if python3 -c "" >/dev/null 2>&1; then PY=python3; else PY=python; fi
rm -rf "$D/out"
mkdir -p "$D/out"
cd "$D"
"$PY" -I -B _run.py build_v112.py > out/gen_stdout.txt
"$PY" -I -B _run.py estudante_json_v112.py > out/estudante_json_stdout.txt
"$PY" -I -B _run.py registro_adendo_v112.py > out/registro_stdout.txt
"$PY" -I -B _run.py estudante_md_v112.py > out/estudante_md_stdout.txt
"$PY" -I -B _run.py registro_alteracoes_v112.py > out/registro_alteracoes_stdout.txt
"$PY" -I -B _run.py validate_v112.py > out/validate_stdout.txt
"$PY" -I -B _run.py conferencias_v112.py > out/conferencias_stdout.txt
"$PY" -I -B _run.py inventario_v112.py out/pacote.json out/pacote_estudante.json out/estudante out/inventario.csv out/inventario.json > out/inventario_stdout.txt
"$PY" -I -B _run.py fidelidade_mutacao_v112.py > out/fidelidade_mutacao_stdout.txt
"$PY" -I -B _run.py manifesto_v1_12.py >&2
echo "pipeline completo: out/ regerado em $D/out (modo em config_v112.py; promoção é ato separado da geração final)" >&2
