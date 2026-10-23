# Ordem à Fábrica — curso de Direito Administrativo no formato da plataforma (19/10/2026)

Origem: pedido do Fundador em 19/10/2026 ("automatizar a criação do curso de Direito Administrativo com layout e design mais bonitos"), preparado pela sessão de design da plataforma (DPE-01). O Fundador cola a ordem na sessão da Fábrica. Rodar a ordem consome cota; o gasto é decisão dele.

```
ORQUESTRADOR: LOTE
REMETENTE: Fundador (pedido de 19/10/2026), preparada pela sessão DPE-01
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: entregar os lotes de Direito Administrativo no formato da plataforma (claude/ESPEC_curso_DA_formato_v1_2026-10-19.md): curso por subitem com quadros DEFINIÇÃO / BASE LEGAL / EXEMPLO PARLAMENTAR / PEGADINHA PROVÁVEL, e, por tópico, emUmMinuto, resumo e 1 ou 2 visuais (compare, baseLegal, esquema, linha, fluxo, tabela).
b) Gerência titular: GCB; QA pela gcb-cqfp e Base legal pelo qa-normativo-da (mapa normativo do lote, com data). Leitura externa do curso pelo ChatGPT, só para listar o que falta (decisão do Fundador de 18/10).
c) Escopo e ordem: primeiro os lotes já canônicos (D6: itens 11 e 12; D1), só reformatando, sem conteúdo novo; depois D5, D2, D3 e D4, na ordem da D-DA-LOTES.
d) Arquivos-base: especificação acima; edital (46 entradas P1-DA-, texto literal); mapas normativos dos lotes; PADRAO_UNICO_v1.md; estado canônico.
e) Regras específicas:
   1. Edital no pacote com ids P1-DA-<n> e prova "P1"; questões com itemEdital desses ids; lote só com itens de DA.
   2. Base legal: todo dispositivo com ref, texto, literal (true só para transcrição exata) e conferido (AAAA-MM-DD); sem data, não entra.
   3. Prazos e fases (visual "linha") só do mapa normativo.
   4. Sem referências de produção (ordem C), sem códigos internos, sem o texto "[demonstração de formato]".
   5. Resumo por tópico de 150 a 250 palavras.
   6. Rodar claude/kit_pacote/checa_pacote.py contra o index.html publicado antes de entregar: zero bloqueios.
f) Saída: pacote novo (número da Fábrica) com edital de DA, lotes, questões e topicos; relatório por lote (tópicos cobertos, dispositivos conferidos e REVERIFICAR, visuais por tópico, o que o leitor externo apontou); parecer de QA; relatório do checa_pacote.py.
g) Classificação: PRÓXIMO (D6 e D1 primeiro; aguarda o Fundador colar a ordem e decidir a cota).
```
