from Engine.Datatypes.Vector2 import Vector2


class Cell:
    CELL_SIZE = 200

    def __init__(self, x, y):
        # Position is top left
        self.Position = Vector2(x, y)
        self.Size = Vector2(Cell.CELL_SIZE, Cell.CELL_SIZE)

        self.Center = self.Position + self.Size / 2

        self.Tiles = []

        self.L = None
        self.R = None
        self.T = None
        self.B = None

    def __str__(self):
        return f'Cell at {self.Center} with Number of Tiles: {len(self.Tiles)}'