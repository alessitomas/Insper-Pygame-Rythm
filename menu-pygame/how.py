import pygame
# fonte Stackoverflow
CIANO = (0, 225, 225)
image1 = pygame.image.load('img/game.kill.png')
def desenha_how(window: pygame.Surface, assets, state):
    window.fill(CIANO)
   
    window.blit(image1, (225, 150))
    
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

