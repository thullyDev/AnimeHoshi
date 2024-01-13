from django.shortcuts import render, redirect
from ...decorators import timer
from ...database import AdminDatabase
from ..base import Base
from ...resources import SITE_KEY 
import json

admin_database = AdminDatabase()
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
    def save_data(self, request):
        if not request.POST:
            return redirect("admin_login")

        user = self.GET_CREDITIALS(data=request.COOKIES, user_type="admin", update=True)

        if not user:
            return self.forbidden_response(data={"message": "login"})

        post = request.POST
        data = json.loads(post.get("save_data"))
        save = post.get("save")

        if save not in { "settings", "values", "attributes", "scripts" }:
            return self.bad_request_response()

        save_data = self.get_save_to_data(save)
        self.update_data(data, save_data)
        self.save_site_data(save_data, save)
        return self.successful_response(data={"data": None})

    def add_admin(self, request):
        pass

    def create_owner(self, request):
        data = request.GET
        req_site_key = data.get("key")
        password = data.get("password")
        
        if req_site_key != SITE_KEY:
            return self.forbidden_response()

        if None in [ password ]:
            return self.bad_request_response()

        if len(password) < 8:
            return self.bad_request_response(data={ "message": "password too short, it should be atleast 8 letters" })

        email = "owner@gmail.com"
        username = "owner"

        admin_data = {
            "email": email,
            "password": password,
            "username": username,
            "profile_image": None,
            "role": "owner",
        }

        res_data = admin_database.update_admin(data=admin_data, unique_id=email, key="email")
        return self.successful_response(data={ "message": "owner was created" })

    def save_site_data(self, data, name):
        site_data = self.get_site_data()
        site_data[name] =  data
        admin_database.hset(name="site_data", data=site_data, expiry=False)

    def update_data(self, new_data, old_data):
        for key, value in new_data.items():
            if not value and key in old_data: break 
            old_data[key] = value

    def get_site_data(self): 
        return admin_database.hget("site_data", {})

    def get_save_to_data(self, name):
        site_data = self.get_site_data()
        return site_data.get(name, {})