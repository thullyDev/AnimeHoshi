from django.shortcuts import render, redirect
from ..database import UserDatabase
from ..decorators import userValidator
from .base import Base

database = UserDatabase()

class User(Base):
    @userValidator
    def profile(self, request, user, context, **kwargs):
        user_list = database.get_list(user)
        context['user_list'] = user_list
        return self.root(request=request, context=context, template="pages/user/profile.html")
        