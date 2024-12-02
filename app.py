import os
from utils import verificar_pastas
from executor import executar_main

def main():
    # Define o diretório base como a localização deste arquivo
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Verifica e cria as pastas necessárias
    verificar_pastas(base_path)

    # Executa o arquivo main.py
    executar_main(base_path)

if __name__ == '__main__':
    main()
