import pygame
# fonte Stackoverflow

image1 = pygame.image.load('img/game.png')
def desenha_credits(window: pygame.Surface, assets, state):
    window.fill(((255, 0, 127)))
   
    window.blit(image1, (225, 150))
    
    pygame.display.update()
    


def atualiza_estado_credits(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
                
              
                
                
    
    
    return True


def gameloop_credits(window, assets, state):
    while atualiza_estado_credits(state):
            if state["tela"] != "creditos":
                return True
            desenha_credits(window, assets, state)
         
            
    return False

