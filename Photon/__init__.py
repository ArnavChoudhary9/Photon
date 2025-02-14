from .Application     import *
from .ECS             import *
from .Events          import *
from .FileManager     import *
from .GraphicsEngine  import *
from .GUI             import *
from .Input           import *
from .Instrumentation import *
from .Layers          import *
from .Logging         import *
from .Project         import *
from .Scene           import *

from pathlib import Path
from OpenGL.GL import * # type: ignore

import imgui
ImVec2 = imgui.Vec2 # type: ignore
ImVec4 = imgui.Vec4 # type: ignore

from .Core.Version import PHOTON_VERSION
CoreLogger.Debug("Version: {}", PHOTON_VERSION)
