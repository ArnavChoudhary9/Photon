from .Components import CTV, SupportsComponents

import esper
from typing import Type, Any, List, Tuple, Callable

class EntityRegistry():
    _World: esper.World
    
    __ComponentAddedFunction   : Callable[[Any, SupportsComponents], None]
    __ComponentRemovedFunction : Callable[[Any, Type[SupportsComponents]], None]
    
    def __init__(
        self,
        componentAddedFunction   : Callable[[Any, SupportsComponents], None],
        componentRemovedFunction : Callable[[Any, Type[SupportsComponents]], None]
    ) -> None:
        self._World = esper.World()
        
        self.__ComponentAddedFunction   = componentAddedFunction
        self.__ComponentRemovedFunction = componentRemovedFunction

    @property
    def NextEntityID(self) -> int:
        return self._World._next_entity_id
    
    def Exists(self, entity: int) -> bool:
        return self._World.entity_exists(entity)

    def CreateEntity(self) -> int:
        return self._World.create_entity()

    def DeleteEntity(self, entity: int, immediate: bool = False) -> None:
        self._World.delete_entity(entity, immediate)

    def AddComponent(self, entity: int, component_type: Type[CTV], *component_args: Any) -> None:
        self.AddComponentInstance(entity, component_type(*component_args))
        
    def AddComponentInstance(self, entity: int, component: CTV) -> None:
        self.__ComponentAddedFunction(entity, component)
        self._World.add_component(entity, component)

    def RemoveComponent(self, entity: int, component_type: Type[CTV]) -> None:
        self._World.remove_component(entity, component_type)
        self.__ComponentRemovedFunction(entity, component_type)

    def GetComponent(self, component_type: Type[Any]) -> List[Tuple[int, CTV]]:
        return self._World.get_component(component_type)

    def HasComponent(self, entity: int, component_type: Type[CTV]) -> bool:
        return self._World.has_component(entity, component_type)

    def GetEntities(self) -> List[int]:
        return list(self._World._entities.keys())
    
    def GetEntitiesForComponent(self, component: Type[CTV]) -> List[int]:
        return [entity for entity, comp in self._World.get_component(component) if comp == component]
    
    def GetEntityForComponent(self, component: Type[CTV]) -> int:
        entities = self.GetEntitiesForComponent(component)
        return entities[0] if len(entities) > 0 else -1
    
    def ComponentsForEntity(self, entity: int) -> Tuple[CTV, ...]:
        return tuple(self._World.components_for_entity(entity))
    
    def ComponentForEntity(self, entity: int, component: Type[CTV]) -> CTV:
        return self._World.component_for_entity(entity, component)
