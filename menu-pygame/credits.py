import pygame
# fonte Stackoverflow


def desenha_credits(window: pygame.Surface, assets, state):
    window.fill(((255, 0, 127)))
   
    
    
    pygame.display.update()
    


def atualiza_estado_credits(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        
                
                
    
    
    return True


def gameloop_credits(window, assets, state):
    while atualiza_estado_credits(state):
        
            desenha_credits(window, assets, state)
         
            
    return False

