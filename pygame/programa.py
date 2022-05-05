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

    state = load_states()

    #Timings from seconds to FPS
    state['synthsewers_up'] = [timing * fps for timing in state['synthsewers_up']]
    state['synthsewers_up_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_up_inputs']]
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
        #pygame.mixer.music.play()
        state['song_playing'] = True



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



    #Enemy Frames
    if state['time_elapsed'] % 5 == 0:
            state['enemy_frame'] += 1
    if state['enemy_frame'] > 5:
        state['enemy_frame'] = 0
    
    #Enemy Movement and Sound
    for time in state['synthsewers_up']:
        if state['time_elapsed'] == time:
            assets['monsterspawn'].play()
            state['stop_time'] = 0
            state['life_state_up'] = 'alive'

    if state['life_state_up'] == 'dead':
        if state['dead_time'] == 0:
            state['enemy_up_y'] = -63
            state['dead_time'] += 1
        elif state['dead_time'] <= 30:
            enemy_dead_up = window.blit(assets['enemy_dead'], (601, 150))
            state['dead_time'] += 1
        else:
            state['dead_time'] = 0
            state['life_state_up'] = 'not_spawned'

    if state['life_state_up'] == 'alive':
        state['dead_time'] = 0
        state['enemy_up_y'] = enemy_move('up', state['enemy_up_x'], state['enemy_up_y'], state['stop_time'])[0][1] #update y
        state['stop_time'] = enemy_move('up', state['enemy_up_x'], state['enemy_up_y'], state['stop_time'])[1] #update stop time

    if state['enemy_up_y'] >= 280:
        state['life_state_up'] = 'damage'
        state['enemy_up_y'] = -63
        assets['hitsound'].play()
        state['synthsewers_up_inputs'].remove(state['synthsewers_up_inputs'][0])
        
    #print(state['synthsewers_up'].remove(state['synthsewers_up_inputs'][0]))

    if state['life_state_up'] == 'damage':
        #assets['hitsound'].play()
        state['life_state_up'] = 'not_spawned'

    #Render Protag and Enemies
    if state['time_elapsed'] <= 14*60 or state['time_elapsed'] >= 16*60:

        if state['life_state_up'] != 'damage':
            enemy_up = window.blit(assets['enemy_blue'][state['enemy_frame']], (state['enemy_up_x'], state['enemy_up_y']))
        
        #enemy_dead_down = window.blit(assets['enemy_dead'], (601, 490))
        
        #enemy_dead_left = window.blit(assets['enemy_dead'], (400, 321))
        
        #enemy_dead_left = window.blit(assets['enemy_dead'], (800, 321))
        
        #protag = window.blit(assets['protag'][state['protagframe']], (577, 181))

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
                assets['swoosh'].play()
                state['slash_direction'] = 'right'
                state['sword_time'] = 0

            #Left Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                assets['swoosh'].play()
                state['slash_direction'] = 'left'
                state['sword_time'] = 0

            #Up Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                assets['swoosh'].play()
                state['slash_direction'] = 'up'
                state['sword_time'] = 0
                state['hits_up'].append(state['time_elapsed'])

                if check_timing(state['synthsewers_up_inputs'], state['hits_up']):
                    assets['monsterdeath'].play()
                    state['life_state_up'] = 'dead'
                    

                state['hits_up'] = []

            

            #Down Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                assets['swoosh'].play()
                state['slash_direction'] = 'down'
                state['sword_time'] = 0

            #Eventos vão aqui!
    if state['slash_direction'] != 'none':
        state['sword_time'] += 1
    if state['sword_time'] >= 18:
        state['slash_direction'] = 'none'
        state['sword_time'] = 0

    for timing in state['synthsewers_up']:
        if state['time_elapsed'] >= timing + 18:
            state['synthsewers_up'].remove(timing)

    #print(state['synthsewers_up'])

    #print(state['slash_direction'])
    #print(state['sword_time'])
    
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
