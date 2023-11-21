# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('sqladmin/', admin.site.urls),
    path('', include('backend.urls')),
]
