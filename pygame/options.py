import pygame
# fonte Stackoverflow
escape = pygame.image.load('img/escape.png')
escape_pt = pygame.image.load('img/escape_pt.png')
background = pygame.image.load('img/menu.png')

english = pygame.image.load('img/english.png')
english_select = pygame.image.load('img/english_select.png')
portugues = pygame.image.load('img/portugues.png')
portugues_select = pygame.image.load('img/portugues_select.png')

def desenha_options(window: pygame.Surface, assets, state):
    
    window.blit(background, (0, 0))
    
    if state['lang'] == 'eng':
        window.blit(escape, (0, 0))
    elif state['lang'] == 'pt':
        window.blit(escape_pt, (0, 0))
   
    if state['lang_direction'] == 'left':
        window.blit(english_select, (100,285))
        window.blit(portugues, (679,285))
    elif state['lang_direction'] == 'right':
        window.blit(english, (100,285))
        window.blit(portugues_select, (679,285))
    
    pygame.display.update()
    


def atualiza_estado_options(state):
   
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                state["tela"] = "inicial"
            elif ev.key == pygame.K_RIGHT or ev.key == pygame.K_LEFT or ev.key == pygame.K_a or ev.key == pygame.K_d:
                if state['lang_direction'] == 'left':
                    state['lang_direction'] = 'right'
                elif state['lang_direction'] == 'right':
                    state['lang_direction'] = 'left'
            elif ev.key == pygame.K_RETURN:
                if state['lang_direction'] == 'left':
                    state['lang'] = 'eng'
                elif state['lang_direction'] == 'right':
                    state['lang'] = 'pt' 
    
    
    return True


def gameloop_options(window, assets, state):
    while atualiza_estado_options(state):
            if state["tela"] != "options":
                return True
            desenha_options(window, assets, state)
         
            
    return False

