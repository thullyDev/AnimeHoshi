from django.shortcuts import render, redirect
from ..decorators import userValidator
from .base import Base

class User(Base):
    @userValidator
    def profile(self, request, user):
        cookies = request.COOKIES

        data = {
            "profile_image_url": user.get("profile_image_url"),
        }
        
        return self.successful_response(data={ "data": data }, cookies=cookies, no_cookies=False)