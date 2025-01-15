from Engine.Datatypes.Vector2 import Vector2
from Engine.Physics.Collisions.CollisionData import CollisionData

# Using Class Model to Organize Collision Functions
class CF_AABB:
    @staticmethod
    def C_AABB(object, tile) -> CollisionData:
        o_aabb = object.AABB
        t_aabb = tile.AABB

        # Test X axis
        # TODO: Should probably change the halfwidths to be int/float instead of vectors because we know they are aligned to the X - Y axes
        x_dist = abs(t_aabb.Position.X - o_aabb.Position.X)
        if x_dist > o_aabb.HalfwidthX.X + t_aabb.HalfwidthX.X:
            # Does not overlap on the x axis, stop check
            return CollisionData(False)

        y_dist = abs(t_aabb.Position.Y - o_aabb.Position.Y)
        if y_dist > o_aabb.HalfwidthY.Y + t_aabb.HalfwidthY.Y:
            # Does not overlap in the y axis, stop check
            return CollisionData(False)

        x_overlap = (o_aabb.HalfwidthX + t_aabb.HalfwidthX).X - abs(o_aabb.Position.X - t_aabb.Position.X)
        y_overlap = (o_aabb.HalfwidthY + t_aabb.HalfwidthY).Y - abs(o_aabb.Position.Y - t_aabb.Position.Y)

        x_axis = 1
        if object.Position.X < tile.Position.X:
            x_axis = -1

        y_axis = 1
        if object.Position.Y < tile.Position.Y:
            y_axis = -1

        #print("Overlaps: ", x_overlap, " ", y_overlap)
        return CollisionData(
            True,
            [Vector2(x_axis, 0), x_overlap],
            [Vector2(0, y_axis), y_overlap],
        )

    @staticmethod
    def C_Triangle(object, tile):
        pass

    @staticmethod
    def C_Circle(object, tile):
        pass

CollisionFunctions = [
    [   # AABBs
        CF_AABB.C_AABB
    ],
    [   # Triangles

    ],
    [   # Circles

    ]
]