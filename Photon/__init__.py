from .Application     import *
from .ECS             import *
from .Events          import *
from .FileManager     import *
from .Instrumentation import *
from .Layers          import *
from .Logging         import *
from .Project         import *
from .Scene           import *

from pathlib import Path

from .Core.Version import PHOTON_VERSION
CoreLogger.Debug("Version: {}", PHOTON_VERSION)
