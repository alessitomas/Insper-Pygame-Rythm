import pygame
# fonte Stackoverflow


def desenha_how(window: pygame.Surface, assets, state):
    window.fill(((255, 165, 0)))
   
    
    
    pygame.display.update()
    


def atualiza_estado_how(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
                
                
    
    
    return True


def gameloop_how(window, assets, state):
    while atualiza_estado_how(state):
            if state["tela"] != "how":
                return True
            desenha_how(window, assets, state)
         
            
    return False

