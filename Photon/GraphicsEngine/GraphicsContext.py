from ..Core.Features import GRAPHICSLIBRARY, GraphicsLibraryENUM
from ..Logging import CoreLogger

from typing import Protocol
from abc import ABC, abstractmethod

class SuppurtsGraphicsContext(Protocol):
    @abstractmethod
    def Init(self) -> None: ...
    @abstractmethod
    def SwapBuffers(self) -> None: ...

class GraphicsContext(ABC):
    _WindowHandle: int

    def __init__(self, windowHandle: int) -> None:
        self._WindowHandle = windowHandle

    @abstractmethod
    def Init(self) -> None: ...
    @abstractmethod
    def SwapBuffers(self) -> None: ...

    @staticmethod
    def Create(windowHandle: int) -> SuppurtsGraphicsContext:
        '''
        Detects the desired Graphics Library, and returns the appropriate Graphics Context.
        '''

        if GRAPHICSLIBRARY == GraphicsLibraryENUM.Headless:
            assert False, CoreLogger.Critical("GraphicsLibraryENUM.Headless not supported Yet!!")

        elif GRAPHICSLIBRARY == GraphicsLibraryENUM.OpenGL:
            from .OpenGL.OpenGLGraphicsContext import OpenGLGraphicsContext
            return OpenGLGraphicsContext(windowHandle) # type: ignore

        else: assert False, CoreLogger.Critical("Unknown Graphics Library: {}", GRAPHICSLIBRARY)
