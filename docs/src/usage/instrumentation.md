# Instrumentation

The engine, when running with the [INSTRUMENTATION flag](../appendix/features.md) set, generates a few `.json` files that can be used to measure the performance of the engine.

The `.json` files will be in [Chrome's Trace Event Format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview?tab=t.0#heading=h.yr4qxyxotyw). To visualize the instrumentation data, you can use [Chrome Tracer](chrome://tracing).

To instrument your own code, you can use the `Timer` object provided by the engine.

```python
# To instrument a function
def fun():
    t = Timer("TimerName")  # This name will appear in the tracer view.
    ...

# To instrument a piece of code
t = Timer("TimerName")
# Your code
del t  # This ensures that the timer is stopped and stored.
```
