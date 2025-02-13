from .Panel import *

class Properties(Panel):
    _Context: Entity | None
    
    def __init__(self, eventHandler: EventDispatcher, eventPropogator: Callable[[Event], bool])  ->  None:
        super().__init__(eventHandler, eventPropogator)
        eventHandler.AddHandler(PanelEventTypes.EntitySelected, self.OnEntitySelected)  # type: ignore
        
        self._Context = None
    
    def OnEntitySelected(self, entitySelectedEvent: EntitySelectedEvent) -> bool:
        self._Context = entitySelectedEvent.SelectedEntity
        return False
    
    def OnGUIRender(self) -> None:
        with imgui.begin("Properties"):
            if not self._Context: return
            
            tag = self._Context.GetComponent(TagComponent).Tag
            _, self._Context.GetComponent(TagComponent).Tag = imgui.input_text("##Tag", tag, 256)