from django.contrib import admin
from django.urls import path
# from django.views.generic import TemplateView
from .lib.routers.users import Users
from .lib.routers.ajax.users import UsersAjax

users = Users()
users_ajax = UsersAjax()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', users.root, name="index"),
    path('home', users.root, name="home"),
    path("ajax/login/", users_ajax.login, name="login"),
]
