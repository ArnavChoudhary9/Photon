import os, sys
from PyInstaller.__main__ import run
from PyInstaller.utils.hooks import collect_all

project, config = sys.argv[1:3]

options = []
options.append("--onefile")
options.append(f"{project}\\{project}.py")

if config=='r': options.append("--noconsole")

modules = [
    project,
    "Photon",
    "uuid",
    "importlib",
    "importlib.recources",
    "spdlog",
    "concurrent",
    "json",
    "glfw",
    "pyrr",
    "esper",
    "cProfile",
    "OpenGL",
    "imgui",
    "PIL",
]

for module in modules:
    datas, binaries, hiddenimports = collect_all(module)
        
    for data in datas:
        options.append(f'--add-data={os.pathsep.join(data)}')
    for binary in binaries:
        options.append(f'--add-binary={os.pathsep.join(binary)}')
    for hiddenimport in hiddenimports:
        options.append(f'--hidden-import={hiddenimport}')
            
run(options)
