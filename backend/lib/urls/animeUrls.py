from ..handlers import produce_urlpatterns, route_producer
from ..routers import Anime

anime = Anime()

routes = [
    route_producer(route="home/", view=anime.home),
    route_producer(route="tioanime/filter/", view=anime.tioanime_filter),
    route_producer(route="latanime/filter/", view=anime.latanime_filter),
    route_producer(route="tioanime/schedule/", view=anime.tioanime_schedule),
    route_producer(route="latanime/schedule/", view=anime.latanime_schedule),
    route_producer(route="latanime/search/", view=anime.latanime_search),
    route_producer(route="tioanime/anime/<str:slug>/", view=anime.tioanime_anime),
    route_producer(route="latanime/anime/<str:slug>/", view=anime.latanime_anime),
    route_producer(route="tioanime/watch/<str:slug>/", view=anime.tioanime_watch),
    route_producer(route="latanime/watch/<str:slug>/", view=anime.latanime_watch),
    route_producer(route="stream/<str:encrypted_link>/", view=anime.stream),
]

urlpatterns = produce_urlpatterns(routes)
