from django.shortcuts import render, redirect
from ..decorators import timing_decorator
from .base import Base
from .ajax import AdminAjax

admin_ajax = AdminAjax()

class Admin(Base):
    @timing_decorator
    def dashboard(self, request):
        return self.root(request=request)

    @timing_decorator
    def scripts(self, request):
        return self.root(request=request)

    @timing_decorator
    def general(self, request):
        return self.root(request=request)

    @timing_decorator
    def advance(self, request):
        return self.root(request=request)   

    @timing_decorator
    def admins(self, request):
        return self.root(request=request)   