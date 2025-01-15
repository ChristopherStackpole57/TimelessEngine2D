import uuid

import pygame

from Engine.Input.InputAction import InputAction
from Engine.Input.InputMap import InputMap

class InputManagerBase:
    def NewInputAction(self, ku: int, action: InputAction):
        action = InputAction(ku, action)
        self.Actions.append(action)

        return action.UUID

    def NewInputMap(self):
        map = InputMap()
        self.Maps.append(map)

        return map.UUID

    def GetAction(self, id: uuid.UUID):
        for action in self.Actions:
            if action.UUID == id:
                return action

    def GetMap(self, id: uuid.UUID):
        for map in self.Maps:
            if map.UUID == id:
                return map

    def ProcessInput(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            unicode = event.key
            for map in self.Maps:
                if unicode in map.Binds.keys() and map.Active:
                    map.Binds[unicode](int(event.type == pygame.KEYDOWN))

        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mb = event.button
            for map in self.Maps:
                if mb in map.MouseBinds.keys():
                    map.MouseBinds[mb](int(event.type == pygame.MOUSEBUTTONDOWN), event.pos)

        elif event.type == pygame.MOUSEMOTION:
            for map in self.Maps:
                if len(map.MouseMovement) > 0:
                    for handler in map.MouseMovement:
                        handler(event.pos, event.rel, event.buttons)

    def __init__(self):
        self.Actions = []
        self.Maps = []

InputManager = InputManagerBase()