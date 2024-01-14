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
    def dashboard(self, request, context):
        # analytics = [
        #     {"icon": "fas fa-user", "numbers": 0, "label": "Users"},
        #     {"icon": "fas fa-user-cog", "numbers": 0, "label": "Admins"},
        #     {"icon": "fas fa-eye", "numbers": 0, "label": "Weekly Views"},
        #     {"icon": "fas fa-code", "numbers": 0, "label": "Scripts"},
        # ]
        admins = admin_database.get_admins()
        users = admin_database.get_users()

        analytics = {
            "users": 0,
            "admins": 0,
            "views": 0,
            "scripts": 0,
        }
        users = [
            {
                "id": 0,
                "username": "animeGirl",
                "email": "animegirl@gmail.com",
                "profile_image": "https://i.pinimg.com/564x/07/d4/34/07d434bcb00e39c8e8d25df1cc89a333.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 1,
                "username": "animeBoy",
                "email": "animeBoy@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/ef/e9/73/efe97322d26afdbb85e03c52b1db7c10.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 2,
                "username": "Megumi",
                "email": "megumi@gmail.com",
                "profile_image": "https://i.pinimg.com/736x/02/05/28/020528711a47abd638ed5ee670cc4705.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 3,
                "username": "Gojo",
                "email": "gojo@gmail.com",
                "profile_image": "https://i.pinimg.com/736x/50/c4/bd/50c4bdba9bbe22a46733edbdb55b65a2.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 4,
                "username": "Kenji",
                "email": "kenji@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/85/42/bb/8542bb42f5e7369e953049fa14ba5170.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 5,
                "username": "sky",
                "email": "sky@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/1d/da/d3/1ddad3615c85b90dccd31c2b5fbcb5a1.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 6,
                "username": "vi",
                "email": "viCatlin@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/e5/60/0e/e5600eac05e07ae2e74492d5060130f0.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 7,
                "username": "jayce",
                "email": "jayce@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/61/b9/59/61b9595898d45dd9e20261a5864455c6.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 8,
                "username": "jinx",
                "email": "jinx@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/7b/48/e1/7b48e1b4561ab7962b582ca20f78e914.jpg",
                "deleted": False,
                "disabled": False,
            },
            {
                "id": 9,
                "username": "nightGirl",
                "email": "nightGirl@gmail.com",
                "profile_image": "https://i.pinimg.com/236x/79/94/e7/7994e7bfaa011c4c4d0675e09cea4d3a.jpg",
                "deleted": False,
                "disabled": False,
            },
        ]

        animes = [
            {
                "id": 0,
                "title": "Sousou no Frieren",
                "slug": "sousou-no-frieren",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 1,
                "title": "Sousou no Frieren 2",
                "slug": "sousou-no-frieren-2",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 2,
                "title": "Sousou no Frieren 3",
                "slug": "sousou-no-frieren-3",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 3,
                "title": "Sousou no Frieren 4",
                "slug": "sousou-no-frieren-4",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 4,
                "title": "Sousou no Frieren 5",
                "slug": "sousou-no-frieren-5",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 5,
                "title": "Sousou no Frieren 6",
                "slug": "sousou-no-frieren-6",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 6,
                "title": "Sousou no Frieren 7",
                "slug": "sousou-no-frieren-7",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 7,
                "title": "Sousou no Frieren 8",
                "slug": "sousou-no-frieren-8",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 8,
                "title": "Sousou no Frieren 9",
                "slug": "sousou-no-frieren-9",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
            {
                "id": 9,
                "title": "Sousou no Frieren 10",
                "slug": "sousou-no-frieren-10",
                "poster_url": "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
                "disabled": False,
            },
        ]
        page = 1
        amount_pages = 100

        set_context(context=context, data={
            "analytics": analytics,
            "users": users,
            "animes": animes,
            "pages": {
                "page": page,
                "amount_pages": amount_pages,
            }
        })
        return self.root(request=request, context=context, template="pages/admin/dashboard.html")

    @adminValidator
    def scripts(self, request, context):
        head_scripts = [
            {"name": "global_head", "value": ""},
            {"name": "home_head", "value": ""},
            {"name": "landing_head", "value": ""},
            {"name": "filter_head", "value": ""},
            {"name": "profile_head", "value": ""},
            {"name": "anime_head", "value": ""},
            {"name": "watch_head", "value": ""},
            {"name": "watch_together_browsing_head", "value": ""},
            {"name": "watch_together_anime_head", "value": ""},
        ]

        foot_scripts = [
            {"name": "global_foot", "value": ""},
            {"name": "home_foot", "value": ""},
            {"name": "landing_foot", "value": ""},
            {"name": "filter_foot", "value": ""},
            {"name": "profile_foot", "value": ""},
            {"name": "anime_foot", "value": ""},
            {"name": "watch_foot", "value": ""},
            {"name": "watch_together_browsing_foot", "value": ""},
            {"name": "watch_together_anime_foot", "value": ""},
        ]

        ads_scripts = {
            "global": [
                {"name": "top_advertisement", "value": "", "height": ""},
                {"name": "bottom_advertisement", "value": "", "height": ""},
            ],
            "landing": [
                {"name": "middle_advertisement", "value": "", "height": ""},
            ],
            "watch": [
                {"name": "under_player_advertisement", "value": "", "height": ""},
                {"name": "under_suggestions_advertisement", "value": "", "height": ""},
            ],
        }

        set_context(context=context, data={
            "head_scripts": head_scripts,
            "foot_scripts": foot_scripts,
            "ads_scripts": ads_scripts,
        })
        return self.root(request=request, context=context, template="pages/admin/scripts.html")

    @adminValidator
    def general(self, request, context):
        images = [
            {"key": "site_logo", "value": "/static/images/site-logo.png"},
            {"key": "favicon_logo", "value": "/static/images/favicon.png"},
            {"key": "alert", "value": "/static/images/gifs/alert.gif"},
            {"key": "maintenance", "value": "/static/images/gifs/maintenance.gif"},
            {"key": "empty", "value": "/static/images/gifs/empty.gif"},
        ]
        inputs = [
            {"value": "AnimeHoshi", "key": "site_name"},
            {"value": "admin@animehoshi.com", "key": "email"},
            {"value": "Watch Anime On AnimeHoshi For No ads | AnimeHoshi", "key": "title"},
            {
                "value": "AnimeHoshi is a vibrant online platform offering a diverse collection of anime content for free streaming. With an extensive library spanning genres and popular titles, AnimeHoshi provides enthusiasts with an immersive experience. User-friendly navigation and high-quality playback make it a go-to destination for anime lovers seeking free, accessible entertainment.",
                "key": "site_description",
                "type": "field",
            },
        ]

        socials = [
            {"value": "https://discord.com/", "key": "discord"},
            {"value": "https://twitter.com/", "key": "twitter"},
            {"value": "https://reddit.com/", "key": "reddit"},
            {"value": "https://ko-fi.com/", "key": "donate"},
        ]

        set_context(context=context, data={
            "images": images,
            "inputs": inputs,
            "socials": socials,
        })
        return self.root(request=request, context=context, template="pages/admin/general.html")

    @adminValidator
    def advance(self, request, context):
        settings = [
            {"key": "maintanence", "value": False},
            {"key": "adblocker_detection", "value": True},
            {"key": "alert", "value": True},
            {"key": "authentication", "value": True},
            {"key": "anime", "value": True},
            {"key": "watch", "value": True},
            {"key": "watch_togather", "value": True},
            {"key": "user", "value": True},
            {"key": "schedule", "value": True},
            {"key": "features", "value": True},
            {"key": "footer", "value": True},
            {"key": "landing", "value": True},
            {"key": "donation", "value": True},
            {"key": "socials", "value": True},
            {"key": "contact", "value": True},
            {"key": "dark_mode", "value": True},
        ]

        set_context(context=context, data={
            "settings": settings,
        })
        return self.root(request=request, context=context, template="pages/admin/advance.html")   

    @adminValidator
    def admins(self, request, context):
        admins_items = [
                {
                    'id': 0,
                    'username': 'animeGirl',
                    'email': 'animegirl@gmail.com',
                    'profile_image': 'https://i.pinimg.com/564x/07/d4/34/07d434bcb00e39c8e8d25df1cc89a333.jpg',
                    'deleted': False,
                },
                {
                    'id': 1,
                    'username': 'animeBoy',
                    'email': 'animeBoy@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/ef/e9/73/efe97322d26afdbb85e03c52b1db7c10.jpg',
                    'deleted': False,
                },
                {
                    'id': 2,
                    'username': 'Megumi',
                    'email': 'megumi@gmail.com',
                    'profile_image': 'https://i.pinimg.com/736x/02/05/28/020528711a47abd638ed5ee670cc4705.jpg',
                    'deleted': False,
                },
                {
                    'id': 3,
                    'username': 'Gojo',
                    'email': 'gojo@gmail.com',
                    'profile_image': 'https://i.pinimg.com/736x/50/c4/bd/50c4bdba9bbe22a46733edbdb55b65a2.jpg',
                    'deleted': False,
                },
                {
                    'id': 4,
                    'username': 'Kenji',
                    'email': 'kenji@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/85/42/bb/8542bb42f5e7369e953049fa14ba5170.jpg',
                    'deleted': False,
                },
                {
                    'id': 5,
                    'username': 'sky',
                    'email': 'sky@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/1d/da/d3/1ddad3615c85b90dccd31c2b5fbcb5a1.jpg',
                    'deleted': False,
                },
                {
                    'id': 6,
                    'username': 'vi',
                    'email': 'viCatlin@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/e5/60/0e/e5600eac05e07ae2e74492d5060130f0.jpg',
                    'deleted': False,
                },
                {
                    'id': 7,
                    'username': 'jayce',
                    'email': 'jayce@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/61/b9/59/61b9595898d45dd9e20261a5864455c6.jpg',
                    'deleted': False,
                },
                {
                    'id': 8,
                    'username': 'jinx',
                    'email': 'jinx@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/7b/48/e1/7b48e1b4561ab7962b582ca20f78e914.jpg',
                    'deleted': False,
                },
                {
                    'id': 9,
                    'username': 'nightGirl',
                    'email': 'nightGirl@gmail.com',
                    'profile_image': 'https://i.pinimg.com/236x/79/94/e7/7994e7bfaa011c4c4d0675e09cea4d3a.jpg',
                    'deleted': False,
                },
            ]

        set_context(context=context, data={
            "admins_items": admins_items,
            "admins_count": len(admins_items),
        })
        return self.root(request=request, context=context, template="pages/admin/admins.html")   



    # @adminValidator
    # def get_scripts(self, request):
    #     user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

    #     if not user:
    #         return self.forbidden_response(data={"message": "login"})

    #     site_data = self.get_site_data()
    #     scripts = site_data.get("scripts")

    #     return self.successful_response(data={"data": scripts})

    # @adminValidator
    # def get_attributes(self, request):
    #     user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

    #     if not user:
    #         return self.forbidden_response(data={"message": "login"})

    #     site_data = self.get_site_data()
    #     attributes = site_data.get("attributes")

    #     return self.successful_response(data={"data": attributes})

    # @adminValidator
    # def get_values(self, request):
    #     user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

    #     if not user:
    #         return self.forbidden_response(data={"message": "login"})

    #     site_data = self.get_site_data()
    #     values = site_data.get("values")

    #     return self.successful_response(data={"data": values})

    # @adminValidator
    # def get_settings(self, request):
    #     user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

    #     if not user:
    #         return self.forbidden_response(data={"message": "login"})

    #     site_data = self.get_site_data()
    #     settings = site_data.get("settings")

    #     return self.successful_response(data={"data": settings})


    # @adminValidator
    # def dashboard(self, request):
    #     user = self.GET_CREDITIALS(request.COOKIES)

    #     if not user:
    #         return redirect("/")

    #     site_data = self.get_site_data()
    #     scripts_amount = len(site_data.get("scripts", {}))
    #     values_amount = len(site_data.get("values", {}))
    #     attributes_amount = len(site_data.get("attributes", {}))
    #     settings_amount = len(site_data.get("settings", {}))
    #     users_amount = len(users)  # top 10 latest users
    #     data = {
    #         "users_amount": users_amount,
    #         "scripts_amount": scripts_amount,
    #         "values_amount": values_amount,
    #         "attributes_amount": attributes_amount,
    #         "settings_amount": settings_amount,
    #         "users": users,
    #     }

    #     return self.successful_response(data={"data": data})

