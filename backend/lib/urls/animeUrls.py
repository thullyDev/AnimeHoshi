from ..routers import AnimeAjax
from django.urls import path

anime_ajax = AnimeAjax()

urlpatterns = [
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
]