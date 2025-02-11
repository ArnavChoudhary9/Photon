from Photon.Events import *

class PanelEventTypes:
    EntitySelected: int = 101

class PanelEvent(Event):
    def __init__(self) -> None: ...
    
    @property
    def CategoryFlags(self) -> int: return EventCategory.UserDefined

class EntitySelectedEvent(PanelEvent):
    _SelectedEntityID: int
    
    def __init__(self, entityId: int) -> None: self._SelectedEntityID = entityId  

    @property
    def SelectedEntityID(self) -> int: return self._SelectedEntityID
    
    @property
    def EventType(self) -> int: return PanelEventTypes.EntitySelected
    def ToString(self) -> str: return "<EntitySelectedEvent: {}>".format(self._SelectedEntityID)
