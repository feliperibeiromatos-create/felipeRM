# T108_conferencia_clone_v1_11_2026-10-18.md — T-108/T-109 (achado 1 da fidelidade) — 2026-10-18 — gerado por orquestrador

Conferência da seção 2.3 de saida/pacote/T108_reconciliacao_v1_11_2026-10-18.md, sobre o commit d52f239 (main), depois da correção .gitattributes.

- Clone a: git clone --no-local (autocrlf do sistema); clone b: git clone --no-local -c core.autocrlf=false.
- sh saida/pacote/gerador_v1_11/rodar_tudo.sh: código 0 nos dois.
- Resumo das conferências nos dois: conferencias_v1_11: 24 OK, 0 PENDENTE, 0 FALHA (modo FINAL)
- out/: 66 de 68 arquivos com SHA-256 igual ao out/ da árvore de trabalho nos dois clones (inclui pacote.json 1b5657c7…, pacote_estudante.json 8533b0c0…, 35 .md, registros); diferem só conferencias_stdout.txt e conferencias_v1_11.json, as duas diferenças admitidas pela seção 2.3 (C-G2 imprime o git status de regras/).

Resultado: CONFERE — condição do gatilho A da GBQ cumprida.
