# GBQ_reconciliacao_2026-10-10_lote1.md — T-13, T-21, T-23, T-26, T-30 — 2026-10-10 — gerado por gbq-gerencia

Papel: gbq-gerencia (com as funções de gce-gerencia no domínio da GBQ). Nível: D1. Regras lidas: CLAUDE.md (com o Adendo v2.1), DECISOES.md (D-LEI-15352, D-LEI15352-PROV, D-ADERENCIA, D-QA-PENDENTE, D-SIM0-V02, D-PACOTE-6, D-LOTE6A/6B-CANONICO, D-FUNDADOR-AGORA-1), TAREFAS.md (T-13, T-21, T-23, T-26, T-27, T-30), regras/pacote_contrato.md, regras/estilo_banca.md, saida/banco/T03_arbitragem_2026-10-09.md, saida/pacote/pacote_reconciliacao_2026-10-10.md.
Conferência: por script, somente leitura (git diff/git show HEAD, csv, json, cópias das fontes oficiais no scratchpad da sessão, s3/t13 e s3/t21; scripts em s3/gbq_rec). A única escrita fora deste arquivo foi a coluna observacoes de 19 linhas do banco (seção 6) e um append em TAREFAS.md. Simulados não foram editados.

## 1. Vereditos

| Tarefa | Produtora / QA | Veredito | Base da conferência |
|---|---|---|---|
| T-13 | qa-normativo | CONCLUÍDA, sem gatilho D | 17/17 MANTIDO conferido (seção 2) |
| T-21 | qa-normativo | CONCLUÍDA, sem gatilho D | BQ-0036 e BQ-0040 mantidos; revogação da Res. CNJ 332/2020 confirmada (seção 3) |
| T-23 | gbq-estilo | CONCLUÍDA; resíduos de forma vão à T-37 | Os 4 ajustes da GBQ aplicados; mudanças de cabeçalho aceitas (seção 4) |
| T-26 | gbq-csc | CONCLUÍDA; D1 de leitura da regra 2; errata menor vai à T-38 | Contrato v1.1 confere com a D1 de pacote_reconciliacao (seção 5) |
| T-30 | gbq-csc | CONCLUÍDA | 180/180 contra a v2, os d-G dos Lotes 6 e o pacote v1 (seção 6) |

## 2. T-13 — QA normativo LGPD × Lei 15.352/2026

Alegações conferidas por script:
- Fontes: o SHA-256 das cópias locais é igual ao do relatório. l13709compilado.htm = ac3b7b37…ad80 e l15352.htm = b54c6875…6b04.
- Conjunto: os 17 ids da tabela são os 17 da linha T-13 (BQ-0002 a 0008, 0023, 0024, 0025, 0031, 0032, 0037, 0045, 0046, 0056 e 0057).
- Gabarito: o do relatório é igual ao do banco em 17/17 (BQ-0031 é X, anulado=sim). Os 17 estão em P2-4.1.
- Literalidade: 33 trechos entre aspas da coluna "Trecho vigente decisivo" e da lista de alterações foram conferidos. Os 33 estão no texto extraído do compilado ou da Lei 15.352/2026; nenhum está ausente.
- O compilado tem 0 ocorrência de "15.211". O art. 55-A traz "Fica criada a Agência Nacional de Proteção de Dados (ANPD), autarquia de natureza especial". O art. 41-A da Lei 15.211/2025 (vigência em 17/3/2026) aparece na Lei 15.352/2026.
- BQ-0003: o texto_integral usa "Autoridade Nacional".

Veredito: CONCLUÍDA. Resultado: 17 MANTIDO, 0 DIVERGENTE e nenhuma candidata a gatilho D.

Efeitos:
- D-SIM0-V02: a condição "T-13 concluída sem gatilho D" está cumprida.
- T-27, item (4), e regra 5 do contrato v1.1: a condição da T-13 para o SIM-0 v0.2 entrar em "simulados" está cumprida.
- A entrega à candidata continua matéria do Fundador e não foi decidida aqui.

Decisões D1 sobre as observações (regra: D-LEI-15352 e D-LEI15352-PROV; a GBQ governa banco/banco.csv; observacoes não é gabarito, texto nem aderência, e por isso a matéria é de nível D1):
- (a) Os 17 itens recebem o registro da passagem pelo QA normativo em observacoes. Nenhum gabarito, texto_integral, aderência ou subitem mudou.
- (b) BQ-0003: entra uma nota de vigência sobre a denominação vigente (Agência Nacional de Proteção de Dados, art. 55-A, redação da Lei 15.352/2026). O texto do item fica literal, como no caderno.
- (c) BQ-0007 e BQ-0008: o fundamento é doutrinário e o texto vigente não o contraria. Fica a nota; os itens não mudam e continuam aptos nas mesmas condições de antes.
- (d) BQ-0046: fica a nota de paráfrase do art. 33, I, aceita no definitivo. O item continua indício C5 no guia e não serve de modelo de redação.
- (e) BQ-0057: fica a nota de que o ECA Digital não alterou o art. 14.
- (f) Simulado 0 v0.2: as referências "T-13 (qa-normativo…)" do gabarito e uma nota de denominação no item 41 (BQ-0003), só no gabarito, vão à T-36. Na folha a nota não entra, porque induziria o E por motivo alheio ao item.
- Classe das observações do QA: (1) AGORA, aplicada (banco) e T-36 PRÓXIMO (simulado); (2) a (4) AGORA, aplicadas (banco).

## 3. T-21 — QA normativo do Marco Civil e das Resoluções CNJ

Alegações conferidas por script:
- Fontes: o SHA-256 das 6 páginas (3429, 6001, 3496, 3975, 4663 e l12965.htm) é igual ao do relatório.
- Literalidade: os trechos abaixo estão no texto extraído. No art. 46, a única diferença é um espaço antes da vírgula, que vem do link HTML.
  - Res. 332/2020, art. 7º, § 3º, com "Situação Revogado" e "Resolução n. 615, de 11 de março de 2025".
  - Res. 615/2025: art. 8º, §§ 2º e 3º; art. 46 ("Revoga-se a Resolução CNJ nº 332/2020…"); art. 47 (120 dias).
  - Marco Civil, art. 3º, caput, II e III.
- Banco: BQ-0036 tem gabarito C e BQ-0040, gabarito E, e os dois têm anulado=nao.

Veredito: CONCLUÍDA, sem gatilho D. BQ-0036 fica mantido (C). BQ-0040 fica mantido (E), e a sucessora reforça o E.

Decisão D1 sobre a nota de vigência de BQ-0040 (regra: EVIDÊNCIA de CLAUDE.md, que exige "verificado em [data]" e fonte oficial; o gabarito não muda, então não é D2):
- Banco: aplicada a nota em observacoes. Diz que a Res. CNJ 332/2020, citada no comando, foi revogada pela Res. CNJ 615/2025 (art. 46), que a regra está hoje no art. 8º, § 3º, da 615/2025 e que as Res. 335/2020, 396/2021 e 468/2022 estão vigentes e não têm efeito no item. A aderência continua DIRETA P1-6 (T-03), e o item continua apto a simulado final.
- Simulado 0 v0.2, item 27: a nota vai à T-36.
  - Na folha, entra uma linha neutra logo abaixo do Comando 15, com o comando mantido literal e sem o conteúdo da regra. Ela é necessária porque o comando remete a norma revogada e a candidata precisa saber qual texto vale.
  - No gabarito, entra a nota completa na linha 27.
  - Item, ordem, numeração, comando, texto e gabarito não mudam.
- A T-36 não bloqueia a T-27. O comando exportado é o literal do bloco (regra 3 do contrato), e a nota acompanha o simulado no pacote seguinte (T-12). A T-36 deve vir antes de qualquer entrega do SIM-0 à candidata, que é matéria do Fundador.
- Classe: banco AGORA, aplicado; simulado PRÓXIMO (T-36).

## 4. T-23 — regras/estilo_banca.md v1.1.1

Conferência (git diff HEAD, 28+/15−, só no arquivo do guia):
- (1) Seção 2: P1-5.3 passou de 7/4/3 para 6/4/3, e entrou a linha P1-5 com 1/0/0 (BQ-0009).
- (2) Tabela C1: BQ-0009 está em P1-5.
- (3) Seção 6: as ressalvas 1, 4, 6 e 7 seguem o texto da revisão da GBQ (T03_arbitragem, ajuste 3).
- (4) O AVISO final traz a fórmula literal do ajuste 4 da GBQ.
- Nenhum padrão, contagem de padrão ou recomendação mudou. As linhas alteradas ficam no cabeçalho, nas seções 2, 3.7, 6 e 7 e no AVISO.

Mudanças fora da lista da tarefa, aceitas em D1 como forma:
- Linha de topo, Versão e Data: são consequência da versão v1.1.1 que a própria linha T-23 fixa como saída.
- Título da seção 7 ("Mudanças entre versões") e subseção "v1.0 → v1.1 (revisada pela GBQ, T-03)": cumprem o ajuste "seção 7 com 'revisada pela GBQ (T-03)'" e dão lugar ao registro v1.1 → v1.1.1. A tabela histórica da v1.0 → v1.1 fica como registro da época, inclusive a anotação "(sujeito à revisão da GBQ)" do E5.

Resíduos, que não são vício da T-23 porque estavam fora da lista de ajustes. Ficam para a T-37, sem mudar padrão, contagem ou recomendação:
- Seção 1, linha de BQ-0025: ainda diz "A GBQ deve confirmar essa inclusão". Deve passar a dizer "confirmada pela GBQ (T-03, D1)".
- 3.5 (E5): a última frase do item "Mudança" ainda condiciona a ampliação à preferência da GBQ. Deve passar a dizer "ampliação aceita pela GBQ (T-03, D1)".
- 3.12 (C6): a última frase ("Se a GBQ os reclassificar…") deve passar a dizer "C6 aceito pela GBQ (T-03, D1)".
- Vigência, desatualizada depois desta reconciliação:
  - 3.3 (E3): "Vigência não verificada… T-13… BQ-0040 também está pendente".
  - 3.11 (C5): "Está pendente de qa-normativo (T-13)".
  - Ressalva 7: "T-13 no qa-normativo"; "Também pendentes: BQ-0036 e BQ-0040".
  - Esses trechos devem registrar a T-13 (17/17 MANTIDO) e a T-21 (BQ-0036 e BQ-0040 mantidos; nota de vigência de BQ-0040: Res. CNJ 332/2020 revogada pela 615/2025, art. 8º, § 3º), com remissão a este arquivo.

Veredito: CONCLUÍDA. A v1.1.1 orienta produção quanto à tipologia. Os resíduos não mudam o uso do guia.

## 5. T-26 — regras/pacote_contrato.md v1.1

Conferência (git diff HEAD contra a D1 de saida/pacote/pacote_reconciliacao_2026-10-10.md e a linha T-26):
- (1) O campo `volatil` é opcional, aparece só quando é true e cobre VOLÁTIL e REVERIFICAR (R1-N), com a nota "inapto a simulado final até a reverificação de 4–8/1/2027". Confere.
- (2) As três expressões de aderência parcial estão na regra 2. Confere.
- (3) Para comando e textoBase, valem as colunas do banco quando existirem (T-29). Até lá, valem o bloco "Comando" do simulado e a nota de texto-base. Confere.
- (4) A tabela de fonte por lote é igual, linha a linha, à tabela da seção 1 de pacote_relatorio.md (L1 a L6B, banco, simulados e edital), e há regra de precedência. Confere.
- (5) Na regra 5, "simulados" só leva simulado pronto, com as condições T-25 e T-13; senão sai `[]` com o motivo. Confere.
- Nenhum campo obrigatório mudou, e `versao` continua 1. O bloco JSON de exemplo continua válido.

Prompt EXPORTAR alinhado: aceito em D1. Ele citava `saida/lote*/RECONCILIADO.md` e colunas inexistentes. Mantê-lo assim contrariaria a regra 4 do próprio contrato, e o alinhamento é consequência direta dos itens (3) a (5).

Achados da conferência, que não invalidam a tarefa:
- (i) Regra 2 sem cláusula de caixa. Aplicada literalmente ("parcial" minúsculo), ela classificaria como "direta" 4 itens PARCIAIS (BQ-0001, 0015, 0036 e 0055), cujo observacoes traz só "PARCIAL". Sem distinção de maiúsculas e minúsculas, o resultado é 60/60 igual ao mapa do Simulado 0 v0.2 e ao pacote v1.
  - Decisão D1, com base em D-ADERENCIA: a regra 2 se lê sem distinção de maiúsculas e minúsculas, como a T-05 a aplicou. A leitura vale desde já para a T-27.
  - A redação vai à T-38.
- (ii) O exemplo JSON passou a mostrar `"volatil": true` em BQ-0001. Esse item não é VOLÁTIL e é PARCIAL no banco, embora o exemplo diga "direta" desde a v1. É só ilustração, mas induz erro. Vai à T-38.

Veredito: CONCLUÍDA. A condição "T-26 CONCLUÍDA" da T-27 está cumprida, e a T-38 não bloqueia a T-27.

Gatilho: nenhum. Pela D1 de pacote_reconciliacao, o contrato muda só por errata de forma retrocompatível, sem campo obrigatório novo, e isso não é D2. O aceite cabe ao gatilho A do pacote.json (T-27).

## 6. T-30 — saida/gbq/claude_GBQ_Registro_AUTORAL_v3.md

Conferência independente (script próprio, sem reuso do verify.py da produtora):
- A primeira linha está no formato. As 150 linhas da v2 estão idênticas na v3 (gabarito, subitem, [TS] e marca). Há 30 linhas novas.
- Contra os d-G atuais dos Lotes 6a e 6b, já com a errata de forma T-17 da GCB nos arquivos de trabalho, gabarito, subitem, [TS] e VOLÁTIL batem em 30/30. O diff da T-17 não toca nenhuma linha de d-G.
- Contra o pacote v1: os ids são iguais (180), o gabarito bate em 180/180 e o `volatil` bate nos 14 VOLÁTEIS. L3-Q21 é REVERIFICAR no registro e entra como `volatil` na T-27, conforme decidido.
- Totais: 180 itens; 89 C/91 E; 91 [TS]; marcas 14 VOLÁTIL + 1 REVERIFICAR = 15; 165 aptos a final. Nos 30 novos: 14 C/16 E, 16 [TS] e 5 VOLÁTEIS (6A-01, 09, 10, 14 e 15).
- Cobertura de 1 a 4, recontada: 1.1 2/3, 1.2 3/3, 1.3 2/2, 1.4 0/2, 2 1/1, 2.1 4/4, 3.1 3/3, 3.2 0/1, 3.3 0/1, 4.1 4/4, 4.2 3/3, 4.3 3/3. Os alertas 1.4, 3.2 e 3.3 são corretos, porque todos os itens desses subitens são VOLÁTEIS. Nenhum enunciado foi copiado.
- Forma: a tabela do 6b não tem coluna "Marca", mas tem 0 VOLÁTIL, como a 1-C, o 2, o 4-C e o 5-C na v2. Isso é aceito.

Veredito: CONCLUÍDA. A v3 substitui a v2 como registro GBQ vigente (regra 4 do contrato v1.1) para a T-27 e as próximas montagens. O Simulado 1 canônico (D-SIM1-CANONICO) não é afetado, porque as 150 linhas da v2 estão intactas.

Gatilho: nenhum. O registro é metadado da GBQ e reflete decisões já aceitas (D-LOTE6A-CANONICO e D-LOTE6B-CANONICO). Ele chega à Presidência pelo gatilho A do pacote (T-27). O espelho no Projeto do claude.ai (claude/GBQ_Registro_AUTORAL_v3.md) cabe ao Fundador e à Secretaria.

## 7. banco/banco.csv — alteração aplicada (D1, seções 2 e 3)

- Foram alteradas 19 linhas, só a coluna observacoes, todas entre BQ-0001 e BQ-0066:
  - BQ-0002 a 0008, 0023, 0024, 0025, 0031, 0032, 0037, 0045, 0046, 0056 e 0057: registro da T-13, com notas próprias em 0003, 0007, 0008, 0031, 0046 e 0057;
  - BQ-0036 e BQ-0040: a remissão a "T-21" foi substituída pelo resultado, com a nota de vigência em BQ-0040.
- As linhas BQ-0067 a BQ-0112, que estão em QA na T-07, ficaram intactas. Nas 19 linhas alteradas, os outros 14 campos não mudaram. O cabeçalho e as outras 93 linhas de dados são idênticos byte a byte.
- Formato: csv.reader/csv.writer, delimiter ';', lineterminator '\n', QUOTE_MINIMAL. Antes de gravar, uma leitura e regravação sem mudança deu resultado idêntico. O arquivo está sem BOM e com LF.
- SHA-256 de antes: d9ab2c68c2e016b9…; de depois: 4ebee3510c9bf0a4…. A cópia de antes está em s3/gbq_rec/banco_antes_rec.csv.
- Sem efeito de exportação:
  - nenhum texto novo contém "parcial", "temática ampla", "apenas por tema", "VOLÁTIL", "REVERIFICAR", "QA PENDENTE" ou "texto-base";
  - a regra 2, sem distinção de caixa, continua dando 60/60 igual ao mapa do Simulado 0;
  - continuam 4 itens VOLÁTEIS de banco.

## 8. Tarefas novas (append único em TAREFAS.md)

- T-36 (PRÓXIMO): notas de vigência e de QA normativo no Simulado 0 v0.2. É ajuste mecânico, sem mudar item, ordem, numeração, comando, texto ou gabarito. Não bloqueia a T-27 e vem antes de qualquer entrega.
  - Alcance do item (2): a troca da referência "T-13 (qa-normativo…)" atinge 16 linhas do gabarito, itens 40 a 50 e 52 a 56, conferidas por grep. São os 17 da T-13 menos BQ-0031, que é anulado e está fora do simulado.
- T-37 (PRÓXIMO): errata de forma do estilo_banca, v1.1.1 → v1.1.2 (resíduos da seção 4).
- T-38 (PRÓXIMO): errata de forma do contrato, v1.1 → v1.1.1 (achados (i) e (ii) da seção 5). Não bloqueia a T-27, que aplica a D1 (i) desde já.

## 9. Gatilhos

Nenhum. Não há pacote concluído para aceite nem necessidade fora do domínio. Também não há conflito acima de D1, decisão D2 ou matéria do Fundador nova: a entrega do SIM-0 já é reservada ao Fundador por D-SIM0-V02 e não está madura antes da T-36 e da T-27. PARA_PRESIDENCIA.md não foi tocado.
