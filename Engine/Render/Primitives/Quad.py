from Engine.BaseClasses.Object import Object
from Engine.Datatypes.Vector2 import Vector2
from Engine.Render.PrimitiveType import PrimitiveType
from Engine.Render.RenderType import RenderType

class Quad(Object):
    def __init__(self, color, *points):
        if len(points) > 4:
            raise Exception("Too many points")

        pos = Vector2(
            min(*[point.X for point in points]),
            min(*[point.Y for point in points])
        )

        size = Vector2(
            max(*[point.X for point in points]),
            max(*[point.Y for point in points])
        ) - pos

        super().__init__(pos, size, color, RenderType.PRIMITIVE, PrimitiveType.QUAD)

        self.Vertices = points