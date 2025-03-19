from ..Events import *

class CommunicationLayer:
    __EventDispatcher: EventDispatcher
    
    def __init__(self) -> None:
        self.__EventDispatcher = EventDispatcher()
        
    def Subscribe(self, eventType: int, listener: Callable[[Event], bool]) -> None:
        self.__EventDispatcher.AddHandler(eventType, listener) # type: ignore
        
    def PublishEvent(self, event: Event) -> bool:
        return self.__EventDispatcher.Dispatch(event)
        
