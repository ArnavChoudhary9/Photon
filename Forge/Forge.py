from Photon import *

class Forge(PhotonApplication):
    def OnStart(self) -> None:
        ClientLoggers.Info("Test")
        
        # Test loading an asset
        self.AssetPath = Path("Test.asset")
        with FileReader(self.AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode())
    
    def OnUpdate(self, dt: float) -> None:
        ClientLoggers.Info("In User teritory")
        self.Close()
        
    def OnEnd(self) -> None:
        # This time we will not see a "Loading Resource" massage
        with FileReader(self.AssetPath) as file:
            ClientLoggers.Trace(file.Read().decode())

if __name__ == "__main__":
    Main()
