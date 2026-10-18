# ORDEM_V15_E_PILOTO_VISUAL.md — encomenda v15 do Fundador (item e) — 2026-10-18 — gravado por orquestrador (sessão s14)
Protocolo: FAB-AUTO v1. Regras comuns da encomenda v15: ver ordens/ORDEM_V15_C_LIMPEZA.md (cabeçalho).

ORQUESTRADOR: LOTE
REMETENTE: Fundador (encomenda de 18/10/2026, item e; piloto confirmado na mesma data)
DESTINATÁRIO: EXEC (Fábrica)
PROMPT:
a) Objeto: piloto de curso visual em 3 tópicos: dois de Fala e um de TI. Sugestão: P2-1.4 (diarização; já tem demonstração no código), P2-2.5 (normalização de texto) e P1-8.2 (tipos de gráficos). A Gerência pode trocar, registrando o motivo.
b) Gerência titular: GCE e GCB; peças que precisarem de desenho seguem CDJ → CII.
c) Escopo: formato "topicos": {"P2-1.4": {"emUmMinuto":[...], "resumo":"...", "visuais":[{"tipo":"fluxo"|"tabela"|"linha"|"esquema"|"barras", ...}]}}
   fluxo: titulo, passos[]; tabela: titulo, colunas[], linhas[[]], legenda; linha: titulo, marcos[{quando,texto}]; esquema: titulo, centro, ramos[]; barras: titulo, dados[{rotulo,valor}], unidade, fonte.
d) Arquivos-base: pacote resultante da ORDEM_V15_C; a prévia v15.2 (componentes prontos e testados em 360 px, claro e escuro; tabela vira cartões no celular).
e) Regras específicas: todo dado de "barras" com fonte oficial e data; nada que não esteja no curso; sem referências de produção; "emUmMinuto" com 3 pontos.
f) Saída: objeto "topicos" para os 3 tópicos, parecer de QA.
g) Classificação: PRÓXIMO (depois da ORDEM_V15_C)
