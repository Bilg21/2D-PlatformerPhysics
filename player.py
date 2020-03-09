from character import Direction, Coordinate
from character import Character

class Player(Character):
    id: int
    health: int
    position: Coordinate
    facingDirection: Direction
    speed: int

    def __init__(self, arg):
        super().__init__(0, arg)


    def getPos(self):
        return self.position
