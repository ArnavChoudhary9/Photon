from ..Core import Features

from abc import ABC, abstractmethod
import importlib.resources
import pkg_resources
from typing import Type
import sys, inspect

class PhotonApplication(ABC):
    _Running: bool
    
    def __init__(self) -> None:
        self._Running = True
    
    @abstractmethod 
    def OnUpdate(self, dt: float) -> None: ...
    
    def Run(self) -> None:
        while self._Running:
            # Handle user input, draw ImGui, etc.
            self.OnUpdate(0)
            
    def Close(self) -> None:
        self._Running = False

def FindSubclass() -> Type[PhotonApplication]:
    """Find a subclass of Application dynamically."""
    for name, obj in inspect.getmembers(sys.modules["__main__"]):
        if inspect.isclass(obj) and issubclass(obj, PhotonApplication) and obj is not PhotonApplication:
            return obj
    raise RuntimeError("No subclass of Application found in the main module.")

def AppRunner() -> None:
    # InstrumentorObj.BeginSession("Asura_Initialization")
    subclass: Type[PhotonApplication] = FindSubclass()
    
    try: app = subclass()
    except Exception as e:
        print("Cannot initialize the application.\n", e, sep="\n")
        return
    # InstrumentorObj.EndSession()

    # InstrumentorObj.BeginSession("Asura_Runtime")
    try: app.Run()
    except Exception as e:
        print("An error occurred while running the application.\n", e, sep="\n")
    # InstrumentorObj.EndSession()

def Main():
    if not Features.INSTUMENTATION:
        AppRunner()
        return
    
    # Code will enter here if INSTRUMENTATION is enabled
    # This will do some in-depth instrumentation of every function call made
    import cProfile
    import pstats

    with cProfile.Profile() as pr: AppRunner()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # importlib.resources.open_text("engine.data", filename)
    stats.dump_stats(filename="DetailedProfile.prof")   # The user gets the profiler output
