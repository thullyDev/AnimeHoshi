from django.shortcuts import render, redirect
from ..decorators import userValidator
from .base import Base

class User(Base):
    @userValidator
    def profile(self, request, user, context, **kwargs):
        return self.root(request=request, context=context, template="pages/user/profile.html")
        