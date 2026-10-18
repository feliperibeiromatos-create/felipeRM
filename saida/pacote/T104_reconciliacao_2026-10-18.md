# T104_reconciliacao_2026-10-18.md — T-104 — 2026-10-18 — gerado por gbq-gerencia

Reconciliação da T-104 (pacote v1.10, v1.10-E, edição .md, adendo 2 e contrato v1.2.7), ciclo 2026-10-18 s13c2. Fontes: fidelidade `saida/pacote/fidelidade_v1_10_gbq-cqe.md` (ACEITO COM RESSALVAS; reprovação 0%), D1 `saida/pacote/T104_D1_v1_10_2026-10-18.md`, relatório `saida/pacote/pacote_relatorio_2026-10-18_v1_10.md`, cobertura `saida/pacote/cobertura_v1_10.md`, D-NUCLEO-CRITERIO, D-REFORCO-2 e D-ONDA4-FILA-2 (DECISOES.md). Nada foi commitado; PARA_PRESIDENCIA.md e TAREFAS.md não foram tocados (textos devolvidos ao orquestrador).

## 1. Decisão sobre cada achado

| # | Severidade | Decisão da gbq-gerencia | Estado |
|---|---|---|---|
| A-1 | média | ACATADO. Corrigido no gerador, sem mudar dados (seção 2) | RESOLVIDO |
| A-2 | média | ACATADO o fato (o fundamento (c) da D-NUCLEO-CRITERIO é inexato). O pacote não muda. A escolha entre as leituras vai à Presidência como gatilho D (seção 3) | ABERTO (gatilho D) |
| A-3 | baixa | Fica para a v1.11 (seção 4) | DIFERIDO (v1.11) |
| A-4 | registro | Sem correção. O pacote cumpre o ponto 2 do contrato v1.2.7 (só a linha de cabeçalho). Se a GCE quiser essas explicações no estudo, a correção é na origem | REGISTRADO |
| A-5 | baixa | ACATADO. Corrigido junto com a A-1 | RESOLVIDO |

## 2. A-1 e A-5: correção do gerador (`saida/pacote/gerador_v1_10/`)

- **`conferencias_v110.py`, bloco (4):** a base v1.2.6 do contrato passa a ser lida do commit fixo `refs.C_V19` (c26fc13), por `refs.git_show(refs.C_V19, 'regras/pacote_contrato.md')`, e não mais de `git show HEAD:`. Conferi que `git show c26fc13:regras/pacote_contrato.md` tem o SHA-256 `7e749c88ae1e194a38529e13105b5b43c53571e0e06d76747cab21fb83d510a8`, que é a v1.2.6. A mensagem do 4a agora diz "base: v1.2.6 do commit c26fc13". Nenhum critério de conferência mudou.
- **`rodar_tudo.sh`, linha 4 (A-5):** "ENSAIO: nada é promovido…" foi trocado por "GERAÇÃO FINAL (D-ONDA4-FILA-2 (2)): a promoção a saida/ já foi feita no commit cacd606 e não é repetida por este script; ele só regenera out/ como contraprova."
- **`manifesto_v1_10.py`:** a docstring dizia "Modo ENSAIO"; agora diz que o modo vem de `config_v110.FINAL`. Só a docstring mudou; o texto gerado é o mesmo.
- **Nova execução, no repositório:** `sh saida/pacote/gerador_v1_10/rodar_tudo.sh` terminou com **código de saída 0**.
  - Passo 5: validate_v110 deu 37/37.
  - Passo 6: conferencias_v110 deu **23/23**; antes do ajuste, depois do commit, dava 21/23.
  - Passo 7: validar_erros_teste deu 12/12, com 0 falha.
  - Passo 8: MANIFESTO regenerado.
- **Os SHA-256 se reproduzem byte a byte:**

  | Objeto | SHA-256 |
  |---|---|
  | `out/pacote.json` = `saida/pacote/pacote.json` | `d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed` |
  | `out/pacote_estudante.json` = `saida/pacote/pacote_estudante.json` | `d8a68156f00e40c6a03937e678d2b3949c68c9ad24e8a7489ff883b5a3497b7f` |
  | `out/registro_adendo2.md` = adendo 2 em `saida/gbq/` | `3c1ba9a6…dfce75c` |
  | `out/estudante/` | igual a `saida/estudante/` (`diff -r` vazio) |

- **MANIFESTO:** `gerador_v1_10/MANIFESTO.md` foi regenerado e tem SHA-256 `dfba843ebf7bc75a1c897865b56a9d9b81e0b642b4c8338ef17bf191dcb8dcd2`. Ele traz os novos SHA dos três scripts e de `out/`:

  | Arquivo | SHA-256 |
  |---|---|
  | `conferencias_v110.py` | `243f458c…` |
  | `rodar_tudo.sh` | `ce1b03b6…` |
  | `manifesto_v1_10.py` | `794ba0f1…` |

- **Diff no git:** só os três scripts, o MANIFESTO e `out/conferencias_stdout.txt` / `out/conferencias_v110.json`. Nenhum dado, nenhum arquivo de `saida/estudante/`, `saida/gbq/` ou `regras/` mudou.
- **Para o gatilho A:** no commit cacd606 as conferências dariam 21/23 só por causa da base no HEAD. Com a correção, dão 23/23. Os dados não foram reabertos.

## 3. A-2: núcleo (gatilho D; o pacote não muda)

O critério do `nucleo` é decisão desta Gerência (D-V110-07/08), ratificada pela presidencia (D-NUCLEO-CRITERIO, SEM OBJEÇÃO). O fundamento (c) dessa ratificação diz que o resultado é "robusto às datas do banco". A gbq-cqe mostrou que isso é falso. Como é a ratificação que está contestada, não decido sozinho: vai como gatilho D.

- **Leitura 1 (é a que está no pacote; recomendo mantê-la).** A "ordem de canonização" é a `data_verificacao` de cada BQ em `banco/banco.csv`:
  - 60 itens têm 08/10 e 46 têm 10/10;
  - os legados contam como 09/10 e o reforço como 18/10.
  - O banco é a fonte do item. Por isso a data própria de cada BQ é o registro de canonização mais fiel à letra da D-REFORCO-2.
  - Resultado: 343 `true` em 41 folhas. A gbq-cqe recalculou sem o `nucleo.py`.
  - Efeito: na P2-4.1, o núcleo são os BQ-0002 a 0008 e 0023 a 0025.
  - Sensibilidade residual de 1 item, se o k3 não se aplicar dentro do banco: BQ-0095 ↔ BQ-0068.
- **Leitura 2.** A canonização do banco é um ato único, com uma de duas datas.

  | Data do ato único | Folhas que mudam | Itens que mudam | Detalhe |
  |---|---|---|---|
  | 09/10 (D-RECUPERACAO) | 3 | 22 | P1-1: entram BQ-0080/81/85/87/91/92 e saem 6A-05 a 10. P1-8.2: entram BQ-0096/97/100/112 e saem 5C-01 e A5-11 a 13. Mais a P1-4.1 |
  | 13/10 (v1.2) | 5 | 38 | Inclui a P2-4.1: entram os 5 diretos L3-Q17 a Q21 e saem BQ-0007, 0008 e 0023 a 0025 |

- **Efeito da escolha:**
  - O campo `nucleo` não muda aptidão a simulado, gabarito, aderência nem `volatil` (contrato v1.2.7, ponto 3).
  - Não está no `pacote.json` e a plataforma v1.7 não o lê.
  - Só muda o que a edição do estudante marca como núcleo, em `NUCLEO.md` e no campo do v1.10-E.
  - Se a Leitura 1 for mantida, nada muda; corrige-se apenas o texto do fundamento (c).
  - Se a Leitura 2 for adotada, o gerador troca o k1 dos BQ para a data única. É uma linha no `nucleo.py`, que entra na v1.11 com contrato v1.2.8 e nova fidelidade. A v1.10 não se reabre.
- **Limite da Presidência:** se ela entender que escolher a data é interpretar a D-REFORCO-2, do Fundador, a matéria vai a PARA_FUNDADOR.md, pelo precedente D-T81-AUDITORIA.

## 4. A-3: L2-R90 "(conta conferida por script)" no estudante: fica para a v1.11

Corrigir agora exigiria três coisas: (a) acrescentar uma deleção à lista fechada da D-V110-09, com errata no contrato (v1.2.8); (b) regenerar o v1.10-E e o `L2_gabarito.md`, o que muda o SHA d8a68156…; (c) refazer a fidelidade. A marca é de processo, não de mérito: não muda gabarito nem conteúdo. Nada vai à candidata antes do sim do Fundador, e a v1.11 virá com a onda 4 (T-98), que já tem fila AGORA. **Decisão:** a deleção entra na lista da v1.11, com contrato v1.2.8. Em paralelo, a GCE pode registrar uma errata de forma na origem (`L2_reforco_onda3_*`, L2-R90). Registrar no escopo da T-12, ocorrência v1.11.

## 5. Estado do aceite

A v1.10 está apta ao gatilho A:
- dados íntegros (560 itens);
- estudante v1.10-E;
- contrato v1.2.7;
- adendo 2;
- edição .md (35 arquivos);
- gerador reproduzível com código 0.

A publicação à candidata é reservada ao Fundador: gatilho E, que substitui a pauta pendente da v1.9 (D-FUNDADOR-RESP-1810, opção A).

Os textos da linha T-104 e dos gatilhos A, D e E foram devolvidos ao orquestrador para PARA_PRESIDENCIA.md e TAREFAS.md.
