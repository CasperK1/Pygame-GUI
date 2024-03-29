import pygame
import random
import window_specs

pygame.init()
pygame.mixer.init()
window = window_specs.Window()


def gui_loop():


    # Game Font
    #font = pygame.font.Font('assets/TarrgetAcademyItalic-qzmx.otf', 65)
    # Rendered layers.
    background = pygame.image.load('assets/bg32.png').convert_alpha()
    bg_scroll = 0
    player = pygame.image.load('assets/player_animation/player_1.png').convert_alpha()
    player_left1 = pygame.image.load('assets/player_animation/player_1_TURNL2.png').convert_alpha()
    player_left2 = pygame.image.load('assets/player_animation/player_1_TURNL.png').convert_alpha()
    turn_left = [player_left1, player_left2]
    turn_left_counter = 0
    player_right1 = pygame.image.load('assets/player_animation/player_1_TURNR2.png').convert_alpha()
    player_right2 = pygame.image.load('assets/player_animation/player_1_TURNR.png').convert_alpha()
    turn_right = [player_right1, player_right2]
    turn_right_counter = 0
    player_coll = player.get_rect(topleft=(50, 150))
    HUD = pygame.image.load('assets/HUD.png').convert_alpha()
    cockpit = pygame.image.load('assets/player_animation/LOCK WARNING.png').convert_alpha()

    # Radar animation
    radar_frames = [pygame.image.load(f'assets/radar/frame_91 ({i}).png') for i in range(1, 92)]
    radar_frame_counter = 0

    # Clouds
    cloud_1 = pygame.image.load('assets/cloud1.png').convert_alpha()
    cloud_1_rect = cloud_1.get_rect(center=(1400, 100))
    cloud_2 = pygame.image.load('assets/cloud4.png').convert_alpha()
    cloud2_x_pos = 1200

    # Sounds
    rwr_lock = pygame.mixer.Sound('assets/sounds/radar_lock.wav')
    rwr_lock.set_volume(0.15)
    rwr_warning = pygame.mixer.Sound('assets/sounds/rwr_WarningWarning.wav')
    rwr_warning.set_volume(0.15)

    last_check_time = pygame.time.get_ticks()
    warning_screen_timer = 0
    detect = False
    running = True
    while running:
        # Check for enemies every 3 seconds (test)
        current_time = pygame.time.get_ticks()
        if (current_time - last_check_time) > 4000 and detect == False:  # 4000 milliseconds = 4 seconds
            print('Checking for enemies...')
            if random.random() < 0.3:  # 30% chance to counter enemy during trip
                print('Enemy detected!')
                rwr_warning.play()
                rwr_lock.play(loops=-1)
                detect = True
                warning_screen_timer = current_time
            last_check_time = current_time
        if detect and  (current_time - warning_screen_timer) > 5000:
            print('Starting combat...')
            break


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
            window.screen.blit(background, (i * background.get_width() + bg_scroll, 0))
        bg_scroll -= 1
        # Reset background
        if abs(bg_scroll) > background.get_width():
            bg_scroll = 0
        # Cloud 1
        if cloud_1_rect.x < -1000:
            cloud_1_rect.x = 1200
            cloud_1_rect.y = random.randint(100, 150)
        window.screen.blit(cloud_1, cloud_1_rect)
        cloud_1_rect.x -= 2
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
            window.screen.blit(turn_left[int(turn_left_counter)], player_coll)
            turn_left_counter += 0.1
            if turn_left_counter >= len(turn_left):
                turn_left_counter = 1
        elif keys[pygame.K_DOWN]:
            window.screen.blit(turn_right[int(turn_right_counter)], player_coll)
            turn_right_counter += 0.1
            if turn_right_counter >= len(turn_right):
                turn_right_counter = 1
        else:
            window.screen.blit(player, player_coll)

        # Cloud 2
        if cloud2_x_pos < -1800:
            cloud2_x_pos = 1200
        window.screen.blit(cloud_2, (cloud2_x_pos, 300))
        cloud2_x_pos -= 3.5
        # HUD and radar
        window.screen.blit(HUD, (0, 0))
        window.screen.blit(radar_frames[int(radar_frame_counter)], (898, 604))
        radar_frame_counter += 0.8
        if radar_frame_counter >= len(radar_frames):
            radar_frame_counter = 0
        if detect == True:
            window.screen.blit(cockpit, (0, 0))
        pygame.display.update()
        window.clock.tick(window.FPS)
