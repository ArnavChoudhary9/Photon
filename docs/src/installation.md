# 2. Installation

## Requirements

* **Python >=3.10**

   The engine is based on [Python 3.10](https://www.python.org/downloads/release/python-31012).

   It is preferred that you use Python 3.10 or upgrade to a version supported by [PyImGUI](https://github.com/pyimgui/pyimgui).

## Installation Methods

You can install Photon using pip or by compiling from source ([GitHub](https://github.com/ArnavChoudhary9/Photon)) or download [precompiled binaries](https://github.com/ArnavChoudhary9/Photon/releases)

### 1. Install via pip

This is the recommended method for most users.

```sh
pip install PhotonEngine
```

* **Dependency**: Python

### 2. Compile from Source (GitHub)

Use this method if you want to contribute to Photon's development or explore its inner workings.

* **Requirement**: Virtual Environment (venv)

   Install using:

   ```sh
   pip install venv
   ```

1. Clone the repository:

   ```sh
   git clone --recursive https://github.com/ArnavChoudhary9/Photon
   ```

2. Navigate to the project directory:

   ```sh
   cd Photon
   ```

3. Initialize the repository:

   ```sh
   setup.bat
   ```

4. Activate the virtual environment:

   ```sh
   venv\Scripts\activate
   ```

5. Run Forge Editor:

   ```sh
   cd Forge
   python Forge.py
   ```

> Congratulations! You have successfully run Forge Editor.

### 3. Running Precompiled binaries

Use this if you only want to run the editor and develope games.

Download the latest precompiled binary from [GitHub](https://github.com/ArnavChoudhary9/Photon/releases).

To run the editor, navigate to the downloaded directory and run `Forge.exe`.
