import pygame
import random

pygame.init()
# Game window specs
pygame.display.set_caption('Flight Game GUI')
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set FPS
clock = pygame.time.Clock()
FPS = 60
# Game Font
font = pygame.font.Font('asset/TarrgetAcademyItalic-qzmx.otf', 65)
# Rendered layers
background = pygame.image.load('asset/bg32.png')
font_surface = font.render('Flying to target...', True, 'indianred3')
player = pygame.image.load('asset/player_1.png')
# Clouds
cloud_1= pygame.image.load('asset/cloud1.png')
cloud1_x_pos=1200
cloud1_y_pos=random.randint(0,200)
cloud_2= pygame.image.load('asset/cloud4.png')
cloud2_x_pos=1200


scroll=0
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(0, 2):
        screen.blit(background, (i * background.get_width() + scroll, 0))
    # Scroll for background
    scroll -= 1
    # Reset background
    if abs(scroll) > background.get_width():
        scroll=0

    if cloud1_x_pos < -500:
        cloud1_x_pos = 1200
        cloud1_y_pos = random.randint(0, 200)
    screen.blit(cloud_1, (cloud1_x_pos, cloud1_y_pos))
    cloud1_x_pos-=1.5
    screen.blit(player, (50, 150))
    if cloud2_x_pos < -1500: cloud2_x_pos = 1200
    screen.blit(cloud_2, (cloud2_x_pos, 300))
    cloud2_x_pos-=3
    screen.blit(font_surface, (10, 530))



    pygame.display.update()
    clock.tick(FPS)
