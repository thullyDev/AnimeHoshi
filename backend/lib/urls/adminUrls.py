from ..routers import Admin, AdminAjax, AdminAuthAjax
from django.urls import path

admin = Admin()
admin_ajax = AdminAjax()
admin_auth_ajax = AdminAuthAjax()

urlpatterns = [
    path("dashboard/", admin.dashboard),
    path("scripts/", admin.scripts),
    path("general/", admin.general),
    path("advance/", admin.advance),
    path("admins/", admin.admins),
    
    path("ajax/get/dashboard/", admin_ajax.dashboard),
    path("ajax/get/scripts/", admin_ajax.get_scripts),
    path("ajax/get/attributes/", admin_ajax.get_attributes),
    path("ajax/get/values/", admin_ajax.get_values),
    path("ajax/get/settings/", admin_ajax.get_settings),
    path("ajax/post/save_data/", admin_ajax.save_data),
]