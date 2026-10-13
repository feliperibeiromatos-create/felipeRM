# Simulado 0-P2 — P2 diagnóstico (Reconhecimento de Fala, Transcrição e IA, itens 1 a 4) — folha

- Tipo: diagnóstico
- Versão: v1
- Número de itens: 25

Julgue cada item (C = certo, E = errado). Gabarito no arquivo SIM-0-P2_gabarito.md.

**Comando.** Julgue os itens a seguir (C = certo, E = errado).

**1** — L1C-Q29 — Em registro oficial, a pontuação inserida automaticamente pode alterar o sentido de um enunciado, como na diferença entre uma afirmação e uma pergunta, razão pela qual a revisão deve conferir a pontuação, e não apenas as palavras.

**2** — L1C-Q27 — Quando se afirma que a diarização "identifica" os diferentes oradores de uma gravação, o verbo pode ser entendido no sentido de distinguir um orador do outro, sem que isso implique saber o nome de cada um.

**3** — L2-Q19 — A ausência de regras de padronização pode fazer com que a mesma sigla ou o mesmo número apareçam grafados de formas diferentes ao longo de uma transcrição, o que compromete a consistência do texto e dificulta a busca por esses termos.

**4** — L3-Q15 — Por serem multilíngues, os modelos de IA têm desempenho equivalente em português e em inglês em qualquer tarefa, inclusive na compreensão de termos regimentais e jurídicos brasileiros.

**5** — L2-Q04 — Uma transcrição automática sem revisão pode ser útil como rascunho para consulta rápida, desde que seu texto não seja tratado como registro oficial da sessão.

**6** — L3-Q29 — Segundo a LGPD, a comunicação à autoridade nacional e ao titular sobre incidente de segurança que possa acarretar risco ou dano relevante é dever do operador, e não do controlador.

**7** — L1C-Q25 — Por receber o áudio diretamente como entrada, um LLM multimodal de áudio nativo produz sempre uma cópia literal da fala, o que dispensa a revisão humana em registros oficiais.

**8** — L3-Q19 — O fato de pronunciamentos parlamentares serem de acesso público não afasta a incidência da LGPD sobre o seu tratamento, que deve considerar a finalidade, a boa-fé e o interesse público que justificaram a sua disponibilização.

**9** — L3-Q12 — Na sumarização abstrativa, o texto gerado pode conter frases que não constam literalmente da transcrição sem que isso, por si só, configure erro; o problema ocorre quando o texto gerado traz informação não sustentada pela fonte.

**10** — L2-Q28 — A adaptação de modelo de linguagem com textos do domínio parlamentar, como pronunciamentos e atas, altera a probabilidade de sequências de palavras, e não apenas a de termos isolados, o que pode auxiliar na escolha entre palavras de som semelhante com base no contexto.

**11** — L1-Q02 — Um sistema ASR, ao converter em texto o áudio de uma sessão, identifica necessariamente qual parlamentar proferiu cada fala, por ser essa uma etapa intrínseca do reconhecimento de fala.

**12** — L3-Q14 — Um modelo especializado em português é, por definição, um modelo treinado exclusivamente com textos em português, sem qualquer conhecimento de outros idiomas.

**13** — L3-Q30 — O envio do áudio de sessões a serviço de transcrição operado em servidores localizados no exterior pode configurar transferência internacional de dados pessoais, que só é permitida nos casos previstos na LGPD, como o de país que proporcione grau de proteção adequado ou o de garantias oferecidas pelo controlador.

**14** — L2-Q15 — A convenção para marcar eventos não falados, como palmas, risos, ruídos e trechos inaudíveis, pode variar entre instituições, mas, dentro de uma mesma transcrição, deve ser aplicada de modo uniforme e distinguível do texto da fala.

**15** — L2-Q09 — Na revisão de transcrições parlamentares, fidelidade equivale a literalidade: qualquer supressão de hesitações, repetições ou vícios de linguagem do orador constitui, necessariamente, infidelidade ao que foi dito.

**16** — L3-Q04 — A transcrição automática de uma sessão pode servir de insumo para a sumarização e a indexação, de modo que erros da transcrição tendem a se propagar para os produtos derivados.

**17** — L3-Q08 — A combinação de busca por palavras-chave e busca semântica pode ser vantajosa em acervos parlamentares, pois termos exatos, como números de proposições e nomes, e semelhança de sentido atendem a necessidades distintas de recuperação.

**18** — L2-Q07 — Em fluxo de degravação assistida por IA, a revisão humana só é necessária ao final do processo, pois eventuais erros de etapas iniciais, como a atribuição de falas a oradores, sempre são detectados na leitura final do texto.

**19** — L1-Q15 — Na transcrição em tempo real (streaming), o sistema pode emitir resultados parciais sujeitos a revisão, e o resultado final de um trecho em geral é consolidado após a detecção do fim do enunciado (endpointing).

**20** — L1-Q12 — Uma vez carregada uma lista de termos parlamentares por adaptação de vocabulário, o sistema ASR passa a reconhecer corretamente esses termos em qualquer condição acústica, independentemente do sotaque do orador.

**21** — L3-Q23 — Segundo a Lei 9.610/1998, os textos de leis, decretos e decisões judiciais são obras intelectuais protegidas, de modo que sua reprodução depende de autorização, ao contrário dos discursos, que podem ser reproduzidos livremente.

**22** — L2-Q23 — O formato WebVTT, embora voltado a legendas, organiza o texto em segmentos associados a intervalos de tempo e admite indicar o falante de cada segmento por marcação própria, podendo, assim, transportar informação de locutor.

**23** — L2-Q26 — Se a auditoria de uma amostra aleatória de transcrições não encontrar nenhum erro, é possível afirmar com certeza que nenhuma das transcrições não amostradas contém erros.

**24** — L1-Q06 — Na arquitetura em cascata (ASR → LLM → TTS), o LLM processa diretamente as características acústicas da fala, razão pela qual preserva informação prosódica como entonação e hesitação.

**25** — L2-Q30 — Elevar ao máximo o peso de reforço de termos do vocabulário parlamentar é sempre vantajoso, pois aumenta a chance de acerto desses termos sem produzir efeitos sobre o reconhecimento das demais palavras.
