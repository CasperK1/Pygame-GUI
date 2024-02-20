import pygame, random
pygame.init()

# Game window specs
pygame.display.set_caption('Flight Game GUI')
programIcon = pygame.image.load('asset/player_animation/player_1.png')
pygame.display.set_icon(programIcon)
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set FPS
clock = pygame.time.Clock()
FPS = 60

def main_menu():
    pygame.mixer.init()
    pygame.mixer.music.load('asset/menu.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    menu_background = pygame.image.load('asset/menu.png').convert_alpha()
    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT or keys[pygame.K_RETURN]:
                running = False
        screen.blit(menu_background, (-30, 0))

        pygame.display.update()
        clock.tick(FPS)

main_menu()
# Game Font
font = pygame.font.Font('asset/TarrgetAcademyItalic-qzmx.otf', 65)
# Rendered layers.
background = pygame.image.load('asset/bg32.png').convert_alpha()
bg_scroll = 0
font_surface = font.render('Flying to target...', True, 'lightslategrey').convert_alpha()
player = pygame.image.load('asset/player_animation/player_1.png').convert_alpha()
player_left1 = pygame.image.load('asset/player_animation/player_1_TURNL2.png').convert_alpha()
player_left2 = pygame.image.load('asset/player_animation/player_1_TURNL.png').convert_alpha()
turn_left = [player_left1, player_left2]
turn_left_counter = 0
player_right1 = pygame.image.load('asset/player_animation/player_1_TURNR2.png').convert_alpha()
player_right2 = pygame.image.load('asset/player_animation/player_1_TURNR.png').convert_alpha()
turn_right = [player_right1, player_right2]
turn_right_counter = 0
player_coll = player.get_rect(topleft=(50, 150))
HUD = pygame.image.load('asset/HUD.png').convert_alpha()

# Radar animation
radar_frames = [pygame.image.load(f'asset/radar/frame_91 ({i}).png') for i in range(1, 92)]
radar_frame_counter = 0

# Clouds
cloud_1 = pygame.image.load('asset/cloud1.png').convert_alpha()
cloud_1_rect = cloud_1.get_rect(center=(1400, 100))

cloud_2 = pygame.image.load('asset/cloud4.png').convert_alpha()
cloud2_x_pos = 1200

# Game Loop
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                turn_left_counter = 0
            if event.key == pygame.K_DOWN:
                turn_right_counter = 0

    pygame.mixer.music.fadeout(8000)
    # Scroll for background
    for i in range(0, 2):
        screen.blit(background, (i * background.get_width() + bg_scroll, 0))
    bg_scroll -= 1
    # Reset background
    if abs(bg_scroll) > background.get_width():
        bg_scroll = 0
    # Cloud 1
    if cloud_1_rect.x < -300:
        cloud_1_rect.x = 1200
        cloud_1_rect.y = random.randint(100, 150)
    screen.blit(cloud_1, cloud_1_rect)
    cloud_1_rect.x -= 1.501
    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_coll.y -= 5
    elif keys[pygame.K_DOWN]:
        player_coll.y += 5
    if player_coll.y <= 0:
        player_coll.y = 0
    elif player_coll.y >= 400:
        player_coll.y = 400
    # player animation
    if keys[pygame.K_UP]:
        screen.blit(turn_left[int(turn_left_counter)], player_coll)
        turn_left_counter += 0.1
        if turn_left_counter >= len(turn_left):
            turn_left_counter = 1
    elif keys[pygame.K_DOWN]:
        screen.blit(turn_right[int(turn_right_counter)], player_coll)
        turn_right_counter += 0.1
        if turn_right_counter >= len(turn_right):
            turn_right_counter = 1
    else:
        screen.blit(player, player_coll)

    # Cloud 2
    if cloud2_x_pos < -1800:
        cloud2_x_pos = 1200
    screen.blit(cloud_2, (cloud2_x_pos, 300))
    cloud2_x_pos -= 3.5
    # HUD and radar
    screen.blit(HUD, (0, 0))
    screen.blit(radar_frames[int(radar_frame_counter)], (898, 604))
    radar_frame_counter += 0.8
    if radar_frame_counter >= len(radar_frames):
        radar_frame_counter = 0

    pygame.display.update()
    clock.tick(FPS)
