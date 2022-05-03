# Import do Pygame
import pygame
import time
from funcoes import *

fps = 60
clock = pygame.time.Clock()

#Inicialização do Game
def inicializa():
    
    pygame.init()
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    window = pygame.display.set_mode((1280, 720), vsync=1)
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Tenor Blade')
    icon = pygame.image.load('sprites/tabicon.png')
    pygame.display.set_icon(icon)

    assets = load_assets()

    state = {
            'protagframe': 0,
            'bgframe': 0,
            'time_elapsed': 0,
            'song_playing': False,
            'protagbounce': False,
            'synthsewers_blue_right': [19*60, 23*60, 27*60, 27.5*60, 31*60, 31.5*60, 33*60, 35*60, 35.5*60, 37*60, 39*60, 39.5*60, 41*60, 43*60, 43.5*60, 45*60, 47*60, 47.5*60, 49.5*60, 51.5*60, 52*60, 53*60],
            'dt': 1,
            'prev_time': time.time(),
            'slash_right': False,
            'slash_left': False,
            'slash_up': False,
            'slash_down': False,
        }

    #para carregar os assets sem lag depois
    #time.sleep(3)

    return window, assets, state

#Finalização do Game
def finaliza():
    pygame.quit()


#Função desenhar na tela
def desenha(window: pygame.Surface, assets, state):
    
    #Play song
    if not state['song_playing']:
        pygame.mixer.music.play()
        state['song_playing'] = True

    #Process Past Timings
    state['events'] = [event for event in state['synthsewers_blue_right'] if event <= state['time_elapsed']]
    
    #BG Blit
    if state['time_elapsed'] <= 14*60 or state['time_elapsed'] >= 16*60:
        bg = window.blit(assets['sewerbg'][state['bgframe']], (0,0))

    #BG Frames
    if state['time_elapsed'] % 8 == 0:
        state['bgframe'] += 1
        if state['bgframe'] > 5:
            state['bgframe'] = 0

    #Sword
    if state['slash_right']:
        right = window.blit(assets['sword_right'], (0,0))
    if state['slash_left']:
        left = window.blit(assets['sword_left'], (0,0))
    if state['slash_up']:
        up = window.blit(assets['sword_up'], (0,0))
    if state['slash_down']:
        down = window.blit(assets['sword_down'], (0,0))

    if state['time_elapsed'] % 60 == 0:
        state['protagbounce'] = True

    if state['protagframe'] > 5:
        state['protagframe'] = 0
        state['protagbounce'] = False
    if state['time_elapsed'] <= 14*60 or state['time_elapsed'] >= 16*60:
        protag = window.blit(assets['protag'][state['protagframe']], (577, 181))
    
    if state['time_elapsed'] % 30 == 0:
        assets['metronome'].play()

    if state['protagbounce']:
        if state['time_elapsed'] % 5 == 0:
            state['protagframe'] += 1


    #Dramatic Lines
    if state['time_elapsed'] <= 14*60:
        pygame.draw.rect(window, (0,0,0), (0,0,1280,150))
        pygame.draw.rect(window, (0,0,0), (0,440,1280,280))

    #3, 2, 1, HIT IT!
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

    state['time_elapsed'] += 1 * (1/state['dt'])
    #print(state['time_elapsed'])

    if state['time_elapsed'] in state['synthsewers_blue_right']:
        assets['hitsound'].play()

    pygame.display.update()

#Atualizar estado
def atualiza_estado(state):

    for event in pygame.event.get():
        
        #Quit event
        if event.type == pygame.QUIT:
            return False

        #Every other event
        else:

            #Right Sword
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                assets['right_test'].play()
                state['slash_right'] = True
            elif event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                state['slash_right'] = False

            #Left Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                assets['left_test'].play()
                state['slash_left'] = True
            elif event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                state['slash_left'] = False
            
            #Up Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                assets['up_test'].play()
                state['slash_up'] = True
            elif event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_w):
                state['slash_up'] = False

            #Down Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                assets['down_test'].play()
                state['slash_down'] = True
            elif event.type == pygame.KEYUP and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                state['slash_down'] = False

            #Eventos vão aqui!
            #a
    
    return True


def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
        clock.tick(fps)
        now = time.time()
        dt = now - state['prev_time']
        state['prev_time'] = now
        pygame.time.delay(5)
        #print(round(clock.get_fps(),2))


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
