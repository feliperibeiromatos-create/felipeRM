# T54_item5_decisao_2026-10-13.md — T-54, item (5) — 2026-10-13 — gerado por gce-gerencia

Objeto: comunicação da GBQ à GCE, para eventual errata (T-54, item (5), em TAREFAS.md; achado 11 de `saida/pacote/QA_T48_2026-10-13_gbq-cqe.md`; `saida/pacote/T48_reconciliacao_R1_2026-10-13.md`, tabela 2.3, item i). Base: `saida/gce/GCE_Lote3_padroes_GCE.md` (SHA-256 `cc17ec964b53…`), `saida/gce/GCE_Lote3_v2_CPP.md` (SHA-256 `a9c3fba59aaf…`, igual ao transportado por D-TRANSPORTE-B-L3), `saida/pacote/pacote.json` v1.3 (SHA-256 `fdcb7afdb4fb…`), `saida/estudante/DISCURSIVAS_padrao.md` e `saida/estudante/L3_estudo.md`. Leitura somente; nenhum arquivo de lote foi alterado.

## 1. Evidência

### (a) Nota R2 da D4 repetida na D5

- `pacote.json`, campo `discursivas`: D4 = questão (alínea "(e) DISCURSIVA" do Lote 3), D5 = peça (alínea "(f) PEÇA TÉCNICA" do Lote 3). As duas vêm de `GCE_Lote3_padroes_GCE.md` (o Lote 2 não tem D4/D5).
- No arquivo canônico da GCE as decisões R2, R3 e R4 aparecem UMA vez cada, no bloco "DECISÕES DE RECONCILIAÇÃO DA GCE" (linhas 14–23), e com objeto próprio:
  - linha 14: `R2. Alínea c da discursiva (R4 do Projeto): NÃO se exige enquadrar o` — objeto: alínea c da discursiva (e) = D4, aspecto (ix) e quesito 2.3 (Lei 9.610/1998). A peça (f) não tem alínea c nem aspecto sobre a Lei 9.610/1998.
  - linha 21: `R3. Voz como dado sensível (biométrico): nem exigido nem penalizado.` — objeto natural: peça, aspecto (vi) (linha 90 e "PONTOS PARA A RECONCILIAÇÃO", 2, linha 140: "(aspecto vi)").
  - linhas 22–23: `R4. Base legal do tratamento pelo poder público: aceitam-se o art. 23 e` / `o art. 7º, II ou III.` — objeto natural: peça, aspecto (vii) (linha 91).
- A repetição não está no texto da GCE. Nasce no gerador da GBQ: `saida/pacote/gerador_v1_3/p2.py`, linhas 394–411, monta `anexo = '\n\nNotas de correção (GCE, R2–R4)\n' + notas` com as linhas R2–R4 e o acrescenta ao `padrao` de D4 E de D5 (decisão de exportação da GBQ, T-27, `pacote_reconciliacao_2026-10-10.md`, seção 2(e)); o validador `validate.py` 275–278 exige o mesmo anexo nas duas.
- Efeito na edição do estudante: `DISCURSIVAS_padrao.md` 506–516 (D5, "Notas de correção") repete as linhas 507–513, `Alínea c da discursiva: NÃO se exige enquadrar o` … `o dispositivo correto.`, idênticas às linhas 407–413 da D4.

### (b) "que eu possa afirmar" no curso do Lote 3

- `GCE_Lote3_v2_CPP.md`, curso (a), seção 4.2 ("--- 4.2 DIREITOS AUTORAIS E ÉTICA NO USO DE IA PARA CONTEÚDO GERADO ---", linha 423), linhas 461–462, literal:
  - 461: `CONTROVERSO / NÃO GABARITO (N4; não há texto legal expresso nem`
  - 462: `jurisprudência firmada que eu possa afirmar):`
- Exportação: `pacote.json`, `lotes[3].curso` (L3), e `saida/estudante/L3_estudo.md` 421–422 (`CONTROVERSO / NÃO GABARITO (não há texto legal expresso nem` / `jurisprudência firmada que eu possa afirmar):`). A GBQ manteve a expressão por ser texto canônico da GCE e porque a deleção tornaria a afirmação absoluta (T48_reconciliacao_R1, 2.3-i).
- Segunda ocorrência no mesmo arquivo: linha 72, `jurisprudência firmada que eu possa afirmar fica NO CURSO, sinalizado` (N4, bloco de limites da produção, escrito em primeira pessoa da unidade do começo ao fim: "Esta unidade não a abriu", "não encontrei", "não os cito"). Esse bloco não é exportado (não está em `pacote.json` nem em `saida/estudante/`; só a linha 462 chega à candidata).
- A expressão sustenta uma ressalva de evidência: a ausência de texto legal ou jurisprudência firmada é afirmada no limite do que se pôde verificar, não como ausência absoluta. Deletá-la apagaria a ressalva.

## 2. D1 da GCE

| # | Ponto | Errata de forma da GCE? | Decisão |
|---|---|---|---|
| D1-T54-a | Nota R2 repetida na D5 | NÃO | O texto canônico da GCE está correto: R2–R4 aparecem uma vez, cada uma com seu objeto. A repetição é do anexo do gerador (domínio da GBQ). Delimitação, pela GCE, do alcance das próprias decisões: R2 vale só para a D4 (alínea c da discursiva). Na D5 o anexo fica só com R3 e R4 (é o que o achado 11 propõe). Na D4 o anexo fica como está (R2–R4): R3 e R4 não contradizem nada na D4, e retirá-las seria mudança fora do achado. Sem mudança de item, gabarito, padrão de resposta, aspecto, quesito, conceito ou valor: só sai da D5 uma nota de correção sem objeto nela. A aplicação é da GBQ na T-57 (T-54, item 5), sem tarefa nova da GCE. |
| D1-T54-b | "que eu possa afirmar" (curso 4.2, linha 462) | SIM, só a linha 462 | Troca mínima de uma palavra, "eu" → "se", com redação impessoal que conserva a ressalva de evidência (a afirmação continua limitada ao que se pode afirmar, e não fica absoluta). Sem mudança de sentido, item, gabarito, fonte, [TS], VOLÁTIL ou marca [V]. A linha 72 (N4, limites) fica como está: não é exportada e é registro de processo em primeira pessoa como o resto do bloco. |

Classificação: D1-T54-a AGORA (na T-57, pela GBQ); D1-T54-b AGORA (errata pela gce-cpp antes da regeração da T-57).

## 3. Erratas exatas

### 3.1 Errata única no arquivo da GCE (aplicar a gce-cpp)

Arquivo: `saida/gce/GCE_Lote3_v2_CPP.md` (base SHA-256 `a9c3fba59aafd21ed9d1f502cc16c610b6cd1389a22da2a350184080358e8ab7`).

E-1 — curso (a), 4.2, bloco "CONTROVERSO / NÃO GABARITO", linha 462 (vira 466 depois do registro abaixo):
- Onde se lê: `jurisprudência firmada que eu possa afirmar):`
- Leia-se: `jurisprudência firmada que se possa afirmar):`

E-2 — registro na Tabela de Correções do cabeçalho: inserir, logo depois da linha 35 (última linha da entrada T-44, `     GCB-CQFP, 08/10/2026)" após "fora dos objetos de avaliação"`) e antes da linha em branco 36, estas 4 linhas literais (5 espaços de recuo nas de continuação, como nas entradas existentes):

```
T-54 → (a), 4.2, bloco "CONTROVERSO / NÃO GABARITO" (errata de forma,
     D1 da GCE, T54_item5_decisao_2026-10-13.md; sem mudança de conteúdo,
     item, gabarito, fonte, troca sutil, volatilidade ou marca V): "que eu
     possa afirmar" → "que se possa afirmar"
```

Nada mais muda no arquivo. A linha 72 continua com "que eu possa afirmar".

### 3.2 Ajuste de exportação (aplicar a GBQ na T-57; não é errata da GCE)

- D5 (`pacote.json`, `discursivas[4].padrao`): o anexo de notas passa a ser só R3 e R4, cópia literal das linhas 21–23 de `GCE_Lote3_padroes_GCE.md`, isto é, sai do anexo da D5 o trecho literal das linhas 14–20 (`R2. Alínea c da discursiva (R4 do Projeto): NÃO se exige enquadrar o` … `    o dispositivo correto.`). Rótulo do anexo da D5: sugestão da GCE `Notas de correção (GCE, R3–R4)`, salvo D1 diversa da GBQ sobre o rótulo (a edição do estudante já o exibe só como "Notas de correção").
- D4: sem mudança (anexo R2–R4, linhas 14–23).
- Efeito esperado em `saida/estudante/DISCURSIVAS_padrao.md`: só saem as 7 linhas da D5 que hoje estão em 507–513; D1–D4 e o resto da D5 idênticos.
- Gerador: `p2.py` (anexo por discursiva) e `validate.py` 275–278 (D4 = linhas 14–23; D5 = linhas 21–23).
- Curso do L3: o gerador lê o arquivo da GCE já com a E-1; esperado em `L3_estudo.md` (linha 422 atual) `jurisprudência firmada que se possa afirmar):` e, em `pacote.json`, `lotes[3].curso` com 1 troca ("eu" → "se") e nada mais. A linha do relatório que registra "que eu possa afirmar" como mantido (`relatorio_R1.py` 123 e equivalente da v1.3) sai ou passa a registrar a errata T-54 da GCE.

## 4. Instrução à gce-cpp (aplicação da E-1 e da E-2)

1. Copiar `saida/gce/GCE_Lote3_v2_CPP.md` para o scratchpad (`…/s5/t54gce/GCE_Lote3_v2_CPP.antes.md`) e conferir o SHA-256 da base (`a9c3fba59aaf…`). Se diferir, parar e devolver à GCE.
2. Aplicar a E-2 (inserção de 4 linhas após a linha 35) e a E-1 (troca da linha 462 → 466), com o texto exato da seção 3.1. Sem git. Não tocar TAREFAS.md, PARA_PRESIDENCIA.md, DECISOES.md, estado/, `GCE_Lote3_padroes_GCE.md` nem arquivos da GBQ.
3. Conferência por script (Python, no scratchpad), com saída no relatório:
   - `difflib` por linhas antes × depois: exatamente 2 operações — inserção das 4 linhas da E-2 entre as linhas 35 e 36 (depois: 36–39) e troca de 1 linha (antes 462 → depois 466) da E-1; nenhuma outra linha diferente (lista das demais linhas igual, descontado o deslocamento de +4).
   - Na linha trocada, o diff de caracteres é só `eu` → `se`.
   - Contagens por linha (sem juntar quebras): "que eu possa afirmar" 2 → 1 (resta a linha 72); "que se possa afirmar" 0 → 2 (linha 39, fim da entrada T-54 da Tabela, e linha 466 do curso).
   - Tamanho em bytes e SHA-256 antes e depois.
4. Gravar o relatório `saida/gce/lote3_errata3_2026-10-13.md` (primeira linha no formato do CLAUDE.md; antes/depois literal; saída do script) e entregar à gce-cqfp, com a GCE em cópia.
5. A gce-cqfp confere por script próprio (os da produção não servem de prova) e dá veredito APROVADO ou CORRIGIR; depois a GCE reconcilia. A T-57 regenera o pacote só depois do APROVADO (a regeração lê o arquivo atual).

## 5. BLOCO TAREFAS

```
T-58; GCE; Errata de forma do curso do Lote 3 (D1 da GCE, saida/gce/T54_item5_decisao_2026-10-13.md, D1-T54-b; T-54 item 5), sem mudar conteúdo, item, gabarito, fonte, [TS], VOLÁTIL ou marca [V]: saida/gce/GCE_Lote3_v2_CPP.md, curso 4.2, bloco "CONTROVERSO / NÃO GABARITO", linha 462: "que eu possa afirmar" → "que se possa afirmar", com registro "T-54" na Tabela de Correções do cabeçalho (seção 3.1, texto exato) e conferência por script (diff só nas linhas da errata); QA gce-cqfp por script próprio; precede a regeração da T-57; a parte (a) do item 5 (R2 fora do anexo da D5) é da GBQ na própria T-57 (seção 3.2), sem tarefa nova; AGORA; PENDENTE; gce-cpp → gce-cqfp → gce-gerencia; saida/gce/GCE_Lote3_v2_CPP.md + saida/gce/lote3_errata3_2026-10-13.md + QA da gce-cqfp
```

(Id T-58 = próximo livre na fila em 13/10/2026; se já tiver sido usado, o próximo livre.)

## 6. BLOCO PARA_PRESIDENCIA

nenhum.

(Previsto, não emitido agora: depois do APROVADO da gce-cqfp e da reconciliação da GCE, o `GCE_Lote3_v2_CPP.md` muda de SHA-256 e diverge do arquivo transportado ao Projeto por D-TRANSPORTE-B-L3; o transporte ao Projeto do claude.ai é matéria do Fundador e será pedido pela GCE como gatilho E na reconciliação da T-58, no rito da D-TRANSPORTE-B-L3.)
