# -*- coding: utf-8 -*-
"""T-94 — executor dos scripts do gerador v1.9 em modo isolado (python3 -I -B _run.py <script.py> [args]): com -I o Python não põe a pasta do script no sys.path;
este executor põe só a pasta do gerador (derivada de __file__) e roda o script como __main__, com sys.argv = [script, args...]."""
import os, runpy, sys
G = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, G)
alvo = os.path.join(G, sys.argv[1])
sys.argv = [alvo] + sys.argv[2:]
runpy.run_path(alvo, run_name='__main__')
