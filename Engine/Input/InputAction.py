import uuid

from typing import Callable

class InputAction:
    def __init__(self, ku: int = None, action: Callable = None):
        self.KeyUnicode = ku
        self.Action = action
        self.UUID = uuid.uuid4()