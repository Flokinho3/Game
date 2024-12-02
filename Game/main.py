import pygame
import sys
import json
import os

# Caminho do arquivo de configuração
FILE_CONFIG = "Game/Config/Config.json"

def carregar_config():
    """Carrega o arquivo de configuração."""
    try:
        with open(FILE_CONFIG, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erro: Arquivo {FILE_CONFIG} não encontrado.")
        sys.exit()
    except json.JSONDecodeError as e:
        print(f"Erro ao ler {FILE_CONFIG}: {e}")
        sys.exit()

def salvar_config(config):
    """Salva o arquivo de configuração."""
    try:
        with open(FILE_CONFIG, "w") as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        print(f"Erro ao salvar {FILE_CONFIG}: {e}")

def criar_janela(config):
    """Cria a janela com base na configuração."""
    modo_tela = config["Janela"]["ModoTela"]
    largura = config["Janela"]["Largura"]
    altura = config["Janela"]["Altura"]

    if modo_tela == "Fullscreen":
        info = pygame.display.Info()
        return pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((largura, altura))

def carregar_fundo(janela, config):
    """Carrega e redimensiona a imagem de fundo com base no tamanho da janela."""
    img_path = config["CenaInicial"]
    base_path = "Game/Assets/Fundos/"
    full_path = os.path.join(base_path, img_path)

    if not os.path.exists(full_path):
        print(f"Erro: Imagem de fundo {full_path} não encontrada.")
        sys.exit()
    
    # Carrega e redimensiona a imagem de fundo
    img = pygame.image.load(full_path)
    img = pygame.transform.scale(img, janela.get_size())
    return img

def main():
    pygame.init()
    
    # Carrega configuração inicial
    config = carregar_config()
    
    # Cria janela
    janela = criar_janela(config)
    pygame.display.set_caption(config["Janela"]["Titulo"])
    clock = pygame.time.Clock()

    # Carrega a imagem de fundo inicial
    fundo = carregar_fundo(janela, config)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # Alterna entre modos de tela
                    if config["Janela"]["ModoTela"] == "Janela":
                        config["Janela"]["ModoTela"] = "Fullscreen"
                    else:
                        config["Janela"]["ModoTela"] = "Janela"
                    
                    salvar_config(config)
                    janela = criar_janela(config)  # Recria janela após mudança
                    fundo = carregar_fundo(janela, config)  # Recarrega o fundo
                    pygame.display.set_caption(config["Janela"]["Titulo"])
                elif event.key == pygame.K_ESCAPE:  # Sai do jogo ao pressionar ESC
                    pygame.quit()
                    sys.exit()

        # Desenha a imagem de fundo na tela
        janela.blit(fundo, (0, 0))

        # Atualiza a tela
        pygame.display.update()
        clock.tick(config["Janela"]["FPS"])

if __name__ == "__main__":
    main()
