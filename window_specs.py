import pygame
class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Flight Game GUI')
        programIcon = pygame.image.load('asset/player_animation/player_1.png')
        pygame.display.set_icon(programIcon)
        self.SCREEN_WIDTH = 1100
        self.SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.FPS = 60
