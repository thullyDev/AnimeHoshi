from ..routers import Admin
from django.urls import path, include
from ..handlers import produce_urlpatterns
from ..handlers import produce_urlpatterns


admin = Admin()
routes = [
    {   
        "name": "admin_login",
        "route": "",
        "view": admin.base,
    },
    {   
        "route": "login/",
        "view": admin.admin_login,
    },
    {   
        "route": "scripts/",
        "view": admin.scripts,
    },
    {   
        "route": "general/",
        "view": admin.general,
    },
    {   
        "route": "advance/",
        "view": admin.advance,
    },
    {   
        "route": "advance/",
        "view": admin.advance,
    },
]

urlpatterns = produce_urlpatterns(routes)
urlpatterns.append(path('ajax/', include('backend.lib.urls.adminAjaxUrls')))
