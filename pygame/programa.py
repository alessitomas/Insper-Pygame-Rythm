# Import do Pygame
import pygame


#Inicialização do Game
def inicializa():
    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((1280, 720))

    assets = {
        'protag': [
            pygame.image.load('sprites/protag1.png'),
            pygame.image.load('sprites/protag2.png'),
            pygame.image.load('sprites/protag3.png'),
            pygame.image.load('sprites/protag4.png'),
            pygame.image.load('sprites/protag5.png'),
            pygame.image.load('sprites/protag6.png')
            ],
        'synthsewers': pygame.mixer.Sound('music/synthsewers.ogg')
        }

    state = {'fps': pygame.time.Clock(),
            'protagframe': 0,
            'time_elapsed': 0,
            'song_playing': False,
            'protagbounce': False,
            'synthsewers_timings': []
        }

    return window, assets, state


#Finalização do Game
def finaliza():
    pygame.quit()


#Função desenhar na tela
def desenha(window: pygame.Surface, assets, state):
    if not state['song_playing']:
        assets['synthsewers'].play()
        state['song_playing'] = True

    window.fill((0, 0, 255))

    #Desenhos vão aqui!
    if state['protagframe'] > 5:
        state['protagframe'] = 0
        state['protagbounce'] = False
    protag = window.blit(assets['protag'][state['protagframe']], (577, 244))
    
    if state['time_elapsed'] % 600 == 0:
        state['protagbounce'] = True

    if state['protagbounce']:
        if state['time_elapsed'] % 60 == 0:
            state['protagframe'] += 1


    state['time_elapsed'] += 1
    print(state['time_elapsed'])

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
    state['fps'].tick(60)
    while atualiza_estado(state):
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
