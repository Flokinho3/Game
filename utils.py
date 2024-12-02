import os

def verificar_pastas(base_path):
    # Caminho da pasta "Ambiente"
    ambiente_path = os.path.join(base_path, 'Game', 'Ambiente')
    
    if not os.path.exists(ambiente_path):
        os.makedirs(ambiente_path)
        print(f"Pasta {ambiente_path} criada com sucesso.")
    else:
        print(f"Pasta {ambiente_path} já existe.")
