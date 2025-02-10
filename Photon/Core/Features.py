DEBUG: bool = True

CONFIG: str = "Debug"

LOGGING: bool = True
INSTUMENTATION: bool = True

class GraphicsLibraryENUM:
    Headless = 0
    OpenGL = 1
    
GRAPHICSLIBRARY: int = GraphicsLibraryENUM.OpenGL
VSYNC: bool = False
