from ..Core.Features import LOGGING
from ..Core.Utility import FlagEnabled
from ..Core.SubscriptionInterface import SubscriptionInterface

import spdlog
from typing import List

class Logger:
    @classmethod
    def INIT(cls):
        cls.__LogSinks = [
            spdlog.stdout_color_sink_mt(),
            spdlog.basic_file_sink_mt("Asura.log", True)
        ]

    __slots__ = "__Name", "__Logger"

    def __init__(self, name: str, logPattern: str="%^[%T] [%l%$] %n: %v%$") -> None:
        self.__Name: str = name

        self.__Logger = spdlog.SinkLogger(name, Logger.__LogSinks)
        self.__Logger.set_pattern(logPattern)
        self.__Logger.set_level(spdlog.LogLevel.TRACE)
        self.__Logger.flush_on(spdlog.LogLevel.TRACE)

        self.Info("Logger *{}* Initialized!", name)

    @property
    def Name(self) -> str: return self.__Name
    
    @FlagEnabled(LOGGING)
    def Trace    (self, msg: str, *args) -> None: self.__Logger.trace    (msg.format(*args))
    
    @FlagEnabled(LOGGING)
    def Info     (self, msg: str, *args) -> None: self.__Logger.info     (msg.format(*args))
    
    @FlagEnabled(LOGGING)
    def Debug    (self, msg: str, *args) -> None: self.__Logger.debug    (msg.format(*args))
    
    @FlagEnabled(LOGGING)
    def Warn     (self, msg: str, *args) -> None: self.__Logger.warn     (msg.format(*args))
    
    @FlagEnabled(LOGGING)
    def Error    (self, msg: str, *args) -> None: self.__Logger.error    (msg.format(*args))
    
    @FlagEnabled(LOGGING)
    def Critical (self, msg: str, *args) -> None: self.__Logger.critical (msg.format(*args))

class LoggerSubscription(SubscriptionInterface[Logger]):  
    '''
    This is basically a wrapper around a list that contains many Loggers.
    The message sent to it will be distributed to all the loggers that have subscribed to it.

    Usage::

        loggers = LoggerSubscription()
        loggers.Subscribe(Logger("A"))
        loggers.Subscribe(Logger("B"))
        loggers.Trace("TEST") # Calling Trace only once

    Will produce::

        [HH:MM:SS] [trace] A: TEST
        [HH:MM:SS] [trace] B: TEST
    '''

    def __init__(self) -> None:
        super().__init__()

    def Trace    (self, msg: str, *args) -> None: self.ForEach( "Trace"    , msg,*args )
    def Info     (self, msg: str, *args) -> None: self.ForEach( "Info"     , msg,*args )
    def Debug    (self, msg: str, *args) -> None: self.ForEach( "Debug"    , msg,*args )
    def Warn     (self, msg: str, *args) -> None: self.ForEach( "Warn"     , msg,*args )
    def Error    (self, msg: str, *args) -> None: self.ForEach( "Error"    , msg,*args )
    def Critical (self, msg: str, *args) -> None: self.ForEach( "Critical" , msg,*args )
