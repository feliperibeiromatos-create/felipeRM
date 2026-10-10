# lote2_errata_2026-10-10.md — T-28 — 2026-10-10 — gerado por gce-cpp

Objeto: errata de forma do curso do Lote 2 (`saida/gce/GCE_Lote2_v2_CPP.md`), seção "Contexto institucional" (linhas 149–152 do HEAD). Base: D-DEREP ("Derep (antigo DETAQ)", Ato da Mesa 251/2026); errata E4/N4 de `saida/gce/GCE_Lote2_consolidacao_GCE.md`; item de forma de `saida/pacote/pacote_reconciliacao_2026-10-10.md`. Sem mudança de gabarito, item, fonte ou marca [V].

## Antes → depois

ANTES:
```
registradas pelo Departamento de Taquigrafia, Revisão e Redação (DETAQ)
[V 08/10/2026 — F2], hoje Departamento de Registro Oficial e Redação
Parlamentar, por força do Ato da Mesa nº 251/2026 [V 08/10/2026 — F8;
NORMATIVO — QA]. A prática oficial inclui ...
```
DEPOIS:
```
registradas pelo Derep (antigo DETAQ) [V 08/10/2026 — F2],
Departamento de Registro Oficial e Redação Parlamentar, por força do
Ato da Mesa nº 251/2026 [V 08/10/2026 — F8; NORMATIVO — QA]. A prática oficial inclui ...
```
Observação: "hoje" foi suprimido porque "antigo" já carrega a ideia; o nome por extenso do Derep e o Ato 251/2026 permanecem na frase. As duas marcas [V] ficaram coladas às mesmas afirmações.

## Verificações (script, `git show HEAD:saida/gce/GCE_Lote2_v2_CPP.md` contra o arquivo atual; só leitura)

1. Diff por linhas: 1 único bloco alterado (HEAD linhas 150–153 → 150–152), exatamente o trecho acima; nenhuma outra linha mudou. OK.
2. Marcas [V]: 18 no HEAD, 18 agora, listas idênticas (mesmo conteúdo e mesma ordem após ordenação). OK.
3. "Gabarito" (1/1) e "Julgue" (1/1): contagens iguais; nenhuma linha de item, gabarito ou fonte tocada (consequência do item 1). OK.
4. Ocorrências de "DETAQ" / "Taquigrafia, Revisão e Redação" no arquivo atual: 7 ao todo, e a única no corpo do curso é a do trecho corrigido, agora na forma aceita "Derep (antigo DETAQ)". As 6 restantes estão no cabeçalho de notas da produtora, nas fontes e nas notas, fora do texto do curso e sem alteração por regra de errata (não mexer em fonte): nota C3 (linha 40), nota A1 (linha 50), título da fonte F6 "Rol do DETAQ" (linha 78), descrição de F8 com o nome antigo do departamento no Ato (linha 86), nota N4 (linha 105) e nota N8 (linha 118). Todas descrevem o que a fonte diz e já remetem ao Ato 251/2026; pela E4 valem como "Derep (antigo DETAQ)". Nenhuma exige alteração para o pacote, que só exporta o curso.
5. Forma do L1 "(Derep, antigo DETAQ; Ato…)" (E10): mantida, não tocada.

Estado: aplicada, pronta para gce-cqfp. Não bloqueia o pacote; o texto do curso do L2 que o EXPORTAR v1.1 (T-27) lê já está na forma de D-DEREP.

## QA — gce-cqfp — 2026-10-10
Objeto: errata de forma T-28 no "Contexto institucional" do curso do Lote 2 (saida/gce/GCE_Lote2_v2_CPP.md). Revisora: gce-cqfp (opus); produtora: gce-cpp (sonnet). Nada editado fora deste relatório; git usado só para leitura.

### 1. Diff (git diff / git show HEAD, só leitura) — CONFERE
- `git diff` do arquivo: 1 hunk (HEAD 150–153 → 150–152), exatamente o trecho antes→depois deste relatório; nenhuma outra linha alterada. Trecho dentro de (a) CURSO (início linha 124; (b) RESUMO em 518).
- Contagens HEAD → atual: "[V " 18→18 (F2 e F8 continuam nas mesmas afirmações; F6 intacta); [NORMATIVO — QA] 7→7; [TS] 20→20; VOLÁTIL 4→4; linhas "Q<n>" 66→66; "Gabarito" 1→1; "Julgue" 1→1; SEM FONTE 0→0; QA PENDENTE 0→0. Nenhum item, gabarito, fonte ou marca [V] alterado.

### 2. Conformidade com D-DEREP e E4/N4 — CONFERE
- D-DEREP (DECISOES.md, l. 11) e CLAUDE.md (NOMENCLATURA): forma "Derep (antigo DETAQ)", Ato da Mesa 251/2026 → aplicada literalmente no corpo do curso (linha 150).
- E4 (GCE_Lote2_consolidacao_GCE.md): denominação atual "Departamento de Registro Oficial e Redação Parlamentar – Derep", antigo DETAQ, pelo Ato 251/2026 → o nome por extenso e o Ato seguem na mesma frase, com [V F8; NORMATIVO — QA]; coerente com F8 (linhas 85–88: o Ato transforma o DETAQ em Derep).
- Demais ocorrências de "DETAQ" (linhas 40, 50, 78, 86, 105, 118) estão em notas, fontes e limites, fora do curso; manter é correto (não se altera título de fonte) e E4 já as cobre. Forma do L1 (E10) não tocada.

### 3. Observação (não bloqueante)
- Linha 152 ficou com 122 caracteres (as demais ~70): sem reembrulho. Cosmético; não afeta conteúdo nem exportação. Correção opcional na próxima errata do arquivo (BACKLOG).

### 4. Veredito
**APROVADO.** Mudança única, de forma, conforme D-DEREP e E4; 0 itens, 0 gabaritos, 0 fontes e 0 marcas [V] alterados. Segue para gce-gerencia.
