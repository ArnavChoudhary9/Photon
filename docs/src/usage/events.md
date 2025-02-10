# Events

## Event Dispatching

The `Event` class and its derivatives manage the flow of events throughout the system. Events are categorized and dispatched using the `EventDispatcher`.

### Key Components

1. **Event Categories**:
   - Defined using bit flags, allowing a single event to belong to multiple categories.
2. **Event Types**:
   - Predefined types like `WindowResize`, `KeyPressed`, `MouseMoved`, etc.
3. **EventDispatcher**:
   - Maps event types to their respective handlers.

### Example

```python
from Event import Event, EventDispatcher, EventType

dispatcher = EventDispatcher()

def on_window_resize(event):
    print(f"Window resized: {event}")
    return True

dispatcher.AddHandler(EventType.WindowResize, on_window_resize)

# Simulating an event
event = WindowResizeEvent()
dispatcher.Dispatch(event)
```

## Event Flow in Layers

1. Events are first propagated to overlays in the `LayerStack`.
2. If an overlay handles the event, propagation stops.
3. If not, the event is passed to the layers in the stack.

### Example of Layer Handling Events

```python
class CustomLayer(Layer):
    def OnEvent(self, event):
        if event.EventType == EventType.KeyPressed:
            print(f"Key pressed event handled by {self.Name}")
            return True
        return False

layer_stack = LayerStack()
layer_stack.AddLayer(CustomLayer("GameLayer"))
layer_stack.OnEvent(event)
```

---

By using the `LayerStack` and `Event` system, the engine provides a robust foundation for organizing application logic and handling events efficiently.
