# 3.8 Scene

## Overview

The `Scene` class represents a scene in a game or application, managing entities and their components. It provides functionality for creating, duplicating, and destroying entities, as well as handling scene-specific operations.

## Class: Scene

### Properties

- `Name`: str
  - Returns the name of the scene.
- `SceneUUID`: UUID
  - Returns the unique identifier of the scene.
- `EntityRegistry`: EntityRegistry
  - Returns the entity registry associated with the scene.
- `Entities`: List[Entity]
  - Returns a list of all entities in the scene.

### Methods

#### Constructor

- `__init__(self, name: str) -> None`
  - Initializes a new Scene with the given name.

#### Entity Management

- `CreateEntity(self, name: str) -> Entity`
  - Creates a new entity with a generated UUID.
- `CreateEntityWithUUID(self, name: str, uuid: UUID) -> Entity`
  - Creates a new entity with a specified UUID.
- `DuplicateEntity(self, entity: Entity) -> Entity`
  - Creates a copy of an existing entity.
- `DefferedDuplicateEntity(self, entity: Entity) -> None`
  - Schedules an entity for duplication in the next update.
- `DestroyEntity(self, entity: Entity) -> None`
  - Marks an entity for deletion in the next update.
- `GetEntitysWithComponent(self, component: Type[CTV]) -> List[Entity]`
  - Returns a list of entities that have a specific component.

#### Scene Lifecycle

- `OnStart(self) -> None`
  - Called when the scene starts.
- `OnUpdate(self) -> None`
  - Called every frame to update the scene.
- `OnStop(self) -> None`
  - Called when the scene stops.
- `OnUpdateEditor(self, dt: float) -> None`
  - Called every frame in editor mode.
- `OnUpdateRuntime(self, dt: float) -> None`
  - Called every frame during runtime.

#### Component Callbacks

- `OnComponentAdded(self, entity: Entity, component: CTV) -> None`
  - Called when a component is added to an entity.
- `OnComponentRemoved(self, entity: Entity, component: CTV) -> None`
  - Called when a component is removed from an entity.

### Usage

The `Scene` class is central to managing game objects and their behaviors. It allows for:

1. Creating and managing entities within the scene.
2. Handling scene lifecycle events (start, update, stop).
3. Managing entity components.
4. Providing a structured approach to game/application organization.

### Example

```python
# Create a new scene
game_scene = Scene("Level 1")

# Create an entity
player = game_scene.CreateEntity("Player")

# Add components to the entity
player.AddComponent(HealthComponent, 100)
player.AddComponent(PositionComponent, x=0, y=0)

# Update the scene
game_scene.OnUpdate()
```
