from .Panel import *

class Viewport(Panel):
    __Texture: Texture
    
    def __init__(self, eventHandler: EventDispatcher, eventPropogator: Callable[[Event], bool]) -> None:
        super().__init__(eventHandler, eventPropogator) 
        self.__Texture = LoadImageAsTexture(Path("Resources/moon.jpg"))
    
    def OnGUIRender(self) -> None:
        with imgui.begin("Viewport"):
            imgui.image(self.__Texture.RendererID, *self.__Texture.Dimension)
