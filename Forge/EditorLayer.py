from Photon import *

class EditorLayer(Overlay):
    __AssetPath: Path
    __CurrentScene: Scene
    __CurrentProject: Project
    
    __dt: float
    
    def OnInitialize(self):
        self.__CurrentProject = Project(Path("DefaultProject"), "DefaultProject")
        
        # Test loading an asset
        self.__AssetPath = Path("Test.asset")
        with FileReader(self.__AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode()) # type: ignore
            
        self.__dt = 0.0
    
    def OnStart(self):
        ClientLoggers.Info("Test")
        
    def OnUpdate(self, dt: float): self.__dt = dt
    
    def OnStop(self):
        # This time we will not see a "Loading Resource" massage
        with FileReader(self.__AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode()) # type: ignore
        
        self.__CurrentProject.Save()
    
    def OnDestroy(self): ...
    
    def OnGUIStart(self):
        # Hackey fix
        # TODO: Fix this later
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # type: ignore
        
    def OnGUIRender(self):
        with imgui.begin("Test"):
            imgui.text("Hello, world!")
            imgui.text(f"FPS: {round(1/self.__dt, 2)}")
            
    def OnGUIEnd(self): ...    
