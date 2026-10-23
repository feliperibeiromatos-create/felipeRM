PROTOCOLO DE AUTONOMIA DA FÁBRICA (FAB-AUTO) — v1 — 12/10/2026
Projeto Câmara 2026 · Proposta técnica para decisão do Fundador (matéria reservada: adoção de automação)
Classificação proposta: AGORA (Fases 0–2) / PRÓXIMO (Fase 3) / BACKLOG (Fase 4)

Todas as afirmações sobre o Claude Code abaixo foram verificadas em 10 e 12/10/2026 na documentação oficial (code.claude.com/docs, support.claude.com). Onde a documentação não confirma algo, está marcado "NÃO CONFIRMADO" — verifique antes de usar. Comandos e JSON foram checados sintaticamente, mas não executados na sua máquina.

==========================================================
0. DECISÃO QUE ESTE PROTOCOLO PEDE
==========================================================

a) Levar a Fábrica v1 (hoje no Claude Code na web, repositório feliperibeiromatos-create/felipeRM) para a máquina local, na pasta "E:\Projeto - Plataforma IA (Câmara 2026)", operada pelo Claude Code dentro do WSL2.
b) Operar no nível de autonomia N2 (definido na seção 2) como padrão: sem prompts de permissão durante um lote, mas com três travas (classificador do modo auto, regras deny, hook de escopo).
c) Nunca usar N3 (bypass total) no Windows hospedeiro; só em container/VM descartável.
d) Manter o Protocolo EXEC (claude/EXEC_Protocolo_Executora_Automatizada.md): a fábrica executa ordens, não decide; produção em Sonnet, QA em Opus; Fundador transporta só o Estado Canônico.

==========================================================
1. PRINCÍPIOS
==========================================================

P1. Autonomia é concedida por camadas, não de uma vez. Cada camada tem um critério de aceite (seção 11) antes de subir para a próxima.
P2. A pasta da fábrica é a fronteira. Nada fora dela é lido ou escrito sem prompt (regra deny + hook).
P3. Quem produz não revisa (Regras Comuns v2.1). Isso vira configuração de subagentes com modelos distintos, não só instrução em texto.
P4. Todo lote deixa rastro: log da execução, transcrição da sessão, commit no git.
P5. O que a documentação não confirma não entra como certeza. A seção 12 lista os pontos a verificar.

==========================================================
2. NÍVEIS DE AUTONOMIA (vocabulário do protocolo)
==========================================================

N0 — Manual. `--permission-mode default`. Cada ação pede aprovação. Uso: primeira execução de qualquer orquestrador novo.

N1 — Supervisionado. `--permission-mode acceptEdits` + regras allow no settings.json. Edições e comandos comuns de arquivo dentro da pasta passam sem prompt; o resto pede. Sessão interativa, você presente.

N2 — Autônomo com travas (PADRÃO DA FÁBRICA). `claude -p` (headless) com `--permission-mode auto`, `--permission-prompts none`, `--max-turns`, `--max-budget-usd`, hook PreToolUse de escopo e regras deny. O modo auto usa um segundo modelo (classificador) que bloqueia ações que escapem do pedido, mirem infraestrutura desconhecida ou pareçam induzidas por conteúdo hostil lido pelo Claude. A documentação diz: "reduz prompts mas não garante segurança". Com `--permission-prompts none`, tudo que pediria aprovação é negado em vez de travar a execução.

N3 — Bypass. `--dangerously-skip-permissions` (= `bypassPermissions`). Desliga prompts e verificações; só regras deny continuam valendo e regras allow deixam de ter efeito. Documentação: "use somente em ambientes isolados como containers, VMs ou dev containers sem internet, onde o Claude Code não possa danificar o sistema hospedeiro". Neste protocolo, N3 só é admitido dentro de um container Docker com a pasta da fábrica montada e nada mais (seção 10). Não há caso de uso da fábrica que exija N3; fica em BACKLOG.

Computer use (mouse/teclado/aplicativos) NÃO faz parte da fábrica. Se um dia for usado, é no Cowork (Configurações > Geral > "Enable computer use", macOS/Windows, planos Pro/Max, beta/research preview), com permissão por aplicativo e sem sandbox entre o Claude e os aplicativos. No Claude Code CLI o `computer-use` é só macOS e não funciona com `-p`, então não é agendável.

==========================================================
3. TOPOLOGIA
==========================================================

Windows (hospedeiro)
 └─ E:\Projeto - Plataforma IA (Câmara 2026)\      ← pasta visível para você no Explorer
      └─ fabrica\                                   ← raiz do repositório felipeRM (clone)
WSL2 (Ubuntu)
 └─ /mnt/e/Projeto - Plataforma IA (Câmara 2026)/fabrica   ← mesma pasta, vista do Linux
      Claude Code instalado e executado AQUI (dentro do WSL), nunca no PowerShell.

Por que WSL2 e não Windows nativo: o sandbox de shell do Claude Code "roda em macOS, Linux e WSL2; em Windows nativo, os comandos rodam sem sandbox" (tabela de setup: Windows nativo "Not supported", WSL 2 "Supported", WSL 1 "Not supported"). A documentação instrui: "instale e inicie `claude` dentro do terminal WSL, não do PowerShell ou CMD".

Sobre o caminho /mnt/e/: o mapeamento de unidades Windows em /mnt/<letra>/ é o comportamento padrão do WSL, mas NÃO CONFIRMADO na documentação do Claude Code (só /mnt/c/ aparece, em contexto de troubleshooting). Dois pontos a testar na Fase 0: (i) se `ls "/mnt/e/Projeto - Plataforma IA (Câmara 2026)"` funciona; (ii) se o sandbox (bubblewrap) aceita escrever em /mnt/e/. Se (ii) falhar, use a variante B: repositório dentro do WSL (`~/fabrica`) e a pasta E:\ como espelho atualizado por `git pull` ao fim de cada lote. A variante B também costuma ser mais rápida (acesso a NTFS via /mnt é lento) — isso é experiência comum, não afirmação da documentação.

Evite espaços e acentos no caminho que o Claude Code vai usar: crie uma junção no Windows (`mklink /J E:\fabrica "E:\Projeto - Plataforma IA (Câmara 2026)\fabrica"`) ou use a variante B. Os exemplos abaixo usam `/mnt/e/fabrica` como raiz; ajuste se mantiver o caminho longo.

==========================================================
4. FASE 0 — PRÉ-REQUISITOS (uma vez)
==========================================================

4.1 No Windows (PowerShell como administrador):
    wsl --install -d Ubuntu
    (reinicie se pedido; crie o usuário Linux NÃO root)

4.2 Dentro do Ubuntu (WSL):
    sudo apt update && sudo apt install -y git python3 curl
    # Instalador nativo do Claude Code para Linux — confirme o comando exato em
    # https://code.claude.com/docs/en/setup antes de rodar:
    curl -fsSL https://claude.ai/install.sh | bash
    claude --version
    claude            # primeira vez: faça /login com a conta do plano (Pro/Max)

4.3 Clonar a fábrica:
    mkdir -p /mnt/e/fabrica && cd /mnt/e/fabrica
    git clone https://github.com/feliperibeiromatos-create/felipeRM .
    git config user.name "Fábrica Câmara 2026"
    git config user.email "felipe.ribeiromatos@gmail.com"

4.4 Testes de aceite da Fase 0:
    [ ] `claude --version` responde dentro do WSL
    [ ] `/login` concluído e `claude -p "diga OK"` responde "OK"
    [ ] Escrita em /mnt/e/fabrica funciona (`touch teste && rm teste`)
    [ ] Dentro do `claude`, `/sandbox` liga sem erro e um `echo` roda sandboxed (se falhar em /mnt/e, adote a variante B da seção 3)

==========================================================
5. ESTRUTURA DA PASTA
==========================================================

fabrica/
├── CLAUDE.md                     ← regras comuns da fábrica (lidas em toda sessão)
├── .claude/
│   ├── settings.json             ← permissões, sandbox, hooks (versionado no git)
│   ├── settings.local.json       ← ajustes só desta máquina (no .gitignore)
│   ├── agents/                   ← um .md por unidade (seção 8)
│   ├── rules/                    ← regras por caminho (opcional)
│   └── hooks/
│       └── escopo.py             ← hook PreToolUse (seção 7)
├── orquestradores/
│   ├── LOTE.md  BANCO.md  SIMULADO.md  DISCURSIVA.md   ← prompts de tarefa
├── ordens/                       ← ordens da Presidência (bloco REMETENTE/DESTINATÁRIO/PROMPT), uma por arquivo
├── estado/
│   └── Estado_Canonico_Camara_2026.md   ← cópia local; o Fundador transporta de/para o Projeto
├── saida/
│   ├── GCE/  GCB/  GBQ/          ← produtos, pareceres de QA e conferências (sufixo _auto)
├── logs/                         ← uma pasta por execução (stdout json + resumo)
├── bin/
│   ├── run_lote.sh               ← executor headless (seção 9)
│   └── nova_ordem.sh             ← cria arquivo de ordem a partir do clipboard/arquivo
└── .gitignore                    ← logs/, .claude/settings.local.json, .env

==========================================================
6. CONFIGURAÇÃO — .claude/settings.json
==========================================================

Chaves e sintaxe de regra conforme https://code.claude.com/docs/en/permissions, /settings-reference e /sandboxing. Regras deny valem em todos os modos e são aplicadas pelo Claude Code, não pelo modelo. O sufixo `:*` equivale a ` *` (curinga final).

```json
{
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": [
      "Read",
      "Edit",
      "Write",
      "Glob",
      "Grep",
      "Bash(git status:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git pull:*)",
      "Bash(python3:*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(wc:*)",
      "Bash(mkdir:*)",
      "WebFetch(domain:cdn.cebraspe.org.br)",
      "WebFetch(domain:www.camara.leg.br)",
      "WebFetch(domain:www2.camara.leg.br)",
      "WebFetch(domain:www.planalto.gov.br)"
    ],
    "ask": [
      "Bash(git push:*)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(~/.ssh/**)",
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(git push --force:*)",
      "Bash(git reset --hard:*)",
      "WebFetch(domain:pciconcursos.com.br)",
      "WebFetch(domain:qconcursos.com)",
      "WebFetch(domain:tecconcursos.com.br)"
    ],
    "blockReadsOutsideWorkingDirectories": true
  },
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "network": {
      "allowedDomains": [
        "github.com",
        "cdn.cebraspe.org.br",
        "www.camara.leg.br",
        "www2.camara.leg.br",
        "www.planalto.gov.br"
      ]
    }
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/escopo.py"
          }
        ]
      }
    ]
  }
}
```

Notas:
- `defaultMode` recebe os mesmos nomes dos modos de permissão; que ele aceite "auto" NÃO CONFIRMADO no trecho lido — por isso o padrão aqui é "acceptEdits" e o modo auto é passado por linha de comando no executor (seção 9).
- `blockReadsOutsideWorkingDirectories` é chave documentada no índice do settings-reference; sua semântica exata deve ser conferida na página antes de confiar nela.
- As regras `WebFetch(domain:...)` em deny implementam a vedação a espelhos de terceiros (Regras Comuns). Acrescente outros domínios conforme aparecerem.
- O sandbox cobre só comandos de shell; "as ferramentas de arquivo, servidores MCP e hooks rodam fora dele". Por isso o hook da seção 7 existe.
- Em modo bypass (N3) as regras allow deixam de valer; deny continua. Mais um motivo para N3 só em container.

==========================================================
7. HOOK DE ESCOPO — .claude/hooks/escopo.py
==========================================================

Recebe no stdin o JSON documentado do PreToolUse (campos `tool_name`, `tool_input`, `cwd`, `permission_mode`, ...). Devolve `hookSpecificOutput.permissionDecision` com valor `allow`, `deny`, `ask` ou `defer`. Saída com exit 0 é lida como JSON; exit 2 bloqueia e o JSON não pode sobrepor o bloqueio. Regras deny e ask do settings continuam prevalecendo sobre um `allow` do hook.

Campo do caminho em Edit/Write: a documentação do hook mostra `tool_input.command` para Bash; para Edit/Write o campo usual é `tool_input.file_path` — confirme nos exemplos de https://code.claude.com/docs/en/hooks antes de depender dele (o script trata ausência do campo como "ask").

```python
#!/usr/bin/env python3
"""Hook PreToolUse de escopo da Fábrica Câmara 2026.
Política: tudo dentro da raiz da fábrica é permitido; fora dela, nega.
Comandos Bash: só a lista branca abaixo; o resto devolve 'ask'
(que, em headless com --permission-prompts none, equivale a negar)."""
import json
import os
import re
import sys

RAIZ = os.environ.get("FABRICA_RAIZ") or os.getcwd()
RAIZ = os.path.realpath(RAIZ)

BASH_PERMITIDO = [
    r"^git (status|add|commit|diff|log|pull)\b",
    r"^python3 ",
    r"^(ls|cat|wc|mkdir|head|tail|find|grep)\b",
]
BASH_PROIBIDO = [
    r"\brm\s+-rf\b", r"\bsudo\b", r"\bcurl\b", r"\bwget\b",
    r"\bgit push\b", r"\bchmod\b", r"\bchown\b", r"\bmv\b.*\.\./",
    r"/mnt/[a-z]/(?!fabrica)",   # outras pastas das unidades Windows
    r"~/|\$HOME", r"\.ssh", r"\.env",
]

def decidir(decisao, motivo):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decisao,
            "permissionDecisionReason": motivo,
        }
    }))
    sys.exit(0)

def dentro_da_raiz(caminho):
    if not caminho:
        return False
    if not os.path.isabs(caminho):
        caminho = os.path.join(RAIZ, caminho)
    return os.path.realpath(caminho).startswith(RAIZ + os.sep)

def main():
    try:
        dados = json.load(sys.stdin)
    except Exception as exc:  # entrada inválida: não aprova nada
        decidir("ask", f"hook: stdin inválido ({exc})")
    ferramenta = dados.get("tool_name", "")
    entrada = dados.get("tool_input", {}) or {}

    if ferramenta in ("Edit", "Write"):
        alvo = entrada.get("file_path")
        if alvo is None:
            decidir("ask", "hook: file_path ausente")
        if dentro_da_raiz(alvo):
            decidir("allow", "hook: arquivo dentro da fábrica")
        decidir("deny", f"hook: fora da fábrica: {alvo}")

    if ferramenta == "Bash":
        cmd = (entrada.get("command") or "").strip()
        for padrao in BASH_PROIBIDO:
            if re.search(padrao, cmd):
                decidir("deny", f"hook: comando proibido ({padrao})")
        for padrao in BASH_PERMITIDO:
            if re.search(padrao, cmd):
                decidir("allow", "hook: comando na lista branca")
        decidir("ask", "hook: comando fora da lista branca")

    decidir("ask", "hook: ferramenta não coberta")

if __name__ == "__main__":
    main()
```

Teste manual do hook (dentro do WSL, na raiz da fábrica):
    echo '{"tool_name":"Bash","tool_input":{"command":"sudo rm -rf /"}}' | python3 .claude/hooks/escopo.py
    → deve imprimir permissionDecision "deny"
    echo '{"tool_name":"Edit","tool_input":{"file_path":"saida/GCE/x.md"}}' | python3 .claude/hooks/escopo.py
    → deve imprimir "allow"

==========================================================
8. SUBAGENTES — .claude/agents/*.md
==========================================================

Local documentado: `.claude/agents/` (projeto). Frontmatter: `name` e `description` obrigatórios; `model` aceita `sonnet`, `opus`, `haiku`, `fable`, ID completo (ex.: `claude-opus-5-5`) ou `inherit`; `tools`/`disallowedTools` como lista separada por vírgula; `permissionMode`, `maxTurns`, `effort` documentados. Nomes de campo são sensíveis a maiúsculas.

Mapa das unidades (modelos conforme Protocolo EXEC e Regras Comuns: produção ≠ QA):

| arquivo              | papel                                   | model  | tools                                   |
|----------------------|-----------------------------------------|--------|-----------------------------------------|
| gce-cpp.md           | produção GCE (P2 fala/transcrição/IA)   | sonnet | Read, Write, Edit, Glob, Grep, WebFetch |
| gce-cqfp.md          | QA GCE                                  | opus   | Read, Write, Glob, Grep, WebFetch       |
| gcb-cpp.md           | produção GCB (P1 TI e dados)            | sonnet | Read, Write, Edit, Glob, Grep, WebFetch |
| gcb-cqfp.md          | QA GCB                                  | opus   | Read, Write, Glob, Grep, WebFetch       |
| qa-normativo.md      | QA de fontes normativas (artigo/inciso) | opus   | Read, Write, Glob, Grep, WebFetch       |
| gbq-cfp.md           | fontes e proveniência do banco          | sonnet | Read, Write, Edit, Glob, Grep, WebFetch |
| gbq-csc.md           | simulados e calibração                  | sonnet | Read, Write, Edit, Glob, Grep           |
| corretor-a.md        | correção de discursiva, corretor A      | sonnet | Read, Write, Glob, Grep                 |
| corretor-b.md        | correção de discursiva, corretor B      | opus   | Read, Write, Glob, Grep                 |
| secretaria.md        | atualiza estado/Estado_Canonico local   | sonnet | Read, Write, Edit, Glob, Grep           |

QA não recebe `Edit`: escreve parecer novo, não altera o produto (separação produção × QA por configuração, não só por instrução).

Exemplo — .claude/agents/gce-cqfp.md:

```markdown
---
name: gce-cqfp
description: QA independente da GCE (Coordenação de Qualidade, Fontes e Proveniência). Usar para revisar lotes produzidos por gce-cpp. Nunca revisa produção própria.
model: opus
tools: Read, Write, Glob, Grep, WebFetch
maxTurns: 40
---

Você é a GCE-CQFP da Fábrica Câmara 2026. Revise o lote indicado conforme as Regras Comuns v2.1 (em CLAUDE.md) e o padrão de lote da GCE.

Entregue APENAS um parecer em saida/GCE/<lote>_parecer_QA_R<n>_auto.md com:
- tabela de itens com veredito (APROVADO / CORRIGIR / REPROVAR) e motivo;
- conferência de rótulos (CEBRASPE_OFICIAL, CEBRASPE_ANALOGA, OUTRA_OFICIAL, AUTORAL; CEBRASPE_ESTILO é vedado);
- fontes: cada link oficial aberto leva "verificado em [data]"; link que não abre é declarado "não aberta", nunca presumido;
- contagem de [TS] e de itens VOLÁTIL contra os tetos do lote;
- lista de pendências classificadas (AGORA / PRÓXIMO / BACKLOG / DESCARTADO).
Não edite o arquivo de produção. Máximo de 2 rodadas; na segunda, registre o que ficou em aberto para decisão da Gerência.
```

Exemplo — .claude/agents/gce-cpp.md (resumido; o texto de instalação completo da unidade já existe no Projeto):

```markdown
---
name: gce-cpp
description: Produção pedagógica da GCE (P2 — reconhecimento de fala, transcrição e IA). Usar para produzir lotes a partir de uma ordem.
model: sonnet
tools: Read, Write, Edit, Glob, Grep, WebFetch
maxTurns: 60
---

Você é a GCE-CPP. Produza o lote conforme a ordem em ordens/ e o padrão de lote da GCE:
marcadores "PARTE n/N", "FIM DA PARTE n/N" e "FIM DO LOTE n"; itens C/E em seção (d) sem [TS] e sem gabarito e seção (d-G) com gabarito comentado, [TS], VOLÁTIL e "convertido/novo"; no máximo 4 itens dependentes de produto (no máximo 1 de risco ALTO); 8 a 12 C em 20; mínimo de 2 itens por subitem.
Fontes: só as oficiais listadas em CLAUDE.md, com "verificado em [data]". Nunca invente fonte. Grave em saida/GCE/<lote>_v<n>_producao_auto.md.
```

==========================================================
9. EXECUTOR HEADLESS — bin/run_lote.sh
==========================================================

Flags documentadas no CLI reference: `-p`, `--output-format json|text|stream-json`, `--permission-mode`, `--permission-prompts none` (v2.1.259+; nega o que pediria aprovação), `--max-turns` (só em print), `--max-budget-usd` (só em print; para quem usa assinatura, é um teto de estimativa, não cobrança — D-GASTO continua: cota do plano, sem gasto extra), `--model`, `--append-system-prompt`. `--bare` NÃO é usado aqui porque pula hooks, agentes e CLAUDE.md, que são justamente as travas.

```bash
#!/usr/bin/env bash
# Uso: bin/run_lote.sh ordens/ORDEM_LOTE6C.md
# Executa um orquestrador em modo N2 (auto + hook + deny), com log e commit.
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"
export FABRICA_RAIZ="$RAIZ"

ORDEM="${1:?informe o arquivo da ordem (ordens/ORDEM_*.md)}"
[ -f "$ORDEM" ] || { echo "ordem não encontrada: $ORDEM" >&2; exit 1; }

# A ordem diz qual orquestrador usar: linha "ORQUESTRADOR: LOTE|BANCO|SIMULADO|DISCURSIVA"
ORQ="$(grep -m1 -E '^ORQUESTRADOR:' "$ORDEM" | sed -E 's/^ORQUESTRADOR:[[:space:]]*//')"
[ -f "orquestradores/${ORQ}.md" ] || { echo "orquestrador inválido: '$ORQ'" >&2; exit 1; }

STAMP="$(date +%Y%m%d-%H%M%S)"
LOG="logs/${STAMP}_${ORQ}_$(basename "$ORDEM" .md)"
mkdir -p "$LOG"

MAX_TURNS="${MAX_TURNS:-150}"
MAX_USD="${MAX_USD:-15}"
MODELO="${MODELO:-sonnet}"   # orquestrador; subagentes usam o model do próprio .md

PROMPT="$(cat "orquestradores/${ORQ}.md")

=== ORDEM ===
$(cat "$ORDEM")
=== FIM DA ORDEM ===

Ao terminar, grave em ${LOG}/RESUMO.md: arquivos produzidos, contagens, resultado do QA, pendências classificadas, e a linha final 'FIM DA EXECUÇÃO'."

claude -p "$PROMPT" \
  --model "$MODELO" \
  --permission-mode auto \
  --permission-prompts none \
  --max-turns "$MAX_TURNS" \
  --max-budget-usd "$MAX_USD" \
  --output-format json \
  > "${LOG}/saida.json" 2> "${LOG}/stderr.log" || echo "claude saiu com código $?" >> "${LOG}/stderr.log"

# Critério de conclusão: resumo existe e termina com a sentinela
if [ -f "${LOG}/RESUMO.md" ] && grep -q 'FIM DA EXECUÇÃO' "${LOG}/RESUMO.md"; then
  git add -A saida/ estado/ ordens/
  git commit -m "fábrica: ${ORQ} $(basename "$ORDEM" .md) [${STAMP}]" || true
  mv "$ORDEM" "ordens/concluidas/" 2>/dev/null || { mkdir -p ordens/concluidas && mv "$ORDEM" ordens/concluidas/; }
  echo "OK: ${LOG}/RESUMO.md"
else
  echo "INCOMPLETO: ver ${LOG}/stderr.log e ${LOG}/saida.json" >&2
  exit 2
fi
```

Observações:
- O executor nunca faz `git push`: push é regra `ask` e, em headless, seria negado. Você faz o push (ou libera `Bash(git push origin main)` em allow quando a Fase 2 estiver aceita).
- `--max-turns` e `--max-budget-usd` são as travas de custo. Comece baixo (50 turnos) e suba conforme o lote exigir.
- A sentinela "FIM DA EXECUÇÃO" cumpre a mesma função que "FIM DO LOTE n" nas entregas: detectar truncamento.

Formato do arquivo de ordem (ordens/ORDEM_LOTE6C.md), compatível com a seção 3 do Protocolo EXEC:

```
ORQUESTRADOR: LOTE
REMETENTE: Presidência
DESTINATÁRIO: EXEC (fábrica local)
PROMPT:
a) Objeto: Lote 6c, produção + QA (máx. 2 rodadas) + conferência de aplicação
b) Gerência titular: GCB
c) Escopo: itens 7.1, 8.1–8.4 do edital (texto literal: ...)
d) Arquivos-base: saida/GCB/Lote6a_v2_producao_auto.md (modelo de formato), estado/Estado_Canonico_Camara_2026.md
e) Regras específicas: 20 itens C/E, 8–12 C, máx. 4 dependentes de produto (máx. 1 ALTO), [TS] e VOLÁTIL marcados
f) Saída: saida/GCB/Lote6c_v1_producao_auto.md, saida/GCB/Lote6c_parecer_QA_R1_auto.md, saida/GCB/Lote6c_conferencia_auto.md
g) Classificação: AGORA
```

Orquestrador — orquestradores/LOTE.md (esqueleto):

```
Você é o orquestrador LOTE da Fábrica Câmara 2026. Não decide matéria reservada; executa a ordem abaixo.
1. Leia estado/Estado_Canonico_Camara_2026.md e a ordem. Se a ordem contradisser o Estado Canônico, pare e registre o conflito no RESUMO (retorno C).
2. Delegue a produção ao subagente da Gerência titular (gce-cpp ou gcb-cpp).
3. Delegue o QA ao subagente de QA da mesma Gerência (gce-cqfp ou gcb-cqfp). Nunca o mesmo subagente para os dois passos.
4. Se o parecer pedir correções, devolva ao produtor UMA vez (v2) e rode QA R2. Depois disso, não há terceira rodada: registre pendências.
5. Peça ao subagente secretaria para anotar no Estado Canônico local: lote, versões, resultado, pendências.
6. Grave o RESUMO conforme instruído no prompt.
```

==========================================================
10. AGENDAMENTO (Fase 3 — PRÓXIMO)
==========================================================

Quatro opções documentadas; a fábrica precisa de acesso à pasta local, o que elimina a primeira.

a) Routines na nuvem (code.claude.com/docs/en/routines): rodam na infraestrutura da Anthropic, sem aprovação, por agenda/HTTP/GitHub; NÃO acessam a máquina local. Descartado para a fábrica. (Serviria, em BACKLOG, para um "vigia" que só lê o repositório no GitHub e abre uma issue.)

b) Tarefas agendadas locais do app Desktop (code.claude.com/docs/en/desktop-scheduled-tasks): aba Code → Routines → New routine → Local; campos Nome, Descrição, Instruções, Agenda, pasta de trabalho obrigatória; presets Manual/Hourly/Daily/Weekdays/Weekly; cada tarefa tem o próprio modo de permissão; regras allow de ~/.claude/settings.json valem; em modo Manual a execução trava até você aprovar; só roda com o app aberto e a máquina acordada (Settings > This computer > System para manter acordada); uma execução de recuperação por horário perdido (últimos 7 dias). Prompt gravado em ~/.claude/scheduled-tasks/<nome>/SKILL.md. Exige Desktop 1.1.5368+. RECOMENDADA como primeira forma de agendamento: zero script, permissões visíveis na interface. Ponto a verificar: se a tarefa Local do Desktop no Windows executa dentro do WSL ou no Windows nativo (NÃO CONFIRMADO) — se for nativo, perde-se o sandbox e vale a opção (c).

c) Agendador de Tarefas do Windows chamando o WSL (robusto, sem app aberto):
   Programa: wsl.exe
   Argumentos: -d Ubuntu -u <seu_usuario> -- bash -lc "cd /mnt/e/fabrica && bin/run_lote.sh ordens/$(ls ordens | grep -m1 '^ORDEM_')"
   Gatilho: diário às 02:00, ou "ao fazer logon". Marque "Executar com privilégios mais altos" DESLIGADO.
   O comando `wsl.exe -d ... -- bash -lc` é comportamento padrão do WSL, não documentado pelo Claude Code (NÃO CONFIRMADO ali).

d) cron dentro do WSL: exige WSL com systemd ativo (/etc/wsl.conf com `[boot] systemd=true`) e o WSL em execução; mais frágil que (c). Só se (c) não servir.

Fora de cogitação: `/loop` e o agendador interno de sessão (CronCreate) — só funcionam com o Claude Code aberto e ocioso, expiram em 7 dias.

==========================================================
11. SEGURANÇA E OPERAÇÃO
==========================================================

S1. Usuário Linux não root; nunca `sudo` na fábrica (deny).
S2. Nenhuma credencial dentro da pasta: `.env`, tokens, chaves ficam fora de /mnt/e/fabrica e em deny. O login do Claude Code fica em ~/.claude, fora da raiz.
S3. Rede: o sandbox limita comandos de shell aos domínios listados; WebFetch é limitado por regras allow/deny de domínio. Novos domínios oficiais entram por decisão registrada (Secretaria), não por conveniência de um lote.
S4. Git é o backup: todo lote concluído vira commit; push manual até a Fase 2 ser aceita.
S5. Botão de parada: Ctrl+C no terminal; no agendador, desabilitar a tarefa; `CLAUDE_CODE_DISABLE_CRON=1` desliga o agendador interno de sessão.
S6. Auditoria: logs/<execução>/ + transcrição (caminho em `transcript_path` do hook, sob ~/.claude/projects/). Guarde 30 dias.
S7. Injeção de prompt: a fábrica lê PDFs e páginas externas. O classificador do modo auto e o hook reduzem, não eliminam, o risco; por isso o escopo de escrita é a pasta e o push é manual.
S8. Quota: produção em Sonnet, QA em Opus; orquestrador em Sonnet. Fable só na Presidência (chat), nunca na fábrica. `--max-budget-usd` é teto de estimativa.
S9. N3 (bypass) somente em container: `docker run --rm -v /mnt/e/fabrica:/work -w /work --network none ...` com o Claude Code instalado na imagem e nada do hospedeiro montado além de /work. Sem rede, WebFetch não funciona — logo N3 só serve para tarefas offline (BANCO/SIMULADO sobre material já coletado). BACKLOG.

==========================================================
12. ROTEIRO DE IMPLANTAÇÃO E CRITÉRIOS DE ACEITE
==========================================================

Fase 0 — Pré-requisitos (seção 4). Aceite: 4 caixas marcadas.
Fase 1 — N0/N1 interativo. Rodar o orquestrador LOTE num lote já aprovado (ex.: 6a) em `--permission-mode default`, observando cada ação; depois em `acceptEdits`. Aceite: produto e parecer gerados sem nenhuma escrita fora de saida/ e estado/; hook testado (seção 7); diff do git revisado por você.
Fase 2 — N2 headless supervisionado. `bin/run_lote.sh` num lote novo, você presente, lendo logs ao vivo (`tail -f logs/.../stderr.log`). Aceite: RESUMO.md com sentinela; QA em Opus comprovado (model no log); zero negações do hook por motivo legítimo (se houver, ajustar lista branca e repetir); custo estimado dentro do teto. Repetir em 2 lotes antes de passar à Fase 3.
Fase 3 — Agendado (opção b ou c da seção 10). Aceite: 3 execuções agendadas consecutivas concluídas sem intervenção; relatório ao Fundador.
Fase 4 — BACKLOG: container N3 para tarefas offline; routine na nuvem como vigia do repositório.

==========================================================
13. PONTOS NÃO CONFIRMADOS NA DOCUMENTAÇÃO (verificar antes de confiar)
==========================================================

1. Mapeamento /mnt/e/ e funcionamento do sandbox (bubblewrap) sobre /mnt/e/ — testar na Fase 0.
2. `permissions.defaultMode` aceitar o valor "auto" — por isso o modo auto vai por linha de comando.
3. Campo `tool_input.file_path` para Edit/Write no JSON do hook — conferir na página de hooks.
4. Semântica exata de `permissions.blockReadsOutsideWorkingDirectories`.
5. Se as tarefas agendadas locais do Desktop no Windows executam no WSL ou no Windows nativo.
6. Comando exato do instalador Linux (install.sh) — conferir em /setup.
7. Nome dos pacotes do Agent SDK (não usado neste protocolo; só se um dia o executor virar programa Python).
8. Limites numéricos: faixa de `maxTurns` de subagente; número máximo de tarefas agendadas no Desktop.
Tudo isso pode mudar rápido: vários recursos (modo auto, routines, computer use) estão em preview. Reverificar as páginas antes de cada fase.

==========================================================
14. GOVERNANÇA (Projeto Câmara 2026)
==========================================================

- Este protocolo não altera o Protocolo EXEC: a fábrica local é a EXEC em outra sede. Só a Presidência ordena; Gerências pedem por retorno B; o Fundador transporta a ordem (arquivo em ordens/) e traz de volta o Estado Canônico.
- A fábrica não cria unidades, não interpreta matéria reservada e não responde "encaminhe para X".
- Entrega de cada execução: arquivos em saida/<Gerência>/ com sufixo _auto + RESUMO.md; o Fundador grava os arquivos no Projeto e a Gerência titular emite o gatilho A pela via normal.
- Decisões deste protocolo a registrar pela Secretaria de Estado Canônico: D-FAB-LOCAL (sede local no WSL2), D-FAB-N2 (nível padrão), D-FAB-N3-CONTAINER (bypass só em container, BACKLOG), D-FAB-FASES (roteiro e aceites).

Fontes oficiais consultadas (verificadas em 10–12/10/2026):
https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/permissions · https://code.claude.com/docs/en/settings-reference · https://code.claude.com/docs/en/hooks · https://code.claude.com/docs/en/headless · https://code.claude.com/docs/en/cli-reference · https://code.claude.com/docs/en/sandboxing · https://code.claude.com/docs/en/sub-agents · https://code.claude.com/docs/en/memory · https://code.claude.com/docs/en/setup · https://code.claude.com/docs/en/scheduled-tasks · https://code.claude.com/docs/en/desktop-scheduled-tasks · https://code.claude.com/docs/en/routines · https://code.claude.com/docs/en/computer-use · https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork · https://support.claude.com/en/articles/13364135-use-claude-cowork-safely

----------------------------------------------------------
REMETENTE: Chat técnico (Fable 5.1) — proposta ao Fundador
DESTINATÁRIO: Fundador; cópia à Secretaria de Estado Canônico após decisão
PROMPT:
┌──────────────────────────────────────────────────────────────┐
│ CIÊNCIA — Secretaria de Estado Canônico: registrar, após      │
│ decisão do Fundador, o documento claude/FABRICA_Protocolo_    │
│ Autonomia_v1.md (12/10/2026) e as decisões D-FAB-LOCAL,       │
│ D-FAB-N2, D-FAB-N3-CONTAINER e D-FAB-FASES, com classificação │
│ AGORA (Fases 0–2), PRÓXIMO (Fase 3) e BACKLOG (Fase 4).        │
└──────────────────────────────────────────────────────────────┘
