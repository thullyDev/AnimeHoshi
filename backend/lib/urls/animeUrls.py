from ..handlers import produce_urlpatterns, route_producer
from ..routers import Anime

anime = Anime()

routes = [
    route_producer(route="", view=anime.home, name="home"),
    route_producer(route="main/filter/", view=anime.tioanime_filter),
    route_producer(route="latino/filter/", view=anime.latanime_filter),
    route_producer(route="main/schedule/", view=anime.tioanime_schedule),
    route_producer(route="latino/schedule/", view=anime.latanime_schedule),
    route_producer(route="latino/search/", view=anime.latanime_search),
    route_producer(route="main/anime/<str:slug>/", view=anime.tioanime_anime),
    route_producer(route="latino/anime/<str:slug>/", view=anime.latanime_anime),
    route_producer(route="main/watch/<str:slug>/", view=anime.tioanime_watch),
    route_producer(route="latino/watch/<str:slug>/", view=anime.latanime_watch),
    route_producer(route="stream/<str:encrypted_link>/", view=anime.stream),
    route_producer(route="alert/", view=anime.alert, name="alert"),
    route_producer(route="maintenance/", view=anime.maintenance, name="maintenance"),
    route_producer(route="not_found/", view=anime.not_found, name="not_found"),
]

urlpatterns = produce_urlpatterns(routes)
