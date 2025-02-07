from .Components import CTV

import esper
from typing import Type, Any, List, Tuple

class EntityRegistry():
    _World: esper.World
    
    def __init__(self):
        self._World = esper.World()

    def CreateEntity(self) -> int:
        return self._World.create_entity()

    def DeleteEntity(self, entity: int, immediate: bool = False) -> None:
        self._World.delete_entity(entity, immediate)

    def AddComponent(self, entity: int, component_type: Type[CTV], *component_args: Any) -> None:
        self._World.add_component(entity, component_type(*component_args))
        
    def AddComponentInstance(self, entity: int, component: CTV) -> None:
        self._World.add_component(entity, component)

    def RemoveComponent(self, entity: int, component_type: Type[CTV]) -> None:
        self._World.remove_component(entity, component_type)

    def GetComponent(self, component_type: Type[Any]) -> List[Tuple[int, CTV]]:
        return self._World.get_component(component_type)

    def HasComponent(self, entity: int, component_type: Type[CTV]) -> bool:
        return self._World.has_component(entity, component_type)

    def GetEntities(self) -> List[int]:
        return list(self._World._entities.keys())
    
    def ComponentsForEntity(self, entity: int) -> Tuple[CTV, ...]:
        return tuple(self._World.components_for_entity(entity))
    
    def ComponentForEntity(self, entity: int, component: Type[CTV]) -> CTV:
        return self._World.component_for_entity(entity, component)
