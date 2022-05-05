import pygame
# fonte Stackoverflow


def desenha_options(window: pygame.Surface, assets, state):
    window.fill(((255, 0, 0)))
   
    
    
    pygame.display.update()
    


def atualiza_estado_options(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
                
                
    
    
    return True


def gameloop_options(window, assets, state):
    while atualiza_estado_options(state):
            if state["tela"] != "options":
                return True
            desenha_options(window, assets, state)
         
            
    return False

