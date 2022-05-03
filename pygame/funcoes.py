import pygame

def test_time_very_close():
    elapsed_time = 0.5
    game = pygame.Game()
    game.update(elapsed_time)
    assert game.happening == [0.5]

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
        
        'up_test': pygame.mixer.Sound('music/up_test.ogg'),
        'down_test': pygame.mixer.Sound('music/down_test.ogg'),
        'left_test': pygame.mixer.Sound('music/left_test.ogg'),
        'right_test': pygame.mixer.Sound('music/right_test.ogg'),

        'swordup': pygame.image.load('sprites/swordup.png'),
        'sworddown': pygame.image.load('sprites/sworddown.png'),
        'swordleft': pygame.image.load('sprites/swordleft.png'),
        'swordright': pygame.image.load('sprites/swordright.png'),
        }
    return loadedassets


