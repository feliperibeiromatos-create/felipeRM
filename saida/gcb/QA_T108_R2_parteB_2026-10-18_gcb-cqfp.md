# QA_T108_R2_parteB_2026-10-18_gcb-cqfp.md — T-108, GCB, Parte B (lote 6a), QA R2 (última rodada) — 2026-10-18 — gerado por gcb-cqfp

Objeto: `saida/gcb/T108_substituicoes_GCB_parteB_v2.csv` e `saida/gcb/T108_producao_notas_GCB_v2_parteB.md`, conforme a seção 6 de `saida/gcb/T108_D1_pos_R1_GCB_2026-10-18.md`. Revisadas só as 5 linhas corrigidas (B0020, B0058, B0103, B0145, B0149) e as 7 novas (B0176 a B0182). As linhas aprovadas na R1 não voltaram ao mérito. Este parecer só revisa: não corrige nem redige texto.

Texto-base: `saida/pacote/pacote.json` v1.10, SHA-256 com LF = d43c32de4b8afb221da91d94573adc426e4ce0fab0de1b1994b149e9d70c2fed (confere).
Script próprio (python -I, somente leitura, cópia em memória): `r2b.py` no scratchpad da sessão. Nada foi gravado no repositório além deste parecer.

## Veredito geral

**APROVADO: 12 de 12 linhas do objeto. 0 REPROVADO (0%).** Nenhuma linha volta à D1 da GCB. Não há pendência na Parte B.

## 1. Mecânica

| Checagem | Resultado |
|---|---|
| (a) Linhas fora do objeto iguais à v1, byte a byte | OK. Os registros brutos foram comparados por id: o cabeçalho é igual, as 170 linhas fora do objeto são iguais, a ordem da v1 é mantida e nenhuma linha usa CRLF. Só diferem as 5 corrigidas e as 7 novas (175 → 182 linhas). |
| (b) `antes` literal e único | OK. Os 182 `antes` são literais e aparecem uma vez no campo do `caminho` (critério da seção 2 do D1 de método). Registro: no pacote inteiro, 5 `antes` do objeto também aparecem em outros campos: B0145 (7 vezes), B0179 e B0180 (3), B0181 e B0182 (2). Isso não afeta a aplicação, que é feita campo a campo. |
| (b) Aplicação sem sobreposição | OK. Nenhuma das 182 edições se sobrepõe a outra. |
| (c) Cobertura | OK. 206 = 199 ocorrências PROCESSO/VERIFICAR do 6a no `T108_ocorrencias.csv` + GCB-EXTRA-05 a 11. Cada uma aparece uma única vez, sem id estranho e sem falta. |
| (d) Varredura do `T108_inventario.py` após aplicar a v2 | OK. Antes: PROCESSO 190, VERIFICAR 9, FP-CONTEUDO 35, FP-R1 1. Depois: PROCESSO 0, VERIFICAR 0, FP-CONTEUDO 35 (mesmos casamentos), FP-R1 1. |
| (d) "A tecla F4" | OK. Casada por texto: está fora de todo `antes` e ocorre 1 vez no curso, antes e depois da aplicação. |
| (d) Resíduo, checagem (6) da seção 5 | OK. Nenhum casamento no curso, no resumo, nas pegadinhas e nas justificativas do 6a para: "(O11)", "fundamenta item", "neste chat", "não sutil", "entra em item", "entram em item", "(CI,", "hoje"/"Hoje", "ITENS REAIS", "TC invertida", "indevida invertida", "em sentido invertido", "invertida (", "reverificar", "conferir de novo" e "NÃO cobra". ", às avessas" aparece 2 vezes (B0145 e B0149). |
| (e) DELETAR e SUBSTITUIR | OK. Nenhum DELETAR tem `depois` preenchido e nenhum SUBSTITUIR tem `depois` vazio. |
| (e) Enunciado, gabarito, itemEdital e demais campos | OK. Zerados os campos editáveis (curso, resumo, pegadinhas e justificativas 6A-*), o restante do pacote v1.10 é idêntico ao pacote com a v2 aplicada. |

## 2. Mérito, linha a linha

| id_edicao | Tipo | Veredito | Motivo |
|---|---|---|---|
| GCB-B0020 | corrigida (QA R1, 4.1-1) | APROVADO | O `depois` repete, palavra por palavra, o texto do parecer R1. A frase "conferir de novo entre 4 e 8/1/2027" saiu. A `nota` também repete o texto do parecer. Os outros campos ficaram iguais à v1. |
| GCB-B0058 | corrigida (QA R1, 4.1-2) | APROVADO | `depois` = "fica fora do estudo o ponto", como no parecer. A frase final fica "por isso fica fora do estudo o ponto "como alterar a permissão de um link existente"." e não contradiz mais a frase anterior. |
| GCB-B0103 | corrigida (QA R1, 4.1-3) | APROVADO | `fonte_origem` passou a listar F20, F21 e F22, no texto exato do parecer. `antes` e `depois` ficaram iguais à v1. |
| GCB-B0145 | corrigida (D1, seção 3) | APROVADO | "Armadilha: generalização indevida, às avessas (". Só "em sentido invertido" foi trocado; o resto do `depois` é igual à v1. |
| GCB-B0149 | corrigida (D1, seção 3) | APROVADO | "Armadilha: troca de conceito, às avessas (". É a forma exata da seção 3, e só mudou o rótulo. |
| GCB-B0176 | nova (EXTRA-05) | APROVADO | Saiu só a oração "nada sobre isso entra em item". O limite do curso ("NÃO descreve como ativar o acompanhamento.") continua, e o ponto final fica. `antes` alargado e ação SUBSTITUIR, como manda a seção 2. |
| GCB-B0177 | nova (EXTRA-06) | APROVADO | Saiu só a oração. A frase "A página não diz o que acontece com o conteúdo das células." continua e está correta. |
| GCB-B0178 | nova (EXTRA-07) | APROVADO | DELETAR com `depois` vazio. O resultado ("…não diz quem pode ver as conversas.") mantém a informação útil e termina com ponto final. |
| GCB-B0179 | nova (EXTRA-08) | APROVADO | Saiu "; não sutil". O resultado é "Armadilha: troca de conceito (inversão).", e a explicação do item ficou inteira. |
| GCB-B0180 | nova (EXTRA-09) | APROVADO | Mesmo tratamento da B0179, em 6A-11. O resultado é "(inversão)" e o resto ficou inteiro. |
| GCB-B0181 | nova (EXTRA-10, caso b) | APROVADO | "Nas páginas de suporte consultadas em 08/10/2026", a forma exata da seção 4. A data consta das 22 linhas do lote 6a em `T108_fontes_GCB.md` ("08/10/2026 (todas, abertas com sucesso)"). Não há fato novo. |
| GCB-B0182 | nova (EXTRA-11, caso c) | APROVADO | "sem fonte consultada", sem data, como manda o caso (c). O resultado é "(conceito geral; sem fonte consultada para detalhes)". O "; sem item" já tinha saído por linha aprovada na R1. Não há sobreposição. |

## 3. Outros pontos do checklist

- Fontes e URLs: o objeto da R2 não traz fonte, URL nem fato novo. A única data introduzida, 08/10/2026, foi conferida na tabela do lote. Não houve abertura de URL, porque nenhuma afirmação nova depende de fonte.
- Normativo: nenhuma linha do objeto cita lei, então não há item PENDENTE.
- Itens AUTORAL ([TS], estilo Cebraspe): nenhum enunciado, gabarito ou itemEdital foi alterado. As linhas B0145, B0149, B0179 e B0180 mexem só no rótulo da justificativa, sem mudar o conceito trocado.
- As notas de produção da Parte B (`T108_producao_notas_GCB_v2_parteB.md`) batem com a conferência independente: 5 corrigidas, 7 novas, 182 linhas no total e nenhuma absorção.
