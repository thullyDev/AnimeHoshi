from django.shortcuts import render, redirect
from ..resources import generate_unique_id
from ..handlers import SiteHandler, ResponseHandler
from ..database import UserDatabase
from ..handlers import set_cookies
import time

site = SiteHandler()
response_handler = ResponseHandler()
database = UserDatabase()

def userValidator(request_func):
    def wrapper(request_obj, *args, **kwargs):
        start_time = time.time()
        request = args[0]
        user = get_user(request)
        ajax = is_ajax(request)

        if not user:
            return redirect("home") if not ajax else response_handler.forbidden_response()


        site_data = site.get_site_data()
        response = request_func(
            request_obj, 
            site_data=site_data, 
            user=user,
            context={ "user_data": user, "site_data": site_data}, 
            email=user["email"], 
            username=user["username"], 
            temporary_id=user["temporary_id"], 
            *args, 
            **kwargs
            )

        SIXTY_DAYS = 2_592_000 * 2  #* 30 days (in seconds) * 2 = 60 days
        set_cookies(response=response,
            key="temporary_id", 
            value=user["temporary_id"], 
            age=SIXTY_DAYS, 
        )

        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = request_func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")

        return response

    return wrapper

def get_user(request):
    cookies = request.COOKIES
    email = cookies.get('email')
    username = cookies.get('username')
    temporary_id = cookies.get('temporary_id')

    if None in [email, username, temporary_id]:
        return 

    user = database.get_user(data={ "email": email })

    if user == None:
        return 

    # if temporary_id != user["temporary_id"]:
    #     return 

    user = database.update_user(data={ "email": email, "temporary_id": generate_unique_id() })

    del user["password"]

    return user

def is_ajax(request):
    meta = request.META
    path = meta.get("PATH_INFO")
    parts = path.split("/")

    return "ajax" in parts