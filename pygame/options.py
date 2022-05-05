import pygame
# fonte Stackoverflow
CIANO = (0, 225, 225)

def desenha_options(window: pygame.Surface, assets, state):
    window.fill(CIANO)
   
    
    
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

