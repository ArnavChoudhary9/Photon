from .Panel import *

class ComponentDrawer:
    @staticmethod
    def Transform(entity: Entity, component: TransformComponent) -> None:
        changedT, newT = GUILibrary.DrawVector3Controls(
            "Transform", component.Translation
        )
        changedR, newR = GUILibrary.DrawVector3Controls(
            "Rotation", component.Rotation,
            resetValues = pyrr.Vector3([0.0, 0.0, 0.0]), speed = 0.5
        )
        changedS, newS = GUILibrary.DrawVector3Controls(
            "Scale", component.Scale,
            resetValues = pyrr.Vector3([1.0, 1.0, 1.0])
        )

        if changedT or changedR or changedS:
            component.SetTranslation(newT)
            component.SetRotation(newR)
            component.SetScale(newS)

class Properties(Panel):
    _Context: Entity | None
    
    def __init__(self, communicationLayer: CommunicationLayer)  ->  None:
        super().__init__(communicationLayer)
        communicationLayer.Subscribe(PanelEventTypes.EntitySelected, self.OnEntitySelected)  # type: ignore
        
        self._Context = None
    
    def OnEntitySelected(self, entitySelectedEvent: EntitySelectedEvent) -> bool:
        self._Context = entitySelectedEvent.SelectedEntity
        return False
    
    def OnGUIRender(self) -> None:
        with imgui.begin("Properties"):
            if not self._Context: return
            
            tag = self._Context.GetComponent(TagComponent).Tag
            _, self._Context.GetComponent(TagComponent).Tag = imgui.input_text("##Tag", tag, 256)
            
            imgui.same_line()
            imgui.push_item_width(-1)
            
            if imgui.button("Add Component"): imgui.open_popup("AddComponent")
            
            if imgui.begin_popup("AddComponent"):
                imgui.end_popup()
            
            imgui.pop_item_width()
            
            self.DrawComponent( "Transform" , self._Context , TransformComponent , ComponentDrawer.Transform )
        
    def DrawComponent(
        self, name: str, entity: Entity, componentType: Type[CTV], UIFunction: Callable[[Entity, CTV], None]
    ) -> None:
        if not entity.HasComponent(componentType): return
        
        flags  = imgui.TREE_NODE_DEFAULT_OPEN
        flags |= imgui.TREE_NODE_FRAMED
        flags |= imgui.TREE_NODE_SPAN_AVAILABLE_WIDTH
        flags |= imgui.TREE_NODE_ALLOW_ITEM_OVERLAP
        flags |= imgui.TREE_NODE_FRAME_PADDING
        
        component = entity.GetComponent(componentType)
        contentRegionAvailable = imgui.get_content_region_available()

        imgui.push_style_var(imgui.STYLE_FRAME_PADDING, (4, 4))
        lineHeight = 26
        imgui.separator()
        isOpen = imgui.tree_node(name, flags)
        imgui.pop_style_var()

        imgui.same_line(contentRegionAvailable[0] - lineHeight * 0.5)
        if imgui.button("+", lineHeight, lineHeight): imgui.open_popup("ComponentSettings")

        removeComponent = False
        if imgui.begin_popup("ComponentSettings"):
            imgui.end_popup()
            
        if isOpen:
            UIFunction(entity, component) # type: ignore
            imgui.tree_pop()

        # Note you will be able to paste the component even after the original is deleted
        if removeComponent: entity.RemoveComponent(componentType)
