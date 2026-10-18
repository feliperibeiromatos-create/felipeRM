# QA_T108_R1_parteC_2026-10-18_gcb-cqfp.md — T-108 (ORDEM_V15_C, limpeza), QA R1 da GCB, Parte C (lotes 5, 5-C, 6b) — 2026-10-18 — gerado por gcb-cqfp

Objeto: saida/gcb/T108_substituicoes_GCB_parteC.csv (155 edições, GCB-C0001 a GCB-C0155), com saida/gcb/T108_fontes_GCB.md. Roteiro: seção 5 de saida/gcb/T108_D1_GCB_2026-10-18.md. Texto-base: saida/pacote/pacote.json v1.10, SHA-256 LF d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed (conferido). Somente leitura: a QA não editou CSV, fonte, pacote, TAREFAS, DECISOES nem PARA_PRESIDENCIA; sem commit. A produtora não gravou arquivo de notas para a Parte C; os pontos dela foram julgados abaixo (seção 4).

## 1. Veredito da Parte C

APROVADO COM RESSALVAS. REPROVADO: 0/155 (0,0%). CORRIGIR: 5/155 (3,2%), com correção exata: GCB-C0006 e GCB-C0097 (texto) e GCB-C0002, C0004, C0005 (só a coluna `regra`). APROVADO: 150/155. Sem GATE (limite 30%). R2: só as 5 linhas CORRIGIR, em parteC_v2, mais a linha nova da tabela de fontes (A-1).

## 2. Conferência mecânica (script próprio, python -I, somente leitura; scratchpad qa_parteC.py)

Não existe T108_conferir_tabela.py da GBQ; o script da produtora (parteA/B) não foi usado.

| checagem | resultado |
|---|---|
| (a) cobertura: universo GCB, pacote.json, PROCESSO+VERIFICAR, lotes 5/5-C/6b = 180 (71/27/82) | OK: 180 ids, cada um em exatamente uma edição; 0 faltando, 0 extra; caminho de cada id = caminho da linha |
| (b) `antes` literal e único no campo | OK 155/155; cada `antes` contém o casamento de cada id; sem sobreposição de edições no mesmo campo; casamentos repetidos cobertos o número certo de vezes |
| (c) FP-CONTEUDO (39, todos no 6b) intactos; FP-R1 | OK; a Parte C não tem FP-R1 (o único da GCB, D-C05-4a878e59, é do 6a) |
| (d) trocas aplicadas em cópia; varredura com saida/pacote/T108_inventario.py (varre) | lote 5: 68 P + 3 V → 0; 5-C: 24 P + 3 V → 0; 6b: 78 P + 4 V → 0, FP-CONTEUDO 39 → 39 |
| (e) `depois` sem código de fonte (F/N/U/GG/TB+dígito), item, par, "lote", QA/CQFP, TC/IC/GI/AT, [TS], VOLÁTIL, "Difere", instrução interna (sem item, PENDENTE, não afirmar, nunca dizer, Só o fato), versão, produção/errata/especificação, "sem armadilha" | OK 0 resíduo pelas 10 categorias do inventário. Exceção fora do inventário: código "CI" (A-1) |
| (f) só curso, resumo, pegadinhas[].texto, pares[].como, justificativa; enunciado, gabarito, itemEdital e todo o resto idênticos (JSON comparado com os campos editados zerados) | OK |
| "verificado em" e datas | OK: nenhuma linha reduz "verificado em" nem datas |
| ações / modos | SUBSTITUIR 142, DELETAR 13, MANTER 0; LIVRE 129, TEMPLATE 26; VERIFICAR 10 (3 VOLÁTIL do L5 → SUBSTITUIR; 7 "sem armadilha" → SUBSTITUIR) |

Contagem por lote e categoria (ocorrências): 5 — C01 3, C03 1, C05 41, C06 14, C07 1, C10 11 (71); 5-C — C02 15, C03 2, C06 10 (27); 6b — C01 4, C05 53, C06 15, C07 3, C08 2, C10 5 (82). Edições por lote: 5 = 58, 5-C = 21, 6b = 76.

## 3. Tabela de fontes (amostra de 5 por lote, contra o arquivo do lote)

| lote | códigos amostrados | resultado |
|---|---|---|
| 5 (GCB_Lote5_v3_canonica_GCB-CPP.md, l. 29–38) | U1, U2, U4, GG4, TB2 | nomes compatíveis, nenhuma fonte nova, data 08/10/2026 = lote. U2: o nome "página de instalação do Power BI Desktop" vem da descrição e do caminho da URL da l. 31; aceito. Conferida a tabela inteira do lote: falta o código CI (l. 38), ver A-1 |
| 5-C (GCB_Lote5C_v1_GCB-CPP.md, l. 9) | nenhum código | confere: "Nenhuma fonte de fornecedor foi necessária"; 0 código de fonte no arquivo |
| 6b (GCB_Lote6b_v2_producao_auto.md, l. 27–42) | F2, F4, F7, F11, F12 | todos conferem (nome, editor, título; 08/10/2026 por acesso direto); F12 com "(Windows Server 2003, conteúdo arquivado)" = l. 39 |

Nomes no `depois` × tabela, 100% das linhas C05: todos conferem; diferenças só nos 5 nomes abreviados declarados (ponto 1) e no fechamento de parêntese fundido com o trecho citado (C0140, C0141, C0143, C0146, C0150: legível, aprovado).

URLs reabertas pela QA hoje (18/10/2026, curl): rfc-editor.org/rfc/rfc1034 (200; "This RFC introduces domain style names, their use for Internet mail and…", l. 37 do .txt), cartilha.cert.br/ransomware/ (200; "torna inacessíveis os dados armazenados em um equipamento"), help.tableau.com/…/tableau_product_overview.htm (200; "A free platform to explore, create, and publicly share", "A self-hosted platform", "fully hosted"). Os três trechos citados nas justificativas 6B-04, 6B-08 e A5-16 conferem.

## 4. Pontos da produtora

1. Cinco nomes abreviados (C0018, C0022, C0024, C0030, C0053) porque data e título já estão na frase: APROVADO. Em todos ficam o editor e um identificador único (título do módulo ou data de publicação), sem fonte nova nem fato novo.
2. Deleção extra no 5C-08 (C0075, "É, entre os itens 5C, o mais próximo do item A5-20: …"): APROVADO. A frase é comparação entre itens com dois códigos (5C, A5-20; ocorrência D-C02-29b6398e), da mesma natureza da nota "Difere…" (regra 3 por analogia; também coberta pela regra de redação do D1 "código de item → DELETAR"). O princípio ("dirigir a atenção") continua explicado no mesmo texto ("Curso 8.4, método: dirigir a atenção (… título que afirma a conclusão)"). Não conflita com a D-ABSORCAO-V110: essa decisão só fixou que a errata T-83 (D-TRANSPORTE-L5C-T83) seria absorvida na v1.10, e foi (o `antes` casa literal no pacote v1.10); a T-108 é ordem posterior do Fundador sobre o texto da v1.10 e não toca o canônico GCB_Lote5C_v1 (v1.2). Registro pedido à GCB (R-1): a reconciliação deve dizer que o trecho da errata T-83 foi absorvido na v1.10 e retirado pela T-108, para que a fidelidade da gbq-cqe do pacote novo não o leia como absorção perdida.
3. "lote" de produção → tópico do edital: APROVADO em C0034, C0036, C0037 (L5 = P1-7.1 e 8.1–8.4; o item 7 só tem 7.1, logo "itens 7 e 8" está certo), C0094 (tópico 3, correio eletrônico), C0104 (tópico 1, OneDrive), C0081 (retirada). CORRIGIR em C0097: governança digital é só o tópico 4 (edital/TI_itens_1_4_P1.md: "4 Conceitos gerais de segurança e governança digital"); "tópicos 2 e 4" sai.
4. 6b, curso 4.0.2 (C0097), retirada de "(a especificação previa o item "se houver base")": APROVADO; é instrução de especificação, sem informação para a candidata. A linha fica CORRIGIR só pelo ponto 3.
5. "invertida" → ", às avessas" (C0059 5C-01, C0128 6B-02, C0151 6B-14, C0154 6B-15): APROVADO. Os quatro itens têm gabarito C e o parêntese seguinte ("tentação: … → marcar E") mantém o mecanismo; sentido preservado. Ressalva R-2: a Parte B usou "troca de conceito invertida"; na consolidação a GCB escolhe uma só forma para as três partes (sugestão, não exigida: "Armadilha em item certo: …"), sem R2 por isso.

## 5. Achados

- A-1 (CORRIGIR, GCB-C0006; lacuna do inventário): em lotes[L5].curso, "(CI, verificado pela CQFP em 8/10/2026)" contém o código de fonte CI, definido em GCB_Lote5_v3_canonica_GCB-CPP.md, l. 38 ("CI — Google Cloud, Data Studio "Conversational Analytics — Code Interpreter" (verificada pela CQFP em 8/10/2026 …)"). O padrão de fonte do T108_inventario.py (F/N/U/GG/TB) não pega CI, e o CSV de ocorrências não tem id para ele; a C0006 tirou só "pela CQFP" e deixou o código. Correção exata: `antes` = `(CI, verificado pela CQFP em 8/10/2026)` (único no campo; conferido), `depois` = `(Google Cloud, Data Studio, "Conversational Analytics — Code Interpreter", verificado em 8/10/2026)`, regra 2, `fonte_origem` = `T108_fontes_GCB.md, lote 5, CI`; e linha nova na tabela do Lote 5: `| 5 | CI | Google Cloud, Data Studio, "Conversational Analytics — Code Interpreter" | GCB_Lote5_v3_canonica_GCB-CPP.md, linha 38 (seção FONTES DE FERRAMENTA, cabeçalho na linha 29) | 08/10/2026 (verificada pela CQFP) | Código fora do padrão do inventário; ocorrência sem id no CSV. |`. A GCB avisa a GBQ (método/inventário) para a contagem final e para as Partes A e B (procurar códigos de duas letras fora do padrão).
- A-2 (CORRIGIR, GCB-C0097): `depois` = `Não foi aberta fonte institucional que defina o termo, e o edital não o detalha; por isso, este material não traz item sobre governança digital (tópico 4 de TI e Dados).`
- A-3 (CORRIGIR, metadado, GCB-C0002, C0004, C0005): coluna `regra` 4 → 5. VOLÁTIL não é prefixo de mecanismo (regra 4 da ordem); a Parte B registra o mesmo caso como 5 (GCB-B0023). Texto aprovado como está.
- Registro, sem veredito (fora das 10 categorias, não pedido pela ordem): restam no texto marcas temporais de produção sem data ("A leitura de hoje do …", "fonte aberta hoje" em 6B-06 e no curso 4.1/4.2 do 6b) e a remissão "(seção ITENS REAIS)" em 6B-06; a GCB decide se leva à T-108 ou a ocorrência seguinte (R-3). A coluna `regra` = 5 para QA/produção/instrução interna é convenção comum às partes (a regra 5 da ordem é "não alterar enunciado…"); a GCB registra a convenção na reconciliação.

## 6. Mérito, linha a linha (LIVRE 129 e VERIFICAR 10 lidos no contexto do campo; TEMPLATE 26: nome 100% contra a tabela, forma lida em todas)

Critérios aplicados: sentido preservado; mecanismo explicado após a troca de TC/IC/GI/AT (expansões conferidas na legenda do Lote 5, l. 248: TC troca de conceito; GI generalização indevida; AT atribuição errada de técnica; IC inversão de causa e efeito); nenhum fato novo; "verificado em" e base legal mantidos; "Difere…" saiu inteira e só ela (C0060, C0062, C0064, C0067, C0069, C0072, C0074, C0077, C0079: cada justificativa fecha na frase anterior); "Item de fixação" conferido contra o enunciado nos 7 VERIFICAR; português.

| id_edicao | lote | caminho | cat. | modo | ação | veredito | observação |
|---|---|---|---|---|---|---|---|
| GCB-C0001 | 5 | lotes[L5].resumo | C10 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0002 | 5 | lotes[L5].resumo | C10 | LIVRE | SUBSTITUIR | CORRIGIR | CORRIGIR (só metadado): regra 4 → 5 (VOLÁTIL não é prefixo TC/IC/GI/AT; alinhar à Parte B, GCB-B0023). Texto aprovado. |
| GCB-C0003 | 5 | lotes[L5].resumo | C10 | LIVRE | SUBSTITUIR | APROVADO | PENDENTE em linguagem comum; sentido mantido |
| GCB-C0004 | 5 | lotes[L5].curso | C10 | LIVRE | SUBSTITUIR | CORRIGIR | CORRIGIR (só metadado): regra 4 → 5. Texto aprovado. |
| GCB-C0005 | 5 | lotes[L5].curso | C10 | LIVRE | SUBSTITUIR | CORRIGIR | CORRIGIR (só metadado): regra 4 → 5. Texto aprovado. |
| GCB-C0006 | 5 | lotes[L5].curso | C07 | LIVRE | SUBSTITUIR | CORRIGIR | CORRIGIR: resíduo de código de fonte "CI" fora do inventário (ver achado A-1). antes → (CI, verificado pela CQFP em 8/10/2026) ; depois → (Google Cloud, Data Studio, "Conversational Analytics — Code Interpreter", verificado em 8/10/2026) ; regra 2; fonte_origem "T108_fontes_GCB.md, lote 5, CI" (linha nova na tabela). |
| GCB-C0007 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0008 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0009 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0010 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0011 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0012 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0013 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0014 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0015 | 5 | lotes[L5].curso | C10 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0016 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0017 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0018 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO | ponto 1 (nome abreviado): APROVADO |
| GCB-C0019 | 5 | lotes[L5].curso | C10 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0020 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0021 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0022 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO | ponto 1: APROVADO |
| GCB-C0023 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0024 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO | ponto 1: APROVADO |
| GCB-C0025 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0026 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0027 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0028 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0029 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0030 | 5 | lotes[L5].curso | C05 | LIVRE | SUBSTITUIR | APROVADO | ponto 1: APROVADO ("segundo o Google Cloud Blog"; data já na frase) |
| GCB-C0031 | 5 | lotes[L5].curso | C10 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0032 | 5 | lotes[L5].curso | C10 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0033 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0034 | 5 | lotes[L5].curso | C01 | LIVRE | SUBSTITUIR | APROVADO | ponto 3: L5 = 7.1 e 8.1–8.4; correto |
| GCB-C0035 | 5 | lotes[L5].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0036 | 5 | lotes[L5].curso | C01 | LIVRE | SUBSTITUIR | APROVADO | ponto 3: correto |
| GCB-C0037 | 5 | lotes[L5].pegadinhas[42].texto | C01 | LIVRE | SUBSTITUIR | APROVADO | ponto 3: correto |
| GCB-C0038 | 5 | itens[A5-02].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0039 | 5 | itens[A5-03].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0040 | 5 | itens[A5-04].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0041 | 5 | itens[A5-06].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0042 | 5 | itens[A5-07].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0043 | 5 | itens[A5-08].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0044 | 5 | itens[A5-09].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0045 | 5 | itens[A5-09].justificativa | C03 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0046 | 5 | itens[A5-10].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0047 | 5 | itens[A5-11].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0048 | 5 | itens[A5-12].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0049 | 5 | itens[A5-13].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0050 | 5 | itens[A5-14].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0051 | 5 | itens[A5-14].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0052 | 5 | itens[A5-15].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0053 | 5 | itens[A5-15].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO | ponto 1: APROVADO |
| GCB-C0054 | 5 | itens[A5-15].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0055 | 5 | itens[A5-16].justificativa | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0056 | 5 | itens[A5-17].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0057 | 5 | itens[A5-17].justificativa | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0058 | 5 | itens[A5-19].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0059 | 5-C | itens[5C-01].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | ponto 5: APROVADO (ressalva R-2) |
| GCB-C0060 | 5-C | itens[5C-01].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0061 | 5-C | itens[5C-02].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0062 | 5-C | itens[5C-02].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0063 | 5-C | itens[5C-03].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0064 | 5-C | itens[5C-03].justificativa | C02;C03 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0065 | 5-C | itens[5C-04].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; frase confere com o enunciado |
| GCB-C0066 | 5-C | itens[5C-05].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; confere |
| GCB-C0067 | 5-C | itens[5C-05].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0068 | 5-C | itens[5C-06].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0069 | 5-C | itens[5C-06].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0070 | 5-C | itens[5C-07].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0071 | 5-C | itens[5C-07].justificativa | C03 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0072 | 5-C | itens[5C-07].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0073 | 5-C | itens[5C-08].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0074 | 5-C | itens[5C-08].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0075 | 5-C | itens[5C-08].justificativa | C02 | LIVRE | DELETAR | APROVADO | ponto 2: APROVADO; sem conflito com a D-ABSORCAO-V110 (A-3) |
| GCB-C0076 | 5-C | itens[5C-09].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; confere |
| GCB-C0077 | 5-C | itens[5C-09].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0078 | 5-C | itens[5C-10].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0079 | 5-C | itens[5C-10].justificativa | C02 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0080 | 6b | lotes[L6B].resumo | C10 | LIVRE | DELETAR | APROVADO |  |
| GCB-C0081 | 6b | lotes[L6B].resumo | C01;C10 | LIVRE | SUBSTITUIR | APROVADO | ponto 3: correto |
| GCB-C0082 | 6b | lotes[L6B].resumo | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0083 | 6b | lotes[L6B].resumo | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0084 | 6b | lotes[L6B].resumo | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0085 | 6b | lotes[L6B].resumo | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0086 | 6b | lotes[L6B].resumo | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0087 | 6b | lotes[L6B].resumo | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0088 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0089 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0090 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0091 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0092 | 6b | lotes[L6B].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0093 | 6b | lotes[L6B].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0094 | 6b | lotes[L6B].curso | C01 | LIVRE | SUBSTITUIR | APROVADO | ponto 3: tópico 3 = correio eletrônico; correto |
| GCB-C0095 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0096 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0097 | 6b | lotes[L6B].curso | C01;C08;C10 | LIVRE | SUBSTITUIR | CORRIGIR | CORRIGIR: escopo errado do tópico (governança digital é só o tópico 4). depois → Não foi aberta fonte institucional que defina o termo, e o edital não o detalha; por isso, este material não traz item sobre governança digital (tópico 4 de TI e Dados). A retirada de "(a especificação previa o item…)" fica APROVADA. |
| GCB-C0098 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO | português aceitável (aposto); ver R-3 sobre "hoje" |
| GCB-C0099 | 6b | lotes[L6B].curso | C07 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0100 | 6b | lotes[L6B].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0101 | 6b | lotes[L6B].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0102 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0103 | 6b | lotes[L6B].curso | C10 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0104 | 6b | lotes[L6B].curso | C01 | LIVRE | SUBSTITUIR | APROVADO | ponto 3: tópico 1 = OneDrive; correto |
| GCB-C0105 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0106 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0107 | 6b | lotes[L6B].curso | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0108 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0109 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0110 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0111 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0112 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0113 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0114 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0115 | 6b | lotes[L6B].curso | C10 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0116 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0117 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0118 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0119 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0120 | 6b | lotes[L6B].curso | C07;C08 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0121 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0122 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0123 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0124 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0125 | 6b | lotes[L6B].curso | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0126 | 6b | lotes[L6B].pares[8].como | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0127 | 6b | itens[6B-01].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0128 | 6b | itens[6B-02].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | ponto 5: APROVADO (R-2) |
| GCB-C0129 | 6b | itens[6B-03].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0130 | 6b | itens[6B-04].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; confere |
| GCB-C0131 | 6b | itens[6B-04].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0132 | 6b | itens[6B-05].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; confere |
| GCB-C0133 | 6b | itens[6B-05].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0134 | 6b | itens[6B-06].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0135 | 6b | itens[6B-07].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0136 | 6b | itens[6B-07].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0137 | 6b | itens[6B-08].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; confere |
| GCB-C0138 | 6b | itens[6B-08].justificativa | C05 | TEMPLATE | SUBSTITUIR | APROVADO |  |
| GCB-C0139 | 6b | itens[6B-09].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0140 | 6b | itens[6B-09].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0141 | 6b | itens[6B-09].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0142 | 6b | itens[6B-10].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0143 | 6b | itens[6B-10].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0144 | 6b | itens[6B-10].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0145 | 6b | itens[6B-11].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | VERIFICAR; confere |
| GCB-C0146 | 6b | itens[6B-11].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0147 | 6b | itens[6B-11].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0148 | 6b | itens[6B-12].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0149 | 6b | itens[6B-13].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0150 | 6b | itens[6B-13].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0151 | 6b | itens[6B-14].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | ponto 5: APROVADO (R-2) |
| GCB-C0152 | 6b | itens[6B-14].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0153 | 6b | itens[6B-14].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |
| GCB-C0154 | 6b | itens[6B-15].justificativa | C06 | LIVRE | SUBSTITUIR | APROVADO | ponto 5: APROVADO (R-2) |
| GCB-C0155 | 6b | itens[6B-15].justificativa | C05 | LIVRE | SUBSTITUIR | APROVADO |  |

## 7. R2

A gcb-cpp grava saida/gcb/T108_substituicoes_GCB_parteC_v2.csv mudando só GCB-C0002, C0004, C0005, C0006 e C0097, conforme as correções exatas acima, e acrescenta a linha CI do Lote 5 em T108_fontes_GCB.md; a gcb-cqfp confere só essas linhas e a linha da tabela. As 150 linhas APROVADAS não voltam à QA.
