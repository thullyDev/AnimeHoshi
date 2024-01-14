from ..handlers import produce_urlpatterns
from ..routers import Users
from django.urls import path

users = Users()

routes = [
    {"route": "", "view": users.root, "name": "home" },
    {"route": "home", "view": users.root},
]

urlpatterns = produce_urlpatterns(routes)
