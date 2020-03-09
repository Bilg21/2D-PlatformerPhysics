import pygame
from character import Direction

class SpriteAnimation():
    sprite: pygame.sprite.Sprite
    current_frame = 0
    frame_time = 0

    def __init__(self, sprite: pygame.sprite.Sprite):
        self.current_frame = 0
        self.sprite = sprite

    def play_standing(self, character, screen):
        rows = 4
        cols = 4
        w = 32.5
        h = 48.5
        box_h = 97
        box_w = 65
        frame = self.sprite.subsurface((0, 0, w, h))
        frame = pygame.transform.scale(frame, (box_w, box_h))
        dirtyRect = screen.blit(frame, (character.position.x, character.position.y))
        pygame.display.update(dirtyRect)

    def play_walk_animation(self, character, screen): 
        self.sprite.convert()

        frame_time = pygame.time.get_ticks()
        if frame_time - self.frame_time > 200:
            # get next frame
            self.current_frame += 1
            if character.facingDirection == Direction.RIGHT:
                self.current_frame = (self.current_frame % 4) + 8
            elif character.facingDirection == Direction.LEFT:
                self.current_frame = (self.current_frame % 4) + 4
            elif character.facingDirection == Direction.DOWN:
                self.current_frame = (self.current_frame % 4) + 0
            elif character.facingDirection == Direction.UP:
                self.current_frame = (self.current_frame % 4) + 12
            # print("next frame:{}".format(self.current_frame))
            
            self.frame_time = frame_time

        """
            0  1  2  3  -> % 4
            4  5  6  7  -> % 4 + 4
            8  9  10 11 -> % 4 + 8
            12 13 14 15 -> % 4 + 12
        """

        # 4x4 sheet
        rows = 4
        cols = 4
        w = 32.5
        h = 48.5
        box_h = 97
        box_w = 65

        row = int(self.current_frame / rows)
        col = self.current_frame % rows

        frame = self.sprite.subsurface((col * w, row * h, w, h))
        frame = pygame.transform.scale(frame, (box_w, box_h))

        dirtyRect = screen.blit(frame, (character.position.x, character.position.y))
        pygame.display.update(dirtyRect)

        return frame


