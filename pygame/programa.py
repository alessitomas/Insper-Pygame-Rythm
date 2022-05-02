# Import do Pygame
import pygame
import time


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
        'synthsewers': pygame.mixer.music.load('music/synthsewers.ogg'),
        'hitsound': pygame.mixer.Sound('music/hitsound.ogg')
        }

    state = {'fps': 60,
            'protagframe': 0,
            'time_elapsed': 0,
            'song_playing': False,
            'protagbounce': False,
            'synthsewers_timings': [19*60],
            'clock': pygame.time.Clock()
        }

    time.sleep(0.3)

    return window, assets, state


#Finalização do Game
def finaliza():
    pygame.quit()


#Função desenhar na tela
def desenha(window: pygame.Surface, assets, state):
    if not state['song_playing']:
        pygame.mixer.music.play()
        state['song_playing'] = True

    window.fill((255, 150, 0))

    #Desenhos vão aqui!
    if state['protagframe'] > 5:
        state['protagframe'] = 0
        state['protagbounce'] = False
    protag = window.blit(assets['protag'][state['protagframe']], (577, 244))
    
    if state['time_elapsed'] % 60 == 0:
        state['protagbounce'] = True
        assets['hitsound'].play()

    if state['protagbounce']:
        if state['time_elapsed'] % 5 == 0:
            state['protagframe'] += 1


    state['time_elapsed'] += 1
    print(state['time_elapsed'])

    #if state['time_elapsed'] in state['synthsewers_timings']:
        #assets['hitsound'].play()

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
        state['clock'].tick(state['fps'])
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
