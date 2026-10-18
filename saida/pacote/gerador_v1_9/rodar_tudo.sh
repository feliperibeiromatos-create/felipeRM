#!/bin/sh
# T-81 — roda o pipeline completo do gerador v1.8, na ordem do MANIFESTO.md, a partir de qualquer pasta.
# Apaga e recria out/; no repositório, só grava em out/ e, no passo 11, o MANIFESTO.md desta pasta. Cada out/*_stdout.txt é a saída-padrão do script homônimo, redirecionada aqui;
# gen_stdout.txt junta as saídas de build_pacote.py (>) e estudante_gen.py (>>). Para na primeira falha (set -e); validate.py e conferencias_v18.py saem com código 1 se houver falha (T-69 (4)).
# Passo 11 (D1-T67-R1): manifesto_v1_8.py reescreve MANIFESTO.md (fora de out/); sua saída vai ao stderr, para não criar arquivo em out/ que ele próprio listaria.
# Uso: sh rodar_tudo.sh            (PYTHONHASHSEED pode ser definido por quem chama; o resultado não depende dele)
set -e
D="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$D/out"
mkdir -p "$D/out"
cd "$D"
python3 -B build_pacote.py > out/gen_stdout.txt
python3 -B estudante_gen.py >> out/gen_stdout.txt
python3 -B estudante_json.py > out/estudante_json_stdout.txt
python3 -B estudante_fidelidade.py > out/fidelidade_stdout.txt
python3 -B sync_check.py > out/sync_stdout.txt
python3 -B validate.py > out/validate_stdout.txt
python3 -B conferencias_v18.py > out/conferencias_stdout.txt
python3 -B fidelidade_mutacao.py > out/mutacao_stdout.txt
python3 -B validar_erros_teste.py > out/validar_erros_stdout.txt
python3 -B relatorio_v1_8.py > out/relatorio_stdout.txt
python3 -B manifesto_v1_8.py >&2
echo "pipeline completo: out/ regerado em $D/out" >&2
