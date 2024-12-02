import os

def verificar_pastas(base_path):
    """
    Verifica e cria as pastas necessárias dentro do diretório base.

    Args:
        base_path (str): Caminho base onde as pastas devem ser verificadas/criadas.
    """
    # Lista de pastas necessárias
    DIRS = [
        "Game",
        "Game/Ambiente",
        "Game/Bibliotecas",  # Corrigido o nome para "Bibliotecas"
    ]

    # Verifica se as pastas existem; caso contrário, cria-as
    for dir_ in DIRS:
        path = os.path.join(base_path, dir_)
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Pasta criada: {os.path.abspath(path)}")
            else:
                print(f"Pasta já existe: {os.path.abspath(path)}")
        except OSError as e:
            print(f"Erro ao criar a pasta {os.path.abspath(path)}: {e}")
