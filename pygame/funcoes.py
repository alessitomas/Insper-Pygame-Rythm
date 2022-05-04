import pygame

def test_time_very_close():
    elapsed_time = 0.5
    game = pygame.Game()
    game.update(elapsed_time)
    assert game.happening == [0.5]