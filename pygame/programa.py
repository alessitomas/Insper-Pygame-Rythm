# Import do Pygame
import pygame


#Inicialização do Game
def inicializa():
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((1280, 720))

    assets = {}

    state = {}

    return window, assets, state


#Finalização do Game
def finaliza():
    pygame.quit()


#Função desenhar na tela
def desenha(window: pygame.Surface, assets, state):
    window.fill((255, 255, 255))

    #Desenhos vão aqui!
    #a

    pygame.display.update()

#Atualizar estado
def atualiza_estado(state):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        else:
            pass
            #Eventos vão aqui!
            #a
    
    return True


def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
