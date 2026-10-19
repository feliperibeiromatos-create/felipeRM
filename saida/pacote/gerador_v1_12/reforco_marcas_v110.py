# -*- coding: utf-8 -*-
"""T-104 (v1.10) — deleções da camada do estudante nas justificativas dos 225 itens novos (lista FECHADA; D1 da GBQ, saida/pacote/T104_D1_v1_10_2026-10-18.md, seção 4).
Só deleção, sem texto novo. Os 48 da onda 1 continuam com a lista da v1.9 (reforco_marcas.py, intacto). Fora desta lista, a justificativa passa literal.
Contagens esperadas fechadas: ESPERADO (conferidas em estudante_json.py e validate_v110.py)."""
import re

REGRAS = [
    # (rótulo, regex, ocorrências esperadas no conjunto dos 225)
    ('V2 (classificação interna de VOLÁTIL no início da justificativa, com ou sem REVERIFICAR)',
     re.compile(r'^VOLÁTIL \((?:baixo|médio|baixo/médio|risco médio; [^)]*)\)[.;] (?:REVERIFICAR\. )?'), 20),
    ('R2 (marca REVERIFICAR no início da justificativa)', re.compile(r'^REVERIFICAR\. '), 51),
    ('C2 (fundamento interno do rótulo VOLÁTIL / não VOLÁTIL, frase final)', re.compile('|'.join(re.escape(s) for s in [
        ' Regra automática do serviço = comportamento padrão de produto (hipótese (b) da D-T96-ONDA2-ACEITE).',                                     # L2-R77
        ' VOLÁTIL pela hipótese (c): a própria página ressalva que siglas não são suportadas em todos os idiomas; o item não afirma suporte a nenhum idioma.',   # L2-R81
        ' VOLÁTIL pela hipótese (c) da D-T96-ONDA2-ACEITE: o gabarito depende de opção configurável de módulo periférico do Whisper (normalizador de avaliação).',  # L2-R85
        ' Não VOLÁTIL: a sensibilidade à caixa é premissa declarada no enunciado, que não nomeia campo, limite nem padrão (mesmo tipo de base do L2-R10, aceito como não VOLÁTIL).',  # L2-R88
        ' Não VOLÁTIL: mecanismo documentado de função do editor, sem versão, limite, padrão ou parâmetro nomeado.',                                   # L2-R96
        ' VOLÁTIL pela hipótese (c): recurso de custom speech que a página condiciona a locais com suporte (pt-BR consta da lista da página), mesma natureza de base do L1-R87.',  # L2-R82
        ' VOLÁTIL pela hipótese (b): padrão do produto; o item não nomeia o parâmetro que altera o índice.',                                            # L2-R94
        ' VOLÁTIL pela hipótese (c): recurso de uma ferramenta específica, periférico ao tema.',                                                         # L2-R99
        ' VOLÁTIL pela hipótese (b): comportamento de produto, em página compartilhada por duas ofertas do serviço.',                                    # L2-R100
    ])), 9),
]
ESPERADO = {r[0]: r[2] for r in REGRAS}
HITS = {}       # (id, rótulo) -> n


def strip_reforco(texto, cnt, iid=None):
    for lab, rx, _ in REGRAS:
        n = len(rx.findall(texto))
        if n:
            texto = rx.sub('', texto)
            cnt[lab] += n
            if iid is not None:
                HITS[(iid, lab)] = HITS.get((iid, lab), 0) + n
    return texto
