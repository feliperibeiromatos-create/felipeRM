# fidelidade_v1_10_gbq-cqe.md — T-104 — 2026-10-18 — gerado por gbq-cqe

Este é o ato próprio de QA de fidelidade do pacote v1.10 (dados), do v1.10-E (estudante), da edição .md, do adendo 2 e do contrato v1.2.7, no ciclo 2026-10-18 s13c2. O rito segue `fidelidade_v1_9_gbq-cqe.md`. O objeto é a geração final: D1 `T104_D1_v1_10_2026-10-18.md` com o adendo 1 (seção 8) e o relatório `pacote_relatorio_2026-10-18_v1_10.md` (seção 6).

**Método.** Trabalhei só com leitura. Os scripts são meus, ficam no scratchpad da sessão (`cqe110/s2.py` a `s8.py`) e rodaram com `python3 -I`:
- Não importei nenhum módulo do gerador e não li o `nucleo.py`.
- As bases vieram do git: `git show c26fc13:` para a v1.9, a v1.9-E e o contrato v1.2.6, e `git show 46496ca:saida/estudante/` para os 34 arquivos .md da v1.8.
- Os 11 arquivos finais foram lidos por um parser meu: Parte 1 (mapa: folha, VOLÁTIL, aderência), Parte 2 (comando e enunciado) e Parte 3 (gabarito, [TS] e justificativa).
- Rodei o pipeline do gerador só como contraprova, num `git clone` descartável no scratchpad (HEAD f88d2e0). Não o rodei no repositório da fábrica.
- Todo o conteúdo comparado é LF; nenhum objeto tem CR.

O HEAD andou durante a conferência (cacd606 → f88d2e0, T-95/T-107). Esse commit só tocou `TAREFAS.md` e `cobertura_v1_10.md`, nenhum objeto desta fidelidade.

## Veredito: **ACEITO COM RESSALVAS**

- **Dados íntegros.** 226/226 itens novos conferem com os arquivos finais. Os 334 da v1.9 estão intactos, salvo as trocas admitidas, e a v1.9 e a v1.9-E se reconstroem byte a byte. Contagens, `nucleo`, edição .md (35/35), adendo 2 e contrato conferem. Reprovação 0%.
- **Ressalvas.** Há 5 achados, nenhum no conteúdo de item do pacote:
  - A-1 (média): a reprodução do pipeline quebrou depois do commit;
  - A-2 (média; duas leituras): fundamento factual inexato da D-NUCLEO-CRITERIO;
  - A-3 (baixa): marca residual no estudante;
  - A-4 e A-5: registros.

## 1. Hashes (recalculados por mim)

| Objeto | Bytes | SHA-256 | Declarado |
|---|---|---|---|
| `saida/pacote/pacote.json` v1.10 | 860070 | `d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed` | confere |
| `saida/pacote/pacote_estudante.json` v1.10-E | 839834 | `d8a68156f00e40c6a03937e678d2b3949c68c9ad24e8a7489ff883b5a3497b7f` | confere |
| adendo 2 do registro (`saida/gbq/…_v3_adendo2_2026-10-18.md`) | 49975 | `3c1ba9a6…dfce75c` | confere |
| `regras/pacote_contrato.md` v1.2.7 / registro `contrato_v1_2_7_2026-10-18.md` | 44631 / 2547 | `461acdce…` / `47b35952…` | conferem |
| `gerador_v1_10/MANIFESTO.md` | 16534 | `5bd6223f…` | confere |
| v1.9 / v1.9-E / contrato v1.2.6 (c26fc13) | — | `13660554…` / `8fa81b45…` / `7e749c88…` | conferem |
| `GCE_Lote2_v2_CPP.md` / `GCE_Lote2_padroes_GCE.md` | — | `27ef5dc0…` / `4f3dde8e…` | conferem |
| 11 arquivos finais (L6B saldo_v2; L1 A_v3, B_v2, C_v2, D_v3, saldo_v2; L2 A_v3, B_v3, C_v3, D_v3, saldo_v2) | — | `785c91e9`, `8fbe66c7`, `201a3172`, `37043a8c`, `12349d7e`, `37f7e91d`, `b6911efb`, `f3b33204`, `4bbde472`, `892526fc`, `22e4c1e2` (SHA inteiros) | = decisões de aceite e tabela do contrato |
| `saida/estudante/` (35 arquivos) | — | — | 35/35 iguais à tabela da seção 1 do relatório (SHA e bytes) |

## 2. Os 334 da v1.9 (dados e estudante, contra c26fc13)

| Conferência | Resultado |
|---|---|
| Chaves de topo | Iguais, na mesma ordem. Diferem só `nome` ("(v1.9)" → "(v1.10)"; "(v1.9-E)" → "(v1.10-E)"), `itens`, `lotes` e `discursivas`. `geradoEm` continua 2026-10-18. `edital` e `simulados` são idênticos |
| 334 primeiros itens | Idênticos campo a campo e na ordem das chaves, salvo `itens[5C-08].justificativa`: a antiga 1 → 0, a nova 0 → 1, e a reversão da troca devolve o texto da v1.9 |
| `lotes[L2].curso` | Exatamente 2 blocos de diff. (1) T-84: l. 176, "ver Lote 1-C." → "ver o complemento do Lote 1 (adendo ao 1.4)."; (2) T-106: 1 linha → 3 linhas, idênticas às l. 525–527 do `GCE_Lote2_v2_CPP.md` (27ef5dc0…), com a indentação de 3 espaços. Os outros lotes não mudam |
| `discursivas[D3].padrao` | Exatamente 1 linha: "      corrige sotaque nem ruído;" → "      trata a causa acústica (ruído, sotaque), que pede dados acústicos;", igual à l. 138 de `GCE_Lote2_padroes_GCE.md` (4f3dde8e…). Sem nota "ERRATA" (0 ocorrência), como diz a D-V110-04. D1, D2, D4 e D5 não mudam |
| Estudante | O mesmo quadro. Há `nucleo` booleano em todo item (560), como último campo, e não há `nucleo` no `pacote.json` |
| Reconstrução | Tirei os 226 do fim e o `nucleo`, reverti as 4 trocas e o `nome` e reserializei com `indent=1`, `ensure_ascii=False` e "\n" final, formato confirmado na própria v1.10. Resultado: a v1.9 e a v1.9-E **byte a byte** (13660554…, 8fa81b45…) |
| L4-11 | Idêntico ao da v1.9, que é o texto da v1.8 ("O F4 afirma que…"). Y1 não foi tocado |

## 3. Os 226 contra os 11 arquivos finais (parser próprio)

| Campo | Resultado (226/226; 0 falha) |
|---|---|
| Ordem | L6B-R01, R02; L1-R19…R130 (sem R43); L1-R131; L2-R19…R130 (sem R67); L2-R131. É a ordem do contrato v1.2.7, ponto 1, e da D-V110-05 |
| `comando` / `enunciado` | GCE: "Julgue o item.", sempre literal da linha do id na Parte 2, e o enunciado de uma linha. L6B: a situação inteira depois de "(P1-4.3). AUTORAL. ", e o enunciado na linha seguinte |
| `gabarito` / [TS] | Vêm da linha de cabeçalho da Parte 3. Há 137 [TS] (L6B 1; onda 2 65; L1-R131 1; onda 3 69; L2-R131 1) e nenhum vai a campo do pacote (0 "[TS]" nos 226) |
| `itemEdital` | Folha do mapa. Onde existe "## Folha" na Parte 3, a folha confere com ela |
| `justificativa` | GCE: texto da linha de cabeçalho depois de "id. G[ [TS]][ (espelho)]. ", literal. L6B: texto depois de "Justificativa (duas linhas): ". Nenhuma linha "Base:", "Formato:", "REVERIFICAR:", "Troca sutil:" ou "Espelho…" entra. Blocos multilinha: ver A-4 |
| `aderencia` | Parcial = 43, que são as marcas "PARCIAL" dos mapas v3 (A 16, B 19, C 7, D 1 = R130) e conferem com a T97_reconciliacao, 3.1. A onda 2, os saldos e o L6B são "direta" |
| `volatil` | `true` em 29: são os "S" do mapa. Onda 2: 11, os da D-T96 (I); R24 e R29 não são VOLÁTEIS. Onda 3: 18, os da D-T97 e da T97, 4.3. Nunca aparece `false`, e a chave vem no fim, como nos legados |
| rotulo / certame / ano / cargo / numero / textoBase / url | AUTORAL / "Projeto Câmara 2026" / 2026 / "Lote 1", "Lote 2" ou "Lote 6b" / número do id (até 131) / "" / caminho do arquivo final |
| L2-R131 | E; [TS] não exportado; `numero` 131; justificativa da linha de cabeçalho; P2-2.4; direta; não VOLÁTIL; último item |

## 4. Contagens (dados = estudante)

- Itens: 560; ids únicos.
- Gabaritos: 285 C / 275 E; os novos, 113/113.
- `volatil`: 54. Parciais: 88.
- Rótulos: AUTORAL 454 e CEBRASPE_ANALOGA 106.
- 0 "QA PENDENTE".
- Folhas tocadas (itens / diretas): P1-4.3 6/6; P2-1.1 a 1.8 com 20/20; P2-2.1 a 2.8 com 20/10, 20/13, 20/10, 20/11, 20/17, 20/16, 20/18 e 20/19. A P2-2.4 tem 10 C / 10 E.
- `simulados` são idênticos aos da v1.9: nenhum item novo entra em SIM-0, SIM-1, SIM-2 ou SIM-0-P2.

## 5. `nucleo` (recalculado sem o `nucleo.py`)

Chave por item: k1 data, k2 linha do ato, k3 direta antes de parcial, k4 posição.
- k1: `data_verificacao` de `banco/banco.csv` (60 itens com 2026-10-08 e 46 com 2026-10-10), 2026-10-09 para os lotes legados e 2026-10-18 para o reforço.
- k2: banco = 0. Os outros atos, pelas linhas que localizei em DECISOES.md: D-CANONICOS 14, D-LOTE6A 20, D-LOTE6B 21, D-T92 103, D-T89 104, D-T91 105, D-T90 106, D-T102 110, D-T96 118, D-T103 119, D-T97 121, D-T105 129.

Resultado: **343 `true` em 41 folhas, igual ao JSON item a item.** Entre os `true` há 25 parciais e 30 VOLÁTEIS. O L2-R131 fica `false`. Na P2-4.1, o núcleo são os BQ-0002 a 0008 e 0023 a 0025, como registra a D-NUCLEO-CRITERIO. Ver A-2.

## 6. Estudante (v1.10-E, os 226)

- Mudam só `url` (226 vezes, sempre "") e `justificativa` (73 itens, 80 trechos).
- Todos os trechos são deleção pura:
  - V2 ("VOLÁTIL (…)…"): 20;
  - R2 ("REVERIFICAR. "): 51;
  - C2 (frases finais de fundamento do rótulo, em L2-R77, R81, R82, R85, R88, R94, R96, R99, R100): 9.
- É a lista fechada da D-V110-09. Nenhum outro campo muda.
- `url` "" nos 454 AUTORAL; os banco mantêm a URL cebraspe.
- Varredura própria nos 226 (comando, enunciado e justificativa): 0 "REVERIFICAR", 0 "VOLÁTIL", 0 "[TS]", 0 "verificado em", 0 "D-T…" e 0 sigla de agente.
- Homônimos de conteúdo: "Secretaria-Geral da Mesa" (L2-R29, R38, R45), "conferir/conferência" e "resultados parciais".
- Exceção: L2-R90 (ver A-3).

## 7. Edição .md (35 arquivos)

- **Iguais à v1.8 (46496ca), byte a byte:** 20 arquivos.
- **v1.8 como prefixo exato, mais a seção "## Itens de reforço" ao fim:** os 10 `_itens`/`_gabarito` do L1, L2, L3, L6A e L6B.
- **Só a troca declarada:** `L5_gabarito.md` (a1, 1 linha), `L2_estudo.md` (a2 e e2, iguais às do JSON) e `DISCURSIVAS_padrao.md` (e1, 1 linha).
- **`README.md`:** versão, data e as linhas novas.
- **Seções de reforço:** 274 itens (48 da onda 1 e 226 novos), na ordem do pacote. Conferem com o `pacote_estudante.json`:
  - em `_itens`: comando, enunciado, "(aderência: parcial)" e aviso de VOLÁTIL;
  - em `_gabarito`: gabarito, folha, aderência, justificativa e aviso.
  - O `_itens` não tem gabarito, [TS], REVERIFICAR nem VOLÁTIL. As únicas menções a "Gabarito" são as linhas-guia herdadas da v1.8.
- **`NUCLEO.md`:** 41 folhas e 343 ids, iguais ao `nucleo` do JSON. As contagens "n de N" conferem.

## 8. Adendo 2

- Tem 226 linhas, nos ids e na ordem do pacote.
- Gabarito, folha, [TS] (o do meu parser), VOLÁTIL e aderência conferem com o pacote.
- Formato e ponto conferem com a coluna literal do mapa, salvo o L1-R99, que vem como PC (o mapa diz D), como manda a T96_reconciliacao, seção 3.
- Fontes com os 11 SHA inteiros.
- **Frase de prevalência:** está presente (T96, seção 3; T97, seções 2 a 7; L1-R43 e L2-R67 retirados; L2-R131 com a Tabela de Correções da T105_reconciliacao, seção 2).
- **Pares de montagem:** os 11 da T97, seção 6, mais o L2-R131 × L2-R68.
- **R1 VOLÁTIL:** lista dos 29, igual à do pacote.
- **Totais:** 226; 113/113; [TS] 137; VOLÁTIL 29; parcial 43; aptos a final 160 (L2 56), que recalculei.

## 9. Contrato v1.2.7

- **Diff contra a v1.2.6 (c26fc13):** só C-1, C-2 e C-3.
  - C-1: linha 1 trocada.
  - C-2: linha 3 trocada só por acréscimo no fim; a linha nova começa com a linha 3 antiga inteira.
  - C-3: 27 linhas inseridas depois da l. 167.
  - Total: de 173 para 200 linhas.
- **Pontos 1 a 7:** cumprem a D-V110-12.
  - Tabela de 11 arquivos, com faixas de ids e prefixos de SHA iguais ao disco.
  - Regra da `justificativa` (resolve a A-7 da v1.9).
  - `nucleo` só no estudante.
  - Deleções da D-V110-09.
  - Os 43 parciais.
  - Edição .md.
  - Aplicação.
- **Registro `contrato_v1_2_7_2026-10-18.md`:** coerente com o diff e os SHA.

## 10. Gerador `gerador_v1_10/`

- **Lista fechada frente ao v1_9:**
  - novos (11): `build_v110`, `conferencias_v110`, `config_v110`, `estudante_md_v110`, `manifesto_v1_10`, `marcas_x_v110`, `nucleo`, `reforco_marcas_v110`, `reforco_v110`, `registro_adendo_v110`, `validate_v110`;
  - alterados: `estudante_json.py`, `refs.py` (só `C_V19` e `v19()`), `rodar_tudo.sh` e `MANIFESTO.md`;
  - removidos: nenhum.
- **`config_v110.py`:** chaves da D-V110-15.
- **MANIFESTO:** 114 entradas, com SHA e bytes iguais ao disco.
- **Contraprova no clone:**
  - Os SHA de `out/pacote.json`, `out/pacote_estudante.json` e `out/registro_adendo2.md` são os declarados, e `out/estudante/` é igual a `saida/estudante/`.
  - validate_v110 dá 37/37 e validar_erros_teste 12/12 (rodado à parte).
  - **Mas `sh rodar_tudo.sh` termina com código 1:** conferencias_v110 dá 21/23 (ver A-1).

## 11. Achados

| # | Tipo | Severidade | Achado | Encaminhamento |
|---|---|---|---|---|
| A-1 | Reprodutibilidade do gerador | média | O bloco (4) de `conferencias_v110.py` (l. 118–121) lê a base v1.2.6 de `git show HEAD:regras/pacote_contrato.md`. Desde o commit cacd606 o HEAD já tem a v1.2.7, e 4a e 4c falham ("base: v1.2.6 do HEAD = 7e749c88…"; diff vazio). Com `set -e`, `rodar_tudo.sh` para no passo 6: os passos 7 (validar_erros_teste) e 8 (MANIFESTO) não rodam e `out/casos_erros/` não é recriado. O "23/23" do relatório só vale antes do commit. Os dados não são afetados: os SHA se reproduzem | CORRIGIR no gerador. Fixar a base no commit `c26fc13`, ou conferir pelo SHA 7e749c88… em vez de usar o HEAD, e regenerar o MANIFESTO. Registrar no gatilho A que, depois do commit, as conferências dão 21/23 por esse motivo. Não reabre os dados |
| A-2 | Mérito: fundamento de decisão (discutível; duas leituras, sem decisão minha) | média | O fundamento (c) da D-NUCLEO-CRITERIO diz que o resultado é "robusto às datas do banco" se a canonização dos BQ for lida como 09/10 ou 13/10. **Não é.** Mantidos k2–k4, com o banco todo em 09/10, mudam 22 itens em 3 folhas: na P1-1 entram BQ-0080/81/85/87/91/92 e saem 6A-05 a 10; na P1-8.2 entram BQ-0096/97/100/112 e saem 5C-01 e A5-11 a 13; e há a P1-4.1. Com o banco todo em 13/10, mudam 38 itens em 5 folhas, entre elas a **P2-4.1**: entram os 5 diretos L3-Q17 a Q21 e saem BQ-0007, 0008 e 0023 a 0025. O banco está misto (08/10 e 10/10), e por isso os BQ de 10/10 ficam depois dos legados de 09/10. Há ainda uma sensibilidade de 1 item: se o k3 não se aplicar dentro do banco ("mesmo ato"), troca BQ-0095 ↔ BQ-0068. **Leitura 1 (D1/presidencia):** canonização = `data_verificacao` de cada BQ, e o pacote está correto como está (é o que conferi). **Leitura 2:** a canonização do banco é um ato único (D-RECUPERACAO, 09/10, ou v1.2, 13/10), o que dá outro núcleo | Arbitragem da gbq-gerencia. Não muda o pacote, que segue o critério fixado. Recomendo corrigir o fundamento (c) no texto do gatilho A, para a Presidência e o Fundador lerem o efeito real |
| A-3 | Estudante: marca residual | baixa | A justificativa do L2-R90 (JSON v1.10-E e `L2_gabarito.md`) termina o cálculo com "(conta conferida por script)". É nota de processo da produção e não está na lista fechada da D-V110-09. Por isso o pacote está fiel à D1 | Errata de forma: deleção a acrescentar à lista na v1.11, ou errata na origem (GCE). Não reabre a v1.10 |
| A-4 | Registro: blocos multilinha (pedido especial) | — | No `L2_reforco_onda3_D_v3.md`, 9 itens (R104, R105, R110, R112, R114, R118, R122, R124, R127) têm uma 2ª linha não rotulada no (d-G), com explicação de mérito (às vezes com "R1 do QA" ou "CONFERE (qa-normativo…)"). Linhas rotuladas "Troca sutil:" (13) e "Espelho de [TS]:" (5) também ficam fora. Pelo ponto 2 da v1.2.7 ("só a linha de cabeçalho"), ficam fora da `justificativa`, e o pacote está conforme. No C_v2 (L1) as linhas extras são todas rotuladas (Base, Formato, REVERIFICAR, VOLÁTIL, Nota de base) e ficam corretamente fora. No L6B, a justificativa é só o texto rotulado, sem [TS]:, VOLÁTIL:, REVERIFICAR:, Ponto: ou Base: | Nenhuma correção. Registrar. Se a GCE quiser essa explicação no estudo, o caminho é a origem (cabeçalho) |
| A-5 | Forma do gerador | baixa | O comentário de cabeçalho de `rodar_tudo.sh` (l. 4) ainda diz "ENSAIO: nada é promovido". Só a mensagem final foi atualizada (D-V110-16) | Opcional, junto com a A-1 |

Mérito de escopo (D1, seção 8.11; relatório, seção 6.8):
- Os ajustes do adendo 1 não tiveram efeito em dados. Os 226 e os 334 conferem com as fontes e com a v1.9 por leitura própria.
- A recusa do m-da (D-V110-13) segue a letra da linha T-104 ("se exigir mudança de contrato, fica para ocorrência própria").
- O objeto .md (D-V110-11) cumpre o "cada uma com edição do estudante" da D-REFORCO-2.
- O critério do `nucleo` está conferido como fixado (D-NUCLEO-CRITERIO), com a ressalva factual da A-2.

## 12. Resumo

- **Aprovado:**
  - SHA de todos os objetos;
  - 334 intactos, com reconstrução byte a byte da v1.9 e da v1.9-E;
  - as 4 trocas, com 1 ocorrência cada, contra os canônicos;
  - 226/226 contra os 11 arquivos finais;
  - contagens;
  - `nucleo` (343 em 41 folhas);
  - estudante (80 deleções da lista fechada);
  - edição .md (35);
  - adendo 2;
  - contrato v1.2.7;
  - lista fechada e MANIFESTO do gerador.
- **Corrigir:** A-1 (base da conferência do contrato fixada fora do HEAD); A-3 (L2-R90, na v1.11).
- **Para a gbq-gerencia arbitrar:** A-2 (fundamento (c) da D-NUCLEO-CRITERIO; duas leituras).
- **Registro:** A-4 e A-5.
- **Reprovado:** nenhum.
- **Não verificado:** a reabertura das URLs-base dos 226. Está fora do escopo da fidelidade; as bases foram conferidas pela QA das ondas.
- **Gravação:** nada foi gravado fora deste arquivo. Não fiz commit nem push.
