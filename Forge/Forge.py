from Photon import *

class Forge(PhotonApplication):
    def OnStart(self) -> None:
        ClientLoggers.Info("Test")
    
    def OnUpdate(self, dt: float) -> None:
        ClientLoggers.Info("In User teritory")
        self.Close()
        
    def OnEnd(self) -> None: pass

if __name__ == "__main__":
    Main()
