from django.shortcuts import render, redirect
from ..decorators import timing_decorator
from .base import Base
from .ajax import AdminAjax

admin_ajax = AdminAjax()

class Admin(Base):
    @timing_decorator
    def dashboard(self, request):
        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        if not user: return redirect("/admin/login")

        context = {
        	"page": "dashboard",
        }

        return self.root(request, context=context)