from .Event       import *
from .Application import *
from .KeyEvent    import *
from .MouseEvent  import *

PHOTON_EVENTSYSTEM_VERSION: tuple = (1,0,0)
PHOTON_EVENTSYSTEM_VERSION_STR: str = ".".join(
    [str(s) for s in PHOTON_EVENTSYSTEM_VERSION]
)
