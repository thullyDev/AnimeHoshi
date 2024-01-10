from ..routers import AdminAjax, AdminAuthAjax
from django.urls import path

admin_ajax = AdminAjax()
admin_auth_ajax = AdminAuthAjax()

urlpatterns = [
    path("get/create_owner/", admin_ajax.create_owner),
    path("post/save/", admin_ajax.save_data),
    path("post/login/", admin_auth_ajax.login),
]

    # path("get/scripts/", admin_ajax.get_scripts),
    # path("get/attributes/", admin_ajax.get_attributes),
    # path("get/values/", admin_ajax.get_values),
    # path("get/settings/", admin_ajax.get_settings),
