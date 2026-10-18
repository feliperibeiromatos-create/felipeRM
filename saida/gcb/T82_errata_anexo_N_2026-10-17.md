# T82_errata_anexo_N_2026-10-17.md — T-82 — 2026-10-17 — gerado por qa-normativo-da

Objeto: errata do Anexo N do Lote D6 (saida/gcb/D6_anexo_N_mapa_normativo.md), dúvida 1 da reconciliação T-72 da GCB (saida/gcb/T72_reconciliacao_2026-10-17.md, seções 3 e 4). Ciclo s11c3.

## 1. Fontes (verificado em 17/10/2026)
- LGPD compilada: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm — HTTP 200, 230.913 bytes, SHA-256 f4173715eed0f53b1b1bb86b469c19318e8146349642156bd117f7e2f46877ed.
- LAI: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm — HTTP 200, 109.489 bytes, SHA-256 7c9a3dc7e78b6e9d596ac631eb55d68ff20c24d5edb4348bd9e42bb82730ad20.
- URLs as registradas no Anexo N, seção 1, localizadas por busca na T-72; nenhuma construída de memória. Nenhuma fonte não oficial usada. Texto íntegro (0 caracteres corrompidos).

## 2. Hash do Anexo N
- Antes: 8D44006779DBEC47725EB973B3BC703A56186FE9D0F18C2E925AA50699A3FCFB
- Depois: 57E8C64D4F27FE2C7549FF9F9B16C16848A51558E9AA181A0ED48C2F85D3E80E

## 3. Corrigido (1)
| Dispositivo | Onde se lia | Leia-se | Fundamento (verificado em 17/10/2026, URL da LGPD acima) |
|---|---|---|---|
| LGPD art. 8º, § 5º | Vigência "— (revogado)"; Observação "Revogado." | Vigência "art. 65, II (24 meses após a publicação)"; Observação "vigente, redação original" | No compilado, texto normal, sem tachado e sem nota de alteração ou revogação; o texto transcrito no Anexo confere literalmente. Falso positivo da extração, causado pela palavra "revogado" no próprio texto. |

## 4. Varredura do mesmo padrão
- Linhas varridas: 715 (LAI 251; LGPD 464) = 701 dispositivos contados + 14 linhas fora da contagem (2 de redação anterior tachada da LAI; 12 de texto de alteração citada: LAI arts. 43 e 44; LGPD art. 60).
- Critério: estado revogado/vetado e nota de redação do Anexo comparados com texto, tachado e nota do compilado, nos dois sentidos (marcado sem base ou com base e sem marca).
- Divergências: 1 (a do item 3).

## 5. Confirmados (verificado em 17/10/2026)
- Revogados, LGPD: art. 7º, § 1º; art. 7º, § 2º; art. 55-A, § 1º; § 2º; § 3º; art. 55-B; art. 55-C, V (7). LAI: nenhum.
- Vigentes com "revog-" no próprio texto, LGPD: art. 8º, § 6º; art. 9º, § 2º; art. 15, III; art. 18, IX (4), mais o art. 8º, § 5º depois da errata.
- Vetados: todas as linhas "(VETADO)" do Anexo, sem divergência. LAI: art. 7º, VIII; art. 19; § 1º "(VETADO)"; art. 35. LGPD: as linhas "(VETADO)" dos arts. 7º a 55-L e os arts. 28, 55, 56, 57 ("Art. 5 7."), 58 e 59.
- Redação anterior tachada: LAI art. 12, caput e parágrafo único antigos (únicos trechos tachados nas duas páginas).
- Demais linhas: estado e nota de redação conferem com o compilado.

## 6. NÃO CONFERIDO
- Nenhum dispositivo novo. A seção 6 do Anexo N fica como estava (termo inicial das alteradoras não abertas).

## 7. Efeito sobre o D6 v1
- Não lido (vedação do qa-normativo-da; D-CEGO-2). Pela reconciliação T-72, dúvida 1, a v1 não usou o dispositivo. Nenhum id de item a apontar a partir desta errata.
