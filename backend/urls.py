from django.contrib import admin
from django.urls import path
from .lib.routers import Users, UsersAjax

users = Users()
users_ajax = UsersAjax()

urlpatterns = [
    path('', users.root, name="index"),
    path('home', users.root, name="home"),
    path("ajax/post/login/", users_ajax.login, name="login"),
    path("ajax/post/signup/", users_ajax.signup, name="signup"),
    path("ajax/post/resend/", users_ajax.resend, name="resend"),
]
