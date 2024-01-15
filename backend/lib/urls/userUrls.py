from ..handlers import produce_urlpatterns, route_producer
from ..routers import User, UserAjax, UserAuthAjax
from django.urls import path

user = User()
user_auth_ajax = UserAuthAjax()
user_ajax = UserAjax()

routes = [
    route_producer(route="ajax/get/profile/", view=user_ajax.get_profile_data),
    route_producer(route="ajax/post/add/watch/", view=user_ajax.add_watch_list),
    route_producer(route="ajax/post/add/likes/", view=user_ajax.add_likes_list),
    route_producer(route="ajax/post/login/", view=user_auth_ajax.login),
    route_producer(route="ajax/post/signup/", view=user_auth_ajax.signup),
    route_producer(route="ajax/post/resend/", view=user_auth_ajax.resend_code),
    route_producer(route="ajax/post/forgot_password/", view=user_auth_ajax.forgot_password),
    route_producer(route="ajax/post/verify/", view=user_auth_ajax.verify),
]

urlpatterns = produce_urlpatterns(routes)
