from django.urls import path, include

urlpatterns = [
    path('', include('backend.lib.urls.animeUrls')),
    path('admin/', include('backend.lib.urls.adminUrls')),
    path('user/', include('backend.lib.urls.userUrls')),
]
