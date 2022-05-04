import pygame
# fonte Stackoverflow


def desenha_extra(window: pygame.Surface, assets, state):
    window.fill((0,0,0))
   
    
    
    pygame.display.update()
    


def atualiza_estado_extra(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        
                
                
    
    
    return True


def gameloop_extra(window, assets, state):
    while atualiza_estado_extra(state):
        
            desenha_extra(window, assets, state)
         
            
    return False


