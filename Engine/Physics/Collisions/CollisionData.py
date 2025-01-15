from typing import List

from Engine.Datatypes.Vector2 import Vector2

class CollisionData:
    def __init__(self, collides, *args: List[Vector2 | int or float]):
        self.Collides = collides
        if self.Collides == True:
            self.UnitAxes = args

    def __str__(self):
        if self.Collides:
            string = "CollisionData: Collides on Unit Axes "
            for axis in self.UnitAxes:
                string += f'\n{axis[0]} with Overlap: {axis[1]}'
            return string
        else:
            return "CollisionData: No Collision"