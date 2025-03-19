from Photon import *

from .Events import *

class Panel:
    _CommunicationLayer: CommunicationLayer
    
    def __init__(self, communicationLayer: CommunicationLayer) -> None:
        self._CommunicationLayer = communicationLayer
        
    def OnGUIRender(self) -> None: ...
