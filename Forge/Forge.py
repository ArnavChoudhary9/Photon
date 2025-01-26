from Photon import *

from EditorLayer import *

class Forge(PhotonApplication):
    def OnStart(self) -> None:        
        self._LayerStack.AddOverlay(EditorLayer())
    
    def OnUpdate(self, dt: float) -> None:
        ClientLoggers.Info("In User teritory")
        self.OnEvent(WindowCloseEvent())
        
    def OnEnd(self) -> None: ...

if __name__ == "__main__":
    Main()
