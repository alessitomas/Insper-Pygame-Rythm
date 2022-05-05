import pygame
import time

def load_assets():
    
    loadedassets = {
        
        'protag': [
            pygame.image.load('sprites/protag1.png'),
            pygame.image.load('sprites/protag2.png'),
            pygame.image.load('sprites/protag3.png'),
            pygame.image.load('sprites/protag4.png'),
            pygame.image.load('sprites/protag5.png'),
            pygame.image.load('sprites/protag6.png')
            ],

        'enemy_blue': [
            pygame.image.load('sprites/enemy_blue1.png'),
            pygame.image.load('sprites/enemy_blue2.png'),
            pygame.image.load('sprites/enemy_blue3.png'),
            pygame.image.load('sprites/enemy_blue4.png'),
            pygame.image.load('sprites/enemy_blue5.png'),
            pygame.image.load('sprites/enemy_blue6.png'),
            ],

        'enemy_dead': pygame.image.load('sprites/enemy_dead.png'),
        
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
        
        'swoosh': pygame.mixer.Sound('music/swoosh.ogg'),
        'ouch': pygame.mixer.Sound('music/ouch.ogg'),

        'monsterspawn': pygame.mixer.Sound('music/monsterspawn.ogg'),
        'monsterdeath': pygame.mixer.Sound('music/monsterdeath.ogg'),

        'swordup': pygame.image.load('sprites/swordup.png'),
        'sworddown': pygame.image.load('sprites/sworddown.png'),
        'swordleft': pygame.image.load('sprites/swordleft.png'),
        'swordright': pygame.image.load('sprites/swordright.png'),
        
        'jooj': pygame.image.load('sprites/jooj.gif'),

        }

    return loadedassets

def load_states():
    
    loaded_states = {
            'song_playing': False,

            'protagframe': 0,
            'protagbounce': False,
            
            'enemy_frame': 0,
            
            'enemy_up_x': 607,
            'enemy_up_y': -63,
            'dead_time_up': 0,
            'stop_time_up': 0,
            'life_state_up': 'not_spawned',

            'enemy_down_x': 607,
            'enemy_down_y': 720,
            'dead_time_down': 0,
            'stop_time_down': 0,
            'life_state_down': 'not_spawned',

            'bgframe': 0,
            
            'time_elapsed': 0,
            'dt': 1,
            'prev_time': time.time(),

            'synthsewers_up': [6, 10, 18, 22, 26, 26.5, 30, 30.5, 32, 34, 34.5, 36, 38, 38.5, 40, 42, 42.5, 44, 46, 46.5, 48.5, 50.5, 51, 52],
            'synthsewers_up_inputs': [6, 10, 18, 22, 26, 26.5, 30, 30.5, 32, 34, 34.5, 36, 38, 38.5, 40, 42, 42.5, 44, 46, 46.5, 48.5, 50.5, 51, 52],
            'synthsewers_down': [2, 4, 8],
            'synthsewers_down_inputs': [2, 4, 8],

            'slash_direction': 'none',
            'sword_time': 0,

            'hits_up': [],
            'hits_down': [],

            }

    return loaded_states

def enemy_move(origin, x, y, stop_time):

    #Initial Movement

    #Up
    if origin == 'up':
        if y <= 40:
            y += 10
        else:
            stop_time += 1

    #Down
    if origin == 'down':
        if y >= 577:
            y -= 10
        else:
            stop_time += 1


    #Second Movement

    #Up
    if origin == 'up':
        if stop_time >= 26:
            if y <= 280:
                y += 5

    #Down
    if origin == 'down':
        if stop_time >= 26:
            if y >= 440:
                y -= 5

    
    new_coords = ((x, y), stop_time)

    return new_coords

def check_timing(synthsewers_timings, player_timings):

    for timing in synthsewers_timings:
        if player_timings[0] >= timing - 18 and player_timings[0] <= timing + 18:
            synthsewers_timings.remove(synthsewers_timings[0])
            return True
        else:
            return False







