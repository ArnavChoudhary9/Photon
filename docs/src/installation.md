# 2. Installation

## Requirements

1. **Python >=3.10**  
   The engine is based on [Python 3.10](https://www.python.org/downloads/release/python-31012), so it is preferred that you use Python 3.10 or upgrade to a version supported by [PyImGUI](https://github.com/pyimgui/pyimgui).

2. **Virtual Environment (venv)**  
   Install using:

   ```sh
   pip install venv
   ```

There are two ways to run the editor. If you just want to use the engine to make games or test its performance, you can download the [precompiled binaries](https://github.com/ArnavChoudhary9/Photon/releases). If you want to develop the engine and see how it works, you can download the [source code from GitHub](https://github.com/ArnavChoudhary9/Photon/).

### 1. Precompiled Binaries

1. Download the [precompiled binaries](https://github.com/ArnavChoudhary9/Photon/releases) from [GitHub](https://github.com/ArnavChoudhary9/Photon).
2. Extract the files and run `Forge.exe`.

> Congratulations! You have successfully installed Photon and Forge Editor.

### 2. Compile from Source

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
