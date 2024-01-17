from ..routers import AdminAjax, AdminAuthAjax
from ..handlers import produce_urlpatterns, route_producer

admin_ajax = AdminAjax()
admin_auth_ajax = AdminAuthAjax()

routes = [
    route_producer(route="get/create_owner/", view=admin_ajax.create_owner),
    route_producer(route="post/save/", view=admin_ajax.save_data),
    route_producer(route="post/login/", view=admin_auth_ajax.login),
    route_producer(route="post/add_admin/", view=admin_ajax.add_admin),
]

urlpatterns = produce_urlpatterns(routes)
