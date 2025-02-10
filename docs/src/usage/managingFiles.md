# Managing Files

## Loading Files

The `FileManager` class offers a robust mechanism for loading files. When a file is loaded, it is cached for efficient reuse. The following example demonstrates how to load a file:

### Example

```python
from FileManager import FileManager

# Initialize FileManager
FileManager.INIT()

# Load a file
file_path = Path("/path/to/your/file")
file = FileManager.Load(file_path)

# Read data from the file
data = file.Read()
print(data)
```

> [Note you need to use `pathlib.Path` to specify paths](../appendix/paths.md)

## Storing Files in Cache

The file manager maintains a cache of files. Cached files are automatically cleared based on the `cacheClearTime` specified during initialization. To disable cache clearing, set `cacheClearTime` to `-1`.

### Example

```python
# Initialize with cache clearing disabled
FileManager.INIT(cacheClearTime=-1)

file1 = FileManager.Load(Path("/path/to/file1"))
file2 = FileManager.Load(Path("/path/to/file1")) # This will reload the file
```

> This can be usefull in dev mode when your files change frequently.

The cache handler thread will periodically check for unused files and release them based on their last release time and usage.

## Writing Files

Writing to files is done asynchronously to ensure performance. The `FileManager.Write` method schedules the write operation using a thread pool.

### Example

```python
# Write data to a file
file = File(Stream(), Path("/path/to/file"))
data_to_write = b"Some data to write"
file.Write(data_to_write)

# FileManager.Write will handle closing and writing to the disk
FileManager.Write(file)
```

## Using Context Managers

Context managers ensure that resources like file streams are properly acquired and released, reducing the risk of resource leaks. The `File`, `FileReader`, and `FileWriter` classes all support context management.

### FileReader Example

```python
from FileManager import FileReader
from pathlib import Path

file_path = Path("/path/to/your/file")

with FileReader(file_path) as file:
    data = file.Read()
    print(data)
```

### FileWriter Example

```python
from FileManager import FileWriter
from pathlib import Path

file_path = Path("/path/to/your/file")

data_to_write = b"New data to write"

with FileWriter(file_path) as file:
    file.Write(data_to_write)
```

### Benefits of Using Context Managers

- **Automatic Resource Management**: Resources like file streams are automatically released when the block exits.
- **Error Handling**: Any exceptions raised within the block are handled, and cleanup still occurs.
- **Cleaner Code**: The syntax is concise and readable.

---

By following these guidelines and leveraging the built-in file handling features, developers can ensure efficient, safe, and clear file operations within the game engine.
