from .Panel import *

class DebugProperties(Panel):
    def __init__(self, eventHandler: EventDispatcher, eventPropogator: Callable[[Event], bool])  ->  None:
        super().__init__(eventHandler, eventPropogator)
        
    def OnGUIRender(self) -> None:
        with imgui.begin("Debug Properties"):
            pass
