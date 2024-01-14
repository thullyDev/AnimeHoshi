from django.shortcuts import render, redirect
from ..resources import generate_unique_id
from ..database import AdminDatabase
from ..handlers import set_cookies
import time

database = AdminDatabase()

def adminValidator(request_func):
    def wrapper(request_obj, *args, **kwargs):
        start_time = time.time()
        request = args[0]
        temporary_id = validating(request)

        if not temporary_id:
            return redirect("admin_login")

        response = request_func(request_obj, *args, **kwargs)
        SIXTY_DAYS = 2_592_000 * 2  #* 30 days (in seconds) * 2 = 60 days

        set_cookies(response=response,
            key="temporary_id", 
            value=temporary_id, 
            age=SIXTY_DAYS, 
        )

        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = request_func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")

        return response

    return wrapper

def validating(request):
    cookies = request.COOKIES
    email = cookies.get('email')
    username = cookies.get('username')
    temporary_id = cookies.get('temporary_id')

    if None in [email, username, temporary_id]:
        return 

    admin = database.get_admin(email=email)

    if admin == None:
        return 

    if temporary_id != admin["temporary_id"]:
        return 

    temporary_id = generate_unique_id()
    database.update_admin(data={ "email": email, "temporary_id": temporary_id })

    return temporary_id