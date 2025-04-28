from .Panel import *

class Console(Panel):
    def __init__(self, communicationLayer: CommunicationLayer)  ->  None:
        super().__init__(communicationLayer)
        
    def OnGUIRender(self) -> None:
        with imgui_ctx.begin("Console"):
            pass
