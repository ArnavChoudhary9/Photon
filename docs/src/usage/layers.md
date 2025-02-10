# Layers

## Overview

The game engine's layer system provides a structured way to manage and organize rendering, updates, and event handling. The `PhotonApplication` supplies the user-defined application class with a `LayerStack`, enabling seamless integration of user-defined layers and overlays into the engine.

---

## Layers

A `Layer` is an abstract base class that defines the essential lifecycle methods for any layer. Users inherit from this class to create custom layers. Layers include event handling and can be toggled on or off.

### Key Features of a Layer

- **Initialization and Lifecycle**:
  - `OnInitialize()`: Setup tasks when the layer is created.
  - `OnStart()`: Called when the layer becomes active.
  - `OnUpdate(dt)`: Updates the layer logic every frame.
  - `OnStop()`: Called when the layer is stopped.
  - `OnDestroy()`: Cleanup tasks when the layer is destroyed.
- **Event Handling**:
  - `OnEvent(event)`: Processes events, returning whether the event was handled.

### Example

```python
from Layers import Layer

class GameLayer(Layer):
    def OnInitialize(self):
        print(f"Initializing {self.Name}")

    def OnStart(self):
        print(f"Starting {self.Name}")

    def OnUpdate(self, dt: float):
        print(f"Updating {self.Name} with dt={dt}")

    def OnStop(self):
        print(f"Stopping {self.Name}")

    def OnDestroy(self):
        print(f"Destroying {self.Name}")

    def OnEvent(self, event):
        print(f"Event {event.Name} handled in {self.Name}")
        return True
```

---

## LayerStack

The `LayerStack` is responsible for managing the layers and overlays. It provides methods to add, update, and remove layers while ensuring the proper lifecycle management.

### Key Features

1. **Layer Management**:
   - `AddLayer(layer)`: Adds a layer to the stack.
   - `AddOverlay(overlay)`: Adds an overlay to the stack.
2. **Lifecycle Handling**:
   - `OnStart()`, `OnUpdate(dt)`, `OnStop()`, `Destroy()` handle layer lifecycles.
3. **Event Propagation**:
   - Events are propagated through overlays first, followed by layers, in the order they were added.

### Example

```python
from LayerStack import LayerStack
from Layers import Layer

class MyApplication:
    def __init__(self):
        self.layer_stack = LayerStack()

    def Run(self):
        self.layer_stack.OnStart()
        self.layer_stack.OnUpdate(0.016)  # Example delta time
        self.layer_stack.OnStop()
        self.layer_stack.Destroy()
```
