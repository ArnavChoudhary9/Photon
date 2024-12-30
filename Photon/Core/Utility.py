from typing import Callable

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
