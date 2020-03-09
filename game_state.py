# Singleton/BorgSingleton.py
# Alex Martelli's 'Borg'

class Singleton:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

import pygame
import random

from player import Player
from npc import NPC
from character import Coordinate
from character import Direction

class GameState(Singleton):
    running = False
    FPS = 0
    frame_counter = 0
    clock = pygame.time.Clock()
    playtime = 0

    maxCharacterId = 1
    actors = {}

    def __init__(self, arg):
        Singleton.__init__(self)
        self.running = True
        self.create_player()
    
    def create_player(self):
        arg = {
            'health': 100,
            'speed': 0.5,
            'position': Coordinate(0,450),
            'facingDirection': Direction.RIGHT
        }
        player1 = Player(arg)
        self.actors["P1"] = player1

    def create_npc(self):
        self.maxCharacterId += 1
        pos_x = random.randint(100, 1024)
        arg = {
            'health': 100,
            'speed': 0.9,
            'position': Coordinate(pos_x, 450),
            'facingDirection': Direction.RIGHT
        }
        
        npc = NPC(self.maxCharacterId, arg)
        self.actors[self.maxCharacterId] = npc
