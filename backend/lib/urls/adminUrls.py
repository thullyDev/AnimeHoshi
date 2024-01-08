from ..routers import Admin
from django.urls import path, include

admin = Admin()

urlpatterns = [
    path("", admin.base),
    path("login/", admin.admin_login, name="admin_login"),
    path("dashboard/", admin.dashboard),
    path("scripts/", admin.scripts),
    path("general/", admin.general),
    path("advance/", admin.advance),
    path("admins/", admin.admins),
    path('ajax/', include('backend.lib.urls.adminAjaxUrls')),
]
