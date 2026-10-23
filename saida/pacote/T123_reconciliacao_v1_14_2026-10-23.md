# T123_reconciliacao_v1_14_2026-10-23.md — T-123 — reconciliação e gatilho A do pacote v1.14 e da página v17 — 2026-10-23 — gerado por gbq-gerencia

REMETENTE: gbq-gerencia (passo final da D1 `saida/pacote/T123_D1_v1_14_2026-10-23.md`, seção 13).
DESTINATÁRIOS:
- presidencia: gatilho A em PARA_PRESIDENCIA.md;
- orquestrador: promoção, build e publicação, só depois do sim (seções 3 a 5);
- secretaria: TAREFAS.md (seção 7).

Base:
- D1 da T-123 (1e3da24c…413c no gravado; a versão do commit 793225e prevalece);
- relatório `saida/pacote/T123_FINAL_v1_14_2026-10-23.md` (LF 2b9d41b0…617c);
- fidelidade `saida/pacote/fidelidade_v1_14_gbq-cqe.md` (LF c49d1f6f…e9a; **ACEITO**);
- cobertura `saida/pacote/cobertura_v1_14.md` (LF d27f1638…0288; sem divergência contra `out/cobertura_v1_14.json`);
- limpeza da GCB `saida/gcb/T123_limpeza_reconciliacao_GCB_2026-10-23.md` (LF 19ec015d…4cb8; QA R2 da gcb-cqfp CONFERIDO 91/91; gatilho A da GCB em PARA_PRESIDENCIA.md);
- QA da plataforma `saida/plataforma/QA_v17_R2_2026-10-23.md` (LF b487610f…131f; **APROVADO**);
- D-V114-PUBLICAR, D-V17-DESIGN, D-V17-NOTA-TOPICO, D-V15-PLATAFORMA, D-DIAG30-DA, D-MOLDURA-CE.

Gate: nenhum. O assunto é de forma, do domínio da GBQ; não há conflito entre Gerências e não houve reprovação.
Gravei só este arquivo e o item da GBQ em PARA_PRESIDENCIA.md. Sem commit, nada promovido, nada publicado.

Conferência própria, em 23/10/2026 (`python3 -I`, só leitura do repositório, scratchpad `gbq_t123/`; SHA-256 calculado sobre o conteúdo LF):
- **Objetos da seção 2.** Os SHA-256 iguais aos do FINAL, do MANIFESTO e da fidelidade.
- **Edição .md.** 53 arquivos em `out/estudante/`. Mudam exatamente 12 frente a `saida/estudante/` (LF); os outros 41 são iguais.
- **Página (ensaio).** Build de ensaio da página v17 no scratchpad, com `out/pacote.json`, `--data 23/10/2026` e o rótulo da seção 4. Resultado:
  - pacote embutido igual, como objeto, a `out/pacote.json` (070bc237…d495);
  - meta única e exata;
  - DIAG30 com P1, P2 e DA de 30 ids cada; todos existem, nenhum volátil;
  - DA: 15 C, todos diretos e fora de simulado, iguais em ids e folhas a `montagem_v1_13/out/diag30_DA.json` (eb1ced6d…6800);
  - página sem pacote e sem meta igual ao `plataforma_v17_template.html` (LF 541fc66c…9b97), o mesmo template de que sai a `plataforma_v17.html` aprovada na R2;
  - conteúdo LF com 3.091.217 bytes, SHA-256 `2a9f7912ea3c1af8d1ea919999474ce35b3c2d6b50cd94f92b7b3eeb2cf8d44b`.

## 1. Decisão (D1)

**ACEITO, para gatilho A**:
- (I) o pacote v1.14: os objetos da seção 2, como canônicos;
- (II) a página `plataforma_v17_publicar.html` para publicação no link da candidata. A página é montada pela seção 4 a partir do pacote promovido e só vale se passar nas conferências da seção 5.

A publicação já tem o sim do Fundador (D-V114-PUBLICAR; D-V17-DESIGN: publicação única, v17 com v1.14). A v16 fica intacta e não é republicada.

Condições do gatilho (D1 da T-123, seção 13), uma a uma:

| Condição | Situação | Evidência |
|---|---|---|
| (a) limpeza da GCB CONFERIDA | CUMPRIDA, com o aceite da Presidência pendente no gatilho A da GCB, no mesmo arquivo | QA R2 da gcb-cqfp CONFERIDO 91/91. CSV df9f53bd…b501 e registro a511fd8d…820e, conferidos em C-SHA e pela gbq-cqe (91/91 "antes" únicos). **O aceite (I) depende do SIM ao gatilho A da GCB.** |
| (b) adendo 6 | CUMPRIDA | `out/registro_adendo6.md` 74855f03…970b. A fidelidade (seção 6) dá OK: 8 SHA das levas, 35 parciais, 18 do núcleo, vagos, erratas, 0 enunciado e scan_q 0. |
| (c) contagens da gbq-csc = secretaria | CUMPRIDA | `cobertura_v1_14.md`: "Sem divergências" contra `cobertura_v1_14.json`. Os totais são iguais: 1.433 itens, C/E 730/703 e DA 644 em folha. |
| (d) fidelidade da gbq-cqe | CUMPRIDA | ACEITO, 0 FALHA nos 7 pontos, com 3 observações só de registro. Inclui clone limpo com autocrlf true e false (83/83 iguais ao MANIFESTO). |
| (e) recontagem de moldura | CUMPRIDA | `out/moldura_v1_14.json` f46004c8…edf. Percentual de C: P1-TI 57,1% (4/3), P2 53,8% (112/96), P1-DA 53,2% (50/44); 0 divergência do campo "Moldura:". |

Registros da GBQ desta reconciliação (D1, sem decisão nova):
1. **Lista X do PROCESSO** (pendência P1 da GCB). "Presidência da República" no D2-R21 e no D2-R24 é conteúdo: remete à Lei 9.007. Fica registrada em `marcas_v114.py` como exceção de conteúdo do critério "0 PROCESSO". Não é MANTER de marca e não precisa do Fundador (fidelidade, achado 3: 0 marca; 22 casamentos de conteúdo).
2. **D-MOLDURA-CE, regra (c).** A recontagem oficial sobre o pacote v1.14 dá as três matérias entre 40% e 60% de C. Por isso, com o aceite canônico da v1.14, **cessa a regra (c)** (teto de 50% de C nos itens com moldura em cada simulado da T-119). A secretaria anota o fim na linha da T-119. As cotas de E com moldura das levas 9 a 12 continuam como fixadas na D-T116-LEVA5-ACEITE, ponto (ii): a margem continua curta e a reconciliação de cada leva registra o acumulado.
3. **Observações da fidelidade 2 a 4.** Ficam só como registro (convenção de contagem de linhas no `contrato_v1_2_12`; falsos positivos de conteúdo; "a mesma publicação" no D4-R19 e no D4-R27). Nenhuma muda dado.
4. **Fora da v1.14, por decisão vigente:**
   - BQ-0141 (T-87) e BQ-0151 (D-BQ0151-DIVERGE);
   - as erratas AJ-L8-E3 e AJ-L8-E4: os itens D4-R42 e D4-R52 entram como aprovados no R2, e as erratas vão para o rito da leva 9;
   - achado 8 da T-117 e a frase "O exemplo é hipotético.": seguem pendentes na T-117.
5. **VOLÁTEIS.** 0 novos; nada a acrescentar à T-11 nem à T-120. Os de DA continuam os 5 da v1.13.

## 2. Objetos aceitos (SHA-256 do conteúdo; `out/` = `saida/pacote/montagem_v1_14/out/`, gravado em LF, sem CR)

| Objeto | Arquivo | Bytes | SHA-256 |
|---|---|--:|---|
| `pacote.json` v1.14 | `out/pacote.json` | 3.194.690 | `070bc237fcc7371a23365f6e66c9341cf5c0aee08ad9206a9f7be6c06150d495` |
| `pacote_estudante.json` v1.14-E | `out/pacote_estudante.json` | 2.930.776 | `6b56a7f8a1c7c42a01e145b0da35ab48691496fde82d2a9ee8fd4a6ff195b9ab` |
| Adendo 6 do registro AUTORAL | `out/registro_adendo6.md` | 16.428 | `74855f037108303454990e27f45447bac0a0d4322bda75a944dd00ce1c37970b` |
| Edição .md v1.14-E (53 arquivos) | `out/estudante/` | — | digest R2-D `f9c1c0651e9fb50009220d5424d441f99ba5fb93e46164fe4d900de0c010916b` |
| Registro de alterações por id (380 linhas) | `out/registro_alteracoes_v1_14.csv` | 74.200 | `56a7a90d6434ea0d4dbaab9fd73d68cf1040500e6c0afbe62ad17b6b637b3abc` |
| Resumo do registro de alterações | `out/registro_alteracoes_v1_14_resumo.md` | 1.371 | `61e12fbe859df70e3eb5c7c45583bb0fd6c20654c2736d68d22b7d3b5659de68` |
| Contrato v1.2.12 (regra vigente; já no lugar) | `regras/pacote_contrato.md` | 76.774 (LF) | `3916ad994cd06ee74b13ba545de5af3b6c241d0004eb0625e922973ab76c38df` |
| Registro da errata v1.2.12 | `saida/pacote/contrato_v1_2_12_2026-10-23.md` | 7.252 | `8b49a306dd1462e75a72c1c57fde76d918854dfeac9ae4550adf23b5615e670b` |
| Cobertura v1.14 (T-95) | `saida/pacote/cobertura_v1_14.md` | 13.459 (LF) | `d27f163878a85f1857fd409edc8e1ee1654237e770222e86627940260f800288` |
| MANIFESTO (83 arquivos + ele mesmo) | `saida/pacote/montagem_v1_14/MANIFESTO_v1_14.md` | 20.768 | `c1dd7fe7419743b8a6a4641a25577db0302bf569bb38c60b8587d22fbbbaf723` |

Ficam em `out/` como contraprova, sem promoção:
- `conferencia_t123.json` (4dc21e58…b2f; 99 OK, 0 FALHA);
- `mutacao_t123.json` (e502f0ec…483; 15/15);
- `cobertura_v1_14.json`, `diag30_check_v1_14.json` e `moldura_v1_14.json`;
- `estudante_md_v1_14.json`, `extracao_t123.json`, `reforco_bruto.json` e `reforco_marcas.json`.

Conteúdo da v1.14:
- **Itens.** 1.433, C/E 730/703. Os 1.159 itens da v1.13 ficam intactos, como objeto e na ordem relativa.
- **Acréscimos.** 238 itens de reforço de DA (122/116; 35 parciais) e 36 itens de banco P1-DA (26/10).
- **Direito Administrativo.** 684 itens (350/334), com estes lotes: D1 72, D2 160, D3 160, D4 136, D5 70, D6 50.
- **Estudante.** `nucleo` 775 (DA 408/276). Doze itens passam de true a false: D1-07, D1-08, D3-79, D3-80, D6-07 a D6-10 e D6-37 a D6-40.
- **Cabeçalho.** `geradoEm` 2026-10-23; `nome` "Câmara 2026 — pacote F4 (v1.14)" / "(v1.14-E)"; `versao` 1.
- **Sem mudança.** Edital, lotes, tópicos, simulados e discursivas.

Os 12 arquivos .md que mudam em `saida/estudante/` (os outros 41 são iguais byte a byte aos atuais):

| Arquivo | Bytes | SHA-256 |
|---|--:|---|
| BANCO_gabarito.md | 12.124 | `253b6291e63da0cd914cb097ffe15373076560eb8272a7aadef43d69a81d2f6f` |
| BANCO_itens.md | 100.223 | `2535197eccad20d9f9d1caee1e5526b0bdf41dfcf06de13ffcac8a1877a63ca4` |
| DA_D1_gabarito.md | 25.122 | `1399cd8cf1bb4b8f21eb300e8bff113eac53cfbe8bf427b8a4c3293e5b1c2edb` |
| DA_D1_itens.md | 16.969 | `b870ecbb4513b408f79a4203122a3dc6846c81ae7ad3f80dcfcd1678db886738` |
| DA_D2_gabarito.md | 69.071 | `56d3886cfaf37235ee45a37e13b5bd151a7849ec2eb3832cd02299e6e6415efc` |
| DA_D2_itens.md | 40.975 | `3ff5c06f76ea858d880c08a8a2b175b2e4c2afc2408e20776b1bab9842ee4f6f` |
| DA_D3_gabarito.md | 68.120 | `733d6657d66aca809775084754fbaa9309df109ada5578dfa6c1dda2903da1fc` |
| DA_D3_itens.md | 41.611 | `4c998cc16c6ec9a512e938b1f27fd9763d70d3d4d21d7887b5b0ddb48d75ff8e` |
| DA_D4_gabarito.md | 56.800 | `8b4d301308010f88470d9ecafd32839702c7eefe394bf5c2ac84137439aad5bf` |
| DA_D4_itens.md | 37.794 | `74a714b9e3a98d35eebb67d690d1f3f269ce386fd16992dd59b8d7297fb4e23c` |
| NUCLEO.md (775 ids) | 8.103 | `0ee0016e21c3ad05908d5f15d3bad81518cae701507ce72883c33af26e5c0e8d` |
| README.md (v1.14-E) | 4.610 | `dd3c4fc26cb6cc810958ebf28b9d20ab7b18797704ab8527009052ce505b82c5` |

## 3. Promoção (ato do orquestrador, só depois do sim aos dois gatilhos A, o da GCB e o da GBQ; promover não é publicar)

O orquestrador roda tudo a partir da raiz do repositório, em Git Bash.

| Origem (`saida/pacote/montagem_v1_14/out/`) | Destino canônico | SHA-256 esperado no destino |
|---|---|---|
| `pacote.json` | `saida/pacote/pacote.json` (substitui a v1.13, 82c4117c…) | `070bc237…d495` |
| `pacote_estudante.json` | `saida/pacote/pacote_estudante.json` (substitui a v1.13-E, 04cbd593…) | `6b56a7f8…b9ab` |
| `registro_adendo6.md` | `saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo6_2026-10-23.md` | `74855f03…970b` |
| `registro_alteracoes_v1_14.csv` | `saida/pacote/registro_alteracoes_v1_14.csv` | `56a7a90d…3abc` |
| `registro_alteracoes_v1_14_resumo.md` | `saida/pacote/registro_alteracoes_v1_14_resumo.md` | `61e12fbe…de68` |
| `estudante/*.md` (53) | `saida/estudante/` (12 mudam, 41 iguais; nenhum novo) | digest `f9c1c065…916b` e os 12 SHA da seção 2 |

```sh
O=saida/pacote/montagem_v1_14/out
cp "$O/pacote.json" "$O/pacote_estudante.json" "$O/registro_alteracoes_v1_14.csv" "$O/registro_alteracoes_v1_14_resumo.md" saida/pacote/
cp "$O/registro_adendo6.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo6_2026-10-23.md
cp "$O"/estudante/*.md saida/estudante/
for f in pacote.json pacote_estudante.json registro_alteracoes_v1_14.csv registro_alteracoes_v1_14_resumo.md; do cmp "$O/$f" "saida/pacote/$f" || exit 1; done \
 && cmp "$O/registro_adendo6.md" saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo6_2026-10-23.md \
 && for f in "$O"/estudante/*.md; do cmp "$f" "saida/estudante/$(basename "$f")" || exit 1; done && echo promocao-ok
ls saida/estudante/*.md | wc -l                                   # esperado 53
(cd saida && find estudante -type f -name '*.md' | LC_ALL=C sort | while read p; do printf '%s\t%s\n' "$p" "$(sha256sum "$p" | cut -d' ' -f1)"; done) | sha256sum   # esperado f9c1c065…916b
sha256sum saida/pacote/pacote.json saida/pacote/pacote_estudante.json saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo6_2026-10-23.md   # 070bc237…, 6b56a7f8…, 74855f03…
```

**Commit.** Acrescentar ao `.gitattributes` as linhas `saida/pacote/montagem_v1_14/** text eol=lf` e `saida/pacote/montagem_v1_14/out/** -text -eol`, como no precedente da v1.13. Depois do `git add`, conferir os blobs:

```sh
git cat-file -p :saida/pacote/pacote.json | sha256sum            # 070bc237…
git cat-file -p :saida/pacote/pacote_estudante.json | sha256sum  # 6b56a7f8…
git cat-file -p :saida/gbq/claude_GBQ_Registro_AUTORAL_v3_adendo6_2026-10-23.md | sha256sum   # 74855f03…
for f in $(git ls-files saida/pacote/montagem_v1_14/out saida/estudante); do git cat-file -p ":$f" | tr -d '\r' | cmp -s - <(tr -d '\r' < "$f") || echo "DIFERE $f"; done   # esperado: nada
```

Se algum `cmp` ou SHA-256 divergir, o orquestrador não commita e devolve à GBQ com o arquivo e os dois valores.

## 4. Build da página publicável (orquestrador, depois da promoção)

```sh
python3 -I saida/plataforma/build_plataforma_v17.py \
  --template saida/plataforma/plataforma_v17_template.html \
  --pacote saida/pacote/pacote.json \
  --saida saida/plataforma/plataforma_v17_publicar.html \
  --data 23/10/2026 \
  --rotulo-pacote "pacote F4 v1.14 embutido (1.433 itens; 684 de Direito Administrativo)"
python3 -I -c "p='saida/plataforma/plataforma_v17_publicar.html'; b=open(p,'rb').read(); open(p,'wb').write(b.replace(b'\r\n', b'\n'))"
```

Por que normalizar: o build grava em modo texto, e no Windows isso gera CRLF. A segunda linha deixa o arquivo em LF.

Meta resultante, exata: `v17 · publicada em 23/10/2026 · três abas · pacote F4 v1.14 embutido (1.433 itens; 684 de Direito Administrativo)`.

Esperado depois da normalização: **3.091.217 bytes, 0 CR, SHA-256 `2a9f7912ea3c1af8d1ea919999474ce35b3c2d6b50cd94f92b7b3eeb2cf8d44b`**. É o resultado do ensaio da GBQ, com o template LF 541fc66c…9b97 e o pacote 070bc237…d495.

Se a publicação não for em 23/10/2026: refazer o build com a data real em `--data`. A meta e o SHA-256 mudam. As conferências 2 a 6 da seção 5 continuam valendo; a conferência 1 passa a valer com o novo valor, registrado.

## 5. Conferências que o orquestrador roda antes de publicar (todas por script, `python3 -I`; qualquer falha = não publica e devolve à GBQ)

1. **Arquivo.** `plataforma_v17_publicar.html` tem 0 CR, 3.091.217 bytes e SHA-256 `2a9f7912…d44b`.
2. **Pacote embutido.** O JSON da linha `const PUB_INLINE = …;` (só uma) é igual, como objeto, ao de `saida/pacote/pacote.json`. O SHA-256 desse arquivo é `070bc237…d495`. Confere também:
   - 1.433 itens;
   - `geradoEm` "2026-10-23" (maior que "2026-10-20": o pacote novo substitui o salvo no aparelho);
   - `nome` "Câmara 2026 — pacote F4 (v1.14)".
3. **Meta.** Exatamente 1 `mapaspro:versao`, com o texto exato da seção 4. Nenhum `__VERSAO__` nem `__PACOTE__` restante.
4. **DIAG30 DA revalidado** (D-DIAG30-DA; a lista não muda).
   - DA: são 30 ids distintos, iguais em ids e ordem a `saida/pacote/montagem_v1_13/out/diag30_DA.json` (eb1ced6d…6800). Os 30 têm de cumprir:
     - existir no pacote embutido, com o `itemEdital` igual às folhas do arquivo;
     - ser `aderencia` "direta" e não ter `volatil`;
     - estar fora de `simulados`;
     - somar C/E 15/15.
   - DIAG30.P1 e P2: 30 ids cada, todos existentes, nenhum volátil.
5. **Template.** Retirados o pacote e a meta, a página é igual ao `plataforma_v17_template.html` (LF 541fc66c…9b97), que é o template aprovado na R2 da QA (`QA_v17_R2_2026-10-23.md`).
6. **v16 intacta.** `plataforma_v16_final_template.html` e `plataforma_v16_publicar.html` têm o SHA-256 do HEAD: LF c6de3f2a…b46c e 4d19eb05…65fb.

Script de referência da GBQ, que cobre os pontos 2 a 5: `…/scratchpad/gbq_t123/chk_v17.py <html> <pacote> <template> "<meta>"`. O orquestrador pode usar o seu próprio, com os mesmos critérios.

Publicação: no mesmo link da candidata (https://claude.ai/artifact/5fyXGpFMomSHwZuRnu36rC), só depois de três condições:
- o sim da Presidência a este gatilho e ao da GCB;
- a promoção OK;
- as 6 conferências OK.

Depois de publicar, registrar em DECISOES.md (ato da Presidência ou do orquestrador, como na D-PLATAFORMA-V16-PUBLICACAO) o arquivo, os bytes, o SHA-256 e a versão do artifact.

## 6. Pendências (nenhuma bloqueia)

| # | Pendência | Responsável | Destino |
|---|---|---|---|
| P1 | Erratas AJ-L8-E3/E4 (D4-R42, D4-R52) | GCB | leva 9 (T-116) e consolidação seguinte |
| P2 | 12 folhas de DA abaixo de 20 (faltam 118) | GCB | T-116, levas 9 a 12 |
| P3 | BQ-0141 e BQ-0151 fora do pacote | qa-normativo-da → GBQ | T-87; novo gatilho D se o texto vigente mudar |
| P4 | Achado 8 e frase "O exemplo é hipotético." | gbq-estilo; Fundador | T-117 |
| P5 | Coluna "Onda programada" de P1 na cobertura | secretaria | T-95, ocorrência seguinte |
| P6 | Simulado 0 e 0-P2 não oferecidos como treino na v17 (registro informativo do QA R2) | Fundador, se quiser ordem nova | — |

## 7. Mudanças para a secretaria em TAREFAS.md (depois do sim, da promoção e da publicação)

- **T-123:** CONCLUÍDA (ato da Presidência). Registrar:
  - pacote.json 070bc237…, pacote_estudante.json 6b56a7f8…, adendo 6 74855f03…;
  - edição .md f9c1c065…, contrato v1.2.12 3916ad99…, cobertura d27f1638…;
  - página v17 2a9f7912… (ou o SHA da data real).
- **T-12:** a ocorrência v1.14 fica concluída pela T-123.
- **T-95:** a ocorrência v1.14 fica concluída.
- **T-119:** "regra (c) da D-MOLDURA-CE encerrada pela D1 da GBQ (T123_reconciliacao_v1_14, seção 1, registro 2), com o aceite canônico da v1.14".
- **T-125:** CONCLUÍDA com a publicação.
- **T-116:** sem mudança de texto; a contagem de partida passa a ser a de `cobertura_v1_14.md`.

## 8. Gatilho

GATILHO A da GBQ em PARA_PRESIDENCIA.md (ciclo 2026-10-23 s17c1): aceitar (I) a v1.14 canônica (seção 2) e (II) a página v17 montada pela seção 4, para publicação depois das conferências da seção 5. O sim do Fundador à publicação já foi dado (D-V114-PUBLICAR; D-V17-DESIGN).
