import os
import subprocess
import sys
from tkinter import messagebox
from variaveis import Variaveis

def executar_main(base_path):
    config = Variaveis.carregar_config(base_path)

    if not config:
        return

    # Constrói o caminho completo do arquivo main.py
    main = os.path.join(config['path'], config['FILE_GAME_MAIN'])

    # Verifica se o arquivo main.py existe
    if not os.path.exists(main):
        messagebox.showerror('Erro', f"Arquivo {main} não encontrado.")
        return

    # Executa o arquivo main.py
    print(f"Executando {main}...")
    try:
        subprocess.Popen([sys.executable, main], shell=True)
    except Exception as e:
        messagebox.showerror('Erro', f"Erro ao executar o arquivo {main}: {e}")
