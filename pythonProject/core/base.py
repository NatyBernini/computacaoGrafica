import pygame
import sys
import core
from core.input import Input


class Base(object):
    def __init__(self, screenSize=[512, 512]):
        # Inicializar todos os módulos do Pygame
        pygame.init()

        # Definir as configurações de renderização
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # Inicializar buffers para realizar antialiasing (suavização de serrilhados)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        # Usar um perfil de OpenGL para compatibilidade entre plataformas
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE
        )

        # Criar e exibir a janela
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # Definir o texto que aparece na barra de título da janela
        pygame.display.set_caption("Graphics Window")

        # Determinar se o loop principal está ativo
        self.running = True

        # Gerenciar dados e operações relacionadas ao tempo
        self.clock = pygame.time.Clock()

        self.input = Input()

    # Método a ser implementado pelas subclasses
    def initialize(self):
        pass

    # Método a ser implementado pelas subclasses
    def update(self):
        pass

    # Método principal para rodar a aplicação
    def run(self):
        ## Inicialização ##
        self.initialize()

        ## Loop principal ##
        while self.running:
            ## Processar entrada ##

            ## Atualizar ##
            self.update()

            ## Renderizar ##
            pygame.display.flip()  # Exibir a imagem na tela

            # Pausar, se necessário, para alcançar 60 FPS
            self.clock.tick(60)

        ## Encerramento ##
        pygame.quit()
        sys.exit()
