from ..routers import UserAjax, User, UserAuthAjax
from django.urls import path

user = User()
user_auth_ajax = UserAuthAjax()
user_ajax = UserAjax()

urlpatterns = [
    path("ajax/get/profile", user_ajax.get_profile_data),
    path("ajax/post/add/watch", user_ajax.add_watch_list),
    path("ajax/post/add/likes", user_ajax.add_likes_list),
    path("ajax/post/login/", user_auth_ajax.login),
    path("ajax/post/signup/", user_auth_ajax.signup),
    path("ajax/post/resend/", user_auth_ajax.resend_code),
    path("ajax/post/forgot_password/", user_auth_ajax.forgot_password),
    path("ajax/post/verify/", user_auth_ajax.verify),
]