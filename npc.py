from character import Character
from character import Coordinate

class NPC(Character):
    isEnemy: bool    

    def __init__(self, id: int, arg):
        super().__init__(id, arg)
        self.isEnemy = False