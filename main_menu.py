import pygame, window_specs
pygame.init()
def main_menu():
    window = window_specs.Window()
    pygame.mixer.init()
    pygame.mixer.music.load('assets/menu.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    menu_background = pygame.image.load('assets/menu.png').convert_alpha()
    main_running = True
    while main_running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT or keys[pygame.K_RETURN]:
                main_running = False
        window.screen.blit(menu_background, (-30, 0))

        pygame.display.update()
        window.clock.tick(window.FPS)

