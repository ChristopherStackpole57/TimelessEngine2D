class Text(object):
    TEXT_LIST = []

    def __init__(self, text, position, color, size = 10, font = "Comic Sans MC"):
        self.Text = text
        self.Position = position
        self.Color = color
        self.Size = size
        self.Font = font

        self.Visible = True

        Text.TEXT_LIST.append(self)
