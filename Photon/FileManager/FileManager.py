from ..Logging import ClientLoggers, CoreLogger
from .Stream import Stream, StreamPool

from typing import Dict, List
from pathlib import Path
from time import time, sleep
from threading import Thread, Lock

class File:
    path: Path
    RefCount: int = 0
    stream: Stream
    LastReleaseTime: int = 0
    
    def __init__(self, path: Path) -> None:
        self.path = path
        self.RefCount = 0
        self.stream = None
        self.LastReleaseTime = 0        

class FileManager:
    __Resources: Dict[Path, File]
    __CacheClearTime: int
    __StreamPool: StreamPool
    
    __CacheHandlerThread: Thread
    __Lock: Lock
    
    def INIT(cacheClearTime: int=360) -> None:
        '''
        cacheClearTime of -1 will disable cache clearing.
        '''
        FileManager.__Resources = {}
        FileManager.__CacheClearTime = cacheClearTime
        FileManager.__StreamPool = StreamPool(8)    # We can reuse 8 streams.
        
        FileManager.__Lock = Lock()
        
        if cacheClearTime != -1:
            FileManager.__CacheHandlerThread = Thread(target=FileManager._CacheHandler, daemon=True)
            FileManager.__CacheHandlerThread.start()
            
        CoreLogger.Info("ResourceManager initialized.")
        
    def Load(filename: Path) -> File:
        if filename in FileManager.__Resources: return FileManager.__Resources[filename]
        
        # Client is loading the resources so they should be notified of new resource load.
        ClientLoggers.Trace("Loading Resource: {}", filename.absolute())
        
        resource = File(filename)
        resource.RefCount += 1
        resource.stream = FileManager.__StreamPool.Get()
        
        with open(filename, 'rb') as f:
            resource.stream.Write(f.read())
        
        with FileManager.__Lock: FileManager.__Resources[filename] = resource
        return resource
    
    def Release(filename: Path) -> None:
        resource = FileManager.__Resources[filename]
        resource.RefCount -= 1
        resource.stream.ResetRead()
        resource.LastReleaseTime = time()
        
    def _CacheHandler() -> None:
        while True:
            now = time()
            with FileManager.__Lock:
                toDel: List[Path] = []
                for uuid, resource in FileManager.__Resources.items():
                    if resource.RefCount == 0 and (now-resource.LastReleaseTime) > FileManager.__CacheClearTime:
                        FileManager.__StreamPool.Return(resource.stream)
                        toDel.append(uuid)
                
                for path in toDel:
                    del FileManager.__Resources[path]
                    
            sleep(FileManager.__CacheClearTime)

class FileOpener:
    def __init__(self, filename: Path) -> None:
        self.resource = FileManager.Load(filename)
        
    def __enter__(self) -> File: return self.resource
    def __exit__(self, exc_type, exc_value, trace):
        FileManager.Release(self.resource.path)
