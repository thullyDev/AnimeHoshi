import time

def timer(func):
    def wrapper(request, *args, **kwargs):
        start_time = time.time()
        request = args[0]
        GET = request.GET
        POST = request.POST
        response = func(request, GET=GET, POST=POST, *args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")
        return response
    return wrapper