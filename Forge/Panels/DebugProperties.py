from .Panel import *

class DebugProperties(Panel):
    def __init__(self, communicationLayer: CommunicationLayer)  ->  None:
        super().__init__(communicationLayer)
        
    def OnGUIRender(self) -> None:
        with imgui.begin("Debug Properties"):
            pass
