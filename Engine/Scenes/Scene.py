from Engine.Datatypes.Color import Color
from Engine.Physics.Collisions.CollisionManager import CollisionManager

class Scene:
    def AddActor(self, actor):
        self.ActorList.append(actor)

    def RequestRemoveActor(self, actor) -> bool:
        # Process for removing an object is as follows:
        # See if it is in the actor list, if so:
        # Remove it from the actor list
        # At this point it still exists in the CollisionManager's tile list
        # Reload the CollisionManager's tiles

        if actor in self.ActorList:
            self.ActorList.remove(actor)
            CollisionManager.CreateTileList(self.ActorList)
            CollisionManager.RefreshCellTiles()

            return True

        return False

    def __init__(self, color: Color = Color()):
        self.ActorList = []
        self.BackgroundColor = color