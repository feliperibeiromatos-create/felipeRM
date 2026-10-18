# fidelidade_v1_9_gbq-cqe.md — T-94 — 2026-10-18 — gerado por gbq-cqe

Este é o ato próprio de QA de fidelidade do pacote v1.9 (dados) e v1.9-E (estudante), no ciclo 2026-10-18 s12c2. O rito segue o precedente `fidelidade_v1_8_gbq-cqe.md`.

**Método.** Trabalhei só com leitura. Os scripts são meus e ficam no scratchpad da sessão (`cqe_a.py`, `cqe_b.py`, `cqe_c.py`), todos rodados com `python3 -I` a partir de /tmp:
- Os 4 arquivos finais foram lidos por um parser meu, com regex por lote. Não importei o `reforco.py` nem nenhum módulo do gerador.
- As bases vieram do git: `git show 46496ca:` para o pacote.json, o pacote_estudante.json e o contrato. O 46496ca é o último commit que tocou os dois JSON antes do c26fc13 (v1.9).
- Rodei o pipeline do gerador só como contraprova, numa cópia descartável do repositório (`git clone` no scratchpad). Não o rodei no repositório da fábrica.
- Comparei sempre o conteúdo LF. Nenhum dos arquivos tem CR.

## Veredito: **ACEITO COM RESSALVAS**

- Fidelidade dos dados: 48/48 itens novos conferem com os arquivos finais, 286/286 itens da v1.8 estão intactos e a v1.8-E também está intacta. Não houve reprovação (0%).
- Há 7 achados, nenhum deles no conteúdo do pacote. São erros de registro e de redação (A-1, A-2, A-6, A-7) e duas questões de mérito de escopo com duas leituras (A-3, A-4), que a gbq-gerencia arbitra. O A-5 é observação. Nenhum achado impede o gatilho A, desde que o A-2 seja corrigido no texto do gatilho E.

## 1. Hashes (calculados por mim)

| Objeto | Bytes | SHA-256 | Declarado |
|---|---|---|---|
| `saida/pacote/pacote.json` v1.9 | 663235 | `1366055496457792bf55f541d901e2d1f277ee42611060b03bbf82b4427610bb` | confere |
| `saida/pacote/pacote_estudante.json` v1.9-E | 642374 | `8fa81b45a92095f8973c2787083d144869fdc195031455f7ff75ecb337e509e2` | confere |
| `regras/pacote_contrato.md` v1.2.6 | 39544 | `7e749c88ae1e194a38529e13105b5b43c53571e0e06d76747cab21fb83d510a8` | confere |
| registro adendo 1 | 14248 | `801a0724462521e30f5fedcd4b1b8aef772491a2621c80e3a39e130aaaaf8df9` | confere |
| v1.8 (`46496ca`) / v1.8-E / contrato v1.2.5 | 621907 / 602815 / 35460 | `09d4a457…` / `851e2370…` / `10eac696…` | conferem |
| L1 v2 / L2 v3 / L3 v3 / L6 v3 | 30014 / 49015 / 29340 / 7692 | `75e4a535…` / `cff8b71e…` / `79404c22…` / `58933b0a…` | iguais aos SHA das D-T89/T90/T91/T92 |

## 2. Os 286 itens da v1.8 e a v1.8-E

| Conferência | Resultado |
|---|---|
| Chaves de topo (dados e estudante) | Mesmas chaves, na mesma ordem. Só `nome`, `geradoEm` e `itens` diferem |
| `nome` / `geradoEm` | "(v1.8)" → "(v1.9)"; "(v1.8-E)" → "(v1.9-E)"; 2026-10-17 → 2026-10-18 |
| 286 primeiros itens | Idênticos aos da v1.8, incluindo a ordem das chaves, nos dados e no estudante |
| `edital`, `simulados`, `lotes`, `discursivas` | Idênticos nos dois arquivos |
| Reconstrução | Tirei os 48 do fim e voltei `nome` e `geradoEm`. Reserializei com `indent=1`, `ensure_ascii=False` e "\n" final, formato que detectei na própria v1.8. O resultado é a v1.8 e a v1.8-E **byte a byte** |

## 3. Os 48 contra os arquivos finais (parser próprio)

| Campo | Resultado (48/48, 0 falha) |
|---|---|
| Ordem | Igual à da tabela do contrato v1.2.6: L1-R01…R18, L2-R01…R18, L3-R01…R11, L6A-R01 |
| `enunciado` | Literal da linha da parte (d) |
| `comando` | "Julgue o item." (L1 e L2: na linha do id; L3: no cabeçalho único da Parte 2). No **L6A-R01**, a situação hipotética inteira com o comando ("Um servidor configurou … julgue o item a seguir."), sem o prefixo "L6A-R01 (P1-3). AUTORAL." |
| `gabarito` / [TS] | Lidos da parte (d-G). [TS] = 23: L1 7 (R01, R03, R07, R09, R12, R13, R17), L2 10, L3 5, L6A 1. Batem com as decisões de aceite. O [TS] não vai a nenhum campo do pacote, como manda o contrato |
| `itemEdital` | Folha do mapa (Parte 1) = folha da Parte 2 = folha da Parte 3, nos lotes em que ela aparece (L3 e L6A) |
| `justificativa` | Literal, sem cabeçalho e sem rótulo ("Justificativa:" no L3; "Justificativa (duas linhas):" no L6A). Nenhuma linha "Base:" ou "Aderência:" entra. Nenhuma linha extra fica fora da captura |
| `aderencia` | Parcial em L2-R02, R14, R15, L3-R01, R02 e R05: é o que declaram os arquivos e o que dizem as D-T90 e D-T91. Os demais itens são "direta" |
| `volatil` | `true` só em L2-R07 e L2-R18, que são os itens com "VOLÁTIL (…)" na justificativa de origem e nas decisões. Nenhum item tem `volatil: false` |
| `rotulo` / `certame` / `ano` / `cargo` / `numero` / `textoBase` / `url` | AUTORAL / "Projeto Câmara 2026" / 2026 / "Lote 1/2/3/6a" / nn do id / "" / caminho do arquivo final. As chaves estão na ordem do contrato |

## 4. Contagens

- 334 itens, 172 C / 162 E, banco 106, AUTORAL 228, `volatil` 25, parcial 45, 0 "QA PENDENTE" (nos dois JSON), ids únicos.
- Onda 1: 23 C / 25 E (47,9% de C).
  - Por lote: L1 9/9, L2 8/10, L3 6/5, L6A 0/1.
  - C/E por folha igual ao das decisões de aceite.
- Itens por folha (banco e AUTORAL):
  - As **23** folhas com item novo passam a ter 6 itens cada: P2-1.1 a 1.8, 2.1 a 2.8, 3.1 a 3.4, 4.2 e 4.3, e P1-3. As contagens de partida batem com as decisões.
  - P1-4.3 fica com 4 (T-102). Ver A-1.
- Simulados SIM-0, SIM-1, SIM-2 e SIM-0-P2: nenhum item de reforço; L4-11 e BQ-0010 nunca estão juntos. As folhas dos 48 existem no `edital`.

## 5. Estudante (v1.9-E)

- Nos 48 itens, só mudam `url` (48 vezes, sempre "") e `justificativa` (2 vezes). Nenhum outro campo muda.
- L2-R07: a justificativa do estudante é a dos dados menos a V1. L2-R18: é a dos dados menos a V1 e a V2. As duas igualdades são exatas, e não há nenhuma outra deleção (lista fechada da D-V19-08 confirmada).
- Minha varredura de marcas de processo nos campos de texto dos 48 deu 0 casamentos reais. Procurei [TS], VOLÁTIL, REVERIFICAR, Base:, Aderência:, QA, D-xxx, "verificado em", siglas de agentes, saida/ e .md. Os únicos acertos foram "pendente" dentro de "independentemente" e "d-t" dentro de "end-to-end".
- `gabarito` continua no `pacote_estudante.json`, como na v1.8-E: a plataforma precisa dele para corrigir (contrato v1.2.5). A ausência de gabarito exigida pela regra (d) da D-REFORCO-1 vale para a lista de itens da edição, não para este campo.
- Não há campo `nucleo` em nenhum dos dois JSON.
- Contagem por lote (prefixo, com fusão): L1 48, L2 48, L3 41, L4 30, L5 30, L6A 16, L6B 15. É a mesma do relatório.

## 6. Registro adendo 1

- 48 linhas de item, nos mesmos ids e na mesma ordem do pacote.
- Gabarito, folha, [TS], marca VOLÁTIL, aderência e formato conferem com o pacote e com o mapa de cada arquivo final.
- O ponto de julgamento é o do mapa, salvo em L1-R10 e L1-R16, que trazem **literalmente** o ponto VIGENTE da seção 4 de `T89_reconciliacao_2026-10-18.md`.
- Os totais (48; 23/25; [TS] 23; VOLÁTIL 2; parcial 6; aptos a final 40) e a tabela de 23 folhas conferem.

## 7. Contrato v1.2.6

O diff linha a linha contra a v1.2.5 (`46496ca`) dá:
- linha 1 trocada (v1.2.5 → v1.2.6, nova data);
- linha 3 trocada, mas só por acréscimo no fim: a linha nova começa com a linha 3 da v1.2.5 inteira;
- 19 linhas inseridas (150 a 168 da v1.2.6), antes do `---`.

Nada mais muda, e o total vai de 154 para 173 linhas. Os pontos 1 a 3 da errata se cumprem no pacote (seções 3 e 4 acima).

## 8. Gerador `gerador_v1_9/`

- **Lista fechada frente à v1_8**, conferida por mim:
  - novos: `_run.py`, `build_v19.py`, `conferencias_v19.py`, `manifesto_v1_9.py`, `reforco.py`, `reforco_marcas.py`, `registro_adendo_v19.py`, `validate_v19.py`;
  - alterados: `estudante_gen.py` (só o mapa de `lote_of`, com `L6A`/`L6B`), `estudante_json.py`, `refs.py` (`C_V18`, `v18()`), `rodar_tudo.sh` e `MANIFESTO.md`;
  - removidos: nenhum.
  - Li os diffs de `estudante_gen.py`, `refs.py` e `estudante_json.py`: estão restritos ao que foi declarado. O `reforco_marcas.py` tem exatamente as regras V1 e V2.
- **MANIFESTO**: os 46 SHA e tamanhos de arquivo batem com o disco, e o status igual/alterado/novo também. Os SHA de `out/` batem com o disco.
- **Reprodução em clone descartável** (o repositório da fábrica não foi tocado):
  - `sh rodar_tudo.sh` termina com código 0 e dá os mesmos 3 SHA (pacote, estudante, adendo);
  - os validadores dão validate_v19 47/47, conferencias_v19 23/23 e validar_erros_teste 12/12;
  - o MANIFESTO regenerado é idêntico (`git status` limpo no clone).
  - Isso é contraprova. A prova está nas seções 1 a 7, feitas com os meus scripts.
- **Pastas intactas desde 46496ca** (`banco/`, `gerador_v1_8/`, `saida/estudante`, `saida/simulados`, `saida/plataforma`, `saida/treino`, registro v3):
  - O único arquivo alterado é `banco/banco.csv` (+40 linhas, DA, commits 5c9b4d1 e 8493515 de 17/10). É anterior à T-94 e está fora do escopo, coerente com a D-V19-03 (a).
  - Os 4 arquivos finais do reforço são novos e têm os SHA das decisões de aceite.

## 9. Aviso sobre o L4-11 (D-V19-03 (d))

**Procede.** O arquivo `saida/gcb/GCB_Lote4_v3_canonica_GCB-CPP.md` já traz o texto do Erratum 1 devolvido (D-L4-T83-DEVOLVIDO):
- linha 368: "A página "What is Machine Learning?", do curso Introduction to Machine Learning do Google for Developers, afirma que…";
- linha 44: Tabela de Correções com o estado "aplicada (v3.5…)".

O `pacote.json` v1.9 mantém o texto da v1.8 ("O F4 afirma que…"), o que está correto. O gerador v1.8, se for rodado sobre as fontes de hoje, absorveria o texto devolvido. O alerta à GCB e a exigência de fixar o L4-11 antes da próxima regeneração são pertinentes.

## 10. Achados

| # | Tipo | Severidade | Achado | Encaminhamento |
|---|---|---|---|---|
| A-1 | Registro / contagem | baixa | "25 folhas" está errado. As folhas com 6 itens são **23**: 8 + 8 + 4 + 2 + 1. A onda 1 da D-REFORCO-1 tem **24** folhas, contando a P1-4.3, que fica com 4 até a T-102. O erro está na D1 (seções 2 e 7.4), no relatório (seção 3) e no rótulo do `validate_v19.py:119`, cuja lista `FOLHAS` tem 23 entradas, ou seja, a verificação está certa e só o texto erra. Os dados estão corretos. O pedido desta conferência repete o "25" | CORRIGIR o texto da D1 e do relatório no gatilho A ("23 folhas com 6; P1-4.3 com 4"). Corrigir o rótulo do validador na v1.10, porque mexer nele agora muda o SHA do arquivo e o MANIFESTO |
| A-2 | Mérito: texto do gatilho E | média | A D1, seção 5, diz que a plataforma v1.7 "precisa reconhecer `L1-R`, `L2-R`, `L3-R` e `L6A-R`" e que, "sem adaptação, os 48 ficam no banco geral". Isso está inexato. A `plataforma_v1_7.html`, linhas 183 a 187 e 258, associa itens a lote com `startsWith` sobre `pref` "L1-", "L2-", "L3-", "6A-". Por isso **47 dos 48** já entram nos testes de lote do L1, L2 e L3 sem adaptação, e só o **L6A-R01** fica de fora (o prefixo dele é "L6A-", e o filtro procura "6A-"). Consequência a registrar: os parciais L2-R02, R14, R15, L3-R01, R02 e R05 aparecem no teste de lote, que só exclui `volatil`. O teste de lote não é simulado, então isso é compatível com a D-ADERENCIA | CORRIGIR o texto do gatilho E/PARA_PRESIDENCIA antes de emiti-lo: só o L6A-R01 depende de adaptação (prefixo "L6A-") |
| A-3 | Mérito de escopo (discutível; duas leituras, sem decisão minha) | — | Adiamento de (b) 5C-08 e (c) `lotes[L2].curso` para a v1.10. **Leitura 1 (GBQ):** a T-94, posterior e específica, manda consolidar "sem mudar item existente", e o delta exclusivo de itens novos concentra a fidelidade; então adia. **Leitura 2:** a D-TRANSPORTE-L5C-T83 ("Derivados (… pacote.json, pacote_estudante.json) absorvem na próxima ocorrência da T-12") e a D-L2-T84-ERRATA ("absorção na próxima ocorrência da T-12") fixam esta ocorrência, e a T-94 é, pela letra da própria linha, "ocorrência da T-12". Além disso, (c) é um campo de **lote**, não de item, e a cláusula "sem mudar item existente" não o cobre literalmente | Arbitragem da gbq-gerencia. A D1 já leva o adiamento à Presidência no gatilho A, que pode revogar por linha. Recomendo citar no gatilho as duas decisões, com a letra delas |
| A-4 | Mérito de escopo (discutível; duas leituras) | — | O objeto "estudante" é só o `pacote_estudante.json`; a edição .md (`saida/estudante/`, 34 arquivos) fica na v1.8 sem os 48. **Leitura 1 (GBQ):** é a letra da T-94 ("no pacote.json e no pacote_estudante.json v1.9 (dados e estudante)"), e a edição .md com reforço vem na v1.10, junto com o `nucleo`. **Leitura 2:** pela D-REFORCO-1 ("Saída consolidada no pacote v1.9 (dados e estudante)") e pelo precedente da v1.8 (D-PACOTE-V18: JSON e edição .md), "estudante" incluiria a edição .md. O risco prático é baixo, porque a plataforma lê o JSON | Arbitragem da gbq-gerencia. Se a leitura 1 prevalecer, registrar no gatilho A que a edição .md v1.8 não traz os 48 |
| A-5 | Observação (sem correção) | — | No `pacote.json` (dados), as justificativas de L2-R07 e L2-R18 mantêm "VOLÁTIL (…); REVERIFICAR." e, no R18, a instrução de montagem e reescrita. A D1 tira as linhas "Base:" alegando "metadados de fábrica", mas o critério não é aplicado por igual. Mesmo assim, segue a letra do contrato (o cabeçalho é id, gabarito e [TS]) e o precedente da v1.8 nos dados (L2-Q23 "NÃO VOLÁTIL"; L3-Q21 "[NORMATIVO — QA…]"). O estudante já remove esse texto | Nenhuma. Registrar |
| A-6 | Forma (baixa) | baixa | A `justificativa` do L6A-R01 começa com minúscula ("o POP3 serve…"). É o literal da origem, depois do rótulo "Justificativa (duas linhas): ", então o pacote está fiel | Opcional: errata de forma na origem (GCB) na próxima ocorrência. O pacote não muda agora |
| A-7 | Redação do contrato | baixa | O ponto 2 da v1.2.6 fala em "o texto rotulado de justificativa". No L1 e no L2 não há rótulo: a justificativa segue o cabeçalho "Lx-Rnn. G [TS]." na mesma linha. A leitura feita (texto depois do cabeçalho) está correta e é a única possível | Precisar a redação numa errata futura ("rotulado, no L3 e no L6A; após o cabeçalho, no L1 e no L2"). Não reabre a v1.2.6 |

## 11. Resumo

- Aprovado: SHA (2 de 2 pacotes, mais contrato e adendo), 286 intactos (dados e estudante, byte a byte), 48/48 contra os arquivos finais, contagens, estudante, adendo, contrato, gerador e o aviso do L4-11.
- Corrigir: A-1 (texto: 23 folhas, não 25) e A-2 (texto do gatilho E: só o L6A-R01 depende de adaptação da plataforma).
- Para a gbq-gerencia arbitrar: A-3 (adiamentos (b) e (c)) e A-4 (a edição .md fora do objeto).
- Registro: A-5, A-6 e A-7.
- Reprovado: nenhum.
- Não verificado:
  - a varredura R com a regex `marcas_processo.py` do gerador: substituí por varredura própria, com 0 casamentos de processo nos 48;
  - a reabertura das URLs-base dos 48: fora do escopo da fidelidade; as bases foram conferidas pela QA dos lotes e pelo qa-normativo.
- Nada foi gravado fora deste arquivo; não fiz commit nem push. Observação: o HEAD do repositório andou durante a conferência (8261bf7, T-95), sem tocar nenhum objeto desta fidelidade.
