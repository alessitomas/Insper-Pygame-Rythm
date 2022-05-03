# Import do Pygame
import pygame
import time
from funcoes import *

fps = 60
clock = pygame.time.Clock()

def enemy_move(origin, x, y):
    if origin == 'up':
        if y <= 100:
            y += 15
    new_coords = (x, y)
    print(new_coords)
    return new_coords


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
            'enemy_blue_frame': 0,
            'bgframe': 0,
            'time_elapsed': 0,
            'song_playing': False,
            'protagbounce': False,
            'synthsewers_blue_right': [19*60, 23*60, 27*60, 27.5*60, 31*60, 31.5*60, 33*60, 35*60, 35.5*60, 37*60, 39*60, 39.5*60, 41*60, 43*60, 43.5*60, 45*60, 47*60, 47.5*60, 49.5*60, 51.5*60, 52*60, 53*60],
            'dt': 1,
            'prev_time': time.time(),
            'slash_direction': 'none',
            'enemy_up_x': 607,
            'enemy_up_y': -63,
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
    if state['slash_direction'] == 'right':
        right = window.blit(assets['swordright'], (741,333))
    elif state['slash_direction'] == 'left':
        left = window.blit(assets['swordleft'], (417,333))
    elif state['slash_direction'] == 'up':
        up = window.blit(assets['swordup'], (612,150))
    elif state['slash_direction'] == 'down':
        down = window.blit(assets['sworddown'], (612,447))

    #Protag Bounce
    if state['time_elapsed'] % 60 == 0:
        state['protagbounce'] = True

    #Protag Frames
    if state['protagbounce']:
        if state['time_elapsed'] % 5 == 0:
            state['protagframe'] += 1
    if state['protagframe'] > 5:
        state['protagframe'] = 0
        state['protagbounce'] = False

    #Enemies
    if state['time_elapsed'] % 5 == 0:
            state['enemy_blue_frame'] += 1
    if state['enemy_blue_frame'] > 5:
        state['enemy_blue_frame'] = 0
    
    state['enemy_up_y'] = enemy_move('up', state['enemy_up_x'], state['enemy_up_y'])[1]
    
    #Render Protag and Enemies
    if state['time_elapsed'] <= 14*60 or state['time_elapsed'] >= 16*60:
        enemy_up = window.blit(assets['enemy_blue'][state['enemy_blue_frame']], (state['enemy_up_x'], state['enemy_up_y']))
        protag = window.blit(assets['protag'][state['protagframe']], (577, 181))

    #Metronome
    if state['time_elapsed'] % 30 == 0:
        assets['metronome'].play()

    #Dramatic Lines
    #if state['time_elapsed'] <= 14*60:
    #    pygame.draw.rect(window, (0,0,0), (0,0,1280,150))
    #    pygame.draw.rect(window, (0,0,0), (0,440,1280,280))

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
                state['slash_direction'] = 'right'
            elif event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and state['slash_direction'] == 'right':
                state['slash_direction'] = 'none'

            #Left Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                assets['left_test'].play()
                state['slash_direction'] = 'left'
            elif event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_a) and state['slash_direction'] == 'left':
                state['slash_direction'] = 'none'
            
            #Up Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                assets['up_test'].play()
                state['slash_direction'] = 'up'
            elif event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_w) and state['slash_direction'] == 'up':
                state['slash_direction'] = 'none'

            #Down Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                assets['down_test'].play()
                state['slash_direction'] = 'down'
            elif event.type == pygame.KEYUP and (event.key == pygame.K_DOWN or event.key == pygame.K_s) and state['slash_direction'] == 'down':
                state['slash_direction'] = 'none'

            #Eventos vão aqui!
    
    return True


def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
        clock.tick(fps)
        now = time.time()
        dt = now - state['prev_time']
        state['prev_time'] = now
        #pygame.time.delay(5)
        #print(round(clock.get_fps(),2))


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
