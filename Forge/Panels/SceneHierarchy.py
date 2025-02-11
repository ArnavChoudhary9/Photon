from .Panel import *

class SceneHierarchy(Panel):
    def __init__(self, eventHandler: EventDispatcher, eventPropogator: Callable[[Event], bool])  ->  None:
        super().__init__(eventHandler, eventPropogator)
        
    def OnGUIRender(self) -> None:
        with imgui.begin("Scene Hierarchy"):
            pass
