import os
import pygame

from global_settings import DIR_SPRITES, DIR_LEVELS
from sprite_animation import SpriteAnimation

class AssetManager():

    def __init__(self):
        self.sprites = {}
        self.backgrounds = {}
        self.sounds = {}

    def load_sprites(self):
        # load list of sprites initially
        pass

    def load_sounds(self):
        pass

    def load_map(self):
        pass

    def get_sprite(self, sprite_id: str):
        if sprite_id not in self.sprites:
            sprite = SpriteAnimation(pygame.image.load(os.path.join(DIR_SPRITES, sprite_id)))
            self.sprites[sprite_id] = sprite
        
        return self.sprites[sprite_id]
    
    def get_background(self, background_id: str):
        if background_id not in self.backgrounds:
            sprite = pygame.image.load(os.path.join(DIR_LEVELS, background_id))
            self.backgrounds[background_id] = sprite
        
        return self.backgrounds[background_id]