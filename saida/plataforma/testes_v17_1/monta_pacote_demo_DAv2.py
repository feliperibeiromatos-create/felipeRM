#!/usr/bin/env python3
"""Pacote de teste para a v17 DA-v2: pacote v1.13 + um lote DEMO no formato DA-v2 (ESPEC v2 + adendo v2.1).
Texto próprio, só para testar a renderização; rotulado DEMO; nunca publicar. Base: Lei 8.112/1990, arts. 36 e 37 [A VERIFICAR na fonte oficial antes de qualquer uso real]."""
import json, sys
src, dst = sys.argv[1], sys.argv[2]
p = json.load(open(src, encoding="utf-8"))

CURSO = """## 3.4 REGIME JURÍDICO DOS SERVIDORES PÚBLICOS FEDERAIS — DEMO DA-v2

### Remoção e redistribuição: o que se desloca

GLOSSÁRIO
Remoção: deslocamento do servidor, a pedido ou de ofício, no âmbito do mesmo quadro, com ou sem mudança de sede.
Redistribuição: deslocamento do cargo de provimento efetivo, ocupado ou vago, para outro órgão ou entidade do mesmo Poder.
Quadro — conjunto de cargos de um órgão ou entidade; na remoção o servidor fica no mesmo quadro.
Sede: localidade de exercício; a remoção pode ou não mudá-la.

CASO
Um analista lotado em uma unidade administrativa da Câmara pede deslocamento para outra cidade, para acompanhar o cônjuge, também servidor público, deslocado no interesse da Administração. A chefia nega, alegando falta de interesse do órgão. A negativa está certa?

Os dois institutos respondem a perguntas diferentes. A remoção trata de onde o servidor trabalha; a redistribuição trata de onde o cargo existe. Por isso a pergunta que decide a maioria dos itens é sempre a mesma: o que foi deslocado?

DEFINIÇÃO
Na remoção quem se desloca é o servidor; o cargo fica onde está. Na redistribuição quem se desloca é o cargo, levando ou não o servidor, para outro órgão ou entidade do mesmo Poder.

BASE LEGAL
- Lei 8.112/1990, art. 36, caput e parágrafo único
- Lei 8.112/1990, art. 37, caput e incisos I a VI

RESPOSTA DO CASO
Não. A remoção para acompanhar cônjuge ou companheiro servidor, deslocado no interesse da Administração, é a pedido e independe do interesse da Administração (art. 36, parágrafo único, III, a). O interesse do órgão é condição de outra modalidade (inciso II), não desta. O exemplo é hipotético.

Esse parágrafo vem depois da resposta do caso e deve aparecer como texto corrido, fora da caixa recolhida.

EXEMPLO PARLAMENTAR
Um cargo efetivo vago em um órgão do Poder Legislativo só pode ser redistribuído para outro órgão do mesmo Poder; não cruza para o Executivo. O exemplo é hipotético.

ITEM DX-01

ITEM DX-04

PEGADINHA PROVÁVEL
A: Remoção
B: Redistribuição
MUDA: a palavra "cargo" (redistribuição) no lugar de "servidor" (remoção), ou "outro órgão" no lugar de "mesmo quadro".
Permutar os dois institutos é a troca mais frequente; a banca também diz que a redistribuição pode ocorrer para órgão de outro Poder. Base: Lei 8.112/1990, arts. 36 e 37.

### Caso prático: redistribuição de cargo vago

Este título começa por "Caso" e deve continuar sendo um título comum, não uma caixa.

DEFINIÇÃO
A redistribuição exige prévia apreciação do órgão central do sistema de pessoal e observa seis preceitos: interesse da administração; equivalência de vencimentos; manutenção da essência das atribuições do cargo; vinculação entre os graus de responsabilidade e complexidade das atividades; mesmo nível de escolaridade, especialidade ou habilitação profissional; compatibilidade entre as atribuições do cargo e as finalidades institucionais do órgão ou entidade.

ITEM DX-03

ITEM DX-99

PEGADINHA PROVÁVEL
A: Cargo ocupado
B: Cargo vago
A redistribuição alcança os dois; esta pegadinha vem sem a linha MUDA de propósito, para o teste.
"""

ITENS = [
 dict(id="DX-01", gabarito="C", mecanismo="LIT", tipo="literal",
      enunciado="A remoção é o deslocamento do servidor, a pedido ou de ofício, no âmbito do mesmo quadro, com ou sem mudança de sede.",
      comentario=dict(decisiva="LIT: 'do servidor' e 'mesmo quadro' — paráfrase fiel do art. 36.", regra="Remoção desloca o servidor dentro do mesmo quadro; a sede pode ou não mudar.", correta="Trocar 'servidor' por 'cargo' ou 'mesmo quadro' por 'outro órgão' tornaria o item errado.")),
 dict(id="DX-02", gabarito="E", mecanismo="SUP", tipo="literal",
      enunciado="A remoção a pedido para acompanhar cônjuge servidor deslocado no interesse da Administração depende de juízo de conveniência do órgão de origem.",
      comentario=dict(decisiva="SUP: suprimiu 'independentemente do interesse da Administração'.", regra="A remoção do art. 36, parágrafo único, III, a, independe do interesse da Administração.", correta="A remoção para acompanhar cônjuge servidor deslocado no interesse da Administração independe do interesse do órgão de origem.")),
 dict(id="DX-03", gabarito="E", mecanismo="AMB", tipo="literal",
      enunciado="A redistribuição é o deslocamento de cargo efetivo, ocupado ou vago, para órgão ou entidade de qualquer dos Poderes da União.",
      comentario=dict(decisiva="AMB: 'qualquer dos Poderes' no lugar de 'mesmo Poder'.", regra="A redistribuição ocorre para outro órgão ou entidade do mesmo Poder (art. 37, caput).", correta="A redistribuição é o deslocamento de cargo efetivo, ocupado ou vago, para outro órgão ou entidade do mesmo Poder.")),
 dict(id="DX-04", gabarito="C", mecanismo="AP", tipo="caso", textoBase="Um cargo efetivo vago de um órgão do Poder Legislativo federal foi deslocado para outro órgão do mesmo Poder, após apreciação do órgão central de pessoal e com equivalência de vencimentos.",
      comando="Com base nessa situação hipotética, julgue o item que se segue.",
      enunciado="Trata-se de redistribuição, admitida mesmo com o cargo vago.",
      comentario=dict(decisiva="AP: 'cargo vago' — a redistribuição alcança cargo ocupado ou vago.", regra="Art. 37, caput: cargo de provimento efetivo, ocupado ou vago, para outro órgão do mesmo Poder.", correta="Dizer que só o cargo ocupado pode ser redistribuído tornaria o item errado.")),
 dict(id="DX-05", gabarito="E", mecanismo="CON", tipo="literal",
      enunciado="O deslocamento do servidor, a pedido, para outra localidade, no âmbito do mesmo quadro, denomina-se redistribuição.",
      comentario=dict(decisiva="CON: 'redistribuição' no lugar de 'remoção'.", regra="Deslocamento do servidor no mesmo quadro é remoção; redistribuição desloca o cargo.", correta="O deslocamento do servidor, a pedido, para outra localidade, no âmbito do mesmo quadro, denomina-se remoção.")),
 dict(id="DX-06", gabarito="E", mecanismo="NEG", tipo="literal",
      enunciado="É vedada a redistribuição de cargo efetivo vago.",
      comentario=dict(decisiva="NEG: 'vedada' onde a lei admite.", regra="A redistribuição alcança o cargo ocupado ou vago (art. 37, caput).", correta="É admitida a redistribuição de cargo efetivo vago.")),
]
for n, it in enumerate(ITENS, 1):
    it.update(rotulo="AUTORAL", certame="Projeto Câmara 2026 — DEMO", cargo="Noções de Direito Administrativo", ano=2026, numero=n,
              comando=it.get("comando", "Acerca do regime jurídico dos servidores públicos federais e da organização administrativa, julgue o item a seguir."),
              textoBase=it.get("textoBase", ""), itemEdital="P1-DA-3.4", aderencia="direta", url="DEMO",
              justificativa=it["comentario"]["regra"])
p["itens"].extend(ITENS)

p["lotes"].append(dict(id="DX", nome="DEMO DA-v2 — remoção × redistribuição (teste de renderização; não publicar)", prova="P1", formato="DA-v2",
    itensEdital=["P1-DA-3.4"], resumo="", curso=CURSO,
    pares=[dict(a="Remoção", b="Redistribuição", como="Remoção desloca o servidor no mesmo quadro; redistribuição desloca o cargo para outro órgão do mesmo Poder.")],
    pegadinhas=[dict(itemEdital="P1-DA-3.4", rotulo="Regime jurídico dos servidores públicos federais", par=dict(a="Remoção", b="Redistribuição", muda="'servidor' × 'cargo'; 'mesmo quadro' × 'outro órgão do mesmo Poder'"),
                     texto="Dizer que a redistribuição desloca o servidor, ou que alcança órgão de outro Poder. Base: Lei 8.112/1990, arts. 36 e 37.")]))

t = p["topicos"].setdefault("P1-DA-3.4", {})
t["formato"] = "DA-v2"
t["tarefas"] = ["Dado um deslocamento, decidir se é remoção (servidor) ou redistribuição (cargo).",
                "Dado um pedido de remoção para acompanhar cônjuge servidor, decidir se depende do interesse da Administração.",
                "Dado um cargo vago, decidir se pode ser redistribuído e para onde."]
t["fechamento"] = dict(levar=["Remoção desloca o servidor; redistribuição desloca o cargo.",
                             "Remoção: mesmo quadro, com ou sem mudança de sede.",
                             "Redistribuição: outro órgão ou entidade do mesmo Poder, com apreciação prévia do órgão central.",
                             "Remoção para acompanhar cônjuge servidor deslocado no interesse da Administração independe do interesse do órgão.",
                             "Redistribuição alcança cargo ocupado ou vago."],
                      literalidade=["art. 36, caput: 'servidor', 'mesmo quadro'", "art. 37, caput: 'mesmo Poder', 'ocupado ou vago'"],
                      caso=["pedido de remoção para acompanhar cônjuge: negativa por falta de interesse do órgão"])
t["escopo"] = [dict(tema="Penalidades e processo disciplinar", onde="P1-DA-4.2"), dict(tema="Estabilidade (CF, art. 41)", onde="P1-DA-3.1")]
p["nome"] = p.get("nome", "pacote") + " + DEMO DA-v2"
json.dump(p, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
print("OK", dst, len(p["itens"]), "itens", len(p["lotes"]), "lotes")
