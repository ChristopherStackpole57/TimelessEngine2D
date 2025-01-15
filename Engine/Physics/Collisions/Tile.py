from Engine.Datatypes.Vector2 import Vector2
from Engine.Physics.Enumerations.TileType import TileType

class Tile:
    def __init__(self, type: TileType, obj, *args):
        # Argument Values
        # For TileType.AABB
            # args: AABB
        # For TileType.TRIANGLE
            # args: vertex1, vertex2, vertex3
        # For TileType.CIRCLE
            # args: center_position, radius

        self.Type = type

        # TODO: Adjust to account for circles not having vertices

        self.Position = Vector2()
        self.Vertices = []

        if self.Type == TileType.AABB:
            self.AABB = args[0]
            self.Position = self.AABB.Position
            self.Vertices = self.AABB.Vertices
        elif self.Type == TileType.TRIANGLE:
            self.Vertices = args
        elif self.Type == TileType.CIRCLE:
            self.Position = args[0]
            self.Radius = args[1]

        self.ObjReference = obj

    def __str__(self):
        if self.Type == TileType.AABB:
            return f'AABB Tile with Position {self.Position}'