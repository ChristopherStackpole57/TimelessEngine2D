import math

class Vector2:
    def Magnitude(self):
        return math.sqrt(self.X ** 2 + self.Y ** 2)

    def Dot(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("Vector2 can only be dotted with Vector2.")

        return (self.X * other.X) + (self.Y * other.Y)

    def __init__(self, x = 0, y = 0):
        self.X = x
        self.Y = y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.X - other.X, self.Y - other.Y)

    def __mul__(self, other: int or float):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.X * other, self.Y * other)

    def __rmul__(self, other: int or float):
        return self * other

    def __truediv__(self, other: int or float):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.X / other, self.Y / other)

    def __iter__(self):
        return iter([self.X, self.Y])

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.X == other.X and self.Y == other.Y
        return NotImplemented

    def __str__(self):
        return f'({self.X}, {self.Y})'