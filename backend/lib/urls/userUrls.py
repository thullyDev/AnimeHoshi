from ..handlers import produce_urlpatterns, route_producer
from ..routers import User
from django.urls import path, include

user = User()

routes = [
    route_producer(route="profile/", view=user.profile),
]

urlpatterns = produce_urlpatterns(routes)
urlpatterns.append(path('ajax/', include('backend.lib.urls.userAjaxUrls')))

