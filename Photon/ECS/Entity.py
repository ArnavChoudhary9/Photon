from ..Logging import ClientLoggers

from typing import Tuple
from typing import Type    as _Type

from .EntityRegistry import EntityRegistry
from .Components import IDComponent, TagComponent, TransformComponent, CTV

class Entity:
    __EntityHandle: int
    __EntityRegistry: EntityRegistry

    def __init__(self, entityHandle: int, entityRegistry: EntityRegistry) -> None:
        self.__EntityRegistry = entityRegistry
        self.__EntityHandle = entityHandle

    # This is just for deffered deletion/duplication
    def __hash__(self) -> int: return self.__EntityHandle

    @property
    def EntityRegistry(self) -> EntityRegistry: return self.__EntityRegistry
    @property
    def EntityHandle(self) -> int: return self.__EntityHandle

    @property
    def AllComponents(self) -> Tuple[CTV, ...]:
        return self.__EntityRegistry.ComponentsForEntity(self.__EntityHandle)
    
    def __int__(self) -> int: return self.__EntityHandle
    def __bool__(self) -> bool: return self.__EntityHandle != None

    def __eq__(self, other) -> bool:
        if not isinstance(other, Entity): return False
        return ((self.__EntityHandle == other.__EntityHandle) and (self.__EntityRegistry == other.__EntityRegistry))
    def __ne__(self, other) -> bool: return not (self == other)

    def HasComponent(self, componentType: _Type[CTV]) -> bool:
        return self.__EntityRegistry.HasComponent(self.__EntityHandle, componentType)
    
    def WarnIfHasComponent(self, componentType: _Type[CTV]) -> bool:
        if self.HasComponent(componentType):
            ClientLoggers.Error("Entity {} ({}) already has Component of type: {}", self, self.__EntityHandle, componentType)
            return True
        
        return False

    def GetComponent(self, componentType: _Type[CTV]) -> CTV:
        return self.__EntityRegistry.ComponentForEntity(self.__EntityHandle, componentType)

    def AddComponent(self, componentType: _Type[CTV], *args, **kwargs) -> CTV:
        if self.WarnIfHasComponent(componentType): return self.GetComponent(componentType)
        
        component = componentType(*args, **kwargs)
        self.__EntityRegistry.AddComponentInstance(self.__EntityHandle, component)
        return component
    
    def AddComponentInstance(self, component: CTV) -> None:
        if self.WarnIfHasComponent(type(component)): return

        self.__EntityRegistry.AddComponentInstance(self.__EntityHandle, component)
    
    def RemoveComponent(self, componentType: _Type[CTV]) -> None:
        if not self.HasComponent(componentType):
            ClientLoggers.Error(
                "Enitiy: {} ({}), Does not have component of type: {}",
                self, int(self), componentType
            )
            return
        
        if componentType in [IDComponent, TagComponent, TransformComponent]:
            ClientLoggers.Warn("Trying to remove an Essential Component from an Entity.")
            return

        self.__EntityRegistry.RemoveComponent(self.__EntityHandle, componentType)
