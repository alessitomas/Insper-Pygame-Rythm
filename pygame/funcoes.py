import pygame

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

        'monsterspawn': pygame.mixer.Sound('music/monsterspawn.ogg'),
        'monsterdeath': pygame.mixer.Sound('music/monsterdeath.ogg'),

        'swordup': pygame.image.load('sprites/swordup.png'),
        'sworddown': pygame.image.load('sprites/sworddown.png'),
        'swordleft': pygame.image.load('sprites/swordleft.png'),
        'swordright': pygame.image.load('sprites/swordright.png'),
        }
    return loadedassets


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
        if y >= 680:
            y -= 10
        else:
            stop_time += 1


    #Second Movement

    #Up
    if stop_time >= 26:
        if origin == 'up':
            if y <= 280:
                y += 5

    
    new_coords = ((x, y), stop_time)
    #print(new_coords)
    return new_coords