import uuid

from Engine.Input.InputAction import InputAction

class InputMap:
    def BindActionToUnicode(self, ku: int, action: InputAction):
        self.Binds[ku] = action

    def BindActionToMouse(self, mb: int, action: InputAction):
        self.MouseBinds[mb] = action

    def BindActionToMouseMovement(self, action: InputAction):
        self.MouseMovement.append(action)

    def __init__(self):
        self.UUID = uuid.uuid4()
        self.Binds = {}
        self.MouseBinds = {}
        self.MouseMovement = []
        self.Active = True