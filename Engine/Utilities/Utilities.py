from typing import List

from Engine.Datatypes.Line import Line
from Engine.Datatypes.Vector2 import Vector2

def GetCenterOfVertices(vertices: List[Vector2]) -> Vector2:
    sum_x, sum_y = 0, 0
    for vertex in vertices:
        sum_x += vertex.X
        sum_y += vertex.Y

    return Vector2(sum_x / len(vertices), sum_y / len(vertices))

def GetBoundingSizeOfVertices(vertices: List[Vector2]) -> Vector2:
    min_x, min_y = vertices[0].X, vertices[0].Y
    max_x, max_y = vertices[0].X, vertices[0].Y

    for vertex in vertices:
        if vertex.X < min_x:
            min_x = vertex.X
        elif vertex.X > max_x:
            max_x = vertex.X

        if vertex.Y < min_y:
            min_y = vertex.Y
        elif vertex.Y > max_y:
            max_y = vertex.Y

    return Vector2(max_x - min_x, max_y - min_y)

def GetFacesFromVertices(vertices: List[Vector2]) -> List[Line]:
    faces = []

    for i in range(0, len(vertices)):
        faces.append(Line(
            vertices[i],
            vertices[(i + 1) % len(vertices)]
        ))

    return faces