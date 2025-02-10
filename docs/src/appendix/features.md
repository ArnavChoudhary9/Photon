# Features

The engine contains a file (`Forge/Core/Features.py`) that can be used to toggle non-essential features of the engine.

- **INSTRUMENTATION** – Used to measure engine performance.
- **LOGGING** – Disables the `CoreLogger` and the logger provided to the client.
  - **Note:** Any logger created by the user and subscribed to `ClientLogger` will work as expected.
