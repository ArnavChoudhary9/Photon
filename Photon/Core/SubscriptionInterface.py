from typing import Generic, TypeVar, List

_T = TypeVar('_T')

class SubscriptionInterface(Generic[_T]):
    __slots__ = "_Subscriptions"
    _Subscriptions: List[_T]
    
    def __init__(self) -> None: self._Subscriptions = []
    
    def Subscribe(self, obj: _T) -> None: self._Subscriptions.append(obj)
    def Unsubscribe(self, obj: _T) -> None: self._Subscriptions.remove(obj)
    
    def ForEach(self, callable: str, *args, **kwargs) -> None:
        for sub in self._Subscriptions: getattr(sub, callable)(*args, **kwargs)
