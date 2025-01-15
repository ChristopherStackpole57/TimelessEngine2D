from Engine.Scenes.Scene import Scene

# Scene Manager is a top level singleton
class SceneManager:
    CurrentScene = Scene()

    @staticmethod
    def SetCurrentScene(scene):
        SceneManager.CurrentScene = scene