from ..routers import AdminAjax, AdminAuthAjax
from ..handlers import produce_urlpatterns

admin_ajax = AdminAjax()
admin_auth_ajax = AdminAuthAjax()

routes = [
    {   
        "route": "get/create_owner/",
        "view": admin_ajax.create_owner,
    },
    {   
        "route": "post/save/",
        "view": admin_ajax.save_data,
    },
    {   
        "route": "post/login/",
        "view": admin_auth_ajax.login,
    },
]

urlpatterns = produce_urlpatterns(routes)

# path("get/scripts/", admin_ajax.get_scripts),
# path("get/attributes/", admin_ajax.get_attributes),
# path("get/values/", admin_ajax.get_values),
# path("get/settings/", admin_ajax.get_settings),