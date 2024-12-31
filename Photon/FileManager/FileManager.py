from ..Logging import CoreLogger, ClientLoggers
from ..Core.Utility import UUID, UUID3Generator
from .Stream import Stream, StreamPool

from typing import Dict, List, ByteString
from pathlib import Path
from time import time, sleep
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

__NUM_WORKERS__: int = 4

class File:
    __UUID: UUID
    __Path: Path
    __RefCount: int = 0
    __Stream: Stream
    __LastReleaseTime: int = 0
    
    def __init__(self, path: Path, stream: Stream) -> None:
        self.__UUID = UUID3Generator(str(path))
        self.__Path = path
        self.__RefCount = 0
        self.__Stream = stream
        self.__LastReleaseTime = 0
    
    def __enter__(self) -> None:
        self.Aquire()
        return self
    
    def __exit__(self, exc_type, exc_value, trace):
        self.Release()
    
    @property
    def UUID(self) -> UUID: return self.__UUID
    @property
    def Path(self) -> Path: return self.__Path
    @property
    def Stream(self) -> Stream: return self.__Stream
    
    def Aquire(self) -> None:
        self.__RefCount += 1
            
    def Release(self) -> None:
        self.__Stream.ResetRead()
        self.__Stream.Close()
        if self.__RefCount > 0:
            self.__RefCount -= 1
            if self.__RefCount == 0:
                self.__LastReleaseTime = time()

    def _Unloadable(self, desTimeout: int) -> bool:
        return ( (not self.__RefCount) and
            (time() - self.__LastReleaseTime) > desTimeout
        )
        
    def Read(self, size: int=-1) -> ByteString:
        while not self.__Stream.Closed:
            sleep(0.01)
            
        with FileManager._Lock:
            return self.__Stream.Read(size)
    
    def Write(self, data: ByteString) -> None:
        with FileManager._Lock:
            self.__Stream.Write(data)        

class FileManager:
    __Resources: Dict[Path, File]
    __CacheClearTime: int
    _StreamPool: StreamPool
    
    __CacheHandlerThread: Thread
    __ThreadPool: ThreadPoolExecutor
    _Lock: Lock
    
    @staticmethod
    def INIT(cacheClearTime: int=360, maxThreads: int=__NUM_WORKERS__) -> None:
        '''
        cacheClearTime of -1 will disable cache clearing.
        '''
        FileManager.__Resources = {}
        FileManager.__CacheClearTime = cacheClearTime
        FileManager._StreamPool = StreamPool(__NUM_WORKERS__)    # We can reuse __NUM_WORKERS__ streams.
        
        FileManager.__ThreadPool = ThreadPoolExecutor(maxThreads)
        FileManager._Lock = Lock()
        
        if cacheClearTime != -1:
            FileManager.__CacheHandlerThread = Thread(target=FileManager._CacheHandler, daemon=True)
            FileManager.__CacheHandlerThread.start()
            
        CoreLogger.Info("ResourceManager initialized.")
    
    @staticmethod
    def Write(file: File) -> None:
        def task() -> None:
            file.Stream.Close()
            with open(file.Path, 'wb') as f:
                f.write(file.Stream.Read())
        
        FileManager.__ThreadPool.submit(task)
    
    def Load(filename: Path) -> File:
        filename = filename.absolute()
        if filename in FileManager.__Resources: return FileManager.__Resources[filename]
        
        # Client is loading the resources so they should be notified of new resource load.
        ClientLoggers.Trace("Loading Resource: {}", filename)

        file = File(filename, FileManager._StreamPool.Get())
        FileManager.__Resources[filename] = file

        def task():
            with FileManager._Lock:
                with file:
                    with open(filename, 'rb') as f:
                        file.Stream.Write(f.read())
        
        FileManager.__ThreadPool.submit(task)
        return file
        
    def _CacheHandler() -> None:
        while True:
            with FileManager._Lock:
                toDel: List[File] = []
                for path, file in FileManager.__Resources.items():
                    if file._Unloadable(FileManager.__CacheClearTime): toDel.append(file)

                for file in toDel:
                    FileManager._StreamPool.Return(file.Stream)
                    del FileManager.__Resources[path]

            sleep(FileManager.__CacheClearTime)

class FileReader:
    def __init__(self, filename: Path) -> None:
        self.File: File = FileManager.Load(filename)
        
    def __enter__(self) -> File:
        self.File.Aquire()
        return self.File
    def __exit__(self, exc_type, exc_value, trace):
        self.File.Release()
        
class FileWriter:
    def __init__(self, filename: Path) -> None:
        self.File: File = File(filename, FileManager._StreamPool.Get())
        
    def __enter__(self) -> File:
        self.File.Aquire()
        return self.File
    def __exit__(self, exc_type, exc_value, trace):
        self.File.Release()
        FileManager.Write(self.File)  
        