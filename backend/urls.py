from .lib.routers import Users, UserAjax, Anime, AnimeAjax, adminAjax
from django.urls import path

users = Users()
anime = Anime()
user_ajax = UserAjax()
anime_ajax = AnimeAjax()
admin_ajax = adminAjax()

urlpatterns = [
    path('', users.root),
    path('home', users.root),
    #***** users post request
    path("ajax/post/login/", user_ajax.login),
    path("ajax/post/signup/", user_ajax.signup),
    path("ajax/post/resend/", user_ajax.resend_code),
    path("ajax/post/forgot_password/", user_ajax.forgot_password),
    path("ajax/post/verify/", user_ajax.verify),
    path("ajax/post/profile/", user_ajax.profile),
    #***** users post request

    #***** admins request
    path("ajax/get/admin/get_scripts/", admin_ajax.get_scripts),
    path("ajax/get/admin/get_attributes/", admin_ajax.get_attributes),
    path("ajax/get/admin/get_values/", admin_ajax.get_values),
    path("ajax/get/admin/get_settings/", admin_ajax.get_settings),
    path("ajax/post/admin/save_data/", admin_ajax.save_data),
    #***** admins request

    #***** admins post request
    path("ajax/get/home/", anime_ajax.get_home_data),
    path("ajax/get/tioanime/filter/", anime_ajax.tioanime_filter),
    path("ajax/get/latanime/filter/", anime_ajax.latanime_filter),
    path("ajax/get/tioanime/schedule/", anime_ajax.tioanime_schedule),
    path("ajax/get/latanime/schedule/", anime_ajax.latanime_schedule),
    path("ajax/get/latanime/search/", anime_ajax.latanime_search),
    path("ajax/get/tioanime/anime/<str:slug>/", anime_ajax.tioanime_anime),
    path("ajax/get/latanime/anime/<str:slug>/", anime_ajax.latanime_anime),
    path("ajax/get/tioanime/watch/<str:slug>/", anime_ajax.tioanime_watch),
    path("ajax/get/latanime/watch/<str:slug>/", anime_ajax.latanime_watch),
    path("ajax/get/stream/<str:encrypted_link>/", anime_ajax.stream),
    #***** admins post request
]
