
from typing import Optional, Callable, Any
from functools import wraps



def log_to_file_or_console(filename: Optional[str] = None) -> Callable:
    def log_decorator (func: Callable) -> Callable:
        @wraps(func)
        def wrapper (*args, **kwargs) -> Any:
            if filename is None:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok!")
                    return result
                except Exception as error:
                    print(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}. ")
                    raise
            else:
                with open(filename, "a") as file:
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} ok!\n")
                        return result
                    except Exception as error:
                        file.write(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}. \n")
                        raise
        return wrapper
    return log_decorator
