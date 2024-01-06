from ..routers import Admin
from django.urls import path, include

admin = Admin()

urlpatterns = [
    path("dashboard/", admin.dashboard),
    path("scripts/", admin.scripts),
    path("general/", admin.general),
    path("advance/", admin.advance),
    path("admins/", admin.admins),
    path("login/", admin.login, name="admin_login"),
    path('ajax/', include('backend.lib.urls.adminAjaxUrls')),
]
