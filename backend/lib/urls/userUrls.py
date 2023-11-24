from ..routers import UserAjax, User
from django.urls import path

user = User()
user_ajax = UserAjax()

urlpatterns = [
    path("ajax/get/profile", user_ajax.get_profile_data),
    path("ajax/post/add/watch", user_ajax.add_watch_list),
    path("ajax/post/add/likes", user_ajax.add_likes_list),
    path("ajax/post/login/", user_ajax.login),
    path("ajax/post/signup/", user_ajax.signup),
    path("ajax/post/resend/", user_ajax.resend_code),
    path("ajax/post/forgot_password/", user_ajax.forgot_password),
    path("ajax/post/verify/", user_ajax.verify),
]