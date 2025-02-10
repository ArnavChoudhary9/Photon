# Entity Component System (ECS)

## Overview

This Entity Component System (ECS) is designed for game development and simulation environments. It provides a flexible and efficient way to manage entities, components, and their interactions within a game or application.

## Key Classes

### EntityRegistry

The `EntityRegistry` class manages entities and their components.

#### Key Methods

- `CreateEntity()`: Creates a new entity and returns its identifier.
- `DeleteEntity(entity, immediate=False)`: Deletes an entity and its components.
- `AddComponent(entity, component_type, *component_args)`: Adds a component to an entity.
- `RemoveComponent(entity, component_type)`: Removes a component from an entity.
- `GetComponent(component_type)`: Retrieves all entities with a specific component type.
- `HasComponent(entity, component_type)`: Checks if an entity has a specific component.

### Entity

The `Entity` class represents a game object and provides an interface to interact with its components.

#### Key Methods

- `HasComponent(componentType)`: Checks if the entity has a specific component.
- `GetComponent(componentType)`: Retrieves a specific component from the entity.
- `AddComponent(componentType, *args, **kwargs)`: Adds a new component to the entity.
- `RemoveComponent(componentType)`: Removes a component from the entity.

## Component Types

- `IDComponent`: Stores a unique identifier for each entity.
- `TagComponent`: Assigns a string tag to an entity for categorization.
- `TransformComponent`: Manages the position, rotation, and scale of an entity in 3D space.

## Usage Example

```python
# Create an entity registry
entity_registry = EntityRegistry(component_added_function, component_removed_function)

# Create a new entity
entity_id = entity_registry.CreateEntity()

# Create an Entity object
entity = Entity(entity_id, entity_registry)

# Add components to the entity
entity.AddComponent(TagComponent, "Player")
entity.AddComponent(TransformComponent)

# Modify component data
transform = entity.GetComponent(TransformComponent)
transform.SetTranslation(pyrr.Vector3([1.0, 2.0, 3.0]))

# Check for component existence
if entity.HasComponent(TagComponent):
    tag = entity.GetComponent(TagComponent)
    print(f"Entity tag: {tag.Tag}")

# Remove a component
entity.RemoveComponent(TagComponent)

# Delete the entity
entity_registry.DeleteEntity(entity_id)
```

## Limitations and Considerations

- The current implementation does not include a full implementation of systems.
- Some commented-out code suggests additional components (CameraComponent, MeshComponent) that are not fully implemented.
- The ECS is tightly coupled with the `pyrr` library for 3D math operations.
- Error handling and logging are implemented but could be expanded for more robust error management.
- Essential components like IDComponent, TagComponent, or TransformComponent cannot be removed from entities.
