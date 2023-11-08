from django.contrib import admin
from django.urls import path
# from django.views.generic import TemplateView
from .lib.routers.users import Users

users = Users()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', users.root, name="index"),
    path('home', users.root, name="home"),
]
