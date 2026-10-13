# -*- coding: utf-8 -*-
"""Regras literais da edição do estudante (T-48). Só deleção: ⟦…⟧ = trecho apagado."""
from estudante_marcas import D

# ===== fase PRE (antes das regras genéricas; o texto é o do pacote) =====
D('V (parcial: mantém a orientação ao estudante)',
  'antes\nda versão definitiva [⟦V 08/10/2026 — F4; NORMATIVO — QA; ⟧norma de\ncaráter experimental, não cobrar o texto].', 'pre')
D('V (parcial: mantém a orientação ao estudante)',
  'outro\nidioma [⟦V 08/10/2026 — F4; NORMATIVO — QA; ⟧contexto histórico].', 'pre')
D('NORMATIVO — QA (parcial: mantém a orientação ao estudante)',
  '[⟦NORMATIVO — QA; ⟧não cobrar além do texto]', 'pre')
D('NORMATIVO — QA (frase de marca e fontes)',
  'Todos os dispositivos abaixo estão em paráfrase⟦, com a marca\n[NORMATIVO — QA]⟧.⟦ Fontes: F1 (LGPD compilada) e F2 (Lei 9.610/1998),\nlidas em 08/10/2026.⟧', 'pre')

# ===== fase POST (depois das regras genéricas) =====
FP = 'F (prosa: referência a fonte)'
FS = 'F (frase de fonte)'
# --- justificativas
D(FP, 'valor numérico⟦; o F4 cita a chuva "in inches or millimeters"⟧.')
D(FP, '⟦; o F3 define os termos separadamente⟧')
D(FS, '⟦ Fonte: F3, conforme o curso 5.1.3.⟧')
D(FS, '⟦ Fonte: F3, conforme o curso 5.1.1.⟧')
D(FS, '⟦ Fonte: F1 e F2, conforme o curso 5.1.3.⟧')
D(FP, 'Fonte: ⟦F3 (temperatura) e ⟧curso 5.1.4 (janela de contexto, conceito geral).')
D(FP, 'definição de alucinação⟦ do F3⟧).')
D(FP, 'Fonte: ⟦F3, zero-shot ("A prompt that does not provide an example of how you want the large language model to respond"), e ⟧curso 5.1.2 e 5.1.3.')
D(FP, '(⟦a F10 informa que ela não é possível; ⟧exclui-se o link e cria-se outro; ver curso 1.4.2)')
D(FP, 'conceito geral⟦; a F13 descreve o Outlook para PC como aplicativo de e-mail⟧)')
D(FP, 'Fonte: conceito geral⟦; F7 (RFC 1034) descreve os "domain style names" e seu uso para "host address support" (trecho lido em 08/10/2026)⟧.')
D(FP, 'Fonte: conceito geral⟦; F11 descreve o HTTP como "a stateless application-level protocol"⟧.')
D(FS, '(o de quarta-feira).⟦ Fonte: F12 (Microsoft Learn, "Types of backup", verificado em 08/10/2026): "If you are performing a combination of normal and differential backups, restoring files and folders requires that you have the last normal as well as the last differential backup."⟧ O item não depende')
D(FS, 'reduz o impacto.⟦ Fonte: F2 (verificado em 08/10/2026).⟧')
D(FS, 'pela rede.⟦ Fonte: F13 (worm: "Propaga-se automaticamente pelas redes, explorando vulnerabilidades nos sistemas e aplicativos instalados"; verificado em 08/10/2026) e F4 (vírus, seção 4.1: "se propaga inserindo cópias de si mesmo").⟧')
D(FS, 'por regras.⟦ Fonte: F14 (firewall: "protege seu computador contra ataques vindos pela rede"; antivírus: "Ferramentas antivírus (antimalware) podem ajudar a detectar uma infecção"; verificado em 08/10/2026) e F5 (a Firewall do Windows "ajuda a proteger o seu dispositivo ao filtrar o tráfego de rede que entra e sai do dispositivo").⟧')
D(FP, 'Fonte: ⟦F13 (spyware: "Projetado para monitorar as atividades de um sistema e enviar as informações coletadas para terceiros."; verificado em 08/10/2026); o antispyware não é mencionado no F13: ⟧conceito geral.')
D(FS, 'código malicioso.⟦ Fonte: F4 (livro, seção 2.3, verificado em 08/10/2026; paráfrase: as mensagens induzem o usuário a fornecer dados por páginas falsas, pela instalação de códigos maliciosos ou pelo preenchimento de formulários; entre as situações, "mensagens com links para código malicioso").⟧')
D(FP, 'Fonte: ⟦F4, seção 2.3.1 (DNS confirmado: "por meio de alterações no serviço de DNS"); F7; ⟧arquivo hosts: conceito geral.')
D(FP, 'também podem usar HTTPS. Fonte: ⟦F11, seção 4.2.2 (verificado em 08/10/2026); ⟧o restante é conceito geral.')
# --- L4 (curso)
D(FP, '— as técnicas⟦ de F1 e F2⟧. Se o resumo')
D(FP, 'Exemplos⟦ do F4 (reverificados em 7/10/2026)⟧: quantidade de chuva')
D(FP, 'Exemplos⟦ do F4⟧: e-mail é spam')
D(FP, 'exemplo⟦ do F4⟧: agrupar dados')
D(FP, 'POLÍTICA (policy), ⟦que o F4 descreve como ⟧a melhor estratégia para acumular recompensas⟦ (verificado em 7/10/2026)⟧. Exemplos⟦ do F4⟧: treinar robôs')
D(FP, 'É o que afirma⟦ o F4⟧: "generative models')
D(FP, 'conferido no GAB_DEFINITIVO_034_TRF6_002_01)⟦; o lote usa o F4 como fundamento, não o TRF6⟧.')
D(FP, 'ficar com a formulação⟦ do F4⟧ e evitar itens')
D(FP, '⟦Segundo o F5 (verificado em 7/10/2026):\n⟧- Modelo generativo')
D(FP, 'Relação entre os termos: ⟦o F3 os define separadamente; ⟧LLMs de uso geral')
D(FP, 'a lista em tópicos⟦ do F4⟧ traz texto→texto')
D(FP, 'a tabela de exemplos⟦ do F4⟧ traz texto→texto')
D(FP, 'ver 5.1.4⟦ (F3 para temperatura)⟧.')
# --- L6A (curso)
D(FP, '⟦O que a F1 afirma (leitura de 08/10/2026):\n⟧- Na guia "Revisão"')
D(FP, 'Limite do curso: ⟦a F1 ⟧NÃO descreve como ativar')
D(FP, '(⟦a F3 diz ⟧"não estão formatados como cabeçalhos"')
D(FP, 'apenas visualizar.⟦ A F9 também usa os rótulos "Pode editar" e "Pode exibir".⟧')
D(FP, '- ⟦A F10 trata de "Interromper o compartilhamento" e de alternar permissões "entre exibir e editar" para quem tem acesso direto; ela ainda avisa que ⟧NÃO é possível')
D(FP, 'ERRADO (⟦a F11 ⟧descreve os dois caminhos)')
D(FP, '(conceito geral⟦; F14 para os protocolos⟧)')
D(FP, 'é conceito geral⟦; a F13 não usa a palavra "instalado"⟧.')
D(FP, 'RFCs DA IETF⟦ E F14⟧)')
D(FP, '⟦Segundo a F14, ⟧por padrão os clientes POP3')
D(FP, '⟦Segundo a F14, ⟧por padrão os clientes IMAP4')
D(FP, 'ficam no servidor).⟦\nA F14 lista portas e criptografia do Exchange Online; esses números são específicos de produto e NÃO são cobrados.⟧\n\n### 3.1.3')
D(FP, '(de edição para exibição ou o contrário)⟦ e orienta excluir o link e criar outro⟧. As duas páginas')
D(FP, 'Cco (cópia oculta): ⟦conforme a F12 (leitura de 08/10/2026), ⟧quem é inserido')
D(FP, 'Microsoft.⟦ A página da F19 descreve a nova experiência como a que "simplifica as conversas ao colocar o chat, as equipas e os canais num único local" (leitura de 08/10/2026).⟧ Reuniões')
D(FP, 'Limite: ⟦a F18 ⟧não define o canal padrão')
D(FP, 'mais próxima) e ⟦a F19 ⟧não diz quem pode ver')
D(FP, 'conceito geral⟦; as páginas de ajuda F20–F22 descrevem o uso⟧)')
D(FP, 'Google Agenda (⟦a F22, ⟧em pt-PT, chama-o')
# --- L6B (curso)
D(FS, 'Fonte: conceito geral.⟦ A leitura de hoje do F4 (Cartilha, livro) menciona confidencialidade e integridade apenas de passagem e associa ataques de negação de serviço a "indisponibilidades ao alvo"; essas passagens NÃO definem a tríade e não foram usadas como definição.⟧')
D(FP, '"Instale um antivírus antes de qualquer aplicativo"⟦ (F3, verificado em 08/10/2026, seção de celulares)⟧.')
D(FP, '(⟦F11, ⟧RFC 9110, seção 4.2.2: "secured" significa que "the server has been authenticated as acting on behalf of the identified authority" e que a comunicação tem "confidentiality and integrity protection"⟦; verificado em 08/10/2026⟧)')
D(FP, 'Fonte: ⟦F11 (seção 4.2.2), verificado em 08/10/2026; ⟧o restante é conceito geral.')
D(FP, '(⟦F4, seção 2.3.1, paráfrase: ⟧desconfiar de site de banco')
# --- unidades/agentes e ids internos
AG = 'agente/unidade interna (CQFP, QA, GCB, GCE, CPP)'
D(AG, 'suprimiu a expressão (⟦conforme a conferência da CQFP; ⟧na')
D(AG, 'Lei 15.352/2026⟦, conforme a\n   CQFP⟧). A autoridade')
D(AG, '— síntese autoral⟦ (GCB-CPP)⟧\n')
D(AG, '(artigo e inciso⟦, para o QA Normativo⟧)')
D(AG, '(⟦fonte: Planalto, Lei 15.352/2026 e LGPD compilada, verificadas pela CQFP em 08/10/2026; ⟧vale para a prova, edital 13.33)')
D(AG, 'dada pela Lei 15.352/2026⟦, verificada pela CQFP em 08/10/2026⟧ | Troca')
D(AG, 'Não usada em item⟦, por despacho da GCB⟧.')
D(AG, 'sem item.⟦ (Síntese da CQFP a partir do texto colado pelo Fundador em 08/10/2026; não é transcrição literal.)⟧')
D(AG, 'visualizations"⟦ (CI, verificado pela CQFP em 8/10/2026)⟧ — exemplo')
D(AG, 'cujo ponto de julgamento foi conferido⟦ pela QA⟧ contra o caderno')
D(AG, '(trecho confirmado⟦ pela QA e reconfirmado pela produção⟧ em 08/10/2026)')
D(AG, 'Decisão⟦ da GCE⟧: sem trava')
D(AG, 'Notas de correção⟦ (GCE, R2–R4)⟧\n')
D(AG, 'afirmação\n    categórica⟦ da versão da CPP⟧, segundo')
D('id interno (R-xx, E-xx, O-xx, D-xx)', 'Alínea c da discursiva⟦ (R4 do Projeto)⟧:')
D('id interno (R-xx, E-xx, O-xx, D-xx)', 'amostras de referência⟦ (errata E1)⟧, não basta')
D('id interno (R-xx, E-xx, O-xx, D-xx)', '(N1⟦; E3⟧)')
D('id interno (R-xx, E-xx, O-xx, D-xx)', 'Distinção de vocabulário⟦ (O11)⟧:')
D('id interno (R-xx, E-xx, O-xx, D-xx)', 'para o Cargo 11⟦ (D-T2)⟧.')

# --- carimbos datados remanescentes ligados às referências removidas
CAR = 'carimbo datado de verificação/leitura (ligado a F-ref)'
D(CAR, 'Anthropic, "XML structuring" e OpenAI, "Message formatting with Markdown and XML"⟦, verificadas em 7/10/2026⟧.')
D(CAR, '"Message formatting with Markdown and XML")⟦, ambas verificadas em 7/10/2026⟧.')
D(CAR, 'reinforcement learning"⟦ (reverificado em 7/10/2026)⟧. Conclusão')
D(CAR, '"principalmente entre o honesto e o desonesto"⟦ (conferido no Planalto em 08/10/2026)⟧.')
D(CAR, 'Microsoft 365"⟦, conforme a leitura de 08/10/2026⟧)')
D(CAR, '(seção 1.1⟦; leitura de 08/10/2026⟧)')
D(CAR, 'seus dados"⟦, ambos verificados em 08/10/2026⟧.')

# ===================================================================== R1 (13/10/2026) — só deleção
# C-17 (DÚVIDA 5-a): "(v2, …)" no L1C
D('id interno / versão do lote (v2)', '(⟦v2, ⟧item 1.4)')
D('id interno / versão do lote (v2)', '(⟦v2, ⟧exemplo parlamentar do 1.4)')
# C-19 (DÚVIDA 5-c): carimbo de leitura "aberta(s) hoje" — 9 alvos
CH = 'carimbo de leitura "aberta(s) hoje"'
D(CH, 'Nas páginas de suporte⟦ abertas hoje⟧, a Microsoft')
D(CH, '(conceito geral⟦; sem fonte aberta hoje para detalhes⟧; sem item)')
D(CH, '(conceito geral⟦; sem base aberta hoje⟧)')
D(CH, 'Fontes⟦ abertas hoje⟧: "Faça backups')
D(CH, 'uma fora do local), ⟦sem fonte aberta hoje e ⟧sem item.')
D(CH, 'Definição de vírus⟦ aberta hoje⟧: "programa')
D(CH, 'Definição de ransomware⟦ aberta hoje⟧: "Ransomware')
D(CH, 'Definição⟦ aberta hoje⟧: o phishing')
D(CH, 'não foi confirmada em fonte⟦ aberta hoje⟧; ver curso 4.1.1')
# C-20 (DÚVIDA 5-d): códigos de fonte do L5 — literais (as genéricas estão em estudante_marcas.GENERIC_R1)
L5 = 'código de fonte do L5 (U/GG/TB)'
D(L5, 'Power BI (Microsoft)⟦ — fonte principal U1 en-us; U2 só para a natureza Windows do Desktop (verificado em 8/10/2026)⟧', 'l5', ('L5_',))
D(L5, 'Tableau (Salesforce)⟦ — U3; dashboards por TB2 (verificado em 8/10/2026)⟧', 'l5', ('L5_',))
D(L5, 'Data Studio (Google)⟦ — U4, U5, U6, GG4 (verificado em 8/10/2026)⟧', 'l5', ('L5_',))
D(L5, '8.3 FERRAMENTAS (VOLÁTIL⟦; verificado em 8/10/2026⟧)', 'l5', ('L5_',))
D(L5, 'Três componentes e fluxo⟦ conforme U1 en-us⟧ ("three primary', 'l5', ('L5_',))
D(L5, 'natureza Windows do Desktop⟦ conforme U2⟧.', 'l5', ('L5_',))
# C-21 (DÚVIDA 5-f): classificação interna nas justificativas
CI_ = 'classificação interna de VOLÁTIL na justificativa'
D(CI_, 'Depende de padrão técnico estável, não de produto⟦; NÃO VOLÁTIL⟧.')
D(CI_, 'passou a ser exercida por ela.⟦ REVERIFICAR (normativo) 04–08/01/2027; não VOLÁTIL.⟧')
D(CI_, '"Message formatting with Markdown and XML".⟦ Sem marca VOLÁTIL: o item afirma o conceito, não recurso de produto.⟧')
# C-23 (D-R1-23): marca de processo no curso do L4
D('marca de processo ("neste chat")', 'situação de tramitação não verificada⟦ neste chat⟧)')
