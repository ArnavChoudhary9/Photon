from typing import Dict, List, Any
from uuid import UUID

from typing import TypeVar, Protocol
import pyrr

class SupportsComponents(Protocol):
    def  Copy(self): ...

# They are applied to all Entities
class IDComponent:
    ID: UUID

    def __init__ (self, id: UUID): self.ID = id

    @property
    def HEX(self) -> str: return self.ID.hex

    def __int__  (self) -> int : return self.ID.int
    def __str__  (self) -> str : return str(self.ID)
    def __repr__ (self) -> str : return self.ID.__repr__()

    def Copy(self):
        # ClientLoggers.Critical("Trying to copy IDComponent! It should not be copied")
        return None
class TagComponent:
    Tag: str

    def __init__(self, tag: str="Entity") -> None: self.Tag = tag
    def __str__(self) -> str: return self.Tag

    def Copy(self): return TagComponent(self.Tag)
    
    def Serialize(self) -> Dict: return {"Tag": self.Tag}
class TransformComponent:
    Translation : pyrr.Vector3
    Rotation    : pyrr.Vector3
    Scale       : pyrr.Vector3

    def __init__(self) -> None: self.Reset()

    @property
    def Transform(self) -> pyrr.Matrix44:
        rotX = pyrr.matrix44.create_from_x_rotation(self.Rotation.x)
        rotY = pyrr.matrix44.create_from_y_rotation(self.Rotation.y)
        rotZ = pyrr.matrix44.create_from_z_rotation(self.Rotation.z)

        rotation = rotX @ rotY @ rotZ

        location = pyrr.matrix44.create_from_translation(self.Translation)
        scale = pyrr.matrix44.create_from_scale(self.Scale)

        return scale @ rotation @ location # type: ignore

    def __pyrr_Matrix44__(self) -> pyrr.Matrix44: return self.Transform

    def SetTranslation(self, pos: pyrr.Vector3) -> None: self.Translation = pos
    def Translate(self, delta: pyrr.Vector3) -> None: self.Translation = self.Translation + delta
    def SetRotation(self, rotation: pyrr.Vector3) -> None: self.Rotation = rotation
    
    def Rotate(self, delta: pyrr.Vector3) -> None: self.Rotation = self.Rotation + delta
    def SetScale(self, scale: pyrr.Vector3) -> None: self.Scale = scale

    def Reset(self) -> None:
        self.Translation = pyrr.Vector3([ 0.0, 0.0, 0.0 ])
        self.Rotation    = pyrr.Vector3([ 0.0, 0.0, 0.0 ])
        self.Scale       = pyrr.Vector3([ 1.0, 1.0, 1.0 ])

    def Copy(self):
        component = TransformComponent()

        component.Translation = self.Translation .copy()
        component.Rotation    = self.Rotation    .copy()
        component.Scale       = self.Scale       .copy()

        return component
    
    def Serialize(self) -> Dict[str, Dict[str, pyrr.Vector3]]:
        return {"Transform": {
            "Translation" : self.Translation,
            "Rotation"    : self.Rotation,
            "Scale"       : self.Scale
        }}
    
    # Special Deserialize, everything should return a object
    def Deserialize(self, data: Dict[str, pyrr.Vector3]) -> None:
        self.Translation = data["Translation"]
        self.Rotation    = data["Rotation"]
        self.Scale       = data["Scale"]
class RelationshipComponent:
    ParentID: UUID | None
    ChildrenIDs: List[UUID]
    
    def __init__(self, parentID: UUID|None=None, childrenIDs: List[UUID]|None=None) -> None:
        self.ParentID = parentID
        self.ChildrenIDs = childrenIDs or []

    def AddChild(self, childID: UUID) -> None:
        self.ChildrenIDs.append(childID)
        
    def RemoveChild(self, childID: UUID) -> None:
        if childID in self.ChildrenIDs:
            self.ChildrenIDs.remove(childID)
            
    def ChangePatent(self, parentID: UUID) -> None:
        self.ParentID = parentID
        
    def Copy(self): ...
    
    def Serialize(self) -> Dict[str, Dict]:
        return {"RelationshipComponent": {
            "ParentID": self.ParentID,
            "ChildrenIDs": self.ChildrenIDs
        }}
    
    @staticmethod
    def Deserialize(data: Dict[str, Any]) -> 'RelationshipComponent':
        component = RelationshipComponent()
        
        component.ParentID = UUID(data["ParentID"]) if data["ParentID"] else None
        component.ChildrenIDs = [UUID(child) for child in data["ChildrenIDs"]]
        
        return component
    
# region Sellective Components
# They are only applied to secective Entities
# class CameraComponent:
#     Camera: SceneCamera

#     Primary: bool
#     FixedAspectRatio: bool

#     def __init__(self, camera: SceneCamera, isPrimary: bool=True, isFixedAspectRatio: bool=False) -> None:
#         self.Camera = camera
#         self.Primary = isPrimary
#         self.FixedAspectRatio = isFixedAspectRatio

#     def __bool__(self) -> bool: return self.Primary

#     def Copy(self):
#         component = CameraComponent(SceneCamera(self.Camera.ProjectionType), self.Primary, self.FixedAspectRatio)
#         component.Camera.CameraObject.AspectRatio = self.Camera.CameraObject.AspectRatio
#         return component
    
#     def Serialize(self) -> Dict[str, Dict[str, int]]:
#         return {"Camera": {
#             "ProjectionType": self.Camera.ProjectionType.value,
#             "Primary": self.Primary,
#             "FixedAspectRatio": self.FixedAspectRatio
#         }}
    
#     def Deserialize(self, data: Dict[str, Dict[str, int]]) -> None:
#         cameraDict = data["Camera"]
#         self.Camera.SetProjectionType(ProjectionTypes(cameraDict["ProjectionType"]))
#         self.Primary = bool(data["Primary"])
#         self.FixedAspectRatio = bool(data["FixedAspectRatio"])
# class MeshComponent:
#     def Copy(self):
#         component = MeshComponent()
#         return component
# endregion

# CTV = ComponentTypeVar
CTV = TypeVar("CTV",
        IDComponent, TagComponent, TransformComponent, RelationshipComponent,
        # CameraComponent, MeshComponent
    )    
