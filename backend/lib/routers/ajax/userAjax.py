from django.shortcuts import render, redirect
from ...resources import (
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
    get_data_from_string,
    generate_unique_id,
)
from ...database import UserDatabase
from ...decorators import userValidator
from ..base import Base

database = UserDatabase()

class UserAjax(Base):
    @userValidator
    def add_to_list(self, request, user, **kwargs):
        if not request.POST: return redirect("/")

        post_data = get_data_from_string(post_data.get("data"))
        
        user_id = user.get("id")

        if not slug: return self.bad_request_response(data={ "message": "slug invalid"})
