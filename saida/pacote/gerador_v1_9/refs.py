# -*- coding: utf-8 -*-
"""T-56 (T-67: acrescenta a v1.5, C_V15; T-71: acrescenta a v1.6, C_V16; T-81: acrescenta a v1.7, C_V17; T-94: acrescenta a v1.8, C_V18) — referências de comparação lidas do git (somente leitura), em vez de arquivos soltos no diretório do gerador.
Cada referência é um par (commit, caminho); a leitura usa `git show <commit>:<caminho>` e `git archive <commit> <caminho>`.
Nada é gravado no repositório."""
import hashlib, io, json, os, subprocess, tarfile
from common import REPO

# Commits de referência (todos anteriores a esta ocorrência)
C_V1 = '5eab2d9'     # pacote v1 (T-05, 10/10/2026)
C_V11 = 'e97ab1f'    # pacote v1.1 (T-27, 10/10/2026)
C_R0 = '27e594d'     # pacote v1.2 e edição R0 (T-48 produção, 13/10/2026)
C_V12 = '2684ab1'    # pacote v1.2 R1 e edição R1 (T-48 correção R1; SHA-256 f46ed9f8…, canônico pela D-PACOTE-V12)
C_V13 = '9622604'    # pacote v1.3, edição v1.3 e contrato v1.2.1 (T-56 produção, 13/10/2026; SHA-256 fdcb7afd…, aceito pela D-PACOTE-V13)
C_V15 = 'a889100'    # pacote v1.5 R1 (T-61 regerada com a T-64; SHA-256 b4bc65c7…, aceito pela D-PACOTE-V15): primeiro commit em que saida/pacote/pacote.json tem esse SHA (T-67 / T66_decisoes, 7.1.1)
C_V16 = '569c5dd'    # pacote v1.6 (T-67 produção, 14/10/2026; SHA-256 ecc284f9…, aceito pela D-PACOTE-V16) e a edição v1.6 (T-71 / T70_T71_decisoes, 5.3)
C_V17 = '62ab128'    # pacote v1.7 (T-71 produção, 14/10/2026; SHA-256 f20216c2…, aceito pela D-PACOTE-V17): primeiro commit em que saida/pacote/pacote.json tem esse SHA (T-81 / T81_D1_escopo_v1_8, 1.2; conferido por git log)
C_V18 = '46496ca'    # pacote v1.8 e pacote_estudante.json v1.8-E (T-81, 17/10/2026; SHA-256 09d4a457… e 851e2370…, aceitos pela D-PACOTE-V18): primeiro commit com esses SHA (T-94; conferido por git log)
C_V14 = 'e9b6402'    # pacote v1.4, edição v1.4 e contrato v1.2.2 (T-57 produção, 13/10/2026; SHA-256 f8c0c131…, aceito pela D-PACOTE-V14)
PACOTE = 'saida/pacote/pacote.json'
RELATORIO_R0 = 'saida/pacote/pacote_relatorio_2026-10-13.md'
RELATORIO_V12 = 'saida/pacote/pacote_relatorio_2026-10-13.md'


def git_show(commit, caminho):
    """Bytes de <commit>:<caminho>."""
    return subprocess.run(['git', '-C', REPO, 'show', '%s:%s' % (commit, caminho)], check=True, capture_output=True).stdout


def pacote(commit):
    return json.loads(git_show(commit, PACOTE).decode('utf-8'))


def sha256(commit, caminho):
    return hashlib.sha256(git_show(commit, caminho)).hexdigest()


def v1(): return pacote(C_V1)
def v11(): return pacote(C_V11)
def v12(): return pacote(C_V12)
def v13(): return pacote(C_V13)
def v14(): return pacote(C_V14)
def v15(): return pacote(C_V15)
def v16(): return pacote(C_V16)
def v17(): return pacote(C_V17)
def v18(): return pacote(C_V18)


def pasta(commit, caminho_dir):
    """{nome de arquivo: texto} de uma pasta (não recursiva) de um commit (ex.: saida/estudante)."""
    raw = subprocess.run(['git', '-C', REPO, 'archive', commit, caminho_dir], check=True, capture_output=True).stdout
    out = {}
    with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
        for m in tf.getmembers():
            if m.isfile():
                out[os.path.basename(m.name)] = tf.extractfile(m).read().decode('utf-8')
    return dict(sorted(out.items()))


def estudante(commit):
    return pasta(commit, 'saida/estudante')


def materializa(commit, destino):
    """Materializa pacote.json e estudante/ de um commit em `destino` (pasta temporária), no layout de conferencias_R1.py."""
    os.makedirs(os.path.join(destino, 'estudante'), exist_ok=True)
    with open(os.path.join(destino, 'pacote.json'), 'wb') as f:
        f.write(git_show(commit, PACOTE))
    for nome, txt in estudante(commit).items():
        with open(os.path.join(destino, 'estudante', nome), 'w', encoding='utf-8', newline='') as f:
            f.write(txt)
    return destino
