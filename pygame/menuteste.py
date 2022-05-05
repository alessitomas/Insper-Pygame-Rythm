from credits import gameloop_credits
from extra import *
import pygame
import funcoes
from how import gameloop_how
from options import gameloop_options
import programa
AZUL = (0,0,255)
ROSA = (255, 0, 127)
CIANO = (0, 225, 225)
# fonte Stackoverflow
pygame.font.init() 
papyrus_font = pygame.font.SysFont('papyrus', 50)
arial_font = pygame.font.SysFont('franklingothicmedium', 75)

def inicializa():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.init()
    w = pygame.display.set_mode((1280, 720), vsync=True, flags=pygame.SCALED)
    pygame.display.set_caption('Tenor Blade')
    icon = pygame.image.load('img/tabicon.png')
    pygame.display.set_icon(icon)
    #pygame.key.set_repeat(50)

    assets = {
        'background': pygame.image.load("img/menu.png"),

        'logo': pygame.image.load("img/logo.png"),

        'start': pygame.image.load("img/start.png"),
        'start_select': pygame.image.load("img/start_select.png"),
        'start_pt': pygame.image.load("img/start_pt.png"),
        'start_select_pt': pygame.image.load("img/start_select_pt.png"),

        'extras': pygame.image.load("img/extras.png"),
        'extras_select': pygame.image.load("img/extras_select.png"),

        'how_to_play': pygame.image.load("img/how_to_play.png"),
        'how_to_play_select': pygame.image.load("img/how_to_play_select.png"),
        'how_to_play_pt': pygame.image.load("img/how_to_play_pt.png"),
        'how_to_play_select_pt': pygame.image.load("img/how_to_play_select_pt.png"),
        
        'options': pygame.image.load("img/options.png"),
        'options_select': pygame.image.load("img/options_select.png"),
        'options_pt': pygame.image.load("img/options_pt.png"),
        'options_select_pt': pygame.image.load("img/options_select_pt.png"),

        'credits': pygame.image.load("img/credits.png"),
        'credits_select': pygame.image.load("img/credits_select.png"),
        'credits_pt': pygame.image.load("img/credits_pt.png"),
        'credits_select_pt': pygame.image.load("img/credits_select_pt.png"),

    }

    state = {
        "rect_start_pos":[375, 150] , 
        "rect_start_dimen":[500, 150], 
        'retangulos_dimen':[350, 75],
        'rect_extras_pos':[235, 350], 
        'rect_how_pos':[675, 350], 
        'rect_opt_pos':[225, 500], 
        'rect_cred_pos':[675, 500], 
        "estado": "inicial",
        "tela":"inicial",
        "menu_direction": 'left',

        'lang': 'pt'

        }

    return w, assets, state


def finaliza():
    pygame.quit()


def desenha(window: pygame.Surface, assets, state):
    #background
    #window.blit(assets['background'],(0,0))
    
    ref_test = window.blit(assets['background'], (0, 0))

    window.blit(assets['logo'], (399, 42))
    
    if state['lang'] == 'eng':
        if state['estado'] == 'start':
            window.blit(assets['start_select'], (387, 213))
        else:
            window.blit(assets['start'], (387, 213))

        if state['estado'] == 'extras':
            window.blit(assets['extras_select'], (222, 405))
        else:
            window.blit(assets['extras'], (222, 405))

        if state['estado'] == 'how':
            window.blit(assets['how_to_play_select'], (711, 405))
        else:
            window.blit(assets['how_to_play'], (711, 405))

        if state['estado'] == 'options':
            window.blit(assets['options_select'], (222, 519))
        else:
            window.blit(assets['options'], (222, 519))

        if state['estado'] == 'creditos':
            window.blit(assets['credits_select'], (711, 519))
        else:
            window.blit(assets['credits'], (711, 519))

    elif state['lang'] == 'pt':
        if state['estado'] == 'start':
            window.blit(assets['start_select_pt'], (387, 213))
        else:
            window.blit(assets['start_pt'], (387, 213))

        if state['estado'] == 'extras':
            window.blit(assets['extras_select'], (222, 405))
        else:
            window.blit(assets['extras'], (222, 405))

        if state['estado'] == 'how':
            window.blit(assets['how_to_play_select_pt'], (711, 405))
        else:
            window.blit(assets['how_to_play_pt'], (711, 405))

        if state['estado'] == 'options':
            window.blit(assets['options_select_pt'], (222, 519))
        else:
            window.blit(assets['options_pt'], (222, 519))

        if state['estado'] == 'creditos':
            window.blit(assets['credits_select_pt'], (711, 519))
        else:
            window.blit(assets['credits_pt'], (711, 519))
    
    pygame.display.update()


def atualiza_estado(state):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            
            if ev.key == pygame.K_UP or ev.key == pygame.K_w:
                if state["estado"] == "inicial":
                    state["estado"] = "start"

                elif state["estado"] == "start":
                    if state['menu_direction'] == 'left':
                        state["estado"] = "options"
                    elif state['menu_direction'] == 'right':
                        state["estado"] = "creditos"
                
                elif state["estado"] == "extras":
                    state["estado"] = "start"

                elif state["estado"] == "options":
                    state["estado"] = "extras"

                elif state["estado"] == "how":
                    state["estado"] = "start"
                
                elif state["estado"] == "how":
                    state["estado"] = "start"

                elif state["estado"] == "creditos":
                    state["estado"] = "how"
               
                 
            if ev.key == pygame.K_RIGHT or ev.key == pygame.K_d:
                
                if state["estado"] == "inicial":
                    state["estado"] = "start"

                elif state["estado"] == "how":
                    state["estado"] = "extras"
                
                elif state["estado"] == "creditos":
                    state["estado"] = "options"
                
                
                elif state["estado"] == "start":
                    state["estado"] = "how"
                
                elif state["estado"] == "extras":
                    state["estado"] = "how"

                elif state["estado"] == "options":
                    state["estado"] = "creditos"

            if ev.key == pygame.K_LEFT or ev.key == pygame.K_a:
                
                if state["estado"] == "inicial":
                    state["estado"] = "start"

                elif state["estado"] == "start":
                    state["estado"] = "extras"
                
                elif state["estado"] == "extras":
                    state["estado"] = "how"
                
                elif state["estado"] == "extras":
                    state["estado"] = "how"
                
                elif state["estado"] == "options":
                    state["estado"] = "creditos"
                
                elif state["estado"] == "how":
                    state["estado"] = "extras"
                
                elif state["estado"] == "creditos":
                    state["estado"] = "options"

            if ev.key == pygame.K_DOWN or ev.key == pygame.K_s:
                
                if state["estado"] == "inicial":
                    state["estado"] = "start"
                
                elif state["estado"] == "start":
                    if state['menu_direction'] == 'left':
                        state["estado"] = "extras"
                    elif state['menu_direction'] == 'right':
                        state["estado"] = "how"

                elif state["estado"] == "options":
                    state["estado"] = "start"

                elif state["estado"] == "creditos":
                    state["estado"] = "start"

                elif state["estado"] == "extras":
                    state["estado"] = "options"

                elif state["estado"] == "how":
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
                    if state["estado"]  == "start":
                        state["tela"] = "start"
        
        if state['estado'] == 'extras' or state['estado'] == 'options':
            state['menu_direction'] = 'left'
        if state['estado'] == 'how' or state['estado'] == 'creditos':
            state['menu_direction'] = 'right'          
    
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
            jogando = programa.game_main(window)
    
        elif state["tela"] == "extras":
            jogando = gameloop_extra(window,assets,state)
       
        elif state["tela"] == "how":
            jogando = gameloop_how(window,assets,state)
        
        elif state["tela"] == "options":
            jogando = gameloop_options(window,assets,state)
        
        elif state["tela"] == "creditos":
            jogando = gameloop_credits(window,assets,state)
            
    finaliza()
