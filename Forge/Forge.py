from Photon import *

class Forge(PhotonApplication):
    def OnStart(self) -> None: pass
    
    def OnUpdate(self, dt: float) -> None:
        print("In User teritory")
        self.Close()
        
    def OnEnd(self) -> None: pass

if __name__ == "__main__":
    Main()
