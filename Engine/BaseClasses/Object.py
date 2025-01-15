from Engine.Datatypes.Color import Color
from Engine.Datatypes.Vector2 import Vector2
from Engine.Physics.Enumerations.BodyType import BodyType
from Engine.Physics.Enumerations.FallingType import FallingType
from Engine.Render.RenderType import RenderType
from Engine.Scenes.SceneManager import SceneManager

class Object(object):
    def GetVertices(self):
        if self.RenderType == RenderType.SPRITE:
            return NotImplemented

        return self.Vertices

    def __init__(self, position: Vector2 = Vector2(), size: Vector2 = Vector2(), color: Color = Color(), render_type: RenderType = RenderType.PRIMITIVE, data = None):
        self.Position = position
        self.Velocity = Vector2()
        self.InputVelocity = Vector2()
        self.Acceleration = Vector2()

        self.Size = size

        self.Color = color

        self.RenderType = render_type
        if self.RenderType == RenderType.SPRITE:
            self.Sprite = data
        elif self.RenderType == RenderType.PRIMITIVE:
            self.PrimitiveType = data

        self.BodyType = BodyType.DYNAMIC
        self.FallingState = FallingType.GROUNDED

        self.Vertices = []

        self.OnCollide = None

        SceneManager.CurrentScene.AddActor(self)