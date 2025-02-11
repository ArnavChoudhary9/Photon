from Photon import *

from EditorLayer import *

class Forge(PhotonApplication):
    def OnStart(self) -> None:        
        self._LayerStack.AddOverlay(EditorLayer(self.OnEvent)) # type: ignore

    def OnUpdate(self, dt: float) -> None: ...

    def OnEnd(self) -> None: ...

if __name__ == "__main__":
    Main()
