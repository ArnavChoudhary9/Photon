# Communication Layer

## **Overview**

The `CommunicationLayer` is a centralized intermediary that facilitates communication between components in an application. It leverages the event system to manage subscriptions and event propagation efficiently. By centralizing communication logic, it reduces the load on individual components and ensures scalability.

---

## **Key Component**

### **CommunicationLayer**

The `CommunicationLayer` provides an interface for components to subscribe to and publish events without directly interacting with each other.

#### Responsibilities

- **Centralized Event Management**: Handles all event-related operations, reducing complexity in individual components.
- **Dynamic Subscription**: Allows components to register themselves as listeners for specific event types.
- **Efficient Event Propagation**: Ensures that events are dispatched to registered listeners in a streamlined manner.

---

## **Workflow**

1. **Subscription**:
   - Components register themselves as listeners for specific event types through the `CommunicationLayer`.

2. **Publishing Events**:
   - Components broadcast events using the `CommunicationLayer`, which forwards them to the event system.

3. **Event Handling**:
   - The event system propagates events to all registered listeners, ensuring efficient communication without direct dependencies between components.

---

## **Usage Examples**

### **1. Initializing the Communication Layer**

To begin using the `CommunicationLayer`, create an instance of it. This instance will act as the central hub for managing events.

```python
from CommunicationLayer import CommunicationLayer

# Initialize the Communication Layer
communication_layer = CommunicationLayer()
```

---

### **2. Subscribing to Events**

Components can subscribe to specific event types by providing a callback function that will handle the event when it is dispatched.

```python
from Events import EventType

# Define a listener function for window resize events
def on_window_resize(event):
    print(f"Window resized: {event.width}x{event.height}")
    return True  # Returning True indicates the event was handled

# Subscribe to the WindowResize event
communication_layer.Subscribe(EventType.WindowResize, on_window_resize)
```

---

### **3. Publishing Events**

Components can publish events using the `PublishEvent` method of the `CommunicationLayer`. These events will be dispatched to all registered listeners.

```python
from Events import WindowResizeEvent

# Create a WindowResizeEvent
window_resize_event = WindowResizeEvent(width=800, height=600)

# Publish the event
communication_layer.PublishEvent(window_resize_event)
```

Output:

```text
Window resized: 800x600
```

---

### **4. Handling Multiple Event Types**

A single component can subscribe to multiple event types by registering different listener functions.

```python
from Events import EventType, KeyPressedEvent

# Define a listener for key press events
def on_key_pressed(event):
    print(f"Key pressed: {event.key_code}")
    return True

# Subscribe to both WindowResize and KeyPressed events
communication_layer.Subscribe(EventType.WindowResize, on_window_resize)
communication_layer.Subscribe(EventType.KeyPressed, on_key_pressed)

# Publish a KeyPressedEvent
key_pressed_event = KeyPressedEvent(key_code=65)  # Example key code for 'A'
communication_layer.PublishEvent(key_pressed_event)
```

Output:

```text
Key pressed: 65
```

---

### **5. Unsubscribing from Events (Optional)**

If needed, components can unsubscribe from specific events by removing their listener functions from the dispatcher.

```python
# Unsubscribe from WindowResize events (if supported in your implementation)
communication_layer.Unsubscribe(EventType.WindowResize, on_window_resize)
```

---

## **Advantages**

### 1. **Reduced Load on Components**

By centralizing event handling, individual components are freed from managing complex communication logic, reducing their computational load.

### 2. **Loose Coupling**

The `CommunicationLayer` ensures loose coupling between components, enabling indirect communication without creating cyclic dependencies.

### 3. **Scalability**

The system is designed to support new components or events without requiring modifications to existing code, making it highly scalable.

### 4. **Efficient Propagation**

Listeners are notified only of events they have subscribed to, ensuring efficient use of resources.
