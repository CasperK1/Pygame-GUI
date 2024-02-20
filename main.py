import pygame
import random

pygame.init()
# Game window specs
pygame.display.set_caption('Flight Game GUI')
programIcon = pygame.image.load('asset/radar.png')

pygame.display.set_icon(programIcon)
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set FPS
clock = pygame.time.Clock()
FPS = 60
# Game Font
font = pygame.font.Font('asset/TarrgetAcademyItalic-qzmx.otf', 65)
# Rendered layers
background = pygame.image.load('asset/bg32.png').convert_alpha()
font_surface = font.render('Flying to target...', True, 'lightslategrey').convert_alpha()
player = pygame.image.load('asset/player_1.png').convert_alpha()
player_coll = player.get_rect(topleft=(50, 150))
HUD = pygame.image.load('asset/HUD.png').convert_alpha()
# Clouds
cloud_1 = pygame.image.load('asset/cloud1.png').convert_alpha()
cloud_1_rect = cloud_1.get_rect(center= (1400, 100))

cloud_2 = pygame.image.load('asset/cloud4.png').convert_alpha()
cloud2_x_pos = 1200

scroll = 0
# Game Loop
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_coll.y -=5
    elif keys[pygame.K_DOWN]:
        player_coll.y +=5
    if player_coll.y <= 0:
        player_coll.y= 0
    elif player_coll.y >= 400:
        player_coll.y = 400

    # Scroll for background
    for i in range(0, 2):
        screen.blit(background, (i * background.get_width() + scroll, 0))
    scroll -= 1
    # Reset background
    if abs(scroll) > background.get_width():
        scroll = 0

    if cloud_1_rect.x < -300:
        cloud_1_rect.x = 1200
        cloud_1_rect.y = random.randint(100, 150)
    screen.blit(cloud_1, cloud_1_rect)
    cloud_1_rect.x -= 1.501

    screen.blit(player, player_coll)

    if cloud2_x_pos < -1800:
        cloud2_x_pos = 1200
    screen.blit(cloud_2, (cloud2_x_pos, 300))
    cloud2_x_pos -= 3.5

    screen.blit(HUD, (0, 0))

    pygame.display.update()
    clock.tick(FPS)
