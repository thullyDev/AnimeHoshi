from django.urls import path, include

urlpatterns = [
    path('', include('backend.lib.urls.usersUrls')),
    path('admin/', include('backend.lib.urls.adminUrls')),
    path('anime/', include('backend.lib.urls.animeUrls')),
    path('user/', include('backend.lib.urls.userUrls')),
]
