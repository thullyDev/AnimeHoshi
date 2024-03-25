from ..handlers import ResponseHandler, ApiHandler
from ..resources import CAPTCHA_SECRET_KEY
import time

api = ApiHandler()
response_handler = ResponseHandler()

def captchaValidator(func):
    def wrapper(request_obj, *args, **kwargs):
        start_time = time.time()
        request = args[0]
        GET = request.GET
        POST = request.POST

        if not valid_captcha(POST): return response_handler.forbidden_response()

        response = func(request_obj, GET=GET, POST=POST, *args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")
        return response
    return wrapper

def valid_captcha(POST):
    token = POST.get("captcha_token", "")
    data = {
        "response": token,
        "secret": CAPTCHA_SECRET_KEY,
    }

    response = api.request(base="api.hcaptcha.com", endpoint="/siteverify", post=True, params=data)
    success = response.get("success", False)

    return success == True