class RendererInterface():

    def display_window(self):
        pass

    def render_display(self):
        pass

    def render_background(self):
        pass

    def render_hud(self):
        pass

    def render_character(self, character):
        """ draw character """
        pass

import pygame
import os
from global_settings import *
from asset_manager import AssetManager
from character import Direction, CharacterClass


class PyGameRenderer(RendererInterface):
    g_settings: GlobalSettings
    _asset_mgr: AssetManager
    screen = {}
    render_clock = pygame.time.Clock
    # TODO:: look at sprite group usage
    # sprite_group: pygame.sprite.Group()

    def __init__(self, settings, asset_mgr, clock):
        self.g_settings = settings
        self._asset_mgr = asset_mgr
        self.render_clock = clock
        
        pygame.init()
        self.display_window()
        self.load_sprites()

    def display_window(self):

        #render logo
        logo2d = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo2d)
        pygame.display.set_caption("2D Platformer")

        #create surface
        self.screen = pygame.display.set_mode((self.g_settings.SCREEN_WIDTH, self.g_settings.SCREEN_HEIGHT))
    
    def load_sprites(self):
        self._asset_mgr.get_background('01.jpg')
        self._asset_mgr.get_sprite('char1.png')
        self._asset_mgr.get_sprite('Frame.png')
    
    def render_background(self, gamestate):
        background = self._asset_mgr.get_background('01.jpg')
        background = pygame.transform.scale(background, (1024, 768))
        self.screen.blit(background, (0,0))

    def render_hud(self, gamestate):
        frame = self._asset_mgr.get_sprite('Frame.png')
        self.screen.blit(frame.sprite, (0, 550))
        port = self._asset_mgr.get_sprite('port2.png')
        port = pygame.transform.scale(port.sprite, (256, 256))
        self.screen.blit(port, (3, 610))

    def render_character(self, character):
        sprite_animation = self._asset_mgr.get_sprite('char1.png')        
        
        if character.is_moving:
            sprite_animation.play_walk_animation(character, self.screen)
        else:
            sprite_animation.play_standing(character, self.screen)
        # dirtyRect = self.screen.blit(frame, (character.position.x, character.position.y))
        # pygame.display.update(dirtyRect)

    def draw_FPS(self, game_state, clock):
        game_state.FPS = clock.get_fps()        
        font = pygame.font.Font('freesansbold.ttf', 16)
        fpsText = font.render("FPS:{} playtime:{}".format(game_state.FPS, game_state.playtime), True, (0, 0, 0))
        self.screen.blit(fpsText, (0,0))

    def flush(self):
        pygame.display.flip()