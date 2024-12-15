# 3.2 Logging

Logging is an essential feature of any game engine. Photon also provides the user with loggers that can be used by the users.

> The loggers are multi-threaded and does not impact the performance that much.

The users are provided with a ClientLoggers[LoggerSupcription] class, You can add your own loggers to it and any logs pass to CLient Loggers will be passed along to these loggers.

> A default logger with the name of the application subclass will already be added to ClientLoggers.

```python
# Logging
ClientLoggers.Trace(msg)        # White
ClientLoggers.Debug(msg)        # Blue
ClientLoggers.Info(msg)         # Green
ClientLoggers.Warn(msg)         # Warn
ClientLoggers.Error(msg)        # Red
ClientLoggers.Critical(msg)     # Red BG with White text

# Adding to ClientLoggers
ClientLoggers.Subscribe(Logger(name))
```
