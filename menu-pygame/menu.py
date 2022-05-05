from credits import gameloop_credits
from extra import *
import pygame

from how import gameloop_how
from options import gameloop_options
AZUL = (0,0,255)
ROSA = (255, 0, 127)
CIANO = (0, 225, 225)
# fonte Stackoverflow
pygame.font.init() 
papyrus_font = pygame.font.SysFont('papyrus', 50)
arial_font = pygame.font.SysFont('franklingothicmedium', 75)
background = pygame.image.load("img/menu.png")
def inicializa():
    pygame.init()
    w = pygame.display.set_mode((1280, 720), vsync=True, flags=pygame.SCALED)
    pygame.key.set_repeat(50)

    assets = {
    }

    state = {
         "cor": [ROSA,ROSA,ROSA,ROSA,ROSA], 
         "rect_start_pos":[375, 150] , 
         "rect_start_dimen":[500, 150], 
         'retangulos_dimen':[350, 75],
         'rect_extras_pos':[235, 350], 
         'rect_how_pos':[675, 350], 
         'rect_opt_pos':[225, 500], 
         'rect_cred_pos':[675, 500], 
         "estado": "inicial",
         "tela":"inicial"
         }

    return w, assets, state


def finaliza():
    pygame.quit()


def desenha(window: pygame.Surface, assets, state):
    window.fill((0, 225, 225))
    #background
    window.blit(background,(0,0))
    
    
    text_surface = arial_font.render("TENOR BLADE", False, (0, 0, 0))
    window.blit(text_surface, (435, 30))
    
    pygame.draw.rect(window, state['cor'][0], pygame.Rect(state['rect_start_pos'], state['rect_start_dimen']))
    text_surface = papyrus_font.render("START", False, (0, 0, 0))
    window.blit(text_surface, (550, 200))
    
    pygame.draw.rect(window, state['cor'][1], pygame.Rect(state['rect_extras_pos'], state['retangulos_dimen']))
    text_surface = papyrus_font.render("EXTRAS", False, (0, 0, 0))
    window.blit(text_surface, (310, 365))
    
    pygame.draw.rect(window, state['cor'][2], pygame.Rect(state['rect_how_pos'], state['retangulos_dimen']))
    text_surface = papyrus_font.render("HOW TO PLAY", False, (0, 0, 0))
    window.blit(text_surface, (693, 365))

    pygame.draw.rect(window, state['cor'][3], pygame.Rect(state['rect_opt_pos'], state['retangulos_dimen']))
    text_surface = papyrus_font.render("OPTIONS", False, (0, 0, 0))
    window.blit(text_surface, (285, 515))
    
    pygame.draw.rect(window, state['cor'][4], pygame.Rect(state['rect_cred_pos'], state['retangulos_dimen']))
    text_surface = papyrus_font.render("CREDITS", False, (0, 0, 0))
    window.blit(text_surface, (735, 510))
    
    pygame.display.update()


def atualiza_estado(state):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_UP:
                if state["estado"] == "inicial":
                    state["cor"][0] = AZUL
                    state["estado"] = "start"

                elif state["estado"] == "start":
                    state["cor"] = [ROSA] * 5
                    state["cor"][3] = AZUL
                    state["estado"] = "options"
                
                elif state["estado"] == "extras":
                    state["cor"] = [ROSA] * 5
                    state["cor"][0] = AZUL
                    state["estado"] = "start"

                elif state["estado"] == "options":
                    state["cor"] = [ROSA] * 5
                    state["cor"][1] = AZUL
                    state["estado"] = "extras"

                elif state["estado"] == "how":
                    state["cor"] = [ROSA] * 5
                    state["cor"][0] = AZUL
                    state["estado"] = "start"
                
                elif state["estado"] == "how":
                    state["cor"] = [ROSA] * 5
                    state["cor"][0] = AZUL
                    state["estado"] = "start"

                elif state["estado"] == "creditos":
                    state["cor"] = [ROSA] * 5
                    state["cor"][2] = AZUL
                    state["estado"] = "how"
               
                 
            if ev.key == pygame.K_RIGHT:
                
                if state["estado"] == "inicial":
                    state["cor"][2] = AZUL
                    state["estado"] = "how"

                elif state["estado"] == "how":
                    state["cor"] = [ROSA] * 5
                    state["cor"][1] = AZUL
                    state["estado"] = "extras"
                
                elif state["estado"] == "creditos":
                    state["cor"] = [ROSA] * 5
                    state["cor"][3] = AZUL
                    state["estado"] = "options"
                
                
                elif state["estado"] == "start":
                    state["cor"] = [ROSA] * 5
                    state["cor"][2] = AZUL
                    state["estado"] = "how"
                
                elif state["estado"] == "extras":
                    state["cor"] = [ROSA] * 5
                    state["cor"][2] = AZUL
                    state["estado"] = "how"

                elif state["estado"] == "options":
                    state["cor"] = [ROSA] * 5
                    state["cor"][4] = AZUL
                    state["estado"] = "creditos"

            if ev.key == pygame.K_LEFT:
                
                if state["estado"] == "inicial":
                    state["cor"][1] = AZUL
                    state["estado"] = "extras"
                
                elif state["estado"] == "extras":
                    state["cor"] = [ROSA] * 5
                    state["cor"][2] = AZUL
                    state["estado"] = "how"
                
                elif state["estado"] == "extras":
                    state["cor"] = [ROSA] * 5
                    state["cor"][2] = AZUL
                    state["estado"] = "how"
                
                elif state["estado"] == "options":
                    state["cor"] = [ROSA] * 5
                    state["cor"][4] = AZUL
                    state["estado"] = "creditos"
                
                elif state["estado"] == "how":
                    state["cor"] = [ROSA] * 5
                    state["cor"][1] = AZUL
                    state["estado"] = "extras"
                
                elif state["estado"] == "creditos":
                    state["cor"] = [ROSA] * 5
                    state["cor"][3] = AZUL
                    state["estado"] = "options"

            if ev.key == pygame.K_DOWN:
                
                if state["estado"] == "inicial":
                    state["cor"][3] = AZUL
                    state["estado"] = "options"
                
                elif state["estado"] == "start":
                    state["cor"] = [ROSA] * 5
                    state["cor"][1] = AZUL
                    state["estado"] = "extras"
                
                elif state["estado"] == "options":
                    state["cor"] = [ROSA] * 5
                    state["cor"][0] = AZUL
                    state["estado"] = "start"

                elif state["estado"] == "creditos":
                    state["cor"] = [ROSA] * 5
                    state["cor"][0] = AZUL
                    state["estado"] = "start"

                elif state["estado"] == "extras":
                    state["cor"] = [ROSA] * 5
                    state["cor"][3] = AZUL
                    state["estado"] = "options"

                elif state["estado"] == "how":
                    state["cor"] = [ROSA] * 5
                    state["cor"][4] = AZUL
                    state["estado"] = "creditos"

            if ev.key == pygame.K_RETURN:
                if not state["estado"]  == "inicial":
                    if state["estado"]  == "extras":
                        state["tela"] = "extras"
                    if state["estado"]  == "how":
                        state["tela"] = "how"
                    if state["estado"]  == "options":
                        state["tela"] = "options"
                    if state["estado"]  == "creditos":
                        state["tela"] = "creditos"
                    
                         
    
    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        
        if state["tela"] != "inicial":
            return True
        desenha(window, assets, state)
    return False
            


if __name__ == '__main__':
    jogando = True
    window, assets, state = inicializa()
    while jogando:
        if state["tela"] == "inicial":
            jogando = gameloop(window, assets, state)
        
        elif state["tela"] == "start":
            pass
    
        elif state["tela"] == "extras":
            jogando = gameloop_extra(window,assets,state)
       
        elif state["tela"] == "how":
            jogando = gameloop_how(window,assets,state)
        
        elif state["tela"] == "options":
            jogando = gameloop_options(window,assets,state)
        
        elif state["tela"] == "creditos":
            jogando = gameloop_credits(window,assets,state)
            
    finaliza()
