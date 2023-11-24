from ..routers import Admin, AdminAjax 
from django.urls import path

admin = Admin()
admin_ajax = AdminAjax()

urlpatterns = [
    path("ajax/get/scripts/", admin_ajax.get_scripts),
    path("ajax/get/attributes/", admin_ajax.get_attributes),
    path("ajax/get/values/", admin_ajax.get_values),
    path("ajax/get/settings/", admin_ajax.get_settings),
    path("ajax/post/save_data/", admin_ajax.save_data),
]