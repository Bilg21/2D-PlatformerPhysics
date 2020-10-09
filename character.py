import pygame
import os
import math
import time

from enum import Enum
from global_settings import DIR_SPRITES
import physics

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

CharacterClass = Enum('CharacterClass', 'Player NPC')

class Coordinate():
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Character():
    id: int
    name: str
    health: int
    position: Coordinate
    facingDirection: Direction
    is_moving: bool
    is_falling: bool
    angle: float
    speed: int
    dt_speed: int
    sprite: pygame.sprite.Sprite
    char_class: CharacterClass

    def __init__(self, charId: int, arg):
        self.id = charId
        self.name = "Char[{}]".format(charId)  

        self.health = arg['health']
        self.speed = arg['speed']
        self.position = arg['position']
        self.facingDirection = arg['facingDirection']
        self.is_moving = False
        self.is_falling = False

        self.spritesheet = pygame.image.load(os.path.join(DIR_SPRITES, 'char1.png'))
        self.facingDirection = Direction.DOWN

    def move(self, direction):
        self.is_moving = True
        direction = Direction(direction)
        self.speed = 10
        if direction == Direction.RIGHT:
            self.facingDirection = Direction.RIGHT
            if self.position.x < 1024:
                self.position.x += self.speed
        elif direction == Direction.LEFT:
            self.facingDirection = Direction.LEFT
            if self.position.x > 0:
                self.position.x -= self.speed
        elif direction == Direction.DOWN:
            self.facingDirection = Direction.DOWN
            if self.position.y < 450:
                self.position.y += self.speed
        elif direction == Direction.UP:
            self.facingDirection = Direction.UP
            self.jump()
            # if self.position.y > 0:
            #     self.position.y -= self.speed
        
        print("{} face_dir:{} pos:{},{}".format(\
            self.name, self.facingDirection, self.position.x, self.position.y))  
    
    def jump(self):
        if self.is_falling:
            return
        self.is_falling = True

        self.angle = math.pi
        self.speed = 20
        
        print("JUMP:x:{} y:{} angle:{} speed:{}".format(\
            self.position.x, self.position.y, self.angle, self.speed))
        # self.move_gravity()

    def move_gravity(self, ticks):
        if self.position.y > 450:
            self.position.y = 450
            self.is_falling = False
            self.speed = 0
            print("finish falling")
            return

        #drag & elasticity
        # self.dt_speed *= physics.drag * physics.elasticity
        print("GRJUMP:x:{} y:{} angle:{} speed:{}".format(\
            self.position.x, self.position.y, self.angle, self.speed))
        #apply gravity
        gravity = physics.gravity
        (self.angle, self.speed) = physics.addVectors((self.angle, self.speed), gravity)
        
        self.position.x += math.sin(self.angle) * self.speed
        self.position.y += math.cos(self.angle) * self.speed
        print("GRJUMP2:x:{} y:{} angle:{} speed:{}".format(\
            self.position.x, self.position.y, self.angle, self.speed))
        print("moving angle:{} (x,y):({},{})".format(self.angle,self.position.x, self.position.y))

    
    def draw(self, screen):
        self.spritesheet.convert()

        frameNo = 0    
        if self.facingDirection == Direction.RIGHT:
            frameNo = 8
        elif self.facingDirection == Direction.LEFT:
            frameNo = 4
        elif self.facingDirection == Direction.DOWN:
            frameNo = 0
        elif self.facingDirection == Direction.UP:
            frameNo = 12

        # 4x4 sheet
        rows = 4
        cols = 4
        w = 32.5
        h = 48.5
        box_h = 97
        box_w = 65

        row = int(frameNo / rows)
        col = frameNo % rows

        frame = self.spritesheet.subsurface((col * w, row * h, w, h))
        frame = pygame.transform.scale(frame, (box_w, box_h))

        pygame.display.update(screen.blit(frame, (self.position.x, self.position.y)))

        