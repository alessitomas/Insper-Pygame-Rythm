import pygame
# fonte Stackoverflow
escape = pygame.image.load('img/escape.png')
escape_pt = pygame.image.load('img/escape_pt.png')
background = pygame.image.load('img/menu.png')
tutorial = pygame.image.load('img/tutorial.png')
def desenha_how(window: pygame.Surface, assets, state):

    window.blit(tutorial, (0, 0))
    
    if state['lang'] == 'eng':
        window.blit(escape, (0, 0))
    elif state['lang'] == 'pt':
        window.blit(escape_pt, (0, 0))
    
    pygame.display.update()
    


def atualiza_estado_how(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
                
                
    
    
    return True


def gameloop_how(window, assets, state):
    while atualiza_estado_how(state):
            if state["tela"] != "how":
                return True
            desenha_how(window, assets, state)
         
            
    return False

