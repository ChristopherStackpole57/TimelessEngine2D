# Axis Aligned Bounding Box

from Engine.Datatypes.Vector2 import Vector2
from Engine.Utilities.Utilities import GetCenterOfVertices, GetBoundingSizeOfVertices


class AABB:
    def __init__(self, vertices):
        size = GetBoundingSizeOfVertices(vertices)

        self.Position = GetCenterOfVertices(vertices)
        self.HalfwidthX = Vector2(size.X / 2, 0)
        self.HalfwidthY = Vector2(0, size.Y / 2)

        self.Vertices = vertices

    def __setattr__(self, key, value):
        if key == 'Position' and "Vertices" in self.__dict__:
            diff = value - self.Position

            for i in range(len(self.Vertices)):
                self.Vertices[i] = self.Vertices[i] + diff

        self.__dict__[key] = value