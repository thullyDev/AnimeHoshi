from django.shortcuts import redirect
from ..decorators import adminValidator, timer
from ..handlers import SiteHandler
from ..scraping import TioanimeScraper, LatanimeScraper
from ..database import AdminDatabase
from .base import Base
from .ajax import AdminAjax
from .anime import Anime

anime = Anime()
site = SiteHandler()
admin_database = AdminDatabase()
tioanime = TioanimeScraper()
latanime = LatanimeScraper()

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
        views = admin_database.cget(name="site_views")
        views = 0 if not views else views 
        scripts = len(site_data.get("scripts", ""))
        raw_tioanimes = tioanime.get_filter(data={ "page": 1 })
        raw_latanimes = latanime.get_filter(data={ "page": 1 })
        tioanimes = anime.filter_data_processing(rawdata=raw_tioanimes, base=tioanime.base)
        latanimes = anime.filter_data_processing(rawdata=raw_latanimes, base=latanime.base)

        analytics = [
            {"icon": "fas fa-user", "numbers": len(users), "label": "Users"},
            {"icon": "fas fa-user-cog", "numbers": len(admins), "label": "Admins"},
            {"icon": "fas fa-eye", "numbers": views, "label": "Weekly Views"},
            {"icon": "fas fa-code", "numbers": scripts, "label": "Scripts"},
        ]

        # do proper pagination here
        user_page = 1
        user_amount_pages = 100

        self.set_context(context=context, data={
            "analytics": analytics,
            "users": users,
            "tioanimes": tioanimes["animes"],
            "latanimes": latanimes["animes"],
            "latanimes_pages": {
                "page": latanimes["page"],
                "pages": latanimes["pages"],
            },
            "tioanimes_pages": {
                "page": latanimes["page"],
                "pages": tioanimes["pages"],
            },
            "users_pages": {
                "page": user_page,
                "pages": user_amount_pages,
            }

        })
        return self.root(request=request, context=context, template="pages/admin/dashboard.html")

    @adminValidator
    def scripts(self, request, site_data, context):
        scripts = site_data["scripts"]
        head_scripts = scripts["head_scripts"]
        foot_scripts = scripts["foot_scripts"]
        ads_scripts = scripts["ads_scripts"]

        self.set_context(context=context, data={
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

        self.set_context(context=context, data={
            "images": images,
            "inputs": inputs,
            "socials": socials,
        })
        return self.root(request=request, context=context, template="pages/admin/general.html")

    @adminValidator
    def advance(self, request, site_data, context):
        settings = site_data["settings"]
        self.set_context(context=context, data={
            "settings": settings,
        })
        return self.root(request=request, context=context, template="pages/admin/advance.html")   

    @adminValidator
    def admins(self, request, site_data, context):
        admins = admin_database.get_admins()
        self.set_context(context=context, data={
            "admins": admins,
            "admins_count": len(admins),
        })
        return self.root(request=request, context=context, template="pages/admin/admins.html")   
