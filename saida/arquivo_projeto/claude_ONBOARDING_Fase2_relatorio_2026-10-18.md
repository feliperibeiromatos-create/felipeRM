# Onboarding multiconcursos — Fase 2 (18/10/2026)

Estado: prévia funcional em cópia, privada (https://claude.ai/artifact/2QxJibWAiNvnU1unBppV5w). Plataforma da candidata intacta (versão 12, id 1792342912-c3ff) até o "sim" do Fundador.

## Revisão independente (GPT) aplicada
Parecer GPT de 18/10/2026 sobre diag30_selecao_para_revisao.json (sha256 0ab3e493…, conferido). Duas trocas aplicadas:
- TI: 6B-06 → BQ-0095 (repetição com BQ-0011 sobre integridade). BQ-0095: CEBRASPE_ANALOGA, Câmara 2012, caderno CAMDEP12_CB1_01, item 43, gabarito C; gabarito vem do pacote aprovado e não foi reconferido no gabarito definitivo nesta etapa.
- Fala: L2-R16 → L2-R17 (L2-R16 cobra indexação/TECAD, mais perto de P2-3.1 que de P2-2.8).
Correção a uma análise recebida: P2-2.8 tinha só L2-R16 na seleção (L2-Q21 é de P2-2.6); após a troca, P2-2.8 fica com L2-R17.
Lista final (diag30_final.json, sha256 0de84bb09770…): TI 30 únicos, 18/18 subitens, 15 C / 15 E, 17 autorais + 13 análogos, 5 do SIM-0; Fala 30 únicos, 23/23, 13 C / 17 E, 30 autorais, nenhum do SIM-0. Zero voláteis, zero aderência parcial, zero itens de SIM-1, SIM-2, SIM-0-P2.
Pendência para a Fábrica: reclassificar L2-R16 (P2-2.8 → P2-3.1?) no pacote; não alterado aqui.

## O que mudou no código (cópia)
- Catálogo CONCURSOS (cd26-c11) e DISCIPLINAS com ids estáveis (cd26-c11/p1/ti etc.).
- Tela 1 (usuária nova): MapasPro, "Vai estudar para qual concurso?", um concurso, um toque.
- Tela 2: explicação das duas opções (66 palavras) antes dos botões; nove disciplinas P1/P2 na ordem do edital; 7 "em preparação" sem botões; "Decidir depois".
- Diagnósticos de 30 (D30-P1, D30-P2) substituem os recortes de 43/17 do Simulado 0 na lista; histórico antigo preservado.
- Painel: "Mudar meu caminho" abre a tela 2 sem apagar a escolha; evento novo caminho_mudado.
- Usuária existente: concurso definido sem perguntar; aviso único "Novo: diagnóstico de 30 itens" na trilha ("Ver as opções" / "Agora não").
- Eventos novos: tela_concurso_aberta, concurso_escolhido, tela_disciplinas_aberta, caminho_mudado, aviso_d30; toque_escolha_caminho ganha o campo disciplina.
- Inalterados: PUB_INLINE (byte a byte), chaves c2026.v01.*, motores de prova e estudo.

## Testes (Chromium headless, estado sintético)
T01–T10 do prompt v1.0, adaptados a 30 itens: 52 verificações, 0 falhas (inclui migração do estado da candidata e 360/390/1280 em claro e escuro). Regressão anterior: 67 verificações, 0 falhas. T03 adaptado: SIM/NÃO só nas disciplinas com conteúdo. T11: nenhuma publicação na URL da candidata. NÃO verificado: celular real, leitor de tela, teclado completo. Limitação da prévia: sem a capacidade de download, "Exportar meus erros" copia o texto.

## Publicação (18/10/2026)
Autorizada pelo Fundador ("Sim, publicar"). Publicada na URL da candidata como versão 13 (id 1792348644-fc94), conteúdo idêntico à prévia salvo o título; capacidade "downloads" mantida. Pós-publicação: arquivo lido de volta (sha256 3593120c…), pacote embutido idêntico ao da v12; testes da Fase 2 repetidos no publicado: 51 de 52 passaram, e o único "falhou" é do próprio teste (procura espaço comum; o botão usa espaço não separável em "35 min", texto correto); regressão anterior: 67/67. Versão anterior para reversão: v12, id 1792342912-c3ff.
