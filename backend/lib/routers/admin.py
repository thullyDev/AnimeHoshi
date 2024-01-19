from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..decorators import adminValidator, timer
from ..handlers import SiteHandler
from ..scraping import TioanimeScraper, LatanimeScraper
from ..database import AdminDatabase
from .base import Base
from .ajax import AdminAjax
from .anime import Anime
from pprint import pprint
import json

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
    def dashboard(self, request, site_data, context, **kwargs):
        # gets data from GET
        get_data = request.GET
        users_keyword = get_data.get("user_keyword")
        users_page = get_data.get("users_page", 1)
        tioanime_keyword = get_data.get("tioanime_keyword", "")
        latanime_keyword = get_data.get("latanime_keyword", "")
        latanime_page = get_data.get("latanime_page", 1)
        tioanime_page = get_data.get("tioanime_page", 1)
        # end

        # /admin/dashboard/?{{content}}_page={{ i }}

        admins = admin_database.get_admins()
        users = admin_database.get_query_users(query=users_keyword) if users_keyword else admin_database.get_users()
        views = admin_database.cget(name="site_views")
        views = 0 if not views else views 
        scripts = site_data.get("scripts", "")

        count = 0
        for inner_key, inner_scripts in scripts.items():
            for key, script in inner_scripts.items():
                if script['value']: count += 1

        raw_tioanimes = tioanime.get_filter(data={ "page": tioanime_page, "keywords": tioanime_keyword })
        raw_latanimes = latanime.get_filter(data={ "page": latanime_page, "keywords": latanime_keyword })

        tioanimes = anime.filter_data_processing(rawdata=raw_tioanimes, base=tioanime.base)
        latanimes = anime.filter_data_processing(rawdata=raw_latanimes, base=latanime.base)

        analytics = [
            {"icon": "fas fa-user", "numbers": len(users), "label": "Users"},
            {"icon": "fas fa-user-cog", "numbers": len(admins), "label": "Admins"},
            {"icon": "fas fa-eye", "numbers": views, "label": "Weekly Views"},
            {"icon": "fas fa-code", "numbers": count, "label": "Scripts"},
        ]

        paginated_users, pages = self.paginate(data=users, page=users_page)

        self.set_context(context=context, data={
            "analytics": analytics,
            "users": paginated_users,
            "tioanimes": tioanimes["animes"],
            "latanimes": latanimes["animes"],
            "latanimes_pages": {
                "page": latanimes["page"],
                "pages": latanimes["pages"],
                "query_url": tioanime.build_url(
                    base="", 
                    endpoint="/admin/dashboard/", 
                    params={ "page": tioanimes["page"], "latanimes_keywords": latanime_keyword }
                    )
            },
            "tioanimes_pages": {
                "page": tioanimes["page"],
                "pages": tioanimes["pages"],
                "query_url": tioanime.build_url(
                    base="", 
                    endpoint="/admin/dashboard/", 
                    params={ "page": tioanimes["page"], "tioanime_keywords": tioanime_keyword }
                    )
            },
            "users_pages": {
                "page": users_page,
                "pages": pages,
                "query_url": tioanime.build_url(
                    base="", 
                    endpoint="/admin/dashboard/", 
                    params={ "page": users_page, "user_keyword": tioanime_keyword }
                    )
            }

        })
        return self.root(request=request, context=context, template="pages/admin/dashboard.html")

    @adminValidator
    def scripts(self, request, site_data, context, **kwargs):
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
    def general(self, request, site_data, context, **kwargs):
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
    def advance(self, request, site_data, context, **kwargs):
        # settings = json.loads(json.dumps(site_data["settings"]))
        settings = site_data["settings"]
        self.set_context(context=context, data={
            "settings": settings,
        })
        return self.root(request=request, context=context, template="pages/admin/advance.html")   

    @adminValidator
    def admins(self, request, site_data, context, **kwargs):
        admins = admin_database.get_admins()
        self.set_context(context=context, data={
            "admins": admins,
            "admins_count": len(admins),
        })
        return self.root(request=request, context=context, template="pages/admin/admins.html")   

    def paginate(self, data, page, limit=20):
        paginator = Paginator(data, limit) 

        try:
            paginated = paginator.page(page)
        except EmptyPage:
            paginated = paginator.page(paginator.num_pages)

        return paginated, paginator.num_pages