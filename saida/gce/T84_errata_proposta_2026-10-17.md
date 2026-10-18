# T84_errata_proposta_2026-10-17.md — T-84 — 2026-10-17 — gerado por gce-cpp

Objeto: errata OPCIONAL de forma no canônico da GCE (T-81; D-RT81-03, saida/pacote/T81_reconciliacao_2026-10-17.md). PROPOSTA: nada foi aplicado no canônico. Nenhum gabarito, enunciado, item, fonte, [TS], VOLÁTIL ou marca [V] muda; só a frase indicada.

## Errata 1 — ACEITA (proposta): remissão "ver Lote 1-C", curso do Lote 2

Arquivo: saida/gce/GCE_Lote2_v2_CPP.md, linhas 310–311 (curso do 2.1/2.2, fim do bloco "Ligação com o 1.4"). A linha 311 é a única com "Lote 1-C" no arquivo.

Onde se lê (literal, 2 linhas):
```
a identificação por NOME é cadastro ou atribuição humana. Adendo de
pegadinha do título do edital: ver Lote 1-C.
```
Leia-se:
```
a identificação por NOME é cadastro ou atribuição humana. Adendo de
pegadinha do título do edital: ver o complemento do Lote 1 (adendo ao 1.4).
```
Alteração mínima: só a linha 311 muda ("Lote 1-C" → "o complemento do Lote 1 (adendo ao 1.4)"); a linha 310 fica intacta.

Fundamento:
- Camada de dados: o Lote 1-C é "complemento do Lote 1" (D-LACUNAS) e o seu item (a) é, literalmente, "ADENDO AO CURSO DO 1.4 — A PEGADINHA DO TÍTULO DO EDITAL" (saida/gce/GCE_Lote1C_v2_CPP.md, linha 35). A nova frase descreve esse conteúdo sem depender do rótulo de lote.
- Camada do estudante (v1.8): o 1-C virou o bloco "## Complemento" no fim do curso do Lote 1; "o complemento do Lote 1" aponta para ele, e "Lote 1-C" não existe mais ali.
- A frase não traz o rótulo "1-C" (rótulo de produção, da lista de menções de processo da D-T12-V13 (a)) e vale nas duas camadas sem condicional.
- Forma pura: nenhuma afirmação de conteúdo, fonte ou gabarito se altera; é idêntica à v1.7 em substância (D-RT81-03: "não é processo").
- Se aceita, absorve-se na próxima ocorrência da T-12 (sem abrir versão, T-12: "itens só de forma não abrem versão"). A GBQ deve, nessa ocasião, conferir que o gerador não depende do texto "Lote 1-C" (verificação de consistência da GBQ; esta unidade não leu o gerador).

## Errata 2 — SEM ERRATA: nota N4 de saida/gce/GCE_Lote3_v2_CPP.md

Local: linhas 75–77 ("jurisprudência firmada que eu possa afirmar fica NO CURSO, sinalizado").

Motivo para não propor:
- Já decidido em D1-T54-b / saida/gce/T54_item5_decisao_2026-10-13.md: a troca "eu" → "se" aplicou-se só à linha do curso (que chega à candidata). A N4 é bloco de limites da produção, escrito em primeira pessoa do começo ao fim ("esta unidade não o leu", "não encontrei", "não os cito"), e NÃO é exportado (não está em pacote.json nem em saida/estudante/).
- Trocar só a N4 para impessoal deixaria o bloco N1–N6 heterogêneo; trocar o bloco inteiro ultrapassa "só a frase indicada" e não tem efeito sobre a candidata.
- A expressão sustenta a ressalva de evidência da produção (limite do que a unidade pôde verificar). O ganho de forma é nulo, o risco de mexer em registro de processo é maior que o benefício.
- Registro e fecha: a N4 permanece como está.

## Resumo
1 errata proposta (Lote 2, linha 311); 1 "sem errata" (N4 do Lote 3). Nada aplicado. Encaminhar ao gce-cqfp (QA de forma) e depois à gce-gerencia (gatilho A da errata).
