from Photon import *

class EditorLayer(Overlay):
    AssetPath: Path
    
    def OnInitialize(self):
        # Test loading an asset
        self.AssetPath = Path("Test.asset")
        with FileReader(self.AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode()) # type: ignore
    
    def OnStart(self):
        ClientLoggers.Info("Test")
        
    def OnUpdate(self, dt: float):
        ClientLoggers.Info("EditorLayer::OnUpdate")
    
    def OnStop(self):
        # This time we will not see a "Loading Resource" massage
        with FileReader(self.AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode()) # type: ignore
    
    def OnDestroy(self): ...
    
    def OnGUIStart(self): ...
    def OnGUIRender(self): ...
    def OnGUIEnd(self): ...    
