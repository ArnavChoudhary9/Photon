from typing import ByteString, Deque
from collections import deque

class Stream:
    '''
    A simple stream implementation with read and write operations.
    
    You can only write at the end of the stream, while read can be performed any where.
    Note reading from a stream will increment the read pointer so multiple threads should not read from same stream at one time.
    '''
    __Buffer: ByteString
    __Rptr : int
    __Wptr : int

    __Closed: bool
    
    class Whence:
        START   = 0
        CURRENT = 1
        END     = 2
    
    def __init__(self): self.Clear()
        
    def __len__(self) -> int: return self.__Wptr
        
    def Write(self, data: ByteString) -> int:
        '''
        - No write operation can be performed after stream is closed.
        - Returns the length of updated stream.
        '''
        if self.__Closed:
            raise IOError("Stream is closed.")
        self.__Wptr += len(data)  # Update write pointer after writing data to buffer
        self.__Buffer += data # type: ignore
        
        return self.__Wptr
        
    def Read(self, size: int=-1) -> ByteString:
        if size == -1:
            size = self.__Wptr
            if size == 0: raise IOError("Stream is empty.")
        if size <= 0:
            return b""
        if self.__Rptr+size > self.__Wptr:
            raise IndexError("Reached end of stream")
        
        self.__Rptr += size
        return self.__Buffer[self.__Rptr-size:self.__Rptr]
    
    def SeekRead(self, offset: int, whence: int=Whence.START) -> None:
        '''
        Sets the position of the read pointer.
        
        Whence:
            - Whence.START means offset from the start of the stream.
            - Whence.CURRENT means offset from the current position of the read pointer.
            - Whence.END means offset (in reverse direction) from the end of the stream.
                - Rptr = end-offset
        '''
        if whence == Stream.Whence.START:
            self.__Rptr = offset
        elif whence == Stream.Whence.CURRENT:
            self.__Rptr += offset
        elif whence == Stream.Whence.END:
            self.__Rptr = self.__Wptr - offset
        else:
            raise ValueError("Invalid whence value.")
        
        if self.__Rptr < 0:
            self.__Rptr = 0
        elif self.__Rptr > self.__Wptr:
            self.__Rptr = self.__Wptr
            
    def SeekWrite(self, offset: int, whence: int=Whence.START) -> None:
        '''
        Sets the position of the write pointer.
        
        Whence:
            - Whence.START means offset from the start of the stream.
            - Whence.CURRENT means offset from the current position of the read pointer.
            - Whence.END means offset (in reverse direction) from the end of the stream.
                - Rptr = end-offset
        '''
        if whence == Stream.Whence.START:
            self.__Wptr = offset
        elif whence == Stream.Whence.CURRENT:
            self.__Wptr += offset
        elif whence == Stream.Whence.END:
            self.__Wptr = self.__Wptr - offset
        else:
            raise ValueError("Invalid whence value.")
        
        if self.__Wptr < 0:
            self.__Wptr = 0
        if self.__Wptr > len(self.__Buffer):
            self.__Wptr = len(self.__Buffer)
            
    def ResetRead(self) -> None: self.__Rptr = 0

    def Clear(self) -> None:
        self.__Buffer = b""
        self.__Rptr, self.__Wptr = 0, 0
        self.__Closed = False
    
    def Close(self) -> None: self.__Closed = True
    
    @property
    def Closed(self) -> bool: return self.__Closed
    @property
    def Empty(self) -> bool: return (self.__Wptr == 0)
    @property
    def Readable(self) -> bool: return not (self.__Rptr == self.__Wptr)
    @property
    def ReadyRead(self) -> bool: return self.Readable and self.Closed
    
class StreamPool:
    __FreeStreams: Deque[Stream]
    __MaxLimit: int
    
    def __init__(self, max_limit: int):
        self.__FreeStreams = deque()
        self.__MaxLimit = max_limit
        
    def Get(self) -> Stream:
        if len(self.__FreeStreams): return self.__FreeStreams.pop()
        return Stream()
    
    def Return(self, stream: Stream) -> None:
        stream.Clear()  # Clear the stream before returning it to pool
        if len(self.__FreeStreams) < self.__MaxLimit:
            self.__FreeStreams.append(stream)
        else:
            del stream
