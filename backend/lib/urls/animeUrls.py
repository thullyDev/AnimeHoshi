from ..handlers import produce_urlpatterns
from ..routers import Anime
from django.urls import path

anime = Anime()

routes = [
    {"route": "home/", "view": anime.home},
    {"route": "tioanime/filter/", "view": anime.tioanime_filter},
    {"route": "latanime/filter/", "view": anime.latanime_filter},
    {"route": "tioanime/schedule/", "view": anime.tioanime_schedule},
    {"route": "latanime/schedule/", "view": anime.latanime_schedule},
    {"route": "latanime/search/", "view": anime.latanime_search},
    {"route": "tioanime/anime/<str:slug>/", "view": anime.tioanime_anime},
    {"route": "latanime/anime/<str:slug>/", "view": anime.latanime_anime},
    {"route": "tioanime/watch/<str:slug>/", "view": anime.tioanime_watch},
    {"route": "latanime/watch/<str:slug>/", "view": anime.latanime_watch},
    {"route": "stream/<str:encrypted_link>/", "view": anime.stream},
]

urlpatterns = produce_urlpatterns(routes)
