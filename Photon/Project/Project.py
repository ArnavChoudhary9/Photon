from ..Logging import CoreLogger, ClientLoggers
from ..Core.Utility import *
from ..Core.Version import PHOTON_VERSION
from ..Scene import *

from pathlib import Path
import yaml

class Project:
    __Name: str
    __WorkingDirectory: Path

    __SceneRegistry: Dict[UUID, Scene]
    __SceneOrder: List[UUID]

    def __init__(self, workingDir: Path, name: str="",  makeIfNotExist: bool=True) -> None:
        doNotLoad: bool = False

        if not workingDir.exists():
            assert name != "", CoreLogger.Error("Making a new Project with no name!!")
            
            assert makeIfNotExist, CoreLogger.Error(
                "Trying to create a project({}) which does not exist!! And makeIfNotExist is set to False",
                str(workingDir.resolve())
            )

            doNotLoad = True
            workingDir.mkdir(parents=True)

        self.__Name = name
        self.__WorkingDirectory = workingDir
        self.__SceneOrder = []
        self.__SceneRegistry = {}

        ClientLoggers.Info("Opened project at {}", workingDir.resolve())

        if not self.ProjectFile.exists(): self.InitProject()
        if not doNotLoad: self.LoadProject()

    @property
    def ProjectFile(self) -> Path: return (self.__WorkingDirectory / "{}.pjproj".format(self.__Name))
    @property
    def AssetsLocation(self) -> Path: return (self.__WorkingDirectory / "Assets")
    @property
    def ScenesLocation(self) -> Path: return (self.AssetsLocation / "Scenes")
    @property
    def ScriptsLocation(self) -> Path: return (self.AssetsLocation / "Scripts")
    @property
    def BuildLocation(self) -> Path: return (self.__WorkingDirectory / "Builds")

    def GetSceneLocation(self, scene: Scene) -> Path: return (self.ScenesLocation / "{}.ph".format(scene.Name))

    def InitProject(self) -> None:
        ClientLoggers.Info("It is a new project, Initializing . . .")
        
        scene = Scene("Scene")
        self.RegisterScene(scene)
        scene.CreateEntity("EmptyEntity")

        # Makes required directories
        self.AssetsLocation.mkdir(exist_ok=True)
        self.ScenesLocation.mkdir(exist_ok=True)
        self.ScriptsLocation.mkdir(exist_ok=True)
        self.BuildLocation.mkdir(exist_ok=True)

        # Makes the file
        self.Save()

    def LoadProject(self) -> None:
        ClientLoggers.Info("Loading the project")

        _SaveProject: bool = False # flag, as the file here is opened as read-only
        with self.ProjectFile.open('r') as projectFile:
            data = yaml.load(projectFile, yaml.Loader)

            if PHOTON_VERSION != data["PhotonVersion"]:
                ClientLoggers.Warn("Photon version mismatch!")
                ClientLoggers.Trace("Trying to open in this version.")

                # TODO: Handle downgrading / upgrading
                _SaveProject = True

            self.__Name = data["Project"]["Name"]

            self.__SceneOrder.clear()
            for uuid in data["Project"]["SceneOrder"]:
                self.__SceneOrder.append(UUID(uuid))

            self.__SceneRegistry.clear()
            for uuid, name in data["Project"]["SceneRegistry"].items():
                path = self.ScenesLocation / "{}.ph".format(name)
                self.__SceneRegistry[UUID(uuid)] = SceneSerializer.Deserialize(path)

        if _SaveProject: self.Save()

        # Confirm required directories
        self.AssetsLocation.mkdir(exist_ok=True)
        self.ScenesLocation.mkdir(exist_ok=True)
        self.ScriptsLocation.mkdir(exist_ok=True)
        self.BuildLocation.mkdir(exist_ok=True)

    def Save(self) -> None:
        ClientLoggers.Info("Saving project")
        with self.ProjectFile.open('w') as projectFile:
            data = {
                "Project": {
                    "Name": self.__Name,
                    "SceneOrder": [ str(uuid) for uuid in self.__SceneOrder ],
                    "SceneRegistry": { str(k): v.Name for k, v in self.__SceneRegistry.items() }
                },
                "PhotonVersion": PHOTON_VERSION
            }
            yaml.dump(data, projectFile)

        for _, scene in self.__SceneRegistry.items():
            SceneSerializer.Serialize(scene, self.GetSceneLocation(scene).absolute())

    def RegisterScene(self, scene: Scene) -> None:
        self.__SceneRegistry[scene.SceneUUID] = scene
        self.__SceneOrder.append(scene.SceneUUID)

    def GetScene(self, index: int) -> Scene:
        return self.__SceneRegistry[self.__SceneOrder[index]]
