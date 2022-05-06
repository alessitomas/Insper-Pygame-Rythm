import pygame
from pygame import mixer
mixer.init()

escape = pygame.image.load('img/escape.png')
escape_pt = pygame.image.load('img/escape_pt.png')
background = pygame.image.load('img/menu.png')

synthsewers_box = pygame.image.load('img/synthsewers_box.png')
menu_box = pygame.image.load('img/menu_box.png')
options_box = pygame.image.load('img/options_box.png')

state_extra = {
    "estado": "inicial",
}
image_jooj = pygame.image.load('img/jooj.gif')


def desenha_extra(window: pygame.Surface, assets, state):

    window.blit(background, (0, 0))
    if state['lang'] == 'eng':
        window.blit(escape, (0, 0))
    elif state['lang'] == 'pt':
        window.blit(escape_pt, (0, 0))
   
    if state['soundtest_select'] == 'synthsewers':
        window.blit(synthsewers_box, (579, 285))
    elif state['soundtest_select'] == 'menu':
        window.blit(menu_box, (579, 285))
    elif state['soundtest_select'] == 'options':
        window.blit(options_box, (579, 285))


    window.blit(image_jooj, (200, 237))
    pygame.display.update()


    pygame.display.update()
    

def atualiza_estado_extra(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
            elif ev.key == pygame.K_RIGHT or ev.key == pygame.K_d:
                if state['soundtest_select'] == 'synthsewers':
                    state['soundtest_select'] = 'menu'
                elif state['soundtest_select'] == 'menu':
                    state['soundtest_select'] = 'options'
                elif state['soundtest_select'] == 'options':
                    state['soundtest_select'] = 'synthsewers'
            elif ev.key == pygame.K_LEFT or ev.key == pygame.K_a:
                if state['soundtest_select'] == 'synthsewers':
                    state['soundtest_select'] = 'options'
                elif state['soundtest_select'] == 'options':
                    state['soundtest_select'] = 'menu'
                elif state['soundtest_select'] == 'menu':
                    state['soundtest_select'] = 'synthsewers'
            
            if ev.key == pygame.K_RETURN:
                if state['soundtest_select'] == 'synthsewers':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/synthsewers.ogg')
                    pygame.mixer.music.play(loops = -1)
                elif state['soundtest_select'] == 'menu':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/menuloop.ogg')
                    pygame.mixer.music.play(loops = -1)
                elif state['soundtest_select'] == 'options':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/options.ogg')
                    pygame.mixer.music.play(loops = -1)
         
                
    return True


def gameloop_extra(window, assets, state):
    while atualiza_estado_extra(state):
            if state["tela"] != "extras":
                return True
            desenha_extra(window, assets, state)
         
            
    return False


