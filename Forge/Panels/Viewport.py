from .Panel import *

class Viewport(Panel):
    __Texture: Texture
    
    def __init__(self, communicationLayer: CommunicationLayer) -> None:
        super().__init__(communicationLayer) 
        self.__Texture = LoadImageAsTexture(Path("Resources/moon.jpg"))
    
    def OnGUIRender(self) -> None:
        with imgui_ctx.begin("Viewport"):
            imgui.image(self.__Texture.RendererID, self.__Texture.Dimension)
