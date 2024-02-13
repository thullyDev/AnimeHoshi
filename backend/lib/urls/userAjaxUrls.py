from ..routers import UserAjax, UserAuthAjax
from ..handlers import produce_urlpatterns, route_producer

user_auth_ajax = UserAuthAjax()
user_ajax = UserAjax()

routes = [
    route_producer(route="ajax/get/logout/", view=user_auth_ajax.logout),
    route_producer(route="ajax/post/add/list/", view=user_ajax.add_to_list),
    route_producer(route="ajax/post/change_user_details/", view=user_ajax.change_user_details),
    route_producer(route="ajax/post/login/", view=user_auth_ajax.login),
    route_producer(route="ajax/post/login/", view=user_auth_ajax.login),
    route_producer(route="ajax/post/signup/", view=user_auth_ajax.signup),
    route_producer(route="ajax/post/resend/", view=user_auth_ajax.resend_code),
    route_producer(route="ajax/post/forgot_password/", view=user_auth_ajax.forgot_password),
    route_producer(route="ajax/post/renew_password/", view=user_auth_ajax.renew_password),
    route_producer(route="ajax/post/verify/", view=user_auth_ajax.verify),
]

urlpatterns = produce_urlpatterns(routes)
