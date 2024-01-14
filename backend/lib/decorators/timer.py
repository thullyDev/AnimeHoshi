import time

def timer(func):
    def wrapper(request, *args, **kwargs):
        start_time = time.time()
        response = func(request, *args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")
        return response
    return wrapper