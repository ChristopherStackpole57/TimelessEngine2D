import sys
import time

import pygame

from Engine.Datatypes.Color import Color
from Engine.Datatypes.Vector2 import Vector2
from Engine.Input.InputManager import InputManager
from Engine.Physics.Collisions.CollisionManager import CollisionManager
from Engine.Physics.Physics import PhysicsStep, SetGravity
from Engine.Render.Render import Renderer
from Engine.Scenes.SceneManager import SceneManager

pygame.init()
pygame.font.init()

def main():
    SetGravity(Vector2(0, -20))

    SceneManager.CurrentScene.BackgroundColor = Color(41, 37, 37)

    CollisionManager.CreateCellList(Renderer.SCREEN_SIZE)
    CollisionManager.CreateTileList(SceneManager.CurrentScene.ActorList)
    CollisionManager.AddTilesToCells()

    previous_time = time.time_ns()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            InputManager.ProcessInput(event)

        # Render Loop and Physics

        current_time = time.time_ns()
        delta_time = current_time - previous_time

        PhysicsStep(delta_time / 100_000)
        Renderer.RenderFrame()

        previous_time = current_time

# Driver Code
main()
sys.exit()