from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import (
    ResponseHandler, 
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
    generate_unique_id,
)
from ...database import Database
from .authentication.usersAuthAjax import UsersAuthAjax

db = Database()

class UsersAjax(APIView, ResponseHandler, UsersAuthAjax):
    def profile(self, request):
        if request.POST: return redirect("/")

        cookies = request.COOKIES
        email = cookies.get("email")
        username = cookies.get("username")
        temporary_id = cookies.get("temporary_id")

        if not email and not username and not temporary_id: 
            return self.forbidden_response(data={ "message": "not authenticated" })

        user = db.get_user(email=email, username=username, temporary_id=temporary_id)

        if not user: return self.forbidden_response(data={ "message": "user does not exist" })

        is_valid = self.is_valid_temporary_id(old_temporary_id=user.get("temporary_id"), temporary_id=temporary_id)

        if not is_valid: return self.forbidden_response(data={ "message": "please login" })
        
        new_temporary_id = generate_unique_id()
        email = user.get("email")

        self.update_user(email=email, temporary_id=new_temporary_id)

        cookie_data = {
            "email": user.get("email"),
            "usename": user.get("usename"),
            "temporary_id": new_temporary_id,
        }

        data = {
            "profile_image_url": user.get("profile_image_url"),
            "wachlist": user.get("wachlist"),
            "likeslist": user.get("likeslist"),
        }
        
        return self.successful_response(data={ "data": {**cookie_data, **data} }, cookies=cookie_data, no_cookies=False)

    def is_valid_temporary_id(self, old_temporary_id, temporary_id):
        return old_temporary_id == temporary_id and temporary_id and old_temporary_id

    # def add_watch_list(self, request):
    #     if not request.POST: return redirect("/")

    #     creditials = self.GET_CREDITIALS(request.COOKIES)

    # def GET_CREDITIALS(self, DATA):
    #     CREDITIALS = { "username", "email", "temporary_id", "password", "confirm" }
    #     CREDITIALS_DATA = {key: value for key, value in DATA.items() if key in CREDITIALS }

    #     email = CREDITIALS_DATA.get("email")
    #     username = CREDITIALS_DATA.get("username")
    #     temporary_id = CREDITIALS_DATA.get("temporary_id")

    #     return CREDITIALS_DATA if CREDITIALS_DATA else None



