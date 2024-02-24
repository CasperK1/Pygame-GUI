import pygame, window_specs, pygame_gui
import time
from pygame_gui.core import ObjectID
pygame.init()


def main_menu():
    window = window_specs.Window()
    launch_button_manager = pygame_gui.UIManager((800, 600), 'assets/buttoncfg.json')
    settings_manager = pygame_gui.UIManager((800, 600), 'assets/settings_button.json')
    # menu music
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/menu.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    # button sound, images etc
    button_click = pygame.mixer.Sound('assets/sounds/uav_targeting.wav')
    button_click.set_volume(0.2)
    menu_background = pygame.image.load('assets/menu.png').convert_alpha()
    launch_b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((460, 90), (250, 160)), text='',
                                            manager=launch_button_manager)

    mute_b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 10), (44, 44)),
                                              text='',
                                              manager=settings_manager,
                                              object_id=ObjectID(class_id='settings_button',
                                                                object_id='mute'))

    main_running = True
    while main_running:
        time_delta = window.clock.tick(window.FPS) / 1000.0
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            launch_button_manager.process_events(event)
            settings_manager.process_events(event)
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                main_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == launch_b:
                    button_click.play()
                    time.sleep(0.3)
                    main_running = False
                if event.ui_element == mute_b:
                    if pygame.mixer.music.get_volume() == 0:
                        pygame.mixer.music.set_volume(0.1)
                        button_click.play()
                    else:
                        pygame.mixer.music.set_volume(0)
                        button_click.play()
                        
        settings_manager.update(time_delta)
        launch_button_manager.update(time_delta)

        window.screen.blit(menu_background, (-30, 0))
        launch_button_manager.draw_ui(window.screen)
        settings_manager.draw_ui(window.screen)

        pygame.display.update()
        window.clock.tick(window.FPS)


main_menu()
