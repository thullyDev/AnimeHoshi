from ..routers import AdminAjax, AdminAuthAjax
from ..handlers import produce_urlpatterns, route_producer

admin_ajax = AdminAjax()
admin_auth_ajax = AdminAuthAjax()

routes = [
    route_producer(route="get/create_owner/", view=admin_ajax.create_owner),
    route_producer(route="post/save/", view=admin_ajax.save_data),
    route_producer(route="post/login/", view=admin_auth_ajax.login),
    # route_producer(route="get/scripts/", view=admin_ajax.get_scripts),
    # route_producer(route="get/attributes/", view=admin_ajax.get_attributes),
    # route_producer(route="get/values/", view=admin_ajax.get_values),
    # route_producer(route="get/settings/", view=admin_ajax.get_settings),
]

urlpatterns = produce_urlpatterns(routes)
