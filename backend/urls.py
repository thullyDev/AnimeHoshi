from .lib.routers import Users, UsersAjax, Anime, AnimeAjax
from django.urls import path

users = Users()
anime = Anime()
users_ajax = UsersAjax()
anime_ajax = AnimeAjax()

urlpatterns = [
    path('', users.root, name="index"),
    path('home', users.root, name="home"),
    path("ajax/post/login/", users_ajax.login, name="login"),
    path("ajax/post/signup/", users_ajax.signup, name="signup"),
    path("ajax/post/resend/", users_ajax.resend_code, name="resend"),
    path("ajax/post/forgot_password/", users_ajax.forgot_password, name="forgot_password"),
    path("ajax/post/verify/", users_ajax.verify, name="verify"),
    path("ajax/post/profile/", users_ajax.profile, name="profile"),
    path("ajax/get/home/", anime_ajax.home, name="get_home_data"),
    path("ajax/get/filter/<str:site>/", anime_ajax.filter, name="get_filter_data"),
    path("ajax/get/schedule/tioanime/", anime_ajax.schedule, name="get_schedule_data"),
]