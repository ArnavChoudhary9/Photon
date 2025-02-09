from Photon import *

class EditorLayer(Overlay):
    __AssetPath: Path
    __CurrentScene: Scene
    __CurrentProject: Project
    
    def OnInitialize(self):
        self.__CurrentProject = Project(Path("DefaultProject"), "DefaultProject")
        
        # Test loading an asset
        self.__AssetPath = Path("Test.asset")
        with FileReader(self.__AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode()) # type: ignore
    
    def OnStart(self):
        ClientLoggers.Info("Test")
        
    def OnUpdate(self, dt: float):
        ClientLoggers.Info("EditorLayer::OnUpdate")
    
    def OnStop(self):
        # This time we will not see a "Loading Resource" massage
        with FileReader(self.__AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode()) # type: ignore
        
        self.__CurrentProject.Save()
    
    def OnDestroy(self): ...
    
    def OnGUIStart(self): ...
    def OnGUIRender(self): ...
    def OnGUIEnd(self): ...    
