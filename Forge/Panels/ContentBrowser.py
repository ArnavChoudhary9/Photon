from .Panel import *

class ContentBrowser(Panel):
    def __init__(self, communicationLayer: CommunicationLayer)  ->  None:
        super().__init__(communicationLayer)
        
    def OnGUIRender(self) -> None:
        with imgui.begin("Content Browser"):
            pass