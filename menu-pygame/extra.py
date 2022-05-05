import pygame
# fonte Stackoverflow


def desenha_extra(window: pygame.Surface, assets, state):
    window.fill((0,0,0))
   
    
    
    pygame.display.update()
    


def atualiza_estado_extra(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
                
                
    
    
    return True


def gameloop_extra(window, assets, state):
    while atualiza_estado_extra(state):
            if state["tela"] != "extras":
                return True
            desenha_extra(window, assets, state)
         
            
    return False


