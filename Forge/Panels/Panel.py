from Photon import *

from .Events import *

class Panel:
    _EventDispatcher: EventDispatcher
    _EventPropogator: Callable[[Event], bool]
    
    def __init__(self, eventHandler: EventDispatcher, eventPropogator: Callable[[Event], bool]) -> None:
        self._EventDispatcher = eventHandler
        self._EventPropogator = eventPropogator
        
    def OnGUIRender(self) -> None: ...
