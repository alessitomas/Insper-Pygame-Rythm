# Import do Pygame
import pygame
import time


#Inicialização do Game
def inicializa():
    pygame.init()
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    window = pygame.display.set_mode((1280, 720))
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Tenor Blade')
    icon = pygame.image.load('sprites/tabicon.png')
    pygame.display.set_icon(icon)

    assets = {
        'protag': [
            pygame.image.load('sprites/protag1.png'),
            pygame.image.load('sprites/protag2.png'),
            pygame.image.load('sprites/protag3.png'),
            pygame.image.load('sprites/protag4.png'),
            pygame.image.load('sprites/protag5.png'),
            pygame.image.load('sprites/protag6.png')
            ],
        'sewerbg': [
            pygame.image.load('sprites/bg1.png'),
            pygame.image.load('sprites/bg2.png'),
            pygame.image.load('sprites/bg3.png'),
            pygame.image.load('sprites/bg4.png'),
            pygame.image.load('sprites/bg5.png'),
            pygame.image.load('sprites/bg6.png'),
            ],
        '3': pygame.image.load('sprites/3.png'),
        '2': pygame.image.load('sprites/2.png'),
        '1': pygame.image.load('sprites/1.png'),
        'hit_it': pygame.image.load('sprites/hit_it.png'),
        'synthsewers': pygame.mixer.music.load('music/synthsewers.ogg'),
        'hitsound': pygame.mixer.Sound('music/hitsound.ogg'),
        'metronome': pygame.mixer.Sound('music/metronome.ogg'),
        }

    state = {'fps': 60,
            'protagframe': 0,
            'bgframe': 0,
            'time_elapsed': 0,
            'song_playing': False,
            'protagbounce': False,
            'synthsewers_timings': [19*60, 23*60, 27*60, 27.5*60, 31*60, 31.5*60, 33*60, 35*60, 35.5*60, 37*60, 39*60, 39.5*60, 41*60, 43*60, 43.5*60, 45*60, 47*60, 47.5*60, 49.5*60, 51.5*60, 52*60, 53*60],
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

    state['events'] = [x for x in state['synthsewers_timings'] if x <= state['time_elapsed']],
    #print(state['events'])

    window.fill((255, 150, 0))
    bg = window.blit(assets['sewerbg'][state['bgframe']], (0,0))

    #Desenhos vão aqui!
    if state['time_elapsed'] % 8 == 0:
        state['bgframe'] += 1
        if state['bgframe'] > 5:
            state['bgframe'] = 0

    if state['protagframe'] > 5:
        state['protagframe'] = 0
        state['protagbounce'] = False
    protag = window.blit(assets['protag'][state['protagframe']], (577, 181))
    
    if state['time_elapsed'] % 30 == 0:
        assets['metronome'].play()

    if state['time_elapsed'] % 60 == 0:
        state['protagbounce'] = True

    if state['protagbounce']:
        if state['time_elapsed'] % 5 == 0:
            state['protagframe'] += 1

    if state['time_elapsed'] <= 14*60:
        pygame.draw.rect(window, (0,0,0), (0,0,1280,150))
        pygame.draw.rect(window, (0,0,0), (0,440,1280,280))

    if state['time_elapsed'] >= 14*60 and state['time_elapsed'] < 15*60:
        pygame.draw.rect(window, (0,0,0), (0,0,1280,720))
    if state['time_elapsed'] >= 15*60 and state['time_elapsed'] < 15.25*60:
        pygame.draw.rect(window, (63.75,63.75,63.75), (0,0,1280,720))
        count_3 = window.blit(assets['3'], (0, 0))
    if state['time_elapsed'] >= 15.25*60 and state['time_elapsed'] < 15.5*60:
        pygame.draw.rect(window, (127.5,127.5,127.5), (0,0,1280,720))
        count_2 = window.blit(assets['2'], (0, 0))
    if state['time_elapsed'] >= 15.5*60 and state['time_elapsed'] < 15.75*60:
        pygame.draw.rect(window, (191.25,191.25,191.25), (0,0,1280,720))
        count_1 = window.blit(assets['1'], (0, 0))
    if state['time_elapsed'] >= 15.75*60 and state['time_elapsed'] < 16*60:
        pygame.draw.rect(window, (255,255,255), (0,0,1280,720))
        count_hit_it = window.blit(assets['hit_it'], (0, 0))

    state['time_elapsed'] += 1
    print(state['time_elapsed'])

    if state['time_elapsed'] in state['synthsewers_timings']:
        assets['hitsound'].play()

    pygame.display.update()

#Atualizar estado
def atualiza_estado(state):

    state['clock'].tick(state['fps'])

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
