from typing import Callable, Dict, Protocol, TypeVar, List

# This just shifts 1 to i th BIT
def BIT(i: int) -> int:
    return int(1 << i)

# This class is equvalent to a C++ enum
class EventType:
    Null,                                                                   \
    WindowClose, WindowResize, WindowFocus, WindowMoved,                    \
    AppTick, AppUpdate, AppRender,                                          \
    KeyPressed, KeyReleased, CharInput,                                     \
    MouseButtonPressed, MouseButtonReleased, MouseMoved, MouseScrolled      \
        = range(0, 15)

# This class is equvalent to a C++ enum

# It uses bitstream to represent flags, so
# a single Event can have multiple flags
class EventCategory:
    Null = 0
    Application    = BIT(0)
    Input          = BIT(1)
    Keyboard       = BIT(2)
    Mouse          = BIT(3)
    MouseButton    = BIT(4)
    
    UserDefined = BIT(5)

class Event:
    Handled = False

    @property
    def EventType(self) -> int: return EventType.Null
    @property
    def Name(self) -> str: return str(type(self))
    @property
    def CategoryFlags(self) -> int: return EventCategory.Null

    def ToString(self) -> str: return self.Name
    def IsInCategory(self, category: int) -> bool: return bool(self.CategoryFlags & category)
    def __repr__(self) -> str: return self.ToString()

class SupportsEvents(Protocol):
    @property
    def EventType(self) -> int: ...
    @property
    def CategoryFlags(self) -> int: ...

_T = TypeVar("_T", bound=SupportsEvents)

class EventDispatcher:
    __Map: Dict[int, Callable[[SupportsEvents], bool] | List[Callable[[SupportsEvents], bool]]]

    @staticmethod
    # Just a placeholder function if nothing matches
    # C005 (See GeneralConventions.txt)
    def DoNothing(_: SupportsEvents) -> bool: return False

    def __init__(self) -> None:
        self.__Map = {}

    def AddHandler(self, eventType: int, handler: Callable[[SupportsEvents], bool]) -> None:
        handlers = self.__Map.get(eventType, False)
        if not handlers:
            self.__Map[eventType] = handler
            return
        
        if isinstance(handlers, list):
            handlers.append(handler)
            return
        
        self.__Map[eventType] = [handlers, handler]  # type: ignore

    def Dispatch(self, event: Event) -> bool:
        handler = self.__Map.get(event.EventType, EventDispatcher.DoNothing)
        
        if isinstance(handler, list):
            for handler in handler:
                if handler(event): return True
            return False
        
        return handler(event)
