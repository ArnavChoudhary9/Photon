# Paths

## Overview

This game engine employs Python's `pathlib.Path` for all path-related operations. This decision was made to ensure consistency, clarity, and cross-platform compatibility when dealing with file system paths. Using `Path` instead of strings for paths eliminates ambiguity and provides a rich set of methods for file manipulation.

## Why `pathlib.Path`?

- **Cross-Platform Compatibility**: `Path` objects abstract away differences between operating systems, ensuring that paths work seamlessly on Windows, macOS, and Linux.
- **Rich Functionality**: `Path` provides methods like `.exists()`, `.is_file()`, `.mkdir()`, etc., making file handling more intuitive and readable.
- **Safety and Consistency**: By using `Path`, the engine avoids potential bugs caused by malformed or incorrect string-based paths.
- **Type Clarity**: Requiring `Path` objects makes function signatures and code behavior more predictable.

## Usage Guidelines

### Input Requirements

All functions and methods in the engine that require a file path must use a `pathlib.Path` object. Strings representing paths are **not** supported and will raise an error if passed.

```python
from pathlib import Path

def load_asset(asset_path: Path):
    if not asset_path.exists():
        raise FileNotFoundError(f"Asset not found: {asset_path}")
    # Proceed with loading the asset
```

#### Combining Paths

Use the `/` operator to combine paths:

```python
from pathlib import Path

config_file = Path("/path/to/project") / "config.json"
print(config_file)  # Outputs: /path/to/project/config.json
```

#### Checking Path Properties

```python
from pathlib import Path

path = Path("/path/to/file")
if path.exists() and path.is_file():
    print(f"The file {path} exists and is ready to use!")
else:
    print(f"The file {path} does not exist or is not a file.")
```

## Developer Recommendations

1. Avoid converting paths to strings unless absolutely necessary (e.g., for third-party library compatibility).
1. When documenting your functions, explicitly state that parameters must be `Path` objects.

## Error Handling

If a string is passed where a `Path` is expected, the engine will raise a `TypeError`:

```python
TypeError: Expected a pathlib.Path object, got str instead.
```

To resolve this, ensure all paths are converted to `Path` objects:

```python
from pathlib import Path

path = Path("/path/to/resource")
```

---

By enforcing the use of `pathlib.Path`, this game engine ensures a robust, consistent, and developer-friendly approach to file system interactions. Embrace `Path` for all your path-related needs!

> The engine uses `pathlib.Path` for defining paths. You automatically import `pathlib.Path` when importing `Photon`.
