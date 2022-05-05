import pygame
from pygame import mixer
mixer.init()
AZUL = (0,0,255)
CIANO = (0, 225, 225)
# fonte Stackoverflow
state_extra = {
    "rect_pos_audio1":[800, 150] , 
    "rect_dimen_audio1":[350, 75], 
    "play1_pos" : [740, 220],
    "play1_dimen" : [50, 10],
    "estado": "inicial",
    "cor" : [AZUL] * 3
}
image_jooj = pygame.image.load('img/jooj.gif')
image_play1 = pygame.image.load('img/play-black.png')
image_play2 = pygame.image.load('img/play-black.png')
image_sound = pygame.image.load('img/wave-soundcopy.tiff')
#mixer.music.load("song.mp3")
def desenha_extra(window: pygame.Surface, assets, state):
    window.fill(CIANO)
   
    # pygame.draw.rect(window,(255,255,255), pygame.Rect(state_extra['rect_pos_audio1'], state_extra['rect_dimen_audio1']))
   
    # audio 1
    window.blit(image_sound, (850, 160))

    window.blit(image_play1, (740, 160))
    pygame.draw.rect(window,(state_extra["cor"][0]), pygame.Rect(state_extra['play1_pos'], state_extra['play1_dimen']))
    
    window.blit(image_jooj, (225, 150))
    pygame.display.update()
    
    window.blit(image_play2, (900, 160))

   


    

    


    pygame.display.update()
    

def atualiza_estado_extra(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
            if ev.key == pygame.K_DOWN:
                if state_extra["estado"] == "inicial":
                    state_extra["cor"][0] = (0,0,0)
                    

            
                
                
    
    
    return True


def gameloop_extra(window, assets, state):
    while atualiza_estado_extra(state):
            if state["tela"] != "extras":
                return True
            desenha_extra(window, assets, state)
         
            
    return False


