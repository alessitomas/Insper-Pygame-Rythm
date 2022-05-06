import pygame
# fonte Stackoverflow
escape = pygame.image.load('img/escape.png')
escape_pt = pygame.image.load('img/escape_pt.png')
background = pygame.image.load('img/menu.png')
credits_names = pygame.image.load('img/credits_names.png')
credits_names_pt = pygame.image.load('img/credits_names_pt.png')

def desenha_credits(window: pygame.Surface, assets, state):

    window.blit(background, (0, 0))
    
    if state['lang'] == 'eng':
        window.blit(credits_names, (0, 0))
    elif state['lang'] == 'pt':
        window.blit(credits_names_pt, (0, 0))
    
    if state['lang'] == 'eng':
        window.blit(escape, (0, 0))
    if state['lang'] == 'pt':
        window.blit(escape_pt, (0, 0))
    
    pygame.display.update()
    


def atualiza_estado_credits(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
                
              
                
                
    
    
    return True


def gameloop_credits(window, assets, state):
    while atualiza_estado_credits(state):
            if state["tela"] != "creditos":
                return True
            desenha_credits(window, assets, state)
         
            
    return False

