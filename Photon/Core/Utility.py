from typing import Callable
from dataclasses import dataclass as DataClass

from uuid import UUID, uuid3, NAMESPACE_URL
UUID3Generator: Callable[[str], UUID] = lambda name: uuid3(NAMESPACE_URL, name)

def FlagEnabled(flag: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not flag:
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

from time import perf_counter, perf_counter_ns, time

class Time:
    class Unit:
        Second: float = 1.0
        Minute: float = 60 * Second
        Millisecond : float = Second * 10**-3
        MicroSecond : float = Second * 10**-6
        NenoSecond  : float = Second * 10**-9
    
    @staticmethod
    def Now() -> float: return time()
    @staticmethod
    def PerfCounter() -> float: return perf_counter()
    @staticmethod
    def PerfCounterNs() -> int: return perf_counter_ns()
    
    @staticmethod
    def Convert(time: float, fromUnit: float, toUnit: float) -> float:
        return time * (fromUnit / toUnit)
