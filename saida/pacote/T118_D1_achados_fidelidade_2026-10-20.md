# T118_D1_achados_fidelidade_2026-10-20.md — T-118 — 2026-10-20 — gerado por gbq-gerencia

D1 da GBQ sobre os achados da fidelidade da v1.13 (`saida/pacote/montagem_v1_13/fidelidade_v1_13_T118_gbq-cqe.md`, APROVADO COM RESSALVAS, achados 1 a 8). Ciclo s15c1. Base: a D1 da T-118 (`saida/pacote/T118_D1_v1_13_2026-10-20.md`, seções 4 e 5), o contrato v1.2.10 (pontos 2, 4, 8, 9 e 11), o MANIFESTO (`saida/pacote/montagem_v1_13/MANIFESTO_v1_13.md`, seção 5), a conferência da gcb-cqfp (`saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md`, CONFERIDO) e a cobertura (`saida/pacote/cobertura_v1_13.md`).
Gate: nenhum. Matéria de forma do pacote e do registro, domínio da GBQ; sem conflito entre Gerências. A GBQ não produz nem corrige item. Esta D1 grava só três arquivos: ela mesma, a errata v1.2.11 em `regras/pacote_contrato.md` e o registro `saida/pacote/contrato_v1_2_11_2026-10-20.md`. Nada em `saida/plataforma/`, nada promovido, sem commit.

Conferências próprias (`python3 -I`, só leitura do repositório; ensaios no scratchpad `ger_t118/`, nunca no repositório):
- `chk_md.py` (anexo B): a .md atual tem 197 pares e 405 pegadinhas de DA, linha a linha iguais a `pacote_estudante.json` na forma `- a × b | como` e `- [itemEdital] rotulo — texto`, com 0 `**`. Resultado: 6/6 lotes OK.
- `patch_adendo.py` (anexo C), aplicado a uma cópia do `registro_adendo_v113.py` (dd7d9a0d…2b22) e rodado contra o repositório: deu o script 42b7025b…fa70 e o adendo a1ca1681…7437 (11.582 bytes, 111 linhas). Contra o adendo atual (7224db40…), o diff fica só nas linhas 10, 12, 26, 29–33, 38, 42 e 47–52 e nas linhas 103–111 acrescentadas. As seções 2 e 9 ficam idênticas.
- `scan_q.py` (anexo A): regra de qualificação do ponto 9 da v1.2.10. Dá 21 ids soltos no adendo atual e 0 no ensaiado. Na seção 5 do MANIFESTO dá 14 hoje e 0 no manifesto ensaiado.
- `patch_manifesto.py` (anexo D), aplicado a uma cópia do `manifesto_v1_13.py` (5f92b713…2ac0) e rodado numa cópia de `montagem_v1_13/` já no estado final: deu o script e06115ee…9f53 e "divergências 0", com 71 arquivos listados.
- Os dois patches são reversíveis. Desfeitas as trocas na ordem inversa, voltam os SHA-256 originais (dd7d9a0d e 5f92b713).

## 0. Quadro das decisões

| Achado | Gravidade | Decisão | Quem executa | Bloqueia o aceite? |
|---|---|---|---|---|
| 1 | MÉDIA | **ERRATA v1.2.11 do contrato (caminho (i)).** A .md não é regerada. | gbq-gerencia (feito nesta D1) | Resolvido. Falta a conferência R2-1. |
| 2 | MÉDIA | **CORRIGIR** a faixa de ids da seção 1 do adendo 5, no script, e regerar | gbq-csc (passos 3 e 4) | Sim, até o R2 |
| 3 | BAIXA | **CORRIGIR** junto com o 2: qualificar os ids de lote no adendo e na seção 5 do MANIFESTO | gbq-csc (passos 3, 4 e 6) | Sim, por estar no mesmo arquivo do achado 2 |
| 4 | BAIXA | **ACRESCENTAR** a seção 10 ao adendo 5 (registros de formato e errata do achado 10) | gbq-csc (passos 3 e 4) | Não, mas entra na mesma regeração |
| 5 | BAIXA (processo) | **SAI de saida/gbq/.** A cópia antecipada é movida (não apagada) para `montagem_v1_13/historico/`, e o adendo fica só em `out/` até a promoção | gbq-csc (passo 2) | Não |
| 6 | INFO | **ATUALIZAR** o MANIFESTO pelo script, com a pasta inteira e as entradas novas | gbq-csc (passos 5 e 6) | Não |
| 7 | INFO | **SEM AÇÃO.** As mudanças em DECISOES.md, TAREFAS.md e PARA_PRESIDENCIA.md são da abertura do ciclo, fora da T-118. As linhas dos atos (93, 117, 162–165) estão intactas | — | Não |
| 8 | INFO | **SEM AÇÃO NOVA.** A divergência já está registrada (D1 da T-118, seções 2 e 3): a v16 publicada embute 007787e3, e a T-123 embute o canônico | orquestrador e desenvolvedor-plataforma, na T-123 | Não |

Depois do R2 ACEITO, sigo para a reconciliação e o gatilho A (D1 da T-118, passo 4.6), com a errata v1.2.11 registrada para a Presidência.

## 1. Fundamentos por achado

### Achado 1: edição .md × ponto 8 da v1.2.10

**Decisão: (i), errata v1.2.11.** Gravada em `regras/pacote_contrato.md`, que passou de 2626a946…28c1 para 85b30fcc…616b, com 72.183 bytes e 325 linhas LF. O registro está em `saida/pacote/contrato_v1_2_11_2026-10-20.md`. A errata substitui o último subitem do ponto 8 e fixa duas formas de linha para DA, `- a × b | como` e `- [itemEdital] rotulo — texto`, com conferência contra o pacote. Os lotes L1 a L6B não mudam.

Fundamentos:
1. **A coerência do conjunto pede a errata, não a regeração.** O ponto 4 da v1.2.10 já tira `**` dos textos de `pares` e `pegadinhas` de DA. Com a errata, o mesmo texto sai igual no pacote, na plataforma e na .md. Regerar no formato do ponto 8 poria negrito na .md e só nos pares, e as pegadinhas ficariam sem regra. O ponto 8 foi escrito quando a .md não seria gerada na v1.13, e a D1 da T-118, posterior, mandou gerá-la sem `**`. A errata alinha o texto mais antigo ao mais novo, que é o já executado.
2. **A conferência do ponto 2 da v1.2.2 não serve para DA.** Ela compara a linha da .md com a linha do canônico "sem '- ' e sem '**'". Em DA isso não fecha, porque o `como` junta duas colunas do canônico com a frase fixa "Como a banca troca:" (ponto 4 da v1.2.10). Para DA, a conferência certa é contra o pacote, e o pacote se confere contra o canônico pelo registro de formato (ponto 2 da v1.2.10). A errata fixa isso.
3. **O risco é menor.** A errata não muda nenhum byte de `out/`. Os 53 arquivos já passaram pela fidelidade: 410/410 itens, 41 ids na amostra e 78 visuais. Regerar exigiria mudar o `estudante_md_v113.py`, refazer a .md e repetir a fidelidade dos 18 arquivos DA.
4. **Fica uma assimetria aceita.** Na .md, os pares dos L4 a L6B têm negrito e os de DA não. É diferença de exibição, sem efeito no conteúdo, e a errata a registra (ponto 4).

### Achado 2: faixa de ids na seção 1 do adendo 5

**Decisão: CORRIGIR por script.** A causa está na linha 106 do `registro_adendo_v113.py`: a faixa usa o primeiro e o último id na ordem de apresentação do canônico (`list(canon[n])`), e em D3 e D5 essa ordem não é a numérica (MANIFESTO, obs. 3). Por isso o último id saía igual ao n. A correção:
- calcula a faixa pela ordem numérica;
- confere, por asserção, que a faixa menos os vagos da seção 4 dá exatamente os ids do lote;
- escreve "(sem o vago da seção 4)" no singular para o lote D5.

Valores esperados: lote D3, "D3-01 a D3-81 (sem os vagos da seção 4)"; lote D5, "D5-01 a D5-71 (sem o vago da seção 4)". Os demais lotes não mudam. Este achado bloqueia a condição (c) do gatilho A.

### Achado 3: ids de lote sem qualificação

**Decisão: CORRIGIR** no adendo 5 e, para manter o conjunto coerente, também na seção 5 do MANIFESTO (obs. 3, 4, 5 e 8), que é relatório da fábrica (ponto 9 da v1.2.10).

A regra verificável é o `scan_q.py` (anexo A). A primeira célula das tabelas fica isenta, porque a coluna "Lote" já qualifica. "D1" também fica isento quando é a decisão de Gerência ("D1 da GBQ", "a D1", "D1 própria"). Ids de item (`D<n>-NN`), nomes de arquivo e atos (`D-LOTED<n>-…`) ficam fora da regra.

### Achado 4: remissão aos registros de formato

**Decisão: ACRESCENTAR** ao adendo 5 a seção "## 10. Registros de formato", no fim, sem renumerar as seções 1 a 9. Ela traz:
- os seis `D<n>_registro_formato.md` com o SHA-256;
- uma linha sobre a errata do achado 10, com remissão ao parecer da gcb-cqfp.

O script confere o SHA-256 do registro do lote D6 contra o valor conferido pela gcb-cqfp (7998cc7b…90ca). É o papel da seção 7 do adendo 4 ("Erratas e URL"), que para DA o ponto 2 da v1.2.10 dá ao registro de formato.

### Achado 5: cópia antecipada em saida/gbq/

**Decisão: o adendo volta a ficar só em `out/` até a promoção.** A cópia de `saida/gbq/` é **movida** (`mv`, sem apagar) para `saida/pacote/montagem_v1_13/historico/registro_adendo5_R1_7224db40.md`. Não fica em `saida/gbq/` marcada "PENDENTE DE ACEITE".

Fundamentos:
1. **A rotina manda.** A D1 da T-118 (passo 4.6) diz que a promoção a `saida/gbq/` é byte a byte, depois do aceite e em ato separado do orquestrador. Uma cópia com a marca "PENDENTE DE ACEITE" teria bytes diferentes de `out/registro_adendo5.md`. Isso criaria um terceiro texto e quebraria o "byte a byte".
2. **A cópia pode ser lida como vigente.** `saida/gbq/` é onde fica o registro GBQ vigente (contrato, regra 4 da v1.1, e ponto 2 da v1.2.10: "v3 + adendos 1 a 4 + adendo 5"). Um adendo não aceito ali pode ser tomado por vigente por quem lê a pasta.
3. **Mover preserva a versão R1.** A R2 da gbq-cqe precisa dela para o diff. Também não se apaga nada: o arquivo não está em git, e o mesmo conteúdo some de `out/` quando o adendo for regerado.

### Achado 6: manifesto incompleto

**Decisão: ATUALIZAR** pelo `manifesto_v1_13.py` corrigido (anexo D). O manifesto passa a:
- listar a pasta inteira (71 arquivos, entre eles `cobertura_v1_13.py`, `fidelidade_v1_13_T118_gbq-cqe.md` e `historico/`);
- não listar nada de `saida/gbq/`, e falhar se o adendo estiver lá;
- conferir na seção 1 os SHA-256 do adendo novo, da versão R1 e do contrato v1.2.11;
- trazer na seção 4 os seis registros de formato e o contrato;
- citar a v1.2.11 na obs. 6 e ganhar a obs. 10.

Regra para não repetir o achado: depois do manifesto, nenhum agente grava em `montagem_v1_13/`. O relatório da R2 vai para `saida/pacote/`, fora da pasta.

### Achados 7 e 8: INFO

Sem ação. Os fundamentos estão no quadro da seção 0 e na D1 da T-118, seções 2 e 3.

## 2. Instruções à gbq-csc (sonnet), em ordem

Todo script roda com `python3 -I`, a partir de `saida/pacote/montagem_v1_13/`. Os anexos A a D são extraídos para o scratchpad, nunca para o repositório. Antes de usar cada anexo, confira o SHA-256 do arquivo extraído: o conteúdo é o do bloco de código, com `\n` no fim.

Não altere nada além do indicado. Ficam intocados:
- `out/pacote.json`, `out/pacote_estudante.json`, `out/stats_v1_13_DA.json`, `out/conferencia_t118.json`, `out/diag30_DA.json`, `out/estudante_md_v1_13.json` e `out/estudante/`;
- `montar_v1_13.py`, `conferir_t118.py`, `estudante_md_v113.py`, `cobertura_v1_13.py` e `diag30_da.py`;
- `regras/`, `saida/gbq/` (salvo o passo 2), `saida/gcb/`, `saida/estudante/` e `saida/plataforma/`;
- DECISOES.md e TAREFAS.md.

Sem commit. Se algum valor esperado divergir, pare e devolva à gbq-gerencia o passo, o esperado e o obtido, sem ajustar nada.

**Passo 1. Pré-condições.** Confira o SHA-256 de cada arquivo:

| Arquivo | SHA-256 esperado |
|---|---|
| `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md` | `7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918` |
| `out/registro_adendo5.md` | o mesmo |
| `registro_adendo_v113.py` | `dd7d9a0d47b0f9d9b98d6a9202cd8edf02cf76bbe9247a16fa2a7e3016652b22` |
| `manifesto_v1_13.py` | `5f92b713ac4616ed9a022992f93f32f9f861c6aed67eca22eccb8ecd14542ac0` |
| `regras/pacote_contrato.md` | `85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b` |
| `saida/gcb/DA_plataforma/D6_registro_formato.md` | `7998cc7be19676125ba13bdcc7f52537012488371ec8e1f9e01aa916b09890ca` |

**Passo 2 (achado 5).** Crie `saida/pacote/montagem_v1_13/historico/` e **mova** o arquivo:
- de `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md`;
- para `saida/pacote/montagem_v1_13/historico/registro_adendo5_R1_7224db40.md`.

Use `mv`, não `rm`. Aceite:
- o destino tem o SHA-256 7224db40…5918 e 10.245 bytes;
- o caminho de origem não existe mais;
- os demais arquivos de `saida/gbq/` mantêm o SHA-256.

**Passo 3 (achados 2, 3 e 4).** Rode `python3 -I <scratch>/patch_adendo.py registro_adendo_v113.py registro_adendo_v113.py`. O anexo C faz 13 trocas, cada uma com âncora única. Aceite:
- a saída "OK 13 trocas";
- `registro_adendo_v113.py` com o SHA-256 `42b7025ba268cd0b6040328f6ac28997a596d06d60be073079a2d1ef3255fa70`.

**Passo 4.** Rode `python3 -I registro_adendo_v113.py`. Aceite:
- exit 0, com a linha "registro_adendo5.md: 111 linhas; 410 itens; VOLÁTEIS 5; PARCIAIS 0; SHA-256 a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437";
- `out/registro_adendo5.md` com 11.582 bytes, LF;
- `python3 -I <scratch>/scan_q.py out/registro_adendo5.md` com a saída "NAO_QUALIFICADOS 0" e exit 0;
- a linha 10 contém "| D3-01 a D3-81 (sem os vagos da seção 4) | 71 |", e a linha 12 contém "| D5-01 a D5-71 (sem o vago da seção 4) | 70 |".

**Passo 5 (achados 3 e 6).** Rode `python3 -I <scratch>/patch_manifesto.py manifesto_v1_13.py manifesto_v1_13.py`, com o anexo D, que faz 10 trocas. Aceite:
- a saída "OK 10 trocas";
- `manifesto_v1_13.py` com o SHA-256 `e06115ee417d1d0e07d973822d36a74822fefea3ffc3b52e6f1a24aa2dbb9f53`.

**Passo 6.** Rode `python3 -I manifesto_v1_13.py` por **último**: depois dele, ninguém grava em `montagem_v1_13/`. Aceite:
- exit 0, com "71 arquivos listados; divergências 0";
- na seção 1, todas as linhas OK, entre elas as três novas (adendo a1ca1681…, R1 7224db40… e contrato 85b30fcc…);
- a linha "Total: 71 arquivos em montagem_v1_13/ (dos quais 53 em out/estudante/). Nenhum arquivo fora desta pasta: …";
- `python3 -I <scratch>/scan_q.py MANIFESTO_v1_13.md <n>`, em que `<n>` é o número da linha "## 5. Divergências e observações …", com a saída "NAO_QUALIFICADOS 0".

Valor de referência do ensaio: 19.621 bytes, SHA-256 8675960…f4f8. Ele só se repete se DECISOES.md e a pasta não mudarem até a execução. Por isso não é critério de aceite.

**Passo 7. Devolução** à gbq-gerencia, em até 10 linhas: o SHA-256 obtido em cada passo e os do manifesto, de `out/registro_adendo5.md` e de `historico/registro_adendo5_R1_7224db40.md`. Também a confirmação, por `git status`, de que nada mudou fora de `montagem_v1_13/`, salvo a remoção do adendo de `saida/gbq/`.

## 3. O que a gbq-cqe confere na R2 (só o que mudou; scripts próprios)

Saída: `saida/pacote/fidelidade_v1_13_T118_R2_gbq-cqe.md`, **fora** de `montagem_v1_13/`, com veredito ACEITO ou DEVOLVIDO por critério. A R2 não repete as conferências A, B, D, de contagens nem a amostra da .md, que a R1 já aprovou e que não mudaram (critério R2-7).

**R2-1. Contrato v1.2.11 (achado 1).**
- `regras/pacote_contrato.md` tem o SHA-256 85b30fcc…616b, 72.183 bytes, 325 linhas, sem CR.
- Contra o blob de HEAD (2626a946…28c1), os opcodes são exatamente `replace 0–1`, `replace 2–3` e `insert 306–306 → 306–320`.
- A seção inserida e a frase da linha 3 são iguais à seção 4 de `saida/pacote/contrato_v1_2_11_2026-10-20.md`.
- Mérito, por leitura: a errata só mexe na .md de DA; não contradiz os pontos 2, 4 e 9 da v1.2.10 nem o ponto 2 da v1.2.2 para L1 a L6B; e não muda campo, `versao` nem os pacotes.

**R2-2. .md contra a v1.2.11.**
- Os 53 arquivos de `out/estudante/` não mudaram: o digest das linhas "caminho TAB sha256", ordenadas por caminho relativo a `out/`, é c6ecc6e5…29a9.
- Por implementação própria do ponto 2 da v1.2.11: 197 pares e 405 pegadinhas, linha a linha iguais ao `pacote_estudante.json`, e 0 `**` nas duas seções dos seis `DA_D<n>_estudo.md`.

**R2-3. Adendo 5 regerado (achados 2, 3 e 4).**
- `out/registro_adendo5.md` tem o SHA-256 a1ca1681…7437.
- O diff contra `historico/registro_adendo5_R1_7224db40.md` fica só nas linhas 10, 12, 26, 29–33, 38, 42 e 47–52 e nas linhas 103–111 acrescentadas. Fora delas, os textos são iguais, e as seções 2 e 9 são iguais byte a byte.
- Seção 1: para cada lote, a faixa é o menor e o maior id numérico dos itens do lote no pacote, e o intervalo menos os vagos da seção 4 dá exatamente os ids do pacote. O lote D5 leva o singular "sem o vago".
- Qualificação: nenhum id de lote solto, pela regra do anexo A refeita por script próprio. A regra pode ficar mais estrita, nunca mais frouxa.
- Seção 10: os seis SHA-256 batem com o disco, e a do lote D6 é 7998cc7b…90ca. A remissão aponta para arquivos que existem. Não há enunciado.

**R2-4. Scripts alterados.** Desfeitas as trocas dos anexos C e D na ordem inversa, `registro_adendo_v113.py` e `manifesto_v1_13.py` voltam a dd7d9a0d… e 5f92b713…. Isso prova que só mudaram as trocas listadas.

**R2-5. Achado 5.**
- O adendo não existe mais em `saida/gbq/`, e o restante da pasta está igual a HEAD (`git status`).
- `historico/registro_adendo5_R1_7224db40.md` tem o SHA-256 7224db40…5918.
- Nada foi promovido: `saida/pacote/pacote*.json`, `saida/estudante/` e `saida/gbq/` não têm arquivo novo.

**R2-6. MANIFESTO (achados 3 e 6).**
- A seção 3 lista exatamente os arquivos de `montagem_v1_13/` (recursivo, sem o próprio manifesto e sem `__pycache__`), com bytes e SHA-256 iguais ao disco, e nada fora da pasta.
- A seção 1 está toda OK, com as três linhas novas.
- A seção 4 tem os seis registros de formato e o contrato.
- A obs. 6 cita a v1.2.11, e a obs. 10 descreve as correções.
- A seção 5 passa na regra de qualificação.

**R2-7. Integridade.** Os SHA-256 continuam iguais aos da R1:

| Arquivo | SHA-256 |
|---|---|
| out/pacote.json | 82c4117c…f240 |
| out/pacote_estudante.json | 04cbd593…0c40 |
| out/stats_v1_13_DA.json | f077cb33…7320 |
| out/conferencia_t118.json | 6c5250c9…844f |
| out/diag30_DA.json | eb1ced6d…6800 |
| out/estudante_md_v1_13.json | ad7374dd…f5fa |
| montar_v1_13.py | 723370f5…1ebe |
| conferir_t118.py | 3fa09b7d…0768 |
| estudante_md_v113.py | 54faa3bf…c976 |
| cobertura_v1_13.py | 72a89f86…5312 |

Também não mudaram:
- os seis `D<n>_plataforma.json` e os seis `D<n>_registro_formato.md`;
- `edital_DA.json`;
- `saida/plataforma/` (4d19eb05… e c6de3f2a…).

**Veredito.** ACEITO quando R2-1 a R2-7 estão OK. Com ACEITO, a gbq-gerencia faz a reconciliação e o gatilho A (D1 da T-118, passo 4.6). A promoção, depois, é feita pelo orquestrador:
- `out/registro_adendo5.md` (a1ca1681…) vai para `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md`;
- os dois pacotes vão para `saida/pacote/`;
- `out/estudante/` vai para `saida/estudante/`.

## Anexos (scripts; o conteúdo é o do bloco, com `\n` final)

### Anexo A — `scan_q.py` (SHA-256 `e82a2e9b84d69e7023c158ca68f2644db8b75dc25b96f56e3cec9e2e9aee36dd`): regra de qualificação de id de lote (achado 3; contrato v1.2.10, ponto 9)

```python
# scan_q.py — regra Q (achado 3 da fidelidade T-118; contrato v1.2.10, ponto 9). Uso: python3 -I scan_q.py <arquivo> [<linha_inicial>]
# Id de lote solto = D[1-6] não precedido de letra, dígito, "_", "/", "-" ou "[" e não seguido de letra, dígito, "_" ou "-".
# Válido se: (a) precedido de "lote ", "lotes ", "discursiva " ou "discursivas ", admitida a enumeração "D<i>, D<j> e D<k>" / "D<i> a D<j>";
# (b) for a primeira célula de linha de tabela (coluna "Lote"), exatamente " D<n> ";
# (c) só para "D1" (decisão de Gerência, não lote): precedido de "a ", "A ", "da ", "na ", "pela ", "por ", "à " ou "(", ou seguido de " da GBQ", " da T-" ou " própria".
import re, sys
t = open(sys.argv[1], encoding='utf-8').read().split('\n')
ini = int(sys.argv[2]) if len(sys.argv) > 2 else 1
pat = re.compile(r'(?<![\w/\[-])D[1-6](?![\w-])')
ok = re.compile(r'(?:lote|lotes|discursiva|discursivas) (?:D[1-6](?:, | e | a ))*$')
dec_pre = re.compile(r'(?:^|[\s(])(?:a|A|da|na|pela|por|à) $|\($')
bad = 0
for i, l in enumerate(t, 1):
    if i < ini: continue
    s = l
    if l.startswith('|'):
        c = l.split('|')
        if len(c) > 2 and re.fullmatch(r' D[1-6] ', c[1]): s = ' ' * (len(c[1]) + 1) + '|'.join(c[2:])
    for m in pat.finditer(s):
        pre = s[:m.start()]
        if ok.search(pre): continue
        if m.group() == 'D1' and (dec_pre.search(pre) or re.match(r' (da GBQ|da T-|própria)', s[m.end():])): continue
        bad += 1; print(i, repr(s[max(0, m.start() - 30):m.end() + 15]))
print('NAO_QUALIFICADOS', bad)
sys.exit(1 if bad else 0)
```

### Anexo B — `chk_md.py` (SHA-256 `1ae66134473c70d7a9677a18fdb46e1e54daa9482f274d7e0461935ebb56054b`): conferência do ponto 2 da v1.2.11 na .md (uso: python3 -I chk_md.py <caminho de montagem_v1_13>)

```python
import json,sys,re,pathlib
B=pathlib.Path(sys.argv[1]); E=B/'out/estudante'
p=json.loads((B/'out/pacote_estudante.json').read_text(encoding='utf-8'))
lot={l['id']:l for l in p['lotes']}
tot=0;bad=0
for n in range(1,7):
    L=(E/('DA_D%d_estudo.md'%n)).read_text(encoding='utf-8').split('\n')
    def sec(h):
        i=L.index(h); j=next((k for k in range(i+1,len(L)) if L[k].startswith('## ')),len(L))
        return [x for x in L[i+1:j] if x.strip()]
    pa=sec('## Pares'); pe=sec('## Pegadinhas')
    ep=['- %s × %s | %s'%(x['a'],x['b'],x['como']) for x in lot['D%d'%n]['pares']]
    eg=['- [%s] %s — %s'%(x['itemEdital'],x['rotulo'],x['texto']) for x in lot['D%d'%n]['pegadinhas']]
    s=sum('**' in x for x in pa+pe)
    ok=(pa==ep and pe==eg and s==0)
    print('lote D%d pares %d/%d pegadinhas %d/%d ** %d %s'%(n,len(pa),len(ep),len(pe),len(eg),s,'OK' if ok else 'FALHA'))
    tot+=len(pa); bad+= (not ok)
print('pares',tot,'FALHAS',bad)
```

### Anexo C — `patch_adendo.py` (SHA-256 `9d0db657cd5dd18f6f2a61fd164612bfff6a1bfa969d7c85024cc8d5d6b4ebdd`): 13 trocas no registro_adendo_v113.py (achados 2, 3 e 4)

```python
# Patch do achado 2/3/4 (fidelidade T-118) sobre registro_adendo_v113.py; uso: python3 -I patch_adendo.py <entrada> <saída>
import sys
src=open(sys.argv[1],encoding='utf-8').read()
P=[
("        ids = list(canon[n]); nome = 'D%d' % n\n        faixa = '%s a %s' % (ids[0], ids[-1]) if not (n == 3 or n == 5) else '%s a %s (sem os vagos da seção 4)' % (ids[0], ids[-1])\n",
 "        ids = list(canon[n]); nome = 'D%d' % n\n        num = sorted(ids, key=lambda x: int(x[3:]))      # faixa pela ordem numérica do id (achado 2 da fidelidade T-118)\n        vg = [x for x in VAGOS if x.startswith('D%d-' % n)]\n        if num[0] != 'D%d-01' % n or [x for x in ('D%d-%02d' % (n, k) for k in range(1, int(num[-1][3:]) + 1)) if x not in ids] != vg: falha('faixa do lote D%d não fecha com os vagos' % n)\n        faixa = '%s a %s' % (num[0], num[-1]) + ('' if not vg else ' (sem o vago da seção 4)' if len(vg) == 1 else ' (sem os vagos da seção 4)')\n"),
("(D2), D6-09, D6-32 e D6-34 (D6);", "(lote D2), D6-09, D6-32 e D6-34 (lote D6);"),
("w('- D%d: %s.' % (n, '; '.join(", "w('- lote D%d: %s.' % (n, '; '.join("),
("w('- D1 e D6: o canônico", "w('- lotes D1 e D6: o canônico"),
("w('- D1, D2, D4 e D6: numeração contínua (D1-01 a D1-60; D2-01 a D2-80; D4-01 a D4-79; D6-01 a D6-50). D3: D3-01 a D3-81, com 10 vagos (71 itens). D5: D5-01 a D5-71, com 1 vago (70 itens).')",
 "w('- Numeração contínua nos lotes D1, D2, D4 e D6 (D1-01 a D1-60; D2-01 a D2-80; D4-01 a D4-79; D6-01 a D6-50). No lote D3: D3-01 a D3-81, com 10 vagos (71 itens). No lote D5: D5-01 a D5-71, com 1 vago (70 itens).')"),
("no canônico do D6 (D-LOTED6-CANONICO)", "no canônico do lote D6 (D-LOTED6-CANONICO)"),
("w('- D1: saida/gcb/T73", "w('- lote D1: saida/gcb/T73"),
("w('- D2: saida/gcb/T75", "w('- lote D2: saida/gcb/T75"),
("w('- D3: saida/gcb/T76", "w('- lote D3: saida/gcb/T76"),
("w('- D4: saida/gcb/T77", "w('- lote D4: saida/gcb/T77"),
("w('- D5: D1 da T-74", "w('- lote D5: D1 da T-74"),
("w('- D6: saida/gcb/T101", "w('- lote D6: saida/gcb/T101"),
("    if tot_f != 410: falha('itens por folha somam %d' % tot_f)\n",
 "    if tot_f != 410: falha('itens por folha somam %d' % tot_f)\n"
 "    w('')\n"
 "    w('## 10. Registros de formato (para DA, fazem o papel do registro de alterações por id; contrato v1.2.10, ponto 2)')\n"
 "    for n in CANON:\n"
 "        rf = sha((DA / ('D%d_registro_formato.md' % n)).read_bytes())\n"
 "        if n == 6 and rf != '7998cc7be19676125ba13bdcc7f52537012488371ec8e1f9e01aa916b09890ca': falha('registro de formato do lote D6 difere do conferido pela gcb-cqfp')\n"
 "        w('- lote D%d: saida/gcb/DA_plataforma/D%d_registro_formato.md (SHA-256 %s)' % (n, n, rf))\n"
 "    w('- Errata de forma do achado 10 (T-118): lote D6, par 0, campo `como`, deleção de negrito; registrada na seção \"Errata de forma — T-118 (achado 10), 20/10/2026\" do registro de formato do lote D6 e conferida pela gcb-cqfp (saida/gcb/QA_D6_achado10_conferencia_2026-10-20_gcb-cqfp.md). Nenhum id, enunciado ou gabarito mudou.')\n"),
]
for o,n in P:
    c=src.count(o)
    if c!=1: print('ANCORA',c,repr(o[:60])); sys.exit(1)
    src=src.replace(o,n)
open(sys.argv[2],'w',encoding='utf-8',newline='\n').write(src)
print('OK', len(P), 'trocas')
```

### Anexo D — `patch_manifesto.py` (SHA-256 `6560b93aaca5704ba24b60adf3f68f5a468fae64309bc121c9f287602fcb30d5`): 10 trocas no manifesto_v1_13.py (achados 3, 5 e 6 e errata v1.2.11)

```python
# Patch dos achados 3 (parte do manifesto), 5 e 6 e da errata v1.2.11 sobre manifesto_v1_13.py; uso: python3 -I patch_manifesto.py <entrada> <saída>
import sys
src=open(sys.argv[1],encoding='utf-8').read()
P=[
("extra = [R / 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md']\n",
 "extra = []\nif (R / 'saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo5_2026-10-20.md').exists(): print('FALHA: adendo 5 em saida/gbq/ antes do aceite (achado 5)'); sys.exit(1)\n"),
("    ('out/diag30_DA.json (intocado)', 'eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800', sha((HERE / 'out/diag30_DA.json').read_bytes()), 'D1, 4.3.1'),\n",
 "    ('out/diag30_DA.json (intocado)', 'eb1ced6df3d624ae62b82337db6a4cfe29b86baa9494e96aed1b3defe61a6800', sha((HERE / 'out/diag30_DA.json').read_bytes()), 'D1, 4.3.1'),\n"
 "    ('out/registro_adendo5.md (regerado, achados 2 a 4)', 'a1ca16811394dd6ec5df186b44155704a498bc03f6ac1e8cddaf87b6f7a87437', sha((HERE / 'out/registro_adendo5.md').read_bytes()), 'D1 achados, 2'),\n"
 "    ('historico/registro_adendo5_R1_7224db40.md (versão anterior, achado 5)', '7224db40670608bff726f67b6b4769a509b225953146b80013b05d9c57f55918', sha((HERE / 'historico/registro_adendo5_R1_7224db40.md').read_bytes()), 'D1 achados, 5'),\n"
 "    ('regras/pacote_contrato.md (v1.2.11)', '85b30fccadce4eb9782e1e056613a2d680cec0c01aed44fd173bda7d248e616b', sha((R / 'regras/pacote_contrato.md').read_bytes()), 'D1 achados, 1'),\n"),
("w('Total: %d arquivos em montagem_v1_13/ (dos quais %d em out/estudante/) mais o adendo 5 em saida/gbq/ (byte a byte igual a out/registro_adendo5.md).' % (",
 "w('Total: %d arquivos em montagem_v1_13/ (dos quais %d em out/estudante/). Nenhum arquivo fora desta pasta: o adendo 5 fica só em out/ até a promoção (achado 5 da fidelidade T-118).' % ("),
("R / 'saida/gcb/DA_plataforma/D6_registro_formato.md', R / 'DECISOES.md'):",
 "R / 'saida/gcb/DA_plataforma/D1_registro_formato.md', R / 'saida/gcb/DA_plataforma/D2_registro_formato.md', R / 'saida/gcb/DA_plataforma/D3_registro_formato.md', R / 'saida/gcb/DA_plataforma/D4_registro_formato.md', R / 'saida/gcb/DA_plataforma/D5_registro_formato.md', R / 'saida/gcb/DA_plataforma/D6_registro_formato.md', R / 'DECISOES.md', R / 'regras/pacote_contrato.md'):"),
("w('3. Ordem de apresentação do canônico: em D3 e D5 a ordem",
 "w('3. Ordem de apresentação do canônico: nos lotes D3 e D5 a ordem"),
("o canônico de D1 e de D6 não traz o campo \"Formato\" por item (só \"Mecanismo\"); o adendo traz os códigos de D2 a D5 (código de 3 letras, T75_reconciliacao, 5.5) e declara D1 e D6 como não classificados.",
 "o canônico dos lotes D1 e D6 não traz o campo \"Formato\" por item (só \"Mecanismo\"); o adendo traz os códigos dos lotes D2 a D5 (código de 3 letras, T75_reconciliacao, 5.5) e declara os lotes D1 e D6 como não classificados."),
("e às reconciliações de D1 e D6. Para D5 o adendo remete a T74_reconciliacao_2026-10-20.md (seções 2 e 5.5); para D1, a T73_reconciliacao_2026-10-17.md (seções 2 e 4); para D6, a T101_reconciliacao",
 "e às reconciliações dos lotes D1 e D6. Para o lote D5 o adendo remete a T74_reconciliacao_2026-10-20.md (seções 2 e 5.5); para o lote D1, a T73_reconciliacao_2026-10-17.md (seções 2 e 4); para o lote D6, a T101_reconciliacao"),
("NUCLEO.md: ordem das linhas pela ordem do edital; as linhas anteriores ficaram idênticas.')\n",
 "NUCLEO.md: ordem das linhas pela ordem do edital; as linhas anteriores ficaram idênticas. Forma admitida pela errata v1.2.11 do contrato (saida/pacote/contrato_v1_2_11_2026-10-20.md), que substitui o último subitem do ponto 8 da v1.2.10 (achado 1 da fidelidade T-118).')\n"),
("mudou só no `sha_json` do D6.", "mudou só no `sha_json` do lote D6."),
("promoção byte a byte e publicação só depois do aceite e do \"sim\" do Fundador.')\n",
 "promoção byte a byte e publicação só depois do aceite e do \"sim\" do Fundador.')\n"
 "w('10. Correções pós-fidelidade (D1 da GBQ, saida/pacote/T118_D1_achados_fidelidade_2026-10-20.md): registro_adendo_v113.py corrigido (achados 2, 3 e 4) e out/registro_adendo5.md regerado; a cópia antecipada do adendo em saida/gbq/ (7224db40…) foi movida para historico/registro_adendo5_R1_7224db40.md, sem promoção (achado 5); este manifesto passou a listar todos os arquivos da pasta, inclusive cobertura_v1_13.py e fidelidade_v1_13_T118_gbq-cqe.md (achado 6). out/pacote.json, out/pacote_estudante.json, out/stats_v1_13_DA.json, out/conferencia_t118.json, out/diag30_DA.json, out/estudante_md_v1_13.json e os 53 arquivos de out/estudante/ não mudaram.')\n"),
]
for o,n in P:
    c=src.count(o)
    if c!=1: print('ANCORA',c,repr(o[:70])); sys.exit(1)
    src=src.replace(o,n)
open(sys.argv[2],'w',encoding='utf-8',newline='\n').write(src)
print('OK',len(P),'trocas')
```
