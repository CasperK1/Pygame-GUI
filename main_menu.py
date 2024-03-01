import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import time
import os
import pickle
import window_specs



pygame.init()


def main_menu():
    window = window_specs.Window()
    launch_button_manager = pygame_gui.UIManager((800, 600), 'assets/buttons/launch_button.json')
    settings_manager = pygame_gui.UIManager((800, 600), 'assets/buttons/volume_button.json')
    save_manager = pygame_gui.UIManager((800, 600), 'assets/buttons/save_button.json')
    # menu music
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/menu.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    # button sound, images etc
    button_click = pygame.mixer.Sound('assets/sounds/uav_targeting.wav')
    button_click.set_volume(0.2)
    menu_background = pygame.image.load('assets/menu.png').convert_alpha()
    launch_b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 90), (250, 160)), text='',
                                            manager=launch_button_manager)

    mute_b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 10), (66, 66)),
                                          text='',
                                          manager=settings_manager,
                                          object_id=ObjectID(class_id='volume_button',
                                                             object_id='mute'))
    save_menu_b = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 100), (66, 66)),
                                               text='',
                                               manager=save_manager,
                                               object_id=ObjectID(class_id='save_button',
                                                                  object_id='save'))

    loaded_save = None
    main_running = True
    while main_running:
        time_delta = window.clock.tick(window.FPS) / 1000.0
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            launch_button_manager.process_events(event)
            settings_manager.process_events(event)
            save_manager.process_events(event)
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                main_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == launch_b:  # Launch button
                    button_click.play()
                    time.sleep(0.3)
                    if loaded_save == None:
                        launch_b.hide()
                        name_input = pygame_gui.elements.UITextEntryLine(
                            relative_rect=pygame.Rect((430, 180), (310, 70)),
                            manager=launch_button_manager,
                            object_id=pygame_gui.core.ObjectID(class_id='name_input', object_id='UITextEntryLine'),
                            placeholder_text='No save file. Enter your name: '
                        )
                    else:
                        return loaded_save

                if event.ui_element == mute_b:  # Mute button
                    if pygame.mixer.music.get_volume() == 0:
                        pygame.mixer.music.set_volume(0.1)
                        button_click.play()
                    else:
                        pygame.mixer.music.set_volume(0)
                        button_click.play()
                if event.ui_element == save_menu_b:  # Save button
                    button_click.play()
                    save_window = pygame_gui.windows.UIFileDialog(rect=pygame.Rect((20, 100), (260, 300)),
                                                                  manager=save_manager,
                                                                  window_title='LOAD GAME',
                                                                  initial_file_path='savedata',
                                                                  allowed_suffixes='.sav',
                                                                  allow_picking_directories=False,
                                                                  allow_existing_files_only=True)
                    save_window.show()

                if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_WINDOW_CLOSE:
                    if event.ui_object_id == '#save_window':  # Check if the closed window is the save window
                        save_menu_b.show()  # Show the save button again


            if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:  # Load game window
                if event.ui_element == save_window:
                    save_path = event.text
                    filename = os.path.basename(save_path)
                    file_path = os.path.join('savedata', filename)
                    if os.path.exists(file_path):
                        with open(os.path.join('savedata', filename), 'rb') as output:
                            print(f'\nLoaded {filename}')
                            loaded_save = pickle.load(output)
                            print(f'Save file player name: {loaded_save[0].player_name}')
                            print(f'Save file player level: {loaded_save[0].player_level}')
                    else:
                        print("File not found/ File error")

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                player_name = event.text

                print(f'\nNew game started as {player_name}\n')
                return player_name



        settings_manager.update(time_delta)
        launch_button_manager.update(time_delta)
        save_manager.update(time_delta)

        window.screen.blit(menu_background, (-30, 0))
        launch_button_manager.draw_ui(window.screen)
        settings_manager.draw_ui(window.screen)
        save_manager.draw_ui(window.screen)

        pygame.display.update()
        window.clock.tick(window.FPS)



