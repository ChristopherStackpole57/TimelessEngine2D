from Engine.Datatypes.Vector2 import Vector2

class Line:
    def Normal(self):
        slope = self.P2 - self.P1
        return Vector2(-slope.Y, slope.X)

    def __init__(self, p1: Vector2, p2: Vector2):
        self.P1 = p1
        self.P2 = p2