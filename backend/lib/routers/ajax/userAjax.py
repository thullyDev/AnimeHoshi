from django.shortcuts import render, redirect
from ...resources import (
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
    generate_unique_id,
)
from ...database import Database
from ...decorators import timing_decorator
from ..base import Base

db = Database()

class UserAjax(Base):
    @timing_decorator
    def get_profile_data(self, request):
        user = GET_CREDITIALS(request.COOKIES)

        if not user: return self.forbidden_response(data={ "message": "login" })

        cookies = self.get_cookies(user)

        data = {
            "profile_image_url": user.get("profile_image_url"),
            "wachlist": user.get("wachlist"),
            "likeslist": user.get("likeslist"),
            **cookies,
        }
        
        return self.successful_response(data={ "data": data }, cookies=cookies, no_cookies=False)

    @timing_decorator
    def add_watch_list(self, request):
        user = self.GET_CREDITIALS(request.COOKIES, no_update=True)

        if not user: return self.forbidden_response(data={ "message": "login" })

        slug = request.POST.get("slug")
        user_id = user.get("id")
        temporary_id = user.get("temporary_id")

        response = self.add_to_list(slug=slug, list_type="watch", user_id=user_id, temporary_id=temporary_id)

        if not slug: return self.bad_request_response(data={ "message": "slug invalid"})

    @timing_decorator
    def add_likes_list(self, request):
        user = self.GET_CREDITIALS(request.COOKIES, no_update=True)

        if not user: return self.forbidden_response(data={ "message": "login" })

        slug = request.POST.get("slug")
        user_id = user.get("id")
        temporary_id = user.get("temporary_id")

        response = self.add_to_list(slug=slug, list_type="likes", user_id=user_id, temporary_id=temporary_id)

        if not slug: return self.bad_request_response(data={ "message": "slug invalid"})

    def is_valid_temporary_id(self, old_temporary_id, temporary_id):
        return old_temporary_id == temporary_id and temporary_id and old_temporary_id

    def GET_CREDITIALS(self, DATA, no_update=False):
        CREDITIALS = { "username", "email", "temporary_id" }
        CREDITIALS_DATA = {key: value for key, value in DATA.items() if key in CREDITIALS }

        email = CREDITIALS_DATA.get("email")
        username = CREDITIALS_DATA.get("username")
        temporary_id = CREDITIALS_DATA.get("temporary_id")

        if not email and not username and not temporary_id: 
            return None

        user = db.get_user(email=email, username=username, temporary_id=temporary_id)

        if not user: return None

        is_valid = self.is_valid_temporary_id(old_temporary_id=user.get("temporary_id"), temporary_id=temporary_id)

        if not is_valid: return None
        
        new_temporary_id = generate_unique_id()
        email = user.get("email")

        if no_update: self.update_user(email=email, temporary_id=new_temporary_id)

        user["temporary_id"] = new_temporary_id

        return user

    def get_cookies(self, data):
        cookies = {
            "email": user.get("email"),
            "usename": user.get("usename"),
            "temporary_id": user.get("temporary_id"),
        }

        return cookies

    def add_to_list(self, slug, list_type, user_id, temporary_id):
        pass
        
        # user_list = watch_list if list_type == "watch" else likes_list 
