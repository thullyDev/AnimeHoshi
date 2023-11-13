from .lib.routers import Users, UsersAjax
from django.urls import path

users = Users()
users_ajax = UsersAjax()

urlpatterns = [
    path('', users.root, name="index"),
    path('home', users.root, name="home"),
    path("ajax/post/login/", users_ajax.login, name="login"),
    path("ajax/post/signup/", users_ajax.signup, name="signup"),
    path("ajax/post/resend/", users_ajax.resend_code, name="resend"),
    path("ajax/post/forgot_password/", users_ajax.forgot_password, name="forgot_password"),
    path("ajax/post/verify/", users_ajax.verify, name="verify"),
    path("ajax/post/profile/", users_ajax.profile, name="profile"),
]