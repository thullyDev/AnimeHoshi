from ..handlers import produce_urlpatterns
from ..routers import AnimeAjax
from django.urls import path

anime_ajax = AnimeAjax()

routes = [
    {"route": "ajax/get/home/", "view": anime_ajax.get_home_data},
    {"route": "ajax/get/tioanime/filter/", "view": anime_ajax.tioanime_filter},
    {"route": "ajax/get/latanime/filter/", "view": anime_ajax.latanime_filter},
    {"route": "ajax/get/tioanime/schedule/", "view": anime_ajax.tioanime_schedule},
    {"route": "ajax/get/latanime/schedule/", "view": anime_ajax.latanime_schedule},
    {"route": "ajax/get/latanime/search/", "view": anime_ajax.latanime_search},
    {"route": "ajax/get/tioanime/anime/<str:slug>/", "view": anime_ajax.tioanime_anime},
    {"route": "ajax/get/latanime/anime/<str:slug>/", "view": anime_ajax.latanime_anime},
    {"route": "ajax/get/tioanime/watch/<str:slug>/", "view": anime_ajax.tioanime_watch},
    {"route": "ajax/get/latanime/watch/<str:slug>/", "view": anime_ajax.latanime_watch},
    {"route": "ajax/get/stream/<str:encrypted_link>/", "view": anime_ajax.stream},
]

urlpatterns = produce_urlpatterns(routes)
