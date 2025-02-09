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

Download the latest precompiled binary from [GitHub](https://github.com/ArnavChoudhary9/Photon/releases).

To run the editor, navigate to the downloaded directory and run `Forge.exe`.

## Inspiration

Photon draws a lot of inspiration from [Hazel](https://github.com/TheCherno/Hazel) and takes a lot of learning from [The Cherno](https://youtube.com/playlist?list=PLlrATfBNZ98dC-V-N3m0Go4deliWHPFwT&si=joZeeB9E0mV37S28).

* Find [Documentation here](https://arnavchoudhary9.github.io/Photon/docs/book)
* Visit the [DevLog site here](https://arnavchoudhary9.github.io/Photon/devlogs/book)
