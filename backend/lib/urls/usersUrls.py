from ..routers import Users
from django.urls import path

users = Users()

urlpatterns = [
    path('', users.root),
    path('home', users.root),
]
