import pygame.display

from typing import Tuple

from Engine.BaseClasses.Text import Text
from Engine.Datatypes.Vector2 import Vector2
from Engine.Datatypes.Color import Color
from Engine.Render.RenderType import RenderType
from Engine.Scenes.SceneManager import SceneManager

class Renderer:
    SCREEN_SIZE: Tuple[int or float] = (1280, 960)
    DRAW_SURFACE = pygame.display.set_mode(SCREEN_SIZE, pygame.SRCALPHA)

    @staticmethod
    def RenderFrame():
        current_scene = SceneManager.CurrentScene
        Renderer.DRAW_SURFACE.fill(tuple(current_scene.BackgroundColor))

        for object in current_scene.ActorList:
            # Flip Y Axis
            # Position on X Axi is Already Handled, Don't Need To Double It
            object_pos = Vector2(0, Renderer.SCREEN_SIZE[1] - object.Size.Y - object.Position.Y)

            if object.RenderType == RenderType.PRIMITIVE:
                modified_vertices = []
                for point in object.Vertices:
                    modified_point = Vector2(point.X, Renderer.SCREEN_SIZE[1] - point.Y) #+ object_pos
                    modified_vertices.append(tuple(modified_point))

                pygame.draw.polygon(
                    Renderer.DRAW_SURFACE,
                    tuple(object.Color),
                    modified_vertices
                )

            elif object.RenderType == RenderType.SPRITE:
                # TODO: Faster to load all bitmaps into one sprite_surface then blit that?
                # TODO: Scale bitmap based on sprite size

                sprite_surface = pygame.image.load(object.Sprite.Source).convert_alpha()
                transformed_surface = pygame.transform.smoothscale(sprite_surface, tuple(object.Sprite.Size))

                Renderer.DRAW_SURFACE.blit(
                    transformed_surface,
                    tuple(Vector2(object.Position.X - object.Size.X / 2, object.Size.Y / 2) + object_pos)
                )

        for text in Text.TEXT_LIST:
            if text.Visible:
                # TODO: Is making a new font everytime slow?
                font = pygame.font.SysFont(text.Font, text.Size)
                text_surface = font.render(text.Text, True, tuple(text.Color))

                Renderer.DRAW_SURFACE.blit(
                    text_surface,
                    tuple(text.Position - Vector2(
                        text_surface.get_size()[0] / 2,
                        text_surface.get_size()[1] / 2)
                    )
                )

        pygame.display.flip()