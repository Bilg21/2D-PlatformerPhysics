#!/usr/bin/env python3

"""
Author:  Bilg
"""

import pygame
import os
import time
import random

from global_settings import GlobalSettings, DIR_SPRITES, DIR_LEVELS
from renderer import PyGameRenderer, RendererInterface
from asset_manager import AssetManager
from sound_mixer import SoundMixer
from game_state import GameState
from player import Player
from character import Direction
from character import Character

clock = pygame.time.Clock()
frames_count = 0
current_time = 0

"Initialization"
def main():

    settings = GlobalSettings()
    asset_mgr = AssetManager()
    renderer = PyGameRenderer(settings, asset_mgr, clock)
    sound_mixer = SoundMixer()
    game_state = GameState(0)

    sound_mixer.play_sound("simple_noteseq.ogg",-1)

    #main loop var
    game_state.running = True
    
    #main loop
    # draw_display(screen, game_state)
    while game_state.running:
        #get events from event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.running = False
                exit(0)
            elif event.type == pygame.KEYDOWN:
                handle_key_events(event, game_state)
            # elif event.type == ADD_ENEMY:
            #     handle_game_events(event)
               
        perform_game_logic(game_state)
        draw(renderer, game_state)
        # draw_display(screen, game_state)

def draw(renderer: RendererInterface, game_state: GameState):
    renderer.render_background(game_state)
    renderer.render_hud(game_state)

    for char_id, character in game_state.actors.items():
        renderer.render_character(character)
    
    # TODO: separate fps metrics etc from gamestate
    renderer.draw_FPS(game_state, clock)
    renderer.flush()
    
    # milliseconds = clock.tick(FPS) lock fps with {FPS} var
    clock.tick(144)


def perform_game_logic(game_state):
    #player movement
    global current_time
    ticks = pygame.time.get_ticks()
    
    if ticks - current_time < 72:
         return

    current_time = pygame.time.get_ticks()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        game_state.actors["P1"].move(Direction.RIGHT)
    elif keys_pressed[pygame.K_LEFT]:
        game_state.actors["P1"].move(Direction.LEFT)
    elif keys_pressed[pygame.K_DOWN]:
        game_state.actors["P1"].move(Direction.DOWN)
    
    if keys_pressed[pygame.K_UP]:
        game_state.actors["P1"].move(Direction.UP)
        # game_state.actors["P1"].jump(clock.tick())
    elif game_state.actors["P1"].is_falling:
        game_state.actors["P1"].move_gravity(clock.tick())
    else:
        game_state.actors["P1"].is_moving = False
    
    
    # #randomly add npc
    # if len(game_state.actors) < 5:
    #     roll = random.randint(1,1000)
    #     if roll % 100 == 0:
    #         game_state.create_npc()

    # # randomly move npc
    # for char_id in game_state.actors:
    #     if char_id == 'P1': 
    #         continue
        
    #     random_direction = random.randint(1,4)
    #     # print("rand_dir:{}".format(random_direction))
    #     game_state.actors[char_id].move(random_direction)
    
    return 0

def handle_game_events(game_state):
    # if event.type == ADD_ENEMY:
    #     game_state.create_npc()
    pass


def handle_key_events(key_event, game_state):
    if key_event.key == pygame.K_ESCAPE:
            game_state.running = False
    elif key_event.key == pygame.K_RIGHT:
        print("key right")
        

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    main()