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
    state['synthsewers_down'] = [timing * fps for timing in state['synthsewers_down']]
    state['synthsewers_down_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_down_inputs']]
    state['synthsewers_right'] = [timing * fps for timing in state['synthsewers_right']]
    state['synthsewers_right_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_right_inputs']]
    state['synthsewers_left'] = [timing * fps for timing in state['synthsewers_left']]
    state['synthsewers_left_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_left_inputs']]

    return window, assets, state

def inicializa_subjogo():
    
    pygame.init()
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    #window = pygame.display.set_mode((1280, 720), vsync=1)
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Tenor Blade')
    icon = pygame.image.load('sprites/tabicon.png')
    pygame.display.set_icon(icon)

    assets = load_assets()

    state = load_states()

    #Timings from seconds to FPS
    state['synthsewers_up'] = [timing * fps for timing in state['synthsewers_up']]
    state['synthsewers_up_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_up_inputs']]
    state['synthsewers_down'] = [timing * fps for timing in state['synthsewers_down']]
    state['synthsewers_down_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_down_inputs']]
    state['synthsewers_right'] = [timing * fps for timing in state['synthsewers_right']]
    state['synthsewers_right_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_right_inputs']]
    state['synthsewers_left'] = [timing * fps for timing in state['synthsewers_left']]
    state['synthsewers_left_inputs'] = [(timing * fps) + 60 for timing in state['synthsewers_left_inputs']]

    return  assets, state


#Finalização do Game
def finaliza():
    pygame.quit()



#Função desenhar na tela
def desenha(window: pygame.Surface, assets, state):


    #Time Elapsed
    state['time_elapsed'] += 1 * (1/state['dt'])


    #BG Blit
    if state['time_elapsed'] <= 14*60 or state['time_elapsed'] >= 16*60:
        bg = window.blit(assets['sewerbg'][state['bgframe']], (0,0))


    #Sword Blit
    if state['slash_direction'] == 'right':
        right = window.blit(assets['swordright'], (741,333))
    elif state['slash_direction'] == 'left':
        left = window.blit(assets['swordleft'], (417,333))
    elif state['slash_direction'] == 'up':
        up = window.blit(assets['swordup'], (612,150))
    elif state['slash_direction'] == 'down':
        down = window.blit(assets['sworddown'], (612,447))

    
    #Enemy Movement and Sound

    #Spawn Enemies
    #Up
    for time in state['synthsewers_up']:
        if state['time_elapsed'] == time:
            assets['monsterspawn'].play()
            state['stop_time_up'] = 0
            state['life_state_up'] = 'alive'
    #Down
    for time in state['synthsewers_down']:
        if state['time_elapsed'] == time:
            assets['monsterspawn'].play()
            state['stop_time_down'] = 0
            state['life_state_down'] = 'alive'
    #Right
    for time in state['synthsewers_right']:
        if state['time_elapsed'] == time:
            assets['monsterspawn'].play()
            state['stop_time_right'] = 0
            state['life_state_right'] = 'alive'
    #Left
    for time in state['synthsewers_left']:
        if state['time_elapsed'] == time:
            assets['monsterspawn'].play()
            state['stop_time_left'] = 0
            state['life_state_left'] = 'alive'

    #Death Animation
    #Up
    if state['life_state_up'] == 'dead':
        if state['dead_time_up'] == 0:
            state['enemy_up_y'] = -63
            state['dead_time_up'] += 1
        elif state['dead_time_up'] <= 30:
            enemy_dead_up = window.blit(assets['enemy_dead'], (601, 150))
            state['dead_time_up'] += 1
        else:
            state['dead_time_up'] = 0
            state['life_state_up'] = 'not_spawned'
    #Down
    if state['life_state_down'] == 'dead':
        if state['dead_time_down'] == 0:
            state['enemy_down_y'] = 720
            state['dead_time_down'] += 1
        elif state['dead_time_down'] <= 30:
            enemy_dead_down = window.blit(assets['enemy_dead'], (601, 490))
            state['dead_time_down'] += 1
        else:
            state['dead_time_down'] = 0
            state['life_state_down'] = 'not_spawned'
    #Right
    if state['life_state_right'] == 'dead':
        if state['dead_time_right'] == 0:
            state['enemy_right_x'] = 1280
            state['dead_time_right'] += 1
        elif state['dead_time_right'] <= 30:
            enemy_dead_right = window.blit(assets['enemy_dead'], (800, 321))
            state['dead_time_right'] += 1
        else:
            state['dead_time_right'] = 0
            state['life_state_right'] = 'not_spawned'
    #Left
    if state['life_state_left'] == 'dead':
        if state['dead_time_left'] == 0:
            state['enemy_left_x'] = -66
            state['dead_time_left'] += 1
        elif state['dead_time_left'] <= 30:
            enemy_dead_left = window.blit(assets['enemy_dead'], (400, 321))
            state['dead_time_left'] += 1
        else:
            state['dead_time_left'] = 0
            state['life_state_left'] = 'not_spawned'

    #Move Animation
    #Up
    if state['life_state_up'] == 'alive':
        state['dead_time_up'] = 0
        state['enemy_up_y'] = enemy_move('up', state['enemy_up_x'], state['enemy_up_y'], state['stop_time_up'])[0][1] #update y
        state['stop_time_up'] = enemy_move('up', state['enemy_up_x'], state['enemy_up_y'], state['stop_time_up'])[1] #update stop time
    #Down
    if state['life_state_down'] == 'alive':
        state['dead_time_down'] = 0
        state['enemy_down_y'] = enemy_move('down', state['enemy_down_x'], state['enemy_down_y'], state['stop_time_down'])[0][1] #update y
        state['stop_time_down'] = enemy_move('down', state['enemy_down_x'], state['enemy_down_y'], state['stop_time_down'])[1] #update stop time
    #Right
    if state['life_state_right'] == 'alive':
        state['dead_time_right'] = 0
        state['enemy_right_x'] = enemy_move('right', state['enemy_right_x'], state['enemy_right_y'], state['stop_time_right'])[0][0] #update x
        state['stop_time_right'] = enemy_move('right', state['enemy_right_x'], state['enemy_right_y'], state['stop_time_right'])[1] #update stop time
    #Left
    if state['life_state_left'] == 'alive':
        state['dead_time_left'] = 0
        state['enemy_left_x'] = enemy_move('left', state['enemy_left_x'], state['enemy_left_y'], state['stop_time_left'])[0][0] #update x
        state['stop_time_left'] = enemy_move('left', state['enemy_left_x'], state['enemy_left_y'], state['stop_time_left'])[1] #update stop time

    #Damage
    #Up
    if state['enemy_up_y'] >= 280:
        state['life_state_up'] = 'damage'
        state['enemy_up_y'] = -63
        assets['ouch'].play()
        state['synthsewers_up_inputs'].remove(state['synthsewers_up_inputs'][0])    
    if state['life_state_up'] == 'damage':
        state['health'] -= 1
        state['life_state_up'] = 'not_spawned'
    #Down
    if state['enemy_down_y'] <= 440:
        state['life_state_down'] = 'damage'
        state['enemy_down_y'] = 720
        assets['ouch'].play()
        state['synthsewers_down_inputs'].remove(state['synthsewers_down_inputs'][0])    
    if state['life_state_down'] == 'damage':
        state['health'] -= 1
        state['life_state_down'] = 'not_spawned'
    #Right
    if state['enemy_right_x'] <= 687:
        state['life_state_right'] = 'damage'
        state['enemy_right_x'] = 1280
        assets['ouch'].play()
        state['synthsewers_right_inputs'].remove(state['synthsewers_right_inputs'][0])    
    if state['life_state_right'] == 'damage':
        state['health'] -= 1
        state['life_state_right'] = 'not_spawned'
    #Left
    if state['enemy_left_x'] >= 527:
        state['life_state_left'] = 'damage'
        state['enemy_left_x'] = -66
        assets['ouch'].play()
        state['synthsewers_left_inputs'].remove(state['synthsewers_left_inputs'][0])    
    if state['life_state_left'] == 'damage':
        state['health'] -= 1
        state['life_state_left'] = 'not_spawned'


    #Render Protag and Enemies
    if state['time_elapsed'] <= 14*60 or state['time_elapsed'] >= 16*60:

        if state['life_state_up'] != 'damage':
            enemy_up = window.blit(assets['enemy_blue'][state['enemy_frame']], (state['enemy_up_x'], state['enemy_up_y']))
        if state['life_state_down'] != 'damage':
            enemy_down = window.blit(assets['enemy_blue'][state['enemy_frame']], (state['enemy_down_x'], state['enemy_down_y']))
        if state['life_state_right'] != 'damage':
            enemy_right = window.blit(assets['enemy_blue'][state['enemy_frame']], (state['enemy_right_x'], state['enemy_right_y']))
        if state['life_state_left'] != 'damage':
            enemy_left = window.blit(assets['enemy_blue'][state['enemy_frame']], (state['enemy_left_x'], state['enemy_left_y']))
        
        protag = window.blit(assets['protag'][state['protagframe']], (577, 181))


    #Metronome
    #if state['time_elapsed'] % 30 == 0:
    #    assets['metronome'].play()


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


    #Hearts
    if state['health'] == 1:
        heart_1 = window.blit(assets['heart'], (30, 630))
        heart_2 = window.blit(assets['heart_empty'], (120, 630))
        heart_3 = window.blit(assets['heart_empty'], (210, 630))
    elif state['health'] == 2:
        heart_1 = window.blit(assets['heart'], (30, 630))
        heart_2 = window.blit(assets['heart'], (120, 630))
        heart_3 = window.blit(assets['heart_empty'], (210, 630))
    elif state['health'] == 3:
        heart_1 = window.blit(assets['heart'], (30, 630))
        heart_2 = window.blit(assets['heart'], (120, 630))
        heart_3 = window.blit(assets['heart'], (210, 630))


    pygame.display.update()



#Atualizar estado
def atualiza_estado(state, assets):


    #Play song
    if not state['song_playing']:
        pygame.mixer.music.play()
        state['song_playing'] = True


    #BG Frames
    if state['time_elapsed'] % 8 == 0:
        state['bgframe'] += 1
        if state['bgframe'] > 5:
            state['bgframe'] = 0


    #Enemy Frames
    if state['time_elapsed'] % 5 == 0:
            state['enemy_frame'] += 1
    if state['enemy_frame'] > 5:
        state['enemy_frame'] = 0


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


    #Inputs
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
                state['hits_right'].append(state['time_elapsed'])

                if check_timing(state['synthsewers_right_inputs'], state['hits_right']):
                    assets['monsterdeath'].play()
                    state['life_state_right'] = 'dead'
                    
                state['hits_right'] = []


            #Left Sword
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                assets['swoosh'].play()
                state['slash_direction'] = 'left'
                state['sword_time'] = 0
                state['hits_left'].append(state['time_elapsed'])

                if check_timing(state['synthsewers_left_inputs'], state['hits_left']):
                    assets['monsterdeath'].play()
                    state['life_state_left'] = 'dead'
                    
                state['hits_left'] = []


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
                state['hits_down'].append(state['time_elapsed'])

                if check_timing(state['synthsewers_down_inputs'], state['hits_down']):
                    assets['monsterdeath'].play()
                    state['life_state_down'] = 'dead'
                    
                state['hits_down'] = []

    #Sword Out Timer
    if state['slash_direction'] != 'none':
        state['sword_time'] += 1
    if state['sword_time'] >= 18:
        state['slash_direction'] = 'none'
        state['sword_time'] = 0


    #Remove Past Timings
    #Up
    for timing in state['synthsewers_up']:
        if state['time_elapsed'] >= timing + 18:
            state['synthsewers_up'].remove(timing)
    #Down
    for timing in state['synthsewers_down']:
        if state['time_elapsed'] >= timing + 18:
            state['synthsewers_down'].remove(timing)
    #Right
    for timing in state['synthsewers_right']:
        if state['time_elapsed'] >= timing + 18:
            state['synthsewers_right'].remove(timing)
    #Left
    for timing in state['synthsewers_left']:
        if state['time_elapsed'] >= timing + 18:
            state['synthsewers_left'].remove(timing)
    

    
    return True



#Gameloop
def gameloop_jogo(window, assets, state):
    while atualiza_estado(state, assets):
        desenha(window, assets, state)
        clock.tick(fps)
        now = time.time()
        dt = now - state['prev_time']
        state['prev_time'] = now


def game_main(window):
    assets, state = inicializa_subjogo()
    return gameloop_jogo(window, assets, state)
    #finaliza()

#name
if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop_jogo(window, assets, state)
    finaliza()
