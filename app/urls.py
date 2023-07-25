from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.landing, name='landing'),
	path('home', views.home, name='home'),
	path('ajax/get_home_data', views.get_home_data, name='get_home_data'),
 ]
