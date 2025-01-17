from ..Core import Features
from ..Logging import *
from ..Layers import *

from abc import ABC, abstractmethod
from typing import Type
import sys, inspect

class PhotonApplication(ABC):
    _Running: bool
    _LayerStack: LayerStack
    
    def __init__(self) -> None:
        self._Running = True
        self._LayerStack = LayerStack()
    
    @abstractmethod 
    def OnStart(self) -> None: ...
    @abstractmethod 
    def OnUpdate(self, dt: float) -> None: ...
    @abstractmethod 
    def OnEnd(self, dt: float) -> None: ...
    
    def OnEvent(self, event: Event):
        self._LayerStack.OnEvent(event)
    
    def Run(self) -> None:
        self.OnStart()
        self._LayerStack.OnStart()
        
        while self._Running:
            self._LayerStack.OnUpdate(0)
            
            # Handle user input, draw ImGui, etc.
            self.OnUpdate(0)
        
        self._LayerStack.OnStop()
        self.OnEnd()
            
    def Close(self) -> None: self._Running = False

def FindSubclass() -> Type[PhotonApplication]:
    """Find a subclass of Application dynamically."""
    for name, obj in inspect.getmembers(sys.modules["__main__"]):
        if inspect.isclass(obj) and issubclass(obj, PhotonApplication) and obj is not PhotonApplication:
            return obj
    raise RuntimeError("No subclass of Application found in the main module.")

def AppRunner() -> None:
    # InstrumentorObj.BeginSession("Asura_Initialization")
    subclass: Type[PhotonApplication] = FindSubclass()
    ClientLoggers.Subscribe(Logger(subclass.__name__))
    
    try: app = subclass()
    except Exception as e:
        print("Cannot initialize the application.", e, sep="\n")
        return
    # InstrumentorObj.EndSession()

    # InstrumentorObj.BeginSession("Asura_Runtime")
    try: app.Run()
    except Exception as e:
        print("An error occurred while running the application.", e, sep="\n")
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
    stats.dump_stats(filename="DetailedProfile.prof")   # The user gets the profiler output
