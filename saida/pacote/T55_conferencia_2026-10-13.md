# T55_conferencia_2026-10-13.md — T-55 — 2026-10-13 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia
DESTINATÁRIO: Presidência, com cópia à Secretaria de Estado Canônico. Cópia: gbq-csc (pontos para a próxima T-12, seção 4).

Objeto: `saida/pacote/gerador_v1_2/` (42 arquivos + `MANIFESTO.md`), copiado pela gbq-csc de `/tmp/claude-0/-home-claude/3cf5e5a2-0a00-52ee-a3d1-ce0f04412748/scratchpad/s4/t48r1/` (scratchpad efêmero desta sessão).

Método: script próprio da gerência (fora do repositório, `scratchpad/t55conf/conf.py`), independente do script da gbq-csc. Execução de teste numa cópia temporária fora do repositório (`scratchpad/t55conf/run/`), com `PYTHONDONTWRITEBYTECODE=1` e SHA-256 de todos os arquivos do repositório (exceto `.git/`) antes e depois: repositório inalterado pelos testes. Git consultado só para leitura (`git log`, `git show`, `git archive`); nenhum commit.

## 1. SHA-256: destino = origem = manifesto

| Verificação | Resultado |
|---|---|
| Arquivos no destino (sem o manifesto) | 42 |
| Linhas da tabela do manifesto | 42 |
| SHA-256 destino = SHA-256 origem, arquivo a arquivo | 42/42 |
| SHA-256 e bytes do manifesto = destino | 42/42 |
| Arquivo do manifesto ausente no destino, ou do destino ausente no manifesto | 0 |
| Divergências | **0** |

## 2. Completude (nada excluído que a T-48 precise para regerar)

- Scripts `*.py` na raiz da origem: 26; no destino: 26; faltando: 0. Nenhum `*.py` em subpasta da origem.
- `lotes_tab.txt` presente. `out/`: 15 arquivos de saída dos validadores R1 copiados.
- Excluídos (103 arquivos), todos justificados:

| Excluído | Justificativa | Conferência da gerência |
|---|---|---|
| `__pycache__/` (12 `.pyc`) | artefato de execução | regenerável; correto |
| `pacote_v1_1.json` | determinado pela T-55; recuperável do histórico | SHA-256 `d318382639ee…` = `git show e97ab1f:saida/pacote/pacote.json` |
| `R0/` (`pacote.json`, `pacote_relatorio_2026-10-13.md`, `estudante/` 43 `.md`) | determinado pela T-55; recuperável do histórico | `R0/pacote.json` = commit `27e594d` (`ae2f346830f8…`); relatório = `27e594d` (`cef11163faf2…`); `estudante/` 43/43 = `git archive 27e594d saida/estudante` |
| `out/pacote.json` | cópia completa do pacote v1.2 | SHA-256 = `saida/pacote/pacote.json` (`f46ed9f8e43d…`, o do gatilho A) |
| `out/estudante/` (43 `.md`) | cópia da edição do estudante | 43/43 iguais a `saida/estudante/` |

## 3. Teste de execução fora do repositório e do scratchpad de origem

Cópia de `saida/pacote/gerador_v1_2/` para pasta temporária, `out/` esvaziado, execução com cwd = pasta da cópia:

| Script | Resultado |
|---|---|
| `build_pacote.py` | rc 0; `out/pacote.json` **byte a byte igual** a `saida/pacote/pacote.json` (`f46ed9f8…`); `out/stats.json` igual ao copiado |
| `estudante_gen.py` | rc 0; `out/estudante/` 43/43 iguais a `saida/estudante/`; `estudante_contagem.json` igual |
| `estudante_fidelidade.py` | rc 0; `estudante_fidelidade.json` igual ao copiado |
| `sync_check.py` | rc 0; `sync_check.txt` igual |
| `validate.py` | **rc 1 sem `pacote_v1_1.json`** (lê o arquivo do cwd, linha 12). Com o v1.1 recuperado (mesmo SHA do git `e97ab1f`) na pasta: rc 0, 103 verificações / 0 falhas; stdout = `out/validate_stdout.txt` |
| `conferencias_R1.py` | exige 3 argumentos (pasta R0, pacote R1, edição R1) e `pacote_v1_1.json` no cwd. Com R0 reconstruído do git `27e594d`: rc 0, 118 conferências / 0 falhas; stdout = `out/conferencias_final.txt`; `conferencias_R1.json` e `varredura_volatil.json` iguais |
| `relatorio_R1.py`, `report.py` | **não executados**: gravam direto no repositório por caminho absoluto (`REPO + '/saida/pacote/pacote_relatorio_2026-10-13.md'` e `'/home/claude/fabrica_camara2026/saida/pacote/pacote_relatorio.md'`) e sobrescreveriam relatórios canônicos |

Conclusão do teste: o gerador **não depende do scratchpad** (nenhum caminho `/tmp/…` nos scripts; confirmado por grep e pela execução). Regera o pacote v1.2 e a edição do estudante idênticos aos canônicos. As dependências remanescentes (v1.1 e R0 vindos do git, caminhos absolutos do repositório, saídas relativas ao cwd) são de ajuste de caminho e ficam para a próxima T-12, sem correção agora, conforme a tarefa.

## 4. Pontos para a próxima T-12 (não corrigidos)

1. `validate.py` (linha 12) e `conferencias_R1.py` (linha 236) leem `pacote_v1_1.json` do cwd; na T-12, parametrizar a base de comparação (a v1.2 canônica passa a ser a "anterior") ou documentar a extração por `git show e97ab1f:saida/pacote/pacote.json`.
2. `conferencias_R1.py` é comparação de rodada R0→R1 e exige a pasta R0 por argumento (recuperável por `git archive 27e594d saida/estudante saida/pacote/pacote.json`); na T-12, generalizar para "ocorrência anterior → atual" ou marcar como script histórico.
3. `relatorio_R1.py` e `report.py` gravam no repositório por caminho absoluto, sobrescrevendo `saida/pacote/pacote_relatorio_2026-10-13.md` e `saida/pacote/pacote_relatorio.md`; na T-12, gravar em `out/` e promover ao repositório só por passo explícito (coerente com o item 2 da lista da T48_reconciliacao_R2, seção 4: relatório inteiro gerado pelo gerador).
4. Caminho absoluto do repositório em `common.py` (`REPO`), `validate.py` (`R`), `relatorio_R1.py`, `report.py`, `report2.py`; saídas relativas ao cwd (`out/…`) em `validate.py`, `conferencias_R1.py`, `sync_check.py` (exigem cwd = pasta do gerador). Na T-12, derivar ambos de `__file__`.
5. `validate.json` não é determinístico na ordem de chaves de um campo `extra` (ordem de iteração de conjunto; difere entre execuções, conteúdo igual). Na T-12, ordenar antes de serializar.

## 5. Ressalvas de forma (sem efeito)

- R-1: o `MANIFESTO.md` descreve `R0/` como "8 scripts da cópia R0"; na origem `R0/` contém `pacote.json`, `pacote_relatorio_2026-10-13.md` e `estudante/` (43 `.md`), sem scripts. Descrição inexata, exclusão correta e recuperável (seção 2). Não exige correção do manifesto agora; registrar aqui basta.
- R-2: `saida/pacote/gerador_v1_2/` está fora do controle de versão (`git status`: não rastreado). A persistência que a T-55 visa só se completa quando a pasta entrar no próximo commit do ciclo (fora do domínio desta conferência; registro para quem fecha o ciclo).

## 6. Veredito

**CONFERIDO COM RESSALVAS** — 42/42 SHA-256 destino = origem = manifesto, 0 divergências; 26/26 scripts presentes; exclusões justificadas e recuperáveis do git; gerador regera o pacote v1.2 (`f46ed9f8…`) e a edição do estudante (43/43) idênticos aos canônicos sem o scratchpad. Ressalvas: R-1 e R-2 (forma) e cinco pontos de caminho para a próxima T-12 (seção 4).

Estado proposto da T-55: **CONCLUÍDA** (ciclo 2026-10-13 s4c1; conferida pela GBQ em saida/pacote/T55_conferencia_2026-10-13.md: CONFERIDO COM RESSALVAS; pontos de caminho na lista da próxima T-12).

## BLOCO TAREFAS

```
T-55; GBQ; Persistir no repositório o gerador R1 do pacote e da edição do estudante, hoje só no scratchpad da sessão (`s4/t48r1/`, fora do repositório; D1 GBQ, T48_reconciliacao_R2_2026-10-13.md, seção 0): copiar sem alterar os scripts `*.py` (inclusive `validate.py`, `estudante_fidelidade.py`, `conferencias_R1.py`, `relatorio_R1.py`, `literais.py`, `estudante_marcas.py`, `estudante_gen.py`, `f4.py`, `peg.py`, `build_pacote.py` e auxiliares), `lotes_tab.txt` e `out/` (saídas dos validadores R1) para `saida/pacote/gerador_v1_2/`, sem `__pycache__`, sem a cópia R0 nem o `pacote_v1_1.json` (recuperáveis do histórico); manifesto com SHA-256 de cada arquivo (origem = destino); ajuste de caminhos só na próxima T-12; antes do fim desta sessão (o scratchpad é efêmero) e antes da próxima T-12; AGORA; CONCLUÍDA (ciclo 2026-10-13 s4c1; conferida pela GBQ em saida/pacote/T55_conferencia_2026-10-13.md: CONFERIDO COM RESSALVAS, 42/42 SHA-256, gerador regera pacote e edição idênticos; pontos de caminho na seção 4 vão à próxima T-12); gbq-csc → gbq-gerencia (conferência por SHA-256); saida/pacote/gerador_v1_2/ + saida/pacote/gerador_v1_2/MANIFESTO.md
T-12; TODAS; Atualização do pacote.json a cada gatilho A novo — recorrente; inclui os Lotes 6a e 6b e os Simulados 0 v0.2 e 0-P2 quando estiverem prontos (D-PACOTE-6); PRÓXIMO (recorrente); PENDENTE — ocorrência v1.2 concluída pela T-48 (gatilho A 13/10/2026); próxima ocorrência (v1.3): lista PARA A PRÓXIMA T-12 de saida/pacote/T48_reconciliacao_R2_2026-10-13.md, seção 4, e pontos de caminho do gerador em saida/pacote/T55_conferencia_2026-10-13.md, seção 4; gerador base: saida/pacote/gerador_v1_2/ (cadência semanal, D-MODO-TREINO); gbq-csc → gbq-gerencia; saida/pacote/pacote.json
```
