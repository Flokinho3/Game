import pygame

class Janela:
    def __init__(self, largura, altura, nome):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.nome = nome
        self.janela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(nome)
        self.fullscreen = False

    def toggle_fullscreen(self):
        # Alterna entre os modos de tela cheia e janela
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            info = pygame.display.Info()  # Obtém informações sobre a tela
            self.janela = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
            self.largura, self.altura = info.current_w, info.current_h
        else:
            self.janela = pygame.display.set_mode((self.largura, self.altura))

    def get_img_fundo(self):
        return pygame.Surface(self.janela.get_size())

    def get_janela(self):
        return self.janela

    def get_largura(self):
        return self.largura

    def get_altura(self):
        return self.altura

    def get_dimensoes(self):
        return (self.largura, self.altura)

    def get_centro(self):
        return (self.largura // 2, self.altura // 2)

    def fechar(self):
        pygame.quit()
