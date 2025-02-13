from Photon.Events import *
from Photon.Scene import *

class PanelEventTypes:
    EntitySelected: int = 101
    SceneContextChanged: int = 102

class PanelEvent(Event):
    def __init__(self) -> None: ...
    
    @property
    def CategoryFlags(self) -> int: return EventCategory.UserDefined

class SceneContextChangedEvent(PanelEvent):
    _NewContext: Scene
    
    def __init__(self, newContext: Scene) -> None: self._NewContext = newContext
    
    @property
    def NewContext(self) -> Scene: return self._NewContext
    
    @property
    def EventType(self) -> int: return PanelEventTypes.SceneContextChanged
    def ToString(self) -> str: return "<SceneContextChanged: {}>".format(self._NewContext)

class EntitySelectedEvent(PanelEvent):
    _SelectedEntity: Entity | None
    
    def __init__(self, entity: Entity | None) -> None: self._SelectedEntity = entity

    @property
    def SelectedEntity(self) -> Entity | None: return self._SelectedEntity
    
    @property
    def EventType(self) -> int: return PanelEventTypes.EntitySelected
    def ToString(self) -> str:
        if not self._SelectedEntity: return "<EntitySelectedEvent: None>"
        return "<EntitySelectedEvent: {}>".format(
            self._SelectedEntity \
                .GetComponent(TagComponent).Tag
        )
