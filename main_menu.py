import pygame, window_specs, pygame_gui

pygame.init()


def main_menu():
    window = window_specs.Window()
    pygame.mixer.init()
    manager = pygame_gui.UIManager((800, 600), 'assets/buttoncfg.json')
    pygame.mixer.music.load('assets/menu.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    menu_background = pygame.image.load('assets/menu.png').convert_alpha()
    hi_b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((475, 130), (200, 65)), text='',
                                        manager=manager)

    main_running = True
    while main_running:
        time_delta = window.clock.tick(window.FPS) / 1000.0
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_running = False
            manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hi_b:
                    main_running = False

        manager.update(time_delta)

        window.screen.blit(menu_background, (-30, 0))
        manager.draw_ui(window.screen)

        pygame.display.update()
        window.clock.tick(window.FPS)


main_menu()
