from django.shortcuts import redirect
from ..decorators import adminValidator, timer
from ..handlers import SiteHandler
from ..database import AdminDatabase
from .base import Base
from .ajax import AdminAjax

admin_ajax = AdminAjax()
site = SiteHandler()
admin_database = AdminDatabase()

class Admin(Base):
    @timer
    def base(self, request):
        return redirect("admin_login")

    @timer
    def admin_login(self, request):
        return self.root(request=request, context={}, template="pages/admin/login.html")   
   
    @adminValidator
    def dashboard(self, request, site_data, context):
        admins = admin_database.get_admins()
        users = admin_database.get_users()
        views = 0 # get_site_views() use a analytics like google analytics to get the views
        scripts = len(site_data.get("scripts", ""))

        # weird side affect is adding 6 empty admins, they're safe tho
        # analytics = {
        #     "users": len(users) - 6,
        #     "admins": len(admins) - 6, 
        #     "views": views,
        #     "scripts": scripts,
        # }

        # do proper analytical_cards rendering, hope you understand
        analytics = [
            {"icon": "fas fa-user", "numbers": len(users) - 6, "label": "Users"},
            {"icon": "fas fa-user-cog", "numbers": len(admins) - 6, "label": "Admins"},
            {"icon": "fas fa-eye", "numbers": views, "label": "Weekly Views"},
            {"icon": "fas fa-code", "numbers": scripts, "label": "Scripts"},
        ]

        # do proper pagination here
        user_page = 1
        user_amount_pages = 100

        set_context(context=context, data={
            "analytics": analytics,
            "users": users,
            # "animes": animes,
            "pages": {
                "user_page": user_page,
                "user_amount_pages": user_amount_pages,
            }
        })
        return self.root(request=request, context=context, template="pages/admin/dashboard.html")

    @adminValidator
    def scripts(self, request, site_data, context):
        scripts = site_data["scripts"]
        head_scripts = scripts["head_scripts"]
        foot_scripts = scripts["foot_scripts"]
        ads_scripts = scripts["ads_scripts"]
        
        set_context(context=context, data={
            "head_scripts": head_scripts,
            "foot_scripts": foot_scripts,
            "ads_scripts": ads_scripts,
        })
        return self.root(request=request, context=context, template="pages/admin/scripts.html")

    @adminValidator
    def general(self, request, site_data, context):
        values = site_data["values"]
        images = values["images"]
        inputs = values["inputs"]
        socials = values["socials"]

        set_context(context=context, data={
            "images": images,
            "inputs": inputs,
            "socials": socials,
        })
        return self.root(request=request, context=context, template="pages/admin/general.html")

    @adminValidator
    def advance(self, request, site_data, context):

        set_context(context=context, data={
            "settings": settings,
        })
        return self.root(request=request, context=context, template="pages/admin/advance.html")   

    @adminValidator
    def admins(self, request, site_data, context):
        set_context(context=context, data={
            "admins_items": admins_items,
            "admins_count": len(admins_items),
        })
        return self.root(request=request, context=context, template="pages/admin/admins.html")   
