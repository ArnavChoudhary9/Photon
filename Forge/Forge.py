from Photon import *

class Forge(PhotonApplication):
    def OnUpdate(self, dt: float) -> None:
        print("In User teritory")
        self.Close()

if __name__ == "__main__":
    Main()
