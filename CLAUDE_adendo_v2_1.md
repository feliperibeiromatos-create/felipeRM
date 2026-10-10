
## Adendo v2.1 (9/10/2026) — Presidência de Ciclo (D-PRES-FABRICA)
- Agente presidencia (model: inherit — a sessão deve rodar no modelo mais capaz disponível, preferencialmente diferente do opus das Gerências) decide os gatilhos A–D de PARA_PRESIDENCIA.md dentro dos limites do seu arquivo de agente; matéria reservada vai para PARA_FUNDADOR.md e a fábrica para.
- Arquivos: PARA_FUNDADOR.md (saída ao Fundador; persistente), LOG_PRESIDENCIA.md (auditoria). Orquestrador contínuo: orquestradores/CICLO_CONTINUO.md.
- A Presidência de chat (claude.ai) audita por amostragem e pode revogar decisões por linha "NOVA | REVOGA D-xxx | motivo" em DECISOES.md.
- D-BACKUP vale a cada ciclo do laço.
