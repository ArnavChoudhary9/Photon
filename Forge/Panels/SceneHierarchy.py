from .Panel import *
from .Events import *

class SceneHierarchy(Panel):
    __Context: Scene | None
    __SelectionContext: Entity | None

    def __init__(self, communicationLayer: CommunicationLayer)  ->  None:
        super().__init__(communicationLayer)
        communicationLayer.Subscribe(PanelEventTypes.SceneContextChanged, self.SceneContextChanged) # type: ignore
        
        self.__Context = None
        self.__SelectionContext = None
    
    def SceneContextChanged(self, sceneContextChangedEvent: SceneContextChangedEvent) -> bool:
        self.__Context = sceneContextChangedEvent.NewContext
        return False
    
    def OnGUIRender(self) -> None:
        with imgui.begin("Scene Hierarchy"):
            if not self.__Context: return
            
            for entity in self.__Context.Entities: self.__DrawEntityNode(entity)
            if imgui.is_mouse_down(0) and imgui.is_window_hovered(): 
                self.ChangeSelectionContext(None)

            if imgui.begin_popup_context_window(popup_flags=imgui.POPUP_NO_OPEN_OVER_ITEMS|imgui.POPUP_MOUSE_BUTTON_RIGHT):
                if imgui.begin_menu("Create Entity"):
                    if imgui.menu_item("Empty Entity")[0]: self.__Context.CreateEntity("Empty Entity") # type: ignore
                    imgui.end_menu()

                imgui.end_popup()

    def ChangeSelectionContext(self, selectionContext: Entity | None) -> None:
        self.__SelectionContext = selectionContext
        self._CommunicationLayer.PublishEvent(EntitySelectedEvent(selectionContext))

    def __DrawEntityNode(self, entity: Entity) -> None:
        tag = entity.GetComponent(TagComponent)
        
        flags = 0
        if self.__SelectionContext == entity: flags |= imgui.TREE_NODE_SELECTED
        flags |= imgui.TREE_NODE_OPEN_ON_ARROW | imgui.TREE_NODE_SPAN_AVAILABLE_WIDTH
    
        # Adding this to make each entity unique
        # NOTE: int(entity) retrives its __EntityHandle
        opened = imgui.tree_node(str(tag) + f"##{int(entity)}", flags)
        if imgui.is_item_clicked(): self.ChangeSelectionContext(entity)
        
        if imgui.begin_popup_context_item():
            if imgui.menu_item("Duplicate Entity")[0]: self.__Context.DefferedDuplicateEntity(entity) # type: ignore
            if imgui.menu_item("Delete Entity")[0]: # type: ignore
                self.__Context.DestroyEntity(entity) # type: ignore
                if self.__SelectionContext == entity:
                    self.ChangeSelectionContext(None)
            imgui.end_popup()
        
        if opened: imgui.tree_pop()
