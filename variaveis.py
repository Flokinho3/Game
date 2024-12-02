import os
import json
from tkinter import messagebox

class Variaveis:
    @staticmethod
    def carregar_config(base_path):
        # Caminho do arquivo Ambiente.json baseado no diretório do projeto
        file_path = os.path.join(base_path, 'Game', 'Ambiente', 'Ambiente.json')

        # Verifica se o arquivo existe
        if not os.path.exists(file_path):
            # Cria um JSON padrão
            data = {
                'path': os.path.join(base_path, 'Game', 'Ambiente'),
                'name': 'Ambiente.json',
                'FILE_GAME_MAIN': 'main.py'
            }
            try:
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=4)
                print(f"Arquivo {file_path} criado com sucesso.")
                return data
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível criar {file_path}: {e}")
                return {}
        else:
            # Carrega o JSON existente
            try:
                with open(file_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, ValueError) as e:
                messagebox.showerror("Erro", f"Erro ao carregar o arquivo {file_path}: {e}")
                return {}
