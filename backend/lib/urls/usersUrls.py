from ..handlers import produce_urlpatterns, route_producer
from ..routers import Users
from django.urls import path

users = Users()

routes = [
    route_producer(route="", view=users.root, name="home"),
    route_producer(route="home/", view=users.root),
]

urlpatterns = produce_urlpatterns(routes)
