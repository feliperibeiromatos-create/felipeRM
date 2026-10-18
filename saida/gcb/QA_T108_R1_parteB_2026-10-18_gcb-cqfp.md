# QA_T108_R1_parteB_2026-10-18_gcb-cqfp.md — T-108 (ORDEM_V15_C, limpeza), R1, Parte B (lote 6a) — 2026-10-18 — gerado por gcb-cqfp

Objeto: QA R1 da Parte B da GCB (lote 6a): `saida/gcb/T108_substituicoes_GCB_parteB.csv` (175 edições, GCB-B0001 a GCB-B0175), com `saida/gcb/T108_producao_notas_GCB_parteB.md` e `saida/gcb/T108_fontes_GCB.md` (tabela do Lote 6a). Roteiro: seção 5 de `saida/gcb/T108_D1_GCB_2026-10-18.md` e seção 4 de `saida/pacote/T108_metodo_GBQ_2026-10-18.md`. Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed (conferido). Somente leitura: nenhum arquivo de produção, fonte ou pacote foi alterado. Revisão em subagente distinto do produtor (gcb-cpp).

## 1. Veredito da Parte B

**APROVADO COM RESSALVAS.** 175 linhas: 172 APROVADO, 3 CORRIGIR, 0 REPROVADO. Reprovação: 0,0% (0/175); linhas que voltam à produção na R2 (CORRIGIR): 1,7% (3/175). Abaixo do gate de 30%.

| veredito | linhas |
|---|---|
| APROVADO | 172 |
| CORRIGIR | 3 (GCB-B0020, GCB-B0058, GCB-B0103) |
| REPROVADO | 0 |

## 2. Conferência mecânica (script próprio, python -I, somente leitura; não há T108_conferir_tabela.py da GBQ)

Script no anexo B, rodado sobre cópia em memória do pacote (nada gravado no repositório). Usa `campos()` e `varre()` de `saida/pacote/T108_inventario.py` para a re-varredura.

| checagem | resultado |
|---|---|
| SHA-256 LF do pacote.json v1.10 | OK (d43c32de…2fed) |
| (a) universo do 6a (gerencia=GCB, pacote.json, PROCESSO ou VERIFICAR) | 199 ids (190 PROCESSO, 9 VERIFICAR); 199 cobertos, 0 faltando, 0 em duplicidade; nenhum id fora do universo; caminho da edição = caminho da ocorrência em todas |
| (b) `antes` literal e único no campo | OK em 175/175; casamento de cada ocorrência dentro do seu `antes` em 175/175; sem sobreposição de edições no mesmo campo |
| (c) D-C05-4a878e59 (tecla F4 do Excel) e 35 FP-CONTEUDO | Fora de todo `antes`. Após aplicar a tabela, "A tecla F4, com a referência selecionada na barra de fórmulas, alterna entre os tipos (a página documenta isso)." está intacta no curso 1.2.2. A re-varredura dá 1 FP-R1 + 35 FP-CONTEUDO, como antes. O id da tecla F4 muda na re-varredura (de 4a878e59 para outro hash) só porque o id inclui a ordem do casamento "F4" no campo e os F4 de fonte anteriores (B0035, B0039) saíram; texto e classe idênticos. Registro para a GBQ: o T108_conferir_tabela.py deve casar a FP-R1 por texto, não por id. |
| (d) re-varredura do 6a após aplicar a tabela | 0 PROCESSO, 0 VERIFICAR; ocorrências fora do 6a: 780 antes e 780 depois |
| (e) `depois` sem código de fonte, item, par, "Lote N", TC/IC/GI/AT, [TS], QA/CQFP, versão, VOLÁTIL, "Difere", instrução interna | 0 casamentos em 175 `depois` |
| (f) enunciado, gabarito, itemEdital (e todos os campos de item exceto justificativa; todos os campos de lote exceto curso/resumo/pegadinhas; raiz) | idênticos após a aplicação |
| formato | DELETAR com `depois` vazio (2/2); SUBSTITUIR com `depois` preenchido (173/173); `fonte_origem` presente nas 146 linhas de regra 2 |
| datas | toda data dd/mm/aaaa presente num `antes` de regra 2 permanece no `depois` |

Contagens conferidas (iguais às notas de produção): edições por campo — curso 94, justificativas 35, pegadinhas 26, resumo 20; ocorrências por categoria — C05 157, C10 16, C06 15, C02 6, C01 5; ações — SUBSTITUIR 173, DELETAR 2, MANTER 0; modo — TEMPLATE 112, LIVRE 63; regra — 2: 146, 4: 15, 5: 14.

## 3. Tabela de fontes do Lote 6a (amostra contra o arquivo do lote)

Arquivo do lote: `saida/gcb/GCB_Lote6a_v2_producao_auto.md`, seção FONTES (linhas 30 a 60), cabeçalho "todas verificado em 08/10/2026".

| código | nome na tabela | no arquivo do lote | data | resultado |
|---|---|---|---|---|
| F4 | Microsoft, documentação de suporte, "Alternar entre referências relativas, absolutas e mistas" | linha 36, mesmo título, support.microsoft.com, bloco "Microsoft — Excel" | 08/10/2026 = 08/10/2026 | confere |
| F10 | Microsoft, documentação de suporte, "Gerenciar compartilhamento e permissões no OneDrive e no SharePoint" | linha 44, mesmo título (a URL trata de parar de compartilhar, como a observação da tabela diz) | 08/10/2026 | confere |
| F14 | Microsoft Learn, "POP3 e IMAP4 em Exchange Online" | linha 49, mesmo título, learn.microsoft.com | 08/10/2026 | confere ("Microsoft Learn" vem do domínio da URL do lote; não é fonte nova) |
| F16 | IETF, RFC 9051, "Internet Message Access Protocol (IMAP) - Version 4rev2" | linha 52, mesmo título, rfc-editor.org; leitura parcial registrada | 08/10/2026 | confere |
| F22 | Ajuda do Google Meet, "Inicie ou agende uma videoconferência do Google Meet" | linha 60, mesmo título, support.google.com/meet | 08/10/2026 | confere |

Nenhuma divergência na amostra; a conferência da tabela inteira não era obrigatória, mas foi feita (F1 a F22, linhas 32 a 60): os 22 nomes conferem com o lote, nenhuma fonte nova, data única 08/10/2026, X1 (fonte que não abriu) corretamente fora da tabela. Conferência de nome nas linhas TEMPLATE e LIVRE de regra 2: 100% (146/146) — o nome da tabela do código de `fonte_origem` está no `depois` e os códigos do `antes` coincidem com os de `fonte_origem`, salvo GCB-B0103 (faixa "F20–F22", ver seção 4). Forma das linhas TEMPLATE: amostra de 25% (28/112: B0002, B0006, B0010, B0015, B0019, B0032, B0040, B0046, B0051, B0062, B0066, B0072, B0083, B0088, B0092, B0102, B0108, B0113, B0117, B0121, B0126, B0131, B0135, B0139, B0146, B0154, B0162, B0169), todas nas formas fixas ("(Fn)" → "(nome)", "; Fn)" → "; nome)", "Fonte: Fn," → "Fonte: nome,", vários códigos separados por ponto e vírgula), sem erro.

## 4. Mérito, linha a linha (63 LIVRE, incluindo os 9 VERIFICAR)

### 4.1 Linhas CORRIGIR (correção exata)

1. **GCB-B0020** (`lotes[L6A].resumo`, C02;C10, VERIFICAR VOLÁTEIS). A troca dos códigos 6A-01, 6A-09, 6A-10, 6A-14 e 6A-15 pelos conceitos está certa (modo de exibição das alterações no Word; compartilhamento e restauração de versões no OneDrive; canais do Teams; apresentação de tela no Meet), e "VOLÁTEIS" virou "sujeitos a mudança", como manda o D1 (seção 1, item 4). Motivo da correção: "reverificar entre 4 e 8/1/2027" virou "conferir de novo entre 4 e 8/1/2027". É a mesma instrução interna com outras palavras: a reverificação de 4 a 8/1/2027 é tarefa da Fábrica (CLAUDE.md, VOLÁTIL), não da candidata, e a regra do D1 manda DELETAR REVERIFICAR, salvo informação útil à candidata, o que não é o caso. Correção: `depois` = `Validade: os pontos sobre o modo de exibição das alterações no Word, o compartilhamento e a restauração de versões no OneDrive, os canais do Teams e a apresentação de tela no Meet dependem de interface e comportamento de serviço e estão sujeitos a mudança.` (todo o resto igual). A `nota` da linha diz "instrução 'não vira item' retirada", o que não se aplica a esta linha; corrigir a nota para "VERIFICAR (VOLÁTEIS): códigos de item trocados pelos conceitos; 'VOLÁTEIS' trocado por 'sujeitos a mudança'; instrução de reverificação retirada".
2. **GCB-B0058** (`lotes[L6A].curso`, C01;C10). "o lote NÃO cobra" virou "o estudo do item 1 de TI e Dados não trata de". Isso muda o sentido e contradiz a frase anterior: o curso trata do ponto ("ela ainda avisa que NÃO é possível mudar o tipo de permissão de um LINK … e orienta excluir o link e criar outro"). O sentido original é "não é objeto de estudo nem de item", que as linhas B0012, B0060 e B0081 já passam como "fica fora do estudo". Correção: `depois` = `fica fora do estudo o ponto` (resultado: "…por isso fica fora do estudo o ponto "como alterar a permissão de um link existente".").
3. **GCB-B0103** (`lotes[L6A].curso`, C05). Texto aprovado: "F20–F22" foi corretamente expandido para os três nomes (F20, F21, F22). Motivo da correção: `fonte_origem` só lista F20 e F22, mas o `depois` leva também o nome da F21, e o D1 exige `fonte_origem` para toda fonte trocada pela regra 2. Correção: `fonte_origem` = `T108_fontes_GCB.md, lote 6a, F20; T108_fontes_GCB.md, lote 6a, F21; T108_fontes_GCB.md, lote 6a, F22`. `antes` e `depois` sem mudança.

### 4.2 Linhas LIVRE e VERIFICAR aprovadas (60), com os pontos conferidos

- C10 internas (B0001 DELETAR "Só o fato e a fonte."; B0012, B0060, B0081 "não cobrado(s)" → "fica(m) fora do estudo"; B0036 DELETAR "; não há item sobre atalho"; B0061, B0094 "sem item" retirado dentro do parêntese): sentido mantido, sem fato novo, pontuação final certa.
- C01 "Lote" de produção: B0022 ("neste lote" → "dos itens 1 e 3 de TI e Dados"; o 6a tem itens com itemEdital P1-1 e P1-3, confirmado no pacote) e B0023 ("do lote" retirado; VOLÁTEIS → "pontos sujeitos a mudança … vêm sinalizados", o que continua verdadeiro após B0020, B0050 e B0125); B0086 e B0099 ("Lote 4 (item 6)" → "tópico 6 de TI e Dados": o Lote 4 tem itens P1-6, ética e responsabilidade digital no serviço público; tópico certo).
- C02 B0027 ("O item 6A-02 usa…" → "O item sobre mesclar células usa…"): código trocado pelo conceito, como o D1 permite. Ressalva sem reprovação: a frase continua sendo nota sobre a redação de um item; o que serve à candidata é que "na mesma linha ou coluna" não é definição exaustiva. A GCB pode simplificar na reconciliação, se quiser.
- VERIFICAR "sem armadilha (ancoragem)" (B0143, B0153, B0157, B0172, B0174): todas SUBSTITUIR por "Item de fixação: …", cada uma com o objeto que a justificativa de fato explica (mesclar × dividir; finalidade do slide mestre; link com edição ou só exibição; tipos de canal do Teams; escopos de apresentação no Meet). Regra 4 e D1, seção 1, item 4: certo. Nenhum MANTER.
- VERIFICAR VOLÁTIL (B0050, B0125, pegadinha P4 de PowerPoint, no curso e na lista de pegadinhas): "— VOLÁTIL; não vira item." → "— informação sujeita a mudança.", com a F7 trocada pelo nome. Certo.
- C06 TC/GI (B0141, B0145, B0147, B0149, B0151, B0155, B0161, B0163, B0167, B0170): "TC (" → "Armadilha: troca de conceito (", "GI invertida (" → "Armadilha: generalização indevida, em sentido invertido (", "TC invertida (" → "Armadilha: troca de conceito invertida ("; o parêntese que explica o mecanismo e a tentação continua inteiro em todas. Ressalva de forma: "invertida" sai de dois jeitos (B0145 × B0149); uniformizar é opcional.
- C05 em frase corrida (B0024–B0026, B0028, B0029, B0035, B0037, B0038, B0043, B0044, B0052, B0054, B0057, B0059, B0067, B0071, B0075–B0078, B0080, B0082, B0093, B0095–B0097, B0105, B0109, B0128, B0159, B0165): nome conforme a tabela; "(leitura de 08/10/2026)" e "verificado em 08/10/2026" mantidos; em B0075 e B0077, "(RFC 1939, F15)" e "(RFC 9051, F16)" viram o nome da fonte, que já traz o número da RFC (sem perda). Ressalva de estilo, sem reprovação: "Conforme Microsoft, documentação de suporte, "…"" e "a fonte Microsoft, documentação de suporte, "…" afirma" ficam pesadas, mas são gramaticais e seguem a forma de nome fixada pelo D1 (seção 2).

Nenhuma frase "Difere do item…" no lote 6a (regra 3 sem objeto). Nenhum enunciado, gabarito ou itemEdital tocado. Nenhum fato novo.

## 5. Pendência fora do universo da Parte B (para a GCB, sem reprovação de linha)

Após a aplicação, o texto do 6a ainda tem três instruções internas que o inventário não pegou, porque o regex C10 da GBQ casa "não entra em item", mas não "nada sobre isso entra em item" nem "não entram em item":
- `lotes[L6A].curso`, 1.1.2: "a fonte … NÃO descreve como ativar o acompanhamento; nada sobre isso entra em item."
- `lotes[L6A].curso`, 1.1.3: "A página não diz o que acontece com o conteúdo das células; nada sobre isso entra em item."
- `lotes[L6A].curso`, 3.2.2: "…não diz quem pode ver as conversas; esses pontos não entram em item além da descrição acima."
Elas não são das 199 ocorrências, então a Parte B não as cobre. A GCB decide em D1 se pede à GBQ ampliar o regex (gerando novas ocorrências) ou se as trata como linhas adicionais da Parte B na R2. Fora do universo, de menor peso: "abertas hoje" e "sem fonte aberta hoje" (1.0.1, 3.2.1) são tempo relativo da produção.

## 6. Contagem por lote e categoria (Parte B = só o lote 6a)

Ocorrências por categoria (199): C05 157, C10 16, C06 15, C02 6, C01 5.

Linhas por categoria declarada (175):

| categoria da linha | linhas | CORRIGIR |
|---|---|---|
| C05 | 144 | 1 (B0103, só metadado) |
| C06 | 15 | 0 |
| C10 | 7 | 0 |
| C01;C10 | 3 | 1 (B0058) |
| C01 | 2 | 0 |
| C05;C10 | 2 | 0 |
| C02;C10 | 1 | 1 (B0020) |
| C02 | 1 | 0 |
| total | 175 | 3 |

Contando cada categoria presente na linha: C05 em 146 linhas, C06 em 15, C10 em 13, C01 em 5, C02 em 2.

## 7. Para a R2

Só as três linhas da seção 4.1, em `saida/gcb/T108_substituicoes_GCB_parteB_v2.csv`. A R2 confere só essas linhas (e as três da seção 5, se a GCB mandar incluí-las).

## Anexo A — veredito por linha (175)

| id_edicao | caminho | cat. | modo | ação | regra | VERIFICAR | veredito |
|---|---|---|---|---|---|---|---|
| GCB-B0001 | lotes[L6A].resumo | C10 | LIVRE | DELETAR | 5 |  | APROVADO |
| GCB-B0002 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0003 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0004 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0005 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0006 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0007 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0008 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0009 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0010 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0011 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0012 | lotes[L6A].resumo | C10 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0013 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0014 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0015 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0016 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0017 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0018 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0019 | lotes[L6A].resumo | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0020 | lotes[L6A].resumo | C02;C10 | LIVRE | SUBSTITUIR | 5 | sim | CORRIGIR |
| GCB-B0021 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0022 | lotes[L6A].curso | C01;C10 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0023 | lotes[L6A].curso | C01;C10 | LIVRE | SUBSTITUIR | 5 | sim | APROVADO |
| GCB-B0024 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0025 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0026 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0027 | lotes[L6A].curso | C02 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0028 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0029 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0030 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0031 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0032 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0033 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0034 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0035 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0036 | lotes[L6A].curso | C10 | LIVRE | DELETAR | 5 |  | APROVADO |
| GCB-B0037 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0038 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0039 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0040 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0041 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0042 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0043 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0044 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0045 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0046 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0047 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0048 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0049 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0050 | lotes[L6A].curso | C05;C10 | LIVRE | SUBSTITUIR | 2 | sim | APROVADO |
| GCB-B0051 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0052 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0053 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0054 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0055 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0056 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0057 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0058 | lotes[L6A].curso | C01;C10 | LIVRE | SUBSTITUIR | 5 |  | CORRIGIR |
| GCB-B0059 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0060 | lotes[L6A].curso | C10 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0061 | lotes[L6A].curso | C10 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0062 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0063 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0064 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0065 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0066 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0067 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0068 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0069 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0070 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0071 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0072 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0073 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0074 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0075 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0076 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0077 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0078 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0079 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0080 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0081 | lotes[L6A].curso | C10 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0082 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0083 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0084 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0085 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0086 | lotes[L6A].curso | C01 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0087 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0088 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0089 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0090 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0091 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0092 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0093 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0094 | lotes[L6A].curso | C10 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0095 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0096 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0097 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0098 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0099 | lotes[L6A].curso | C01 | LIVRE | SUBSTITUIR | 5 |  | APROVADO |
| GCB-B0100 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0101 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0102 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0103 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | CORRIGIR |
| GCB-B0104 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0105 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0106 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0107 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0108 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0109 | lotes[L6A].curso | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0110 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0111 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0112 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0113 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0114 | lotes[L6A].curso | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0115 | lotes[L6A].pegadinhas[0].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0116 | lotes[L6A].pegadinhas[4].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0117 | lotes[L6A].pegadinhas[5].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0118 | lotes[L6A].pegadinhas[7].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0119 | lotes[L6A].pegadinhas[8].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0120 | lotes[L6A].pegadinhas[9].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0121 | lotes[L6A].pegadinhas[11].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0122 | lotes[L6A].pegadinhas[12].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0123 | lotes[L6A].pegadinhas[13].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0124 | lotes[L6A].pegadinhas[14].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0125 | lotes[L6A].pegadinhas[15].texto | C05;C10 | LIVRE | SUBSTITUIR | 2 | sim | APROVADO |
| GCB-B0126 | lotes[L6A].pegadinhas[16].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0127 | lotes[L6A].pegadinhas[18].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0128 | lotes[L6A].pegadinhas[19].texto | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0129 | lotes[L6A].pegadinhas[21].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0130 | lotes[L6A].pegadinhas[23].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0131 | lotes[L6A].pegadinhas[24].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0132 | lotes[L6A].pegadinhas[25].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0133 | lotes[L6A].pegadinhas[26].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0134 | lotes[L6A].pegadinhas[27].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0135 | lotes[L6A].pegadinhas[28].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0136 | lotes[L6A].pegadinhas[29].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0137 | lotes[L6A].pegadinhas[30].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0138 | lotes[L6A].pegadinhas[31].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0139 | lotes[L6A].pegadinhas[33].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0140 | lotes[L6A].pegadinhas[34].texto | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0141 | itens[6A-01].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0142 | itens[6A-01].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0143 | itens[6A-02].justificativa | C06 | LIVRE | SUBSTITUIR | 4 | sim | APROVADO |
| GCB-B0144 | itens[6A-02].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0145 | itens[6A-03].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0146 | itens[6A-03].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0147 | itens[6A-04].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0148 | itens[6A-04].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0149 | itens[6A-05].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0150 | itens[6A-05].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0151 | itens[6A-06].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0152 | itens[6A-06].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0153 | itens[6A-07].justificativa | C06 | LIVRE | SUBSTITUIR | 4 | sim | APROVADO |
| GCB-B0154 | itens[6A-07].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0155 | itens[6A-08].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0156 | itens[6A-08].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0157 | itens[6A-09].justificativa | C06 | LIVRE | SUBSTITUIR | 4 | sim | APROVADO |
| GCB-B0158 | itens[6A-09].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0159 | itens[6A-09].justificativa | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0160 | itens[6A-09].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0161 | itens[6A-10].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0162 | itens[6A-10].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0163 | itens[6A-11].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0164 | itens[6A-11].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0165 | itens[6A-11].justificativa | C05 | LIVRE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0166 | itens[6A-11].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0167 | itens[6A-12].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0168 | itens[6A-12].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0169 | itens[6A-12].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0170 | itens[6A-13].justificativa | C06 | LIVRE | SUBSTITUIR | 4 |  | APROVADO |
| GCB-B0171 | itens[6A-13].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0172 | itens[6A-14].justificativa | C06 | LIVRE | SUBSTITUIR | 4 | sim | APROVADO |
| GCB-B0173 | itens[6A-14].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |
| GCB-B0174 | itens[6A-15].justificativa | C06 | LIVRE | SUBSTITUIR | 4 | sim | APROVADO |
| GCB-B0175 | itens[6A-15].justificativa | C05 | TEMPLATE | SUBSTITUIR | 2 |  | APROVADO |

## Anexo B — script de conferência mecânica (python -I, somente leitura; rodado em cópia fora do repositório)

```python
# QA R1 T-108 parte B (gcb-cqfp) - somente leitura
import csv, json, re, hashlib, collections, importlib.util, os
R = 'C:/Users/Felipe/felipeRM_push/saida/'
HERE = 'C:/Users/Felipe/AppData/Local/Temp/qaBc'
raw = open(R + 'pacote/pacote.json', 'rb').read(); lf = raw.replace(b'\r\n', b'\n')
sha = hashlib.sha256(lf).hexdigest(); print('SHA', sha, sha == 'd43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed')
P = json.loads(lf.decode('utf-8'))
rows = list(csv.DictReader(open(R + 'gcb/T108_substituicoes_GCB_parteB.csv', encoding='utf-8', newline='')))
occ = list(csv.DictReader(open(R + 'pacote/T108_ocorrencias.csv', encoding='utf-8', newline='')))
spec = importlib.util.spec_from_file_location('inv', R + 'pacote/T108_inventario.py'); inv = importlib.util.module_from_spec(spec); spec.loader.exec_module(inv)
F = {cam: t for (lo, c, cam, t, e) in inv.campos(P, 'D')}
mine = [o for o in occ if o['arquivo'] == 'pacote.json' and o['gerencia'] == 'GCB' and o['lote'] == '6a']
univ = {o['id_ocorrencia']: o for o in mine if o['classe'] in ('PROCESSO', 'VERIFICAR')}
print('universo 6a', len(univ), collections.Counter(o['classe'] for o in mine))
print('edicoes', len(rows))
fails = collections.defaultdict(list)
cnt = collections.Counter()
for r in rows:
    for i in r['ids_ocorrencia'].split(';'):
        cnt[i] += 1
        if i not in univ: fails['id fora do universo'].append((r['id_edicao'], i))
        elif univ[i]['caminho'] != r['caminho']: fails['caminho difere'].append((r['id_edicao'], i))
    t = F.get(r['caminho'])
    if t is None: fails['caminho inexistente'].append(r['id_edicao']); continue
    if t.count(r['antes']) != 1: fails['antes nao literal/unico'].append((r['id_edicao'], t.count(r['antes'])))
    if r['acao'] == 'DELETAR' and r['depois'] != '': fails['DELETAR com depois'].append(r['id_edicao'])
    if r['acao'] != 'DELETAR' and r['depois'] == '': fails['depois vazio'].append(r['id_edicao'])
    if r['regra'] == '2' and not r['fonte_origem']: fails['regra 2 sem fonte_origem'].append(r['id_edicao'])
miss = set(univ) - set(cnt); dup = [i for i, v in cnt.items() if v > 1]
print('(a) cobertura: ids distintos', len(cnt), 'faltam', len(miss), 'duplicados', len(dup))
byc = collections.defaultdict(list)
for r in rows:
    t = F[r['caminho']]; s = t.find(r['antes']); byc[r['caminho']].append((s, s + len(r['antes']), r['id_edicao']))
for c, l in byc.items():
    l.sort()
    for a, b in zip(l, l[1:]):
        if b[0] < a[1]: fails['sobreposicao'].append((a[2], b[2]))
for r in rows:
    for i in r['ids_ocorrencia'].split(';'):
        if i in univ and univ[i]['casamento'] not in r['antes']: fails['casamento fora do antes'].append((r['id_edicao'], i))
fp = [o for o in mine if o['classe'] in ('FP-R1', 'FP-CONTEUDO')]
print('FP no 6a:', len(fp), collections.Counter(o['classe'] for o in fp))
for r in rows:
    if 'tecla F4' in r['antes']: print('  antes com tecla F4:', r['id_edicao'])
    for o in fp:
        if o['caminho'] == r['caminho'] and o['casamento'] in r['antes'] and o['casamento'] not in r['depois']:
            fails['FP possivelmente tocado'].append((r['id_edicao'], o['id_ocorrencia'], o['casamento']))
P2 = json.loads(lf.decode('utf-8'))
def setf(P, cam, v):
    L = {l['id']: l for l in P['lotes']}
    m = re.match(r'lotes\[(\w+)\]\.(curso|resumo)$', cam)
    if m: L[m.group(1)][m.group(2)] = v; return
    m = re.match(r'lotes\[(\w+)\]\.pegadinhas\[(\d+)\]\.(rotulo|texto)$', cam)
    if m: L[m.group(1)]['pegadinhas'][int(m.group(2))][m.group(3)] = v; return
    m = re.match(r'itens\[(.+)\]\.justificativa$', cam)
    I = {i['id']: i for i in P['itens']}; I[m.group(1)]['justificativa'] = v
RB = {r['id_edicao']: r for r in rows}
new = dict(F)
for c, l in byc.items():
    out = F[c]
    for s, e, eid in sorted(l, reverse=True):
        out = out[:s] + RB[eid]['depois'] + out[e:]
    new[c] = out; setf(P2, c, out)
oc2 = inv.varre(P2, 'D')
g6 = [o for o in oc2 if o['gerencia'] == 'GCB' and o['lote'] == '6a']
print('(d) pos-aplicacao 6a por classe:', collections.Counter(o['classe'] for o in g6))
for o in g6:
    if o['classe'] in ('PROCESSO', 'VERIFICAR'): print('   RESIDUO', o['caminho'], o['categoria'], o['casamento'], '|', o['trecho'][:140])
fp2 = [o for o in g6 if o['classe'] in ('FP-R1', 'FP-CONTEUDO')]
print('   FP antes', len(fp), 'depois', len(fp2), 'D-C05-4a878e59 presente:', any(o['id_ocorrencia'] == 'D-C05-4a878e59' for o in fp2))
print('   ids FP iguais:', set(o['id_ocorrencia'] for o in fp) == set(o['id_ocorrencia'] for o in fp2))
others = [o for o in oc2 if not (o['gerencia'] == 'GCB' and o['lote'] == '6a')]
print('   ocorrencias fora do 6a antes/depois:', len([o for o in occ if o['arquivo'] == 'pacote.json' and not (o['gerencia'] == 'GCB' and o['lote'] == '6a')]), len(others))
BAD = re.compile(r'(?<![\w])(?:F\d{1,2}|N\d{1,2}|U\d|GG\d|TB\d)(?![\w])|Lotes? \d|(?:neste|deste|do|no) lote|(?<![\w])(?:TC|IC|GI|AT)(?![\w])|\[TS\]|(?<![\w])QA(?![\w])|CQFP|VOLÁTIL|VOLÁTEIS|Difere d|(?<![\w.])v\d|(?:4C|5C|A5|6A|6B)-\d{2}|\(C\d+\)|par C\d|SEM ITEM|NÃO GABARITO|Só o fato|[Ee]rrata|[Rr]everificar|REVERIFICAR|produção|ancoragem')
for r in rows:
    m = BAD.search(r['depois'])
    if m: fails['(e) residuo no depois'].append((r['id_edicao'], m.group(0)))
for a, b in zip(P['itens'], P2['itens']):
    for k in a:
        if k != 'justificativa' and a[k] != b[k]: fails['(f) campo de item alterado'].append((a['id'], k))
for la, lb in zip(P['lotes'], P2['lotes']):
    for k in la:
        if k not in ('curso', 'resumo', 'pegadinhas') and la[k] != lb[k]: fails['(f) campo de lote alterado'].append((la['id'], k))
for k in P:
    if k not in ('lotes', 'itens') and P[k] != P2[k]: fails['(f) raiz alterada'].append(k)
for k, v in fails.items(): print('FALHA', k, len(v), v[:12])
if not fails: print('SEM FALHAS MECANICAS')
print('modo', collections.Counter(r['modo'] for r in rows), 'acao', collections.Counter(r['acao'] for r in rows), 'regra', collections.Counter(r['regra'] for r in rows))
print('cat ocorr', collections.Counter(univ[i]['categoria'] for i in univ), 'classe', collections.Counter(univ[i]['classe'] for i in univ))
print('campo edicoes', collections.Counter(re.sub(r'\[[^\]]*\]', '', r['caminho']) for r in rows))
json.dump({c: new[c] for c in byc}, open(os.path.join(HERE, 'novo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
a=set(o['id_ocorrencia'] for o in fp); b=set(o['id_ocorrencia'] for o in fp2)
print('FP so antes', [(o['id_ocorrencia'],o['casamento'],o['classe']) for o in fp if o['id_ocorrencia'] not in b])
print('FP so depois', [(o['id_ocorrencia'],o['casamento'],o['classe'],o['trecho'][:60]) for o in fp2 if o['id_ocorrencia'] not in a])
```
