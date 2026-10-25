# T134_reconciliacao_2026-10-25.md — T-134 — 2026-10-25 — gerado por gbq-gerencia

**Objeto:** publicação da plataforma v17.1 com o pacote v1.14 embutido no link da candidata (D-V17-1-PUBLICAR parte (i), sim do Fundador de 25/10; D-V17-1-ESTILO). Ciclo s19c1.
**Entregas reconciliadas:** build (sonnet) — `saida/plataforma/plataforma_v17_1_publicar.html`, `T134_build_2026-10-25.md`, `T134_checa_pacote_v2_2026-10-25.md`, `T134_checa_estilo_DA_2026-10-25.txt`, `testes_T134/`; QA-plataforma gbq-cqe (opus) — `QA_T134_2026-10-25.md`.

## 1. Conferência própria da Gerência (25/10/2026)
- `sha256sum saida/plataforma/plataforma_v17_1_publicar.html` = `769a14d76432d6e9760a48c05e6d1b3c80eafd34b110099da569597b06fc1d26`; 3.115.770 bytes. Bate com o build e com a QA.
- Pacote embutido: `saida/pacote/pacote.json` SHA-256 `070bc237fcc7371a23365f6e66c9341cf5c0aee08ad9206a9f7be6c06150d495` (v1.14 canônica, D-PACOTE-V114-CANONICO; 1.433 itens; DA 684). É o mesmo pacote já publicado na v17 (D-PLATAFORMA-V17-PUBLICACAO). A QA atestou que `PUB_INLINE` é igual, objeto a objeto, ao pacote.json e igual, byte a byte, à linha da v17 publicada.
- Build e QA concordam: não há divergência a arbitrar.

## 2. Condições da D-V17-1-PUBLICAR, uma a uma
| # | Condição | Evidência | Situação |
|---|---|---|---|
| 1 | Gatilho A | Pacote v1.14 inalterado: `checa_pacote_v2` diz "conteúdo idêntico ao pacote em uso"; itens 1433→1433, novos 0, removidos 0; lotes 16, simulados 4, discursivas 5, voláteis 91→91. As contagens são as do pacote canônico, que já teve gatilho A e aceite (T-123). O gatilho A desta publicação vai em PARA_PRESIDENCIA.md (seção 4) | ATENDIDA com a emissão abaixo |
| 2 | Zero bloqueios | `T134_checa_pacote_v2_2026-10-25.md`: 0 bloqueios. Há 1 aviso, "base sem DIAG30", que é esperado porque a base passada foi um .json e não o index publicado; não é bloqueio. `T134_checa_estilo_DA_2026-10-25.txt`: 0 avisos. Marcas de produção: 0 | ATENDIDA |
| 3 | Regressão verde (R1–R9) | `testes_v17_1.js` passou em 67/67, com 0 erros de JS. Em regr_md, regr_estado e regr_prova, as únicas diferenças em relação à v17 publicada são o bloco `details.estilo-da`; sem esse bloco, as telas saem idênticas (8/8, 7/7, 0 diferenças nas 122 telas de prova). divTopico, pctTopico e nInline são idênticos nos 93 tópicos. A QA repetiu de forma independente a comparação v17 × v17.1 (3/3 idênticos em todos os passos) | ATENDIDA |
| 4 | QA-plataforma aprovada por modelo distinto | gbq-cqe (opus) × build (sonnet). Veredito: APROVADO, sem defeitos. O1 e O2 são só informativos | ATENDIDA |
| — | D-V17-1-ESTILO (card discreto) | O card fica fechado por padrão: uma linha de 13,5 px, sem fundo, borda ou sombra, acima dos tópicos, e abre ao toque. Aparece só em DA (TI 0, Fala-IA 0). "CEBRASPE_ESTILO" não ocorre no HTML. O card não traz texto de terceiro e as proporções conferem com `regras/estilo_banca_DA_v1.md` §4 | ATENDIDA |

## 3. D1 da GBQ
1. **Ressalva do build** ("card visto na TI ao navegar na mesma página"): a GBQ acolhe o diagnóstico da QA (§5). É artefato do seletor do `t134.js`: o acordeão de abertura múltipla mantém aberta a matéria DA, como já acontece na v17. Não é defeito nem regressão.
2. **O1** (corpus do estilo DA vem do TEC Concursos; 25 gabaritos foram confrontados com o definitivo): fica registrado na trilha de evidência e não impede a publicação. A matéria já foi decidida pelo Fundador na D-V17-1-ESTILO; o card não reproduz texto de terceiro e declara as proporções como aproximadas. Não é matéria da GBQ reabri-la.
3. **O2** (CRLF e falha de `print` em cp1252 nos scripts `patch_v17_1_DAv2.py` e `checa_pacote_v2.py`): afeta só as ferramentas, não o HTML. Vai para o BACKLOG como manutenção de kit; não condiciona a publicação.
4. **Decisão:** a v17.1 + v1.14 (SHA-256 `769a14d7…fc1d26`) está **APTA A PUBLICAR**. Ficam pendentes, a cargo do orquestrador e na ordem do roteiro de entrada: atualizar o painel (skill atualizar-painel-camara), gerar a prévia e então publicar no link da candidata. Isso só depois do aceite deste gatilho A. Ao publicar, o orquestrador grava `saida/plataforma/T134_publicacao_<data>.md` com a versão do artifact e confere que o hash publicado é o mesmo.
5. Reprovação da QA: 0%. Nenhum gate foi acionado.

## 4. Linha proposta para o Estado Canônico (após a publicação)
> T-134 CONCLUÍDA (s19c1, 25/10): plataforma v17.1 publicada no link da candidata com o pacote v1.14 embutido (070bc237…; 1.433 itens; DA 684), HTML SHA-256 769a14d7…fc1d26 (3.115.770 bytes), versão <n> do artifact. O card discreto "Como a Cebraspe constrói o item" fica só em DA (D-V17-1-ESTILO). checa_pacote_v2 deu 0 bloqueios; a regressão está verde (67/67; diferenças só no card); a QA-plataforma gbq-cqe (opus) aprovou sem achados; o gatilho A da GBQ foi aceito. Supera D-PLATAFORMA-V17-PUBLICACAO. Pendência de kit: O2 (CRLF/cp1252) no BACKLOG.
