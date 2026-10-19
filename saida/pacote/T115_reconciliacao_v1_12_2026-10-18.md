# T115_reconciliacao_v1_12_2026-10-18.md — T-115 — reconciliação do pacote v1.12 após a fidelidade — 2026-10-18 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (D1).
DESTINATÁRIO: gbq-csc (correção e regeneração, seção 2); orquestrador (fim de linha, commit e clones, seção 4; promoção, seção 7); presidencia (gatilho A em PARA_PRESIDENCIA.md, seção 8).
Base: fidelidade `saida/pacote/fidelidade_v1_12_gbq-cqe.md` (gbq-cqe, opus, R1: ACEITO COM RESSALVAS); D1 `saida/pacote/T115_D1_v1_12_2026-10-18.md`; `saida/pacote/gerador_v1_12/MANIFESTO.md` e `out/` da rodada 1. Para a conferência da seção 3, copiei a rodada 1 de `out/`, sem mudar nada, para `C:/Users/Felipe/AppData/Local/Temp/t115/out_r1/`; o script confere o SHA de cada arquivo dessa cópia antes de usá-la. Gravei: este arquivo, `saida/pacote/T115_conferencia_correcao.py` e o gatilho A em PARA_PRESIDENCIA.md. Não editei DECISOES.md, estados de TAREFAS.md, o gerador nem `out/`. Sem commit.

## 1. Decisão (D1)

O conteúdo dos JSON está aceito pela fidelidade. A gbq-cqe reconstruiu de forma independente e chegou ao mesmo resultado, campo a campo: os 189 itens, as 73 pegadinhas e os 40 `topicos`. A reversão à v1.11 é byte a byte, e as contagens batem. Não há segunda rodada da gbq-cqe, porque nenhum achado muda dado do `pacote.json` nem do `pacote_estudante.json`. O que muda é a edição .md (achados 1 e 2) e a reprodutibilidade do gerador (achado 3); os dois se fecham por regeneração e por conferência minha, com script. A GBQ emite o gatilho A da v1.12 como canônica, **condicionado** às seções 2 a 4. Nada é promovido antes disso.

| Achado | Disposição |
|---|---|
| 1. Linha 1 dos 7 `_estudo.md` com o nome antigo do lote | CORRIGIR antes de promover (seção 2, passo 2; conferência na seção 3) |
| 2. 6 linhas "Mecanismo" em 5 `_gabarito.md` | Arbitrado: leitura (b), retirar (seção 2, passo 3) |
| 3. Fim de linha do gerador (MANIFESTO e M-o) | Gerador todo em LF e `.gitattributes` com `eol=lf`; `out/` com `-text` (seções 2 e 4) |
| 4. 6 entradas X | CONFIRMADAS as 6 (seção 5) |
| 5 a 7 | Registro (seção 6) |

## 2. Instrução exata à gbq-csc (correção do gerador_v1_12 e regeneração)

> gbq-csc: corrija o `saida/pacote/gerador_v1_12/` e regere, sem mudar nenhum dado do `pacote.json`, do `pacote_estudante.json`, do adendo 4 nem do registro de alterações.
> 1. **Fim de linha (achado 3).** Converta para LF (`\r\n` → `\n`, sem outra mudança) todos os arquivos de `saida/pacote/gerador_v1_12/`, exceto os de `out/` e `__pycache__/`. Por exemplo (Git Bash, raiz do repositório): `python -I -B - <<'EOF'` / `import os` / `for r, d, f in os.walk('saida/pacote/gerador_v1_12'):` / `    d[:] = [x for x in d if x not in ('out', '__pycache__')]` / `    for n in f:` / `        p = os.path.join(r, n); b = open(p, 'rb').read()` / `        if b'
' in b: open(p, 'wb').write(b.replace(b'
', b'
'))` / `EOF` (uma linha por barra), ou equivalente. Depois disso, nenhum arquivo fora de `out/` pode ter o byte CR. Não toque no gerador_v1_11.
>    - `manifesto_v1_12.py`: a coluna "Frente ao gerador_v1_11" compara o conteúdo LF dos dois lados (`bytes.replace(b'\r\n', b'\n')`), e a tabela "Arquivos da pasta" passa a ter os SHA e bytes do disco (agora LF, iguais ao blob depois do commit).
>    - `fidelidade_mutacao_v112.py`, caso (M-o): a mutação é feita sobre o conteúdo LF do insumo, numa cópia temporária fora do repositório e com posição fixa. O SHA que o caso imprime passa a ser o do conteúdo LF mutado, igual em qualquer checkout.
> 2. **Cabeçalho dos `_estudo.md` (achado 1).** Em `estudante_md_v112.py`, ache o passo que desfaz a troca do passo (1) nos `_estudo.md`: a saída da rodada 1 mantém o nome antigo na linha 1, embora o passo (1) conte uma ocorrência e a troque. O provável é que um passo posterior remonte o arquivo a partir da base v1.11. Corrija para que a linha 1 de `L1`, `L2`, `L3`, `L4`, `L5`, `L6A` e `L6B` `_estudo.md` seja `# ` seguido do `nome` do lote no `pacote_estudante.json` (seção 3.8 da D1). Nenhuma outra linha desses arquivos muda.
> 3. **Legendas de mecanismo (achado 2; decisão da GBQ, seção 1).** Em `estudante_md_v112.py`, retire de `L4_gabarito.md`, `L5_gabarito.md`, `L6A_gabarito.md` e `L6B_gabarito.md` a linha 3 ("Mecanismo: …" / "Mecanismos: …") e a linha em branco que vem logo depois dela. Em `SIM-1_gabarito.md`, retire as linhas 6 e 8 (as duas legendas), cada uma com a linha em branco seguinte. Isso dá 6 linhas de legenda e 6 linhas em branco. Falhe se o número de legendas encontradas não for exatamente 1, 1, 1, 1 e 2. Atualize a docstring (a frase "NÃO é tocada" deixa de valer) e o relatório `out/estudante_md_v1_12.json`.
> 4. **Conferências novas** em `conferencias_v112.py`:
>    - C-MD1: nos 35 .md, 0 ocorrência dos nomes antigos de lote, dos códigos RF-ASR, RF-DEGRAVACAO, RF-IA-PARLAMENTAR, RF-PROTECAO, TID-IA, TID-DADOS-VIZ, TI-FERRAMENTAS e TI-REDES-SEGURANCA e de "(v0.2)"; a linha 1 de cada `L<n>_estudo.md` é `# ` + `nome`;
>    - C-MD2: 0 linha que comece por "Mecanismo: troca de conceito (TC)" ou "Mecanismos: TC troca de conceito" nos 35 .md;
>    - C-LF: 0 CR nos arquivos de `gerador_v1_12/` fora de `out/`.
>    Inclua no bloco M as mutações (M-p) "repor o nome antigo na linha 1 do `L3_estudo.md`" e (M-q) "repor uma legenda no `L5_gabarito.md`", ambas detectadas.
> 5. **Entradas X (achado 4).** As 6 de `marcas_x_v112.py` (X7, X17 a X21) estão confirmadas pela GBQ (seção 5). Registre isso no MANIFESTO; o arquivo não muda.
> 6. Rode `sh saida/pacote/gerador_v1_12/rodar_tudo.sh` em FINAL. São exigidos código 0, "OK, 0 PENDENTE, 0 FALHA (modo FINAL)" e 100% das mutações detectadas.
>    - Ficam iguais à rodada 1: `out/pacote.json` (`34765253…e6024f`), `out/pacote_estudante.json` (`23224c96…612abd`), `out/registro_adendo4.md`, `out/registro_alteracoes_v1_12.csv`, `out/registro_alteracoes_v1_12_resumo.md`, `stats_v1_12.json` e `folhas_v1_12.json`.
>    - Mudam só 12 .md: os 7 `_estudo.md`, os 4 `_gabarito.md` de P1 e o `SIM-1_gabarito.md`.
> 7. Não promova, não faça commit e não toque em DECISOES.md, TAREFAS.md, `saida/estudante/`, `saida/gbq/` nem na plataforma. Se algum dado de JSON ou de registro mudar, pare e devolva à gbq-gerencia com o arquivo e os dois SHA.
> 8. Devolva:
>    - o código de saída;
>    - a última linha de `out/conferencias_stdout.txt`;
>    - a última linha de `out/fidelidade_mutacao_stdout.txt`;
>    - os SHA-256 dos 12 .md mudados;
>    - a confirmação de que `git status --short saida/pacote/gerador_v1_11` está vazio.

## 3. Conferência da GBQ depois da regeneração (por script)

Comando (Git Bash, raiz do repositório): `python -I -B saida/pacote/T115_conferencia_correcao.py C:/Users/Felipe/AppData/Local/Temp/t115/out_r1`

O script falha (código 1) na primeira divergência e só imprime "OK" se tudo abaixo valer:
- A rodada 1 copiada está íntegra: SHA de 7 arquivos e dos 35 .md iguais às constantes, que são os valores que a gbq-cqe examinou.
- Os 7 arquivos de dados e registro estão iguais à rodada 1.
- Dos 35 .md, 23 estão iguais. Os 7 `_estudo.md` diferem só na linha 1, que é `# ` + `nome` do -E. Os 5 `_gabarito.md` perdem só as legendas (1, 1, 1, 1 e 2), cada uma com a linha em branco seguinte.
- Nos 35 .md não sobra nenhum código RF-, TID- ou TI-, nenhum "(v0.2)" e nenhuma legenda.
- Não há CR no gerador fora de `out/`.
- As conferências do gerador estão sem falha e as mutações, 100% detectadas.
- O MANIFESTO bate com o disco.

O script imprime os SHA dos 12 .md mudados. A GBQ grava esses 12 valores na seção 7 deste arquivo, como adendo datado, antes da promoção. Rodei o script contra a rodada 1 para testá-lo: ele para em `L1_estudo.md` (linha 1 não mudou), como esperado.

## 4. Fim de linha, commit e clones (orquestrador; depois das seções 2 e 3 OK)

```sh
cd /c/Users/Felipe/felipeRM_push
printf '%s\n' '# gerador_v1_12: scripts em LF; out/ com os bytes gerados (T115_reconciliacao_v1_12, seção 4)' \
  'saida/pacote/gerador_v1_12/** text eol=lf' 'saida/pacote/gerador_v1_12/out/** -text -eol' >> .gitattributes
git add .gitattributes
git add -- saida/pacote/gerador_v1_12 regras/pacote_contrato.md saida/pacote/T115_D1_v1_12_2026-10-18.md saida/pacote/T115_reconciliacao_v1_12_2026-10-18.md \
  saida/pacote/T115_volateis.py saida/pacote/T115_volateis_T11.md saida/pacote/T115_conferencia_correcao.py saida/pacote/contrato_v1_2_9_2026-10-18.md saida/pacote/fidelidade_v1_12_gbq-cqe.md
git check-attr text eol -- saida/pacote/gerador_v1_12/build_v112.py saida/pacote/gerador_v1_12/out/pacote.json   # esperado: text set, eol lf; text unset, eol unspecified
git ls-files --eol -- saida/pacote/gerador_v1_12 | grep -v '/out/' | grep -v '^i/lf *w/lf ' ; echo "fora de out/ fora do padrão: acima (esperado nada)"
for f in $(git ls-files saida/pacote/gerador_v1_12/out); do git cat-file -p ":$f" | cmp -s - "$f" || echo "DIFERE $f"; done      # esperado: nada
git cat-file -p :saida/pacote/gerador_v1_12/out/pacote.json | sha256sum                                                     # esperado 3476525319b027fe…e6024f
```

Se algum desses comandos sair diferente do esperado, o orquestrador não commita e devolve à GBQ. O commit do ciclo leva `.gitattributes`, o gerador_v1_12 (sem `__pycache__/`), o contrato v1.2.9 e os arquivos T115. Isso fecha também o achado 7.

Depois do commit, a conferência em clones descartáveis é a mesma da seção 2.3 da T108_reconciliacao_v1_11, trocando `gerador_v1_11` por `gerador_v1_12`:
- clone 1: `git clone -q --no-local` com o autocrlf do sistema;
- clone 2: `-c core.autocrlf=false`;
- em cada um, `sh saida/pacote/gerador_v1_12/rodar_tudo.sh`.

Critério, nos dois clones:
- código 0;
- "OK, 0 PENDENTE, 0 FALHA (modo FINAL)";
- os entregáveis da seção 7 e `stats_v1_12.json` / `folhas_v1_12.json` com o mesmo SHA-256 de `out/`;
- `MANIFESTO.md` igual ao da árvore de trabalho;
- `fidelidade_mutacao_*` iguais (o M-o fica estável).

Diferenças admitidas, e só estas: `conferencias_stdout.txt` e `conferencias_v1_12.json`, pela linha C-G2 (`git status` de `regras/`). O resultado (dois códigos e a lista das diferenças) vai à Presidência antes da decisão do gatilho A.

## 5. Achado 4 — entradas X (D1 da GBQ)

CONFIRMADAS as 6 de `marcas_x_v112.py` como conteúdo (FP), não como marca de produção:
- X7: ANPD "órgão da Presidência (redação superada)", na pegadinha 32 do L3, que é a 25 da v1.11 e tem o mesmo texto;
- X17 e X18: medida F1 no L3-R64 (enunciado e justificativa);
- X19: medida F1 no L1-R176;
- X20: tecla F4 no resumo de P1-1;
- X21: "órgão da Presidência" no resumo de P2-4.1.

A X21 tem a mesma natureza da X7 e passa a integrar a lista MANTER da D1, seção 3.5. Isso é precisão de registro e não muda dado. As demais (X17 a X20) já estavam lá.

## 6. Achados 5 a 7 — registro

- **5 (URL da LGPD):** na reverificação de L3-R105 a R108, vale `https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm` (registro T115-U-01 e U-02; `saida/pacote/T115_volateis_T11.md`, seção 2, já indica essa URL). O arquivo canônico `T113_onda1_D_v2.md` não muda (precedente: arquivo canônico intacto, errata no registro).
- **6 (proximidade):** L1-R201 × L1-R211 (P2-1.7 e 1.8; Amazon Transcribe em streaming; mesma moldura; pontos distintos; Jaccard 0,39). Acrescento a proximidade à lista de montagem da D1, seção 3.9 (D2 da GBQ): os dois não ficam no mesmo simulado. O adendo 4 não é regerado por isso (ficaria fora do critério da seção 3); a proximidade entra no próximo adendo do registro AUTORAL e vale desde já para a gbq-csc.
- **7 (não commitado):** fechado pelo commit da seção 4, que é condição do gatilho A.

## 7. Promoção depois do aceite (byte a byte; ato separado, depois da decisão da Presidência e das seções 2 a 4 OK)

| Origem (`saida/pacote/gerador_v1_12/out/`) | Destino canônico | SHA-256 | Bytes |
|---|---|---|---|
| `pacote.json` | `saida/pacote/pacote.json` | `3476525319b027fe4427bf93598d516087ad6f18fb8dd5bbed4ad8c04be6024f` | 1 396 410 |
| `pacote_estudante.json` | `saida/pacote/pacote_estudante.json` | `23224c96b4189097012f139f52a9b995c29d930c6ac72801659720d6db612abd` | 1 134 920 |
| `registro_adendo4.md` | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_2026-10-18.md` | `52a47eec0f7c33e63ff73968fc5064d8665a18e08b6c2e45694f5da63b6af228` | 7 320 |
| `registro_alteracoes_v1_12.csv` | `saida/pacote/registro_alteracoes_v1_12.csv` | `437e2303172e25e1c45a9500b0d1fffb54e75fb59e3aa952b3eacf1c4da98662` | 149 187 |
| `registro_alteracoes_v1_12_resumo.md` | `saida/pacote/registro_alteracoes_v1_12_resumo.md` | `e5a92904ce3abda41415d6403474fee63280c1eb88afb3d4eeecac5b5744ff84` | 2 820 |
| `estudante/` (35 .md) | `saida/estudante/` (substitui os 35) | 23 abaixo; 12 a gravar pela seção 3 | — |

Os 23 .md que não mudam na correção têm o SHA-256 da rodada 1:
- BANCO_gabarito `f7d9bb470356e98962227bc7d19dbd6de2eff053aa718df002b26d6f2b4cb5ed`, BANCO_itens `879e1769c76c3bc655510a18a8fd66f49abb6dec52d7e3030adf93132a226c2c`;
- DISCURSIVAS `7777c52ca635cdd0e33a525aadd3b86699d333def9bb61816c79b67653f17bd0`, DISCURSIVAS_padrao `4d5a4e6e9cb23fffee9b401f7b8b9537ce9475cdc8127e34cd27c6592f77dcb4`;
- L1_gabarito `2947f638e5f9f1a08133716a7bb3b4d6f961330aa87dc5fc9d5252bec363cf7a`, L1_itens `94e106e720f28ace0fedabb9e5050ee018e2e5147cef926700cff45929325050`;
- L2_gabarito `7aa74384f5dd7e5bac2f49dc3d6b50af0322ccc10ba07cfcd0a41f9cb166d2b4`, L2_itens `9bb73429f2a9e29713c49247a61b58b1c4537aeac3850a47e3c698af5ffe7924`;
- L3_gabarito `5a2516422ebb27293f0a337fcae04ad539de3122e6e9c97c0cfdfd450028ce92`, L3_itens `b4ca1f7707a5789eb1750caa833d9a4d6a60d930642dc4908065e2b128bf2281`;
- L4_itens `6620555a3b368b66c1ca21a2ebc1faf9a2515016e747d64acf567d6a523c6545`, L5_itens `e110570384225bda943dd709e1a4272faa6581b94eadad6ebf6f42fc488afaa3`;
- L6A_itens `afa0a0e333ff7ac2d4857ee80e72142a8825befb417832c15921f1663ff31b1e`, L6B_itens `cac479bf65a9d8fc9e8d94822eed87e8f6b0257cf49c2028dab6f43873565077`;
- NUCLEO `bf13d9dff214e1e3dd699028c27617c11f96e640c4bbdf8bba42e96e0d15260a`, README `8048d862c58afbedd9d952e576e758c43989b1245815a367e8990e261ea0379a`;
- SIM-0-P2_folha `f69efe607e7b575c246b46eded5ce15d5b6cf1e14ae755bc1bff23087c8bdab5`, SIM-0-P2_gabarito `cdd8a6588d0e24ebd4e445a50a7d11334e324eb4a85dbfd46b7babe0bbdcc081`;
- SIM-0_folha `7ef04f37578a2da082ab8c016ac06a06e8463db96089c268cd7e9b100815cd16`, SIM-0_gabarito `2df79ffa2501e38c66564a8b2a23cd5632372255bf7214c9179ca8ece3788374`;
- SIM-1_folha `e0e21ea32da954f4d20ac9df23937dab412179873d28211876600e938c2b9a38`;
- SIM-2_folha `d576cc3fecc6f9973a028f82e303abb65aedd00ad14000cbc263c51423daaa92`, SIM-2_gabarito `2113d4a7c1e399a1ce25b71d5819fe565121d3fc41c9a4d4c2b3e3e75e248c9e`.

Os 12 mudados (L1, L2, L3, L4, L5, L6A e L6B `_estudo`; L4, L5, L6A e L6B `_gabarito`; SIM-1_gabarito) ficam **a gravar aqui** com a saída da seção 3. A v1.12 não tem `_manter.csv`: os MANTER estão listados no `_resumo.md`.

Não são promovidos: ficam em `out/` como registro e contraprova `stats_v1_12.json` e `folhas_v1_12.json` (este último é insumo da cobertura, `saida/pacote/cobertura_v1_12.md`, da secretaria, T-95), além das conferências, validação, inventário, similaridade, mutação, `casos_erros/` e dos stdout.

Comandos (orquestrador, depois do sim da Presidência e com as seções 2 a 4 OK):

```sh
cd /c/Users/Felipe/felipeRM_push; G=saida/pacote/gerador_v1_12/out
cp "$G/pacote.json" "$G/pacote_estudante.json" "$G/registro_alteracoes_v1_12.csv" "$G/registro_alteracoes_v1_12_resumo.md" saida/pacote/
cp "$G/registro_adendo4.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_2026-10-18.md
cp "$G"/estudante/*.md saida/estudante/
cmp "$G/pacote.json" saida/pacote/pacote.json && cmp "$G/pacote_estudante.json" saida/pacote/pacote_estudante.json && cmp "$G/registro_adendo4.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_2026-10-18.md && cmp "$G/registro_alteracoes_v1_12.csv" saida/pacote/registro_alteracoes_v1_12.csv && cmp "$G/registro_alteracoes_v1_12_resumo.md" saida/pacote/registro_alteracoes_v1_12_resumo.md && for f in "$G"/estudante/*.md; do cmp "$f" "saida/estudante/$(basename "$f")" || exit 1; done && echo promocao-ok
(cd saida/estudante && sha256sum *.md)        # esperado: os 23 acima e os 12 da seção 3
git add saida/pacote/pacote.json saida/pacote/pacote_estudante.json saida/pacote/registro_alteracoes_v1_12.csv saida/pacote/registro_alteracoes_v1_12_resumo.md saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo4_2026-10-18.md saida/estudante/
git cat-file -p :saida/pacote/pacote.json | sha256sum; git cat-file -p :saida/pacote/pacote_estudante.json | sha256sum   # esperado 34765253… e 23224c96…
```

Se algum `cmp` ou SHA divergir, não commita e devolve à GBQ. Depois da promoção, a T-115 fica CONCLUÍDA (competência D da Presidência), e as T-110 a T-112 e a onda 1 da T-113 ficam concluídas quanto a P1 e P2 (D-V112-BAEF-P1/P2-ACEITE). O orquestrador acrescenta à T-11 o texto da seção 5 de `T115_volateis_T11.md`, e a cobertura fica com a secretaria. Promover não é publicar: nada vai à plataforma da candidata nem à prévia sem o sim do Fundador (D-V15-PLATAFORMA); a skill do painel roda quando o pacote for carregado.

## 8. Gatilho

GATILHO A da GBQ, em PARA_PRESIDENCIA.md (ciclo 2026-10-18 s14c4): aceite da v1.12 como canônica, condicionado às seções 2 (correção e regeneração), 3 (conferência da GBQ), 4 (fim de linha, commit e clones) e à promoção da seção 7.
