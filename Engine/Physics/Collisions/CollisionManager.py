# Use this resource
# https://www.metanetsoftware.com/technique/tutorialA.html

import math

from typing import List

from Engine.BaseClasses.AABB import AABB
from Engine.Physics.Collisions.Cell import Cell
from Engine.Physics.Collisions.CollisionFunctions import CollisionFunctions
from Engine.Physics.Collisions.Tile import Tile
from Engine.Physics.Enumerations.BodyType import BodyType
from Engine.Physics.Enumerations.TileType import TileType
from Engine.Utilities.Utilities import *

class CollisionManager:
    TILE_LIST = []
    CELL_LIST = []

    @staticmethod
    def CreateCellList(screen_size):
        # Width and Height of the Screen with a border on Top and Bottom

        width = math.ceil(screen_size[0] / Cell.CELL_SIZE) + 2
        height = math.ceil(screen_size[1] / Cell.CELL_SIZE) + 2

        for i in range(0, width):
            CollisionManager.CELL_LIST.append([])
            for j in range(0, height):
                # Quick Note about Cell Positioning
                # In the render code the Y - Axis is flipped so that it appears on the bottom of the screen instead of the top
                # This does not need to be reflected here, as the physics uses the original positions.

                cell = Cell(
                    (i - 1) * Cell.CELL_SIZE,
                    (j - 1) * Cell.CELL_SIZE
                )

                if not i == 0:
                    cell.L = CollisionManager.CELL_LIST[i - 1][j]
                    CollisionManager.CELL_LIST[i - 1][j].R = cell
                if not j == 0:
                    cell.B = CollisionManager.CELL_LIST[i][j - 1]
                    CollisionManager.CELL_LIST[i][j - 1].T = cell

                CollisionManager.CELL_LIST[i].append(cell)

    # TODO: Might be wiser to just pull the object list from scenemanager
    @staticmethod
    def CreateTileList(objects):
        CollisionManager.TILE_LIST = []
        for object in objects:
            # TODO: More than just static objects can be collidable, right?
            # TODO: Also this needs to handle more than just objects with AABBs
            if object.BodyType == BodyType.STATIC:
                tile = Tile(
                    TileType.AABB,
                    object,
                    AABB(object.Vertices)
                )

                CollisionManager.TILE_LIST.append(tile)

    @staticmethod
    def AddTilesToCells():
        for tile in CollisionManager.TILE_LIST:
            pos = GetCenterOfVertices(tile.Vertices)
            ti = math.floor(pos.X / Cell.CELL_SIZE) + 1
            tj = math.floor(pos.Y / Cell.CELL_SIZE) + 1

            CollisionManager.CELL_LIST[ti][tj].Tiles.append(tile)

    @staticmethod
    def RefreshCellTiles():
        for row in CollisionManager.CELL_LIST:
            for cell in row:
                cell.Tiles = []

        CollisionManager.AddTilesToCells()

    @staticmethod
    def BroadPhase(obj) -> List[Tile]:
        pos = GetCenterOfVertices(obj.Vertices)
        pos.Y = round(pos.Y)

        ci = int(pos.X // Cell.CELL_SIZE) + 1
        cj = int(pos.Y // Cell.CELL_SIZE) + 1

        current_cell = CollisionManager.CELL_LIST[ci][cj]

        overlap_cells = [current_cell]

        le_cx = pos.X <= current_cell.Center.X
        le_cy = pos.Y <= current_cell.Center.Y

        if le_cx:
            overlap_cells.append(current_cell.L)
        else:
            overlap_cells.append(current_cell.R)

        if le_cy:
            overlap_cells.append(current_cell.B)
        else:
            overlap_cells.append(current_cell.T)

        if le_cx and le_cy:
            overlap_cells.append(current_cell.L.B)
        elif le_cx and not le_cy:
            overlap_cells.append(current_cell.L.T)
        elif not le_cx and le_cy:
            overlap_cells.append(current_cell.R.B)
        elif not le_cx and not le_cy:
            overlap_cells.append(current_cell.R.T)

        # Determine Tilemap to Collide Against
        collision_list = []

        for cell in overlap_cells:
            collision_list.extend(cell.Tiles)

        return collision_list

    @staticmethod
    def NarrowPhase(obj, tiles) -> List[Vector2]:
        projection_vectors = []

        # This is where the collision functions get used
        for tile in tiles:
            collision_data = CollisionFunctions[int(obj.Type)][int(tile.Type)](obj, tile)

            if collision_data.Collides == True:
                min_axis = collision_data.UnitAxes[0][0]
                min_overlap = collision_data.UnitAxes[0][1]

                for axis in collision_data.UnitAxes:
                    if axis[1] < min_overlap:
                        min_axis = axis[0]
                        min_overlap = axis[1]

                proj_vector = min_axis * min_overlap
                projection_vectors.append(proj_vector)

                # obj here is a tile, so to look for collision responses we need get its object reference
                if not obj.ObjReference.OnCollide == None:
                    obj.ObjReference.OnCollide(tile)

                if not tile.ObjReference.OnCollide == None:
                    tile.ObjReference.OnCollide(obj)

        return projection_vectors

    @staticmethod
    def DetectCollision(obj, objects) -> List[Vector2]:
        adjacent_objects = CollisionManager.BroadPhase(obj)
        projection_vectors = CollisionManager.NarrowPhase(obj, adjacent_objects)

        return projection_vectors