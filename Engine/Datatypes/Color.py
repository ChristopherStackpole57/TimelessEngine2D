class Color:
    def __init__(self, r: int or float = 0, g: int or float = 0, b: int or float = 0):
        self.R = max(0, min(r, 255))
        self.G = max(0, min(g, 255))
        self.B = max(0, min(b, 255))

    # TODO: Implement arithmetic operators and helpers

    def __iter__(self):
        return iter([self.R, self.G, self.B])

    def __str__(self):
        return f'Color: ({self.R}, {self.G}, {self.B})'