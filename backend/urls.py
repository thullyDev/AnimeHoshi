from .lib.routers import Users, UsersAjax, Anime, AnimeAjax
from django.urls import path

users = Users()
anime = Anime()
users_ajax = UsersAjax()
anime_ajax = AnimeAjax()

urlpatterns = [
    path('', users.root),
    path('home', users.root),
    path("ajax/post/login/", users_ajax.login),
    path("ajax/post/signup/", users_ajax.signup),
    path("ajax/post/resend/", users_ajax.resend_code),
    path("ajax/post/forgot_password/", users_ajax.forgot_password),
    path("ajax/post/verify/", users_ajax.verify),
    path("ajax/post/profile/", users_ajax.profile),
    path("ajax/get/home/", anime_ajax.get_home_data),
    path("ajax/get/tioanime/filter/", anime_ajax.tioanime_filter),
    path("ajax/get/latanime/filter/", anime_ajax.latanime_filter),
    path("ajax/get/tioanime/schedule/", anime_ajax.tioanime_schedule),
    path("ajax/get/latanime/schedule/", anime_ajax.latanime_schedule),
    path("ajax/get/latanime/search/", anime_ajax.latanime_search),
    path("ajax/get/tioanime/anime/<str:slug>/", anime_ajax.tioanime_anime),
]