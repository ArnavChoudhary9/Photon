from ..Core import Features
from ..Logging import *
from ..Events import *
from ..Layers import *
from ..FileManager import FileManager
from ..Instrumentation import *
from ..GraphicsEngine import *
from ..GUI import GUIInitializer

from abc import ABC, abstractmethod
from typing import Type
import sys, inspect

class PhotonApplication(ABC):
    _Running: bool
    _LayerStack: LayerStack
    _EventDispatcher: EventDispatcher
    _Window: Window
    
    _LastUpdateTime: float
    _dt: float
    
    def __init__(self) -> None:
        self._Running = True
        self._LayerStack = LayerStack()
        
        self._EventDispatcher = EventDispatcher()
        self._EventDispatcher.AddHandler(EventType.WindowClose, self.CloseEventHandler)
        
        winProps = WindowProperties(self.__class__.__name__)
        winProps.Width = 1280
        winProps.Height = 720
        winProps.EventCallback = self.OnEvent
        
        self._Window = Window(winProps)
        self._LayerStack.AddOverlay(GUIInitializer(self._Window))
        
        self._LastUpdateTime = Time.PerfCounter()
        self._dt = 1/60
    
    @abstractmethod 
    def OnStart(self) -> None: ...
    @abstractmethod 
    def OnUpdate(self, dt: float) -> None: ...
    @abstractmethod 
    def OnEnd(self) -> None: ...
    
    def OnEvent(self, event: Event):
        if self._EventDispatcher.Dispatch(event): return
        self._LayerStack.OnEvent(event)
    
    def Run(self) -> None:
        appRun = Timer("Application::Run")
        
        self.OnStart()
        self._LayerStack.OnStart()
        
        while self._Running:
            tick = Timer("Application::Tick")
            
            self._dt = Time.PerfCounter() - self._LastUpdateTime
            self._LastUpdateTime = Time.PerfCounter()
            
            layerUpdate = Timer("Application::LayerUpdate")
            self._LayerStack.OnUpdate(self._dt)
            del layerUpdate
            
            userUpdate = Timer("Application::OnUpdate")
            self.OnUpdate(self._dt)
            del userUpdate
            
            guiRender = Timer("Application::GUIRender")
            self._LayerStack.OnGUIStart()
            self._LayerStack.OnGUIRender()
            self._LayerStack.OnGUIEnd()
            del guiRender
            
            windowUpdate = Timer("Application::WindowUpdate")
            self._Window.OnUpdate(self._dt)
            del windowUpdate
            
            del tick
        
        self._LayerStack.OnStop()
        self.OnEnd()
            
    def CloseEventHandler(self, windowCloseEvent: WindowCloseEvent) -> bool:
        windowCloseEvent.Handled = True
        self._Running = False
        return True

def FindSubclass() -> Type[PhotonApplication]:
    """Find a subclass of PhotonApplication dynamically."""
    for name, obj in inspect.getmembers(sys.modules["__main__"]):
        if inspect.isclass(obj) and issubclass(obj, PhotonApplication) and obj is not PhotonApplication:
            return obj
    raise RuntimeError("No subclass of Application found in the main module.")

def AppRunner() -> None:
    InstrumentorObj.BeginSession("ApplicationStartUp")
    
    startUp = Timer("AppRunner")
    subclass: Type[PhotonApplication] = FindSubclass()
    ClientLoggers.Subscribe(Logger(subclass.__name__))
    
    try: app = subclass()
    except Exception as e:
        print("Cannot initialize the application.", e, sep="\n")
        return
    
    del startUp
    InstrumentorObj.EndSession()

    InstrumentorObj.BeginSession("ApplicationRuntime")
    try: app.Run()
    except Exception as e:
        print("An error occurred while running the application.", e, sep="\n")
    InstrumentorObj.EndSession()

def Main() -> None:
    # Engine Start Up Code
    FileManager.INIT()
    
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
