from django.shortcuts import render, redirect
from ...resources import (
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
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

        slug = request.POST.get("slug")
        user_id = user.get("id")
        temporary_id = user.get("temporary_id")

        response = self.add_to_list(slug=slug, list_type="watch", user_id=user_id, temporary_id=temporary_id)

        if not slug: return self.bad_request_response(data={ "message": "slug invalid"})
