# Project

This module defines the `Project` class, which manages the overall structure and data of a project within the Photon engine. It handles project creation, loading, saving, and scene management.

## Project Class Overview

The `Project` class is responsible for:

- Storing project-level information such as name, working directory, and scene organization.
- Initializing new projects with default settings and directory structure.
- Loading existing projects from disk, including scene data.
- Saving project data to disk, including project settings and individual scenes.
- Managing the scene registry and scene order within the project.

## Class Details

### `__init__(self, workingDir: Path, name: str="", makeIfNotExist: bool=True) -> None`

Initializes a new `Project` instance.

**Parameters:**

- `workingDir` (`Path`): The directory where the project will be stored.
- `name` (`str`, optional): The name of the project. Defaults to "".  Must be provided if `workingDir` does not exist.
- `makeIfNotExist` (`bool`, optional): If `True`, creates the project directory if it doesn't exist. Defaults to `True`.  If `False` and the directory does not exist, an error is raised.

**Raises:**

- `AssertionError`: If `name` is empty and a new project is being created.
- `AssertionError`: If `makeIfNotExist` is `False` and the project directory does not exist.

**Logic:**

1. Checks if the `workingDir` exists.
2. If it doesn't exist and `makeIfNotExist` is `True`, creates the directory and initializes the project as new.
3. If it doesn't exist and `makeIfNotExist` is `False`, raises an error.
4. If the directory exists, loads the project data from the project file.

### `ProjectFile` Property

Returns the `Path` to the project file (`.pjproj`).

**Returns:**

- `Path`: The path to the project file.

### `AssetsLocation` Property

Returns the `Path` to the project's "Assets" directory.

**Returns:**

- `Path`: The path to the Assets directory.

### `ScenesLocation` Property

Returns the `Path` to the project's "Scenes" directory (located inside the Assets directory).

**Returns:**

- `Path`: The path to the Scenes directory.

### `ScriptsLocation` Property

Returns the `Path` to the project's "Scripts" directory (located inside the Assets directory).

**Returns:**

- `Path`: The path to the Scripts directory.

### `BuildLocation` Property

Returns the `Path` to the project's "Builds" directory.

**Returns:**

- `Path`: The path to the Builds directory.

### `GetSceneLocation(self, scene: Scene) -> Path`

Returns the `Path` to a specific scene file within the project's "Scenes" directory.

**Parameters:**

- `scene` (`Scene`): The `Scene` object for which to retrieve the location.

**Returns:**

- `Path`: The path to the scene file.

### `InitProject(self) -> None`

Initializes a new project with default settings and directory structure.

**Logic:**

1. Creates a default scene named "Scene".
2. Registers the default scene with the project.
3. Creates an empty entity within the default scene.
4. Creates the "Assets", "Scenes", "Scripts", and "Builds" directories.
5. Saves the initial project data to disk.

### `LoadProject(self) -> None`

Loads an existing project from disk.

**Logic:**

1. Reads the project file (`.pjproj`) using `yaml.load`.
2. Checks for Photon version mismatch and logs a warning if versions are different.
3. Populates the project's `__Name`, `__SceneOrder`, and `__SceneRegistry` from the loaded data.
4. Deserializes each scene using `SceneSerializer.Deserialize`.
5. Creates the "Assets", "Scenes", "Scripts", and "Builds" directories if they don't exist.

### `Save(self) -> None`

Saves the project data to disk.

**Logic:**

1. Writes the project's `__Name`, `__SceneOrder`, and `__SceneRegistry` to the project file (`.pjproj`) using `yaml.dump`.
2. Serializes each scene using `SceneSerializer.Serialize` and saves it to the appropriate location within the "Scenes" directory.

### `RegisterScene(self, scene: Scene) -> None`

Registers a scene with the project, adding it to the scene registry and scene order.

**Parameters:**

- `scene` (`Scene`): The `Scene` object to register.

### `GetScene(self, index: int) -> Scene`

Retrieves a scene from the project by its index in the scene order.

**Parameters:**

- `index` (`int`): The index of the scene in the scene order.

**Returns:**

- `Scene`: The `Scene` object at the specified index.

## Helper Classes and Functions

### `SceneSerializer`

The `SceneSerializer` class (not directly part of the `Project` class but closely related) likely provides methods for serializing (saving) and deserializing (loading) `Scene` objects to and from files.  It would handle the specific details of converting a `Scene` object's data into a storable format (e.g., YAML, JSON, or a binary format) and recreating the `Scene` object from that stored format.
