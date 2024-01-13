from .timer import timer

def validator(request_func):
    def wrapper(request, *args, **kwargs):
        response = request_func(request, *args, **kwargs)
        return response
    return timer(wrapper, FUNCTION_NAME=request_func.__name__.upper())