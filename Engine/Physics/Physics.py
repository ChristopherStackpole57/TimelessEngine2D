from Engine.Datatypes.Vector2 import Vector2
from Engine.Physics.Collisions.CollisionManager import CollisionManager
from Engine.Physics.Collisions.Tile import Tile
from Engine.Physics.Enumerations.BodyType import BodyType
from Engine.Physics.Enumerations.FallingType import FallingType
from Engine.Physics.Enumerations.TileType import TileType
from Engine.Scenes.SceneManager import SceneManager

Gravity = Vector2(0, 0)

def SetGravity(gravity: Vector2):
    global Gravity
    Gravity = gravity

def PhysicsStep(delta_time: float):
    delta_time = delta_time / 1_000 # Converts from ms to second

    current_scene = SceneManager.CurrentScene
    actor_list = current_scene.ActorList

    for object in actor_list:
        obj_velocity = object.Velocity + object.InputVelocity

        if (not tuple(obj_velocity) == (0.0, 0.0) or not tuple(object.Acceleration + Gravity) == (0, 0)) and object.BodyType == BodyType.DYNAMIC:
            acceleration = object.Acceleration + Gravity

            dx = (0.5 * acceleration.X * (delta_time ** 2)) + (obj_velocity.X * delta_time)
            dy = (0.5 * acceleration.Y * (delta_time ** 2)) + (obj_velocity.Y * delta_time)

            new_pos = object.Position + Vector2(dx, dy)
            new_velo = Vector2(object.Velocity.X + acceleration.X * delta_time, object.Velocity.Y + acceleration.Y * delta_time)

            # TODO: Fix edge logic
            if new_pos.X - object.Size.X / 2 < 0:
                new_pos.X = object.Size.X / 2
            elif new_pos.X + object.Size.X / 2 >= 1280:
                new_pos.X = 1280 - object.Size.X / 2

            if new_pos.Y - object.Size.Y / 2 < 0:
                new_pos.Y = object.Size.Y / 2
                new_velo.Y = 0
            elif new_pos.Y + object.Size.Y / 2 >= 1280:
                new_pos.Y = 1280 - object.Size.Y
                new_velo.Y = 0

            # Falling State Adjustments
            if object.Velocity.Y > 0 and new_velo.Y == 0:
                # Hit Peak
                object.FallingState = FallingType.PEAK
            elif object.Velocity.Y >= 0 and new_velo.Y < -1:
                # Began Falling
                object.FallingState = FallingType.FALLING
            elif new_velo.Y < -1 and not object.FallingState == FallingType.FALLING:
                # TODO: This is a workaround, find better solution
                object.FallingState = FallingType.FALLING
            elif object.Velocity.Y < 0 and new_velo.Y == 0:
                # Hit Ground
                object.FallingState = FallingType.GROUNDED

            object.Position = new_pos
            object.Velocity = new_velo

        # TODO: Find better solution
        if object.BodyType == BodyType.DYNAMIC:
            projection_vectors = CollisionManager.DetectCollision(
                Tile(
                    TileType.AABB,
                    object,
                    object.AABB),
                actor_list)

            # TODO: Cannot guarantee that this will get player out of collision, find better solution
            for proj_vector in projection_vectors:
                object.Position += proj_vector

                # Set the object velocity in that direction to 0
                # To do this, find the projection of the velocity on that angle by multiplying the velocity by the cosine of the angle between it and the axis
                # To get the angle you divide the dot product by the magnitude of velocity and the axis

                # v * a = |v| |a| cos theta
                # (v * a) / (|v| |a|) = cos theta
                # Projection of v onto a = v cos theta

                # TODO: These values are slightly messed up, fix (start by checking cos theta)
                # TODO: I foresee issues here

                dot_prod = object.Velocity.Dot(-1 * proj_vector)
                magnitudes = (object.Velocity.Magnitude() * proj_vector.Magnitude())
                if not magnitudes == 0:
                    cos_theta = dot_prod / magnitudes
                    velocity_proj = object.Velocity * cos_theta
                    object.Velocity -= velocity_proj

                    if object.Velocity.Y == 0:
                        object.FallingState == FallingType.GROUNDED