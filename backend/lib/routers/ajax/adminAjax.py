from django.shortcuts import render, redirect
from ...decorators import timing_decorator
from ...database import Cache
from ..base import Base
import json

cache = Cache()
users = [
    {
        "id": 0,
        "username": "animeGirl",
        "email": "animegirl@gmail.com","password": "1234567890",
        "profile_image": "https://i.pinimg.com/564x/07/d4/34/07d434bcb00e39c8e8d25df1cc89a333.jpg",
        "deleted": False,
    },
    {
        "id": 1,
        "username": "animeBoy",
        "email": "animeBoy@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/ef/e9/73/efe97322d26afdbb85e03c52b1db7c10.jpg",
        "deleted": False,
    },
    {
        "id": 2,
        "username": "Megumi",
        "email": "megumi@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/736x/02/05/28/020528711a47abd638ed5ee670cc4705.jpg",
        "deleted": False,
    },
    {
        "id": 3,
        "username": "Gojo",
        "email": "gojo@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/736x/50/c4/bd/50c4bdba9bbe22a46733edbdb55b65a2.jpg",
        "deleted": False,
    },
    {
        "id": 4,
        "username": "Kenji",
        "email": "kenji@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/85/42/bb/8542bb42f5e7369e953049fa14ba5170.jpg",
        "deleted": False,
    },
    {
        "id": 5,
        "username": "sky",
        "email": "sky@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/1d/da/d3/1ddad3615c85b90dccd31c2b5fbcb5a1.jpg",
        "deleted": False,
    },
    {
        "id": 6,
        "username": "vi",
        "email": "viCatlin@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/e5/60/0e/e5600eac05e07ae2e74492d5060130f0.jpg",
        "deleted": False,
    },
    {
        "id": 7,
        "username": "jayce",
        "email": "jayce@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/61/b9/59/61b9595898d45dd9e20261a5864455c6.jpg",
        "deleted": False,
    },
    {
        "id": 8,
        "username": "jinx",
        "email": "jinx@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/7b/48/e1/7b48e1b4561ab7962b582ca20f78e914.jpg",
        "deleted": False,
    },
    {
        "id": 9,
        "username": "nightGirl",
        "email": "nightGirl@gmail.com",
        "password": "1234567890",
        "profile_image": "https://i.pinimg.com/236x/79/94/e7/7994e7bfaa011c4c4d0675e09cea4d3a.jpg",
        "deleted": False,
    },
]

class AdminAjax(Base):
    @timing_decorator
    def dashboard(self, request):
        user = self.GET_CREDITIALS(request.COOKIES)

        if not user:
            return redirect("/")

        site_data = self.get_site_data()
        scripts_amount = len(site_data.get("scripts", {}))
        values_amount = len(site_data.get("values", {}))
        attributes_amount = len(site_data.get("attributes", {}))
        settings_amount = len(site_data.get("settings", {}))
        users_amount = len(users)  # top 10 latest users
        data = {
            "users_amount": users_amount,
            "scripts_amount": scripts_amount,
            "values_amount": values_amount,
            "attributes_amount": attributes_amount,
            "settings_amount": settings_amount,
            "users": users,
        }

        return self.successful_response(data={"data": data})

    @timing_decorator
    def get_scripts(self, request):
        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        if not user:
            return self.forbidden_response(data={"message": "login"})

        site_data = self.get_site_data()
        scripts = site_data.get("scripts")

        return self.successful_response(data={"data": scripts})

    @timing_decorator
    def get_attributes(self, request):
        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        if not user:
            return self.forbidden_response(data={"message": "login"})

        site_data = self.get_site_data()
        attributes = site_data.get("attributes")

        return self.successful_response(data={"data": attributes})

    @timing_decorator
    def get_values(self, request):
        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        if not user:
            return self.forbidden_response(data={"message": "login"})

        site_data = self.get_site_data()
        values = site_data.get("values")

        return self.successful_response(data={"data": values})

    @timing_decorator
    def get_settings(self, request):
        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        if not user:
            return self.forbidden_response(data={"message": "login"})

        site_data = self.get_site_data()
        settings = site_data.get("settings")

        return self.successful_response(data={"data": settings})

    def save_data(self, request):
        if not request.POST:
            return redirect("admin_login")

        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        if not user:
            return self.forbidden_response(data={"message": "login"})

        post = request.POST
        data = json.loads(post.get("save_data"))
        save = post.get("save")

        if save not in {"settings", "values", "attributes", "scripts"}:
            return self.bad_request_response()

        site_data = self.get_site_data()
        for item in site_data:
            print(f"item =====> {item}")
        site_data[save] = data

        # cache.dcset(name="site_data", data=site_data, expiry=False)

    def add_admin(self, request):
        pass

    def get_site_data(self): return cache.dcget("site_data")