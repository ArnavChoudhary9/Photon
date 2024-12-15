def FlagEnabled(flag: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not flag:
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator
