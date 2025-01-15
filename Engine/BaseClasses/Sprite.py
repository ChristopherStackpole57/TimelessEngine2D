from Engine.Datatypes.Vector2 import Vector2

class Sprite:
    def __init__(self, source: str = "", size = Vector2(10, 10)):
        self.Source = source
        self.Size = size