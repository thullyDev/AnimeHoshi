from django.shortcuts import render, redirect
from ...decorators import timer, adminValidator
from ...handlers import SiteHandler
from ...database import AdminDatabase, Storage
from ..base import Base
from pprint import pprint
from ...resources import SITE_KEY 
import json

admin_database = AdminDatabase()
site = SiteHandler()
storage = Storage()

class AdminAjax(Base):
    @adminValidator
    def save_data(self, request, site_data, *args, **kwargs):
        if not request.POST:
            return redirect("admin_login")

        post = request.POST
        data = json.loads(post.get("save_data"))
        save = post.get("save")

        if save not in { "settings", "values", "scripts" }:
            return self.bad_request_response()

        save_data = site_data.get(save, {})
        if save == "values": self.process_images(data, save_data)
        self.update_data(save, data, save_data)
        self.save_site_data(save_data, save)
        
        return self.successful_response()

    @adminValidator
    def reset_settings(self, request, *args, **kwargs):
        if not request.POST:
            return redirect("admin_login")

        post = request.POST
        site_key = post.get("site_key")

        if SITE_KEY != site_key:
            return self.forbidden_response(data={ "message": "site key is invalid" })
            
        site.set_default_site_data()
        return self.successful_response()

    @adminValidator
    def add_admin(self, request, *args, **kwargs):
        if not request.POST:
            return redirect("admin_login")

        post = request.POST
        site_key = post.get("site_key")

        if SITE_KEY != site_key:
            return self.forbidden_response(data={ "message": "site key is invalid" })

        data = json.loads(post.get("data"))
        is_validate = self.validate(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            confirm=data["confirm"],
            )

        del data["confirm"]
        admin_database.set_admin(email=data["email"], data=data)
        return self.successful_response()

    @adminValidator
    def update_admin(self, request, *args, **kwargs):
        if not request.POST:
            return redirect("admin_login")

        post = request.POST
        site_key = post.get("site_key")

        if SITE_KEY != site_key:
            return self.forbidden_response(data={ "message": "site key is invalid" })

        data = json.loads(post.get("data"))

        admin_database.update_admin(data=data)
        return self.successful_response()

    @adminValidator
    def update_user(self, request, *args, **kwargs):
        if not request.POST:
            return redirect("admin_login")

        post = request.POST
        email = post.get("id")
        data = json.loads(post.get("data"))
        data["email"] = email

        admin_database.update_users(data=data)
        return self.successful_response()

    @adminValidator
    def update_anime(self, request, site_data, *args, **kwargs):
        if not request.POST:
            return redirect("admin_login")

        post = request.POST
        slug = post.get("id")
        disabled_animes = site_data["disabled_animes"]

        if slug in disabled_animes:
            del disabled_animes[slug]
            site.save_site_data(name="disabled_animes", data=disabled_animes)
            return self.successful_response(data={ "data": { "deleted": False }})

        disabled_animes[slug] = 0
        site.save_site_data(name="disabled_animes", data=disabled_animes)
        return self.successful_response(data={ "data": { "deleted": True }})

    @timer
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

    def update_data(self, save, new_data, old_data):
        if save == "settings":
            for key, value in old_data.items():
                old_data[key]["value"] = new_data[key]
            return

        for type_key, type_values in old_data.items():
            for key, value in type_values.items():
                old_data[type_key][key]["value"] = new_data[key]

    def process_images(self, new_data, old_data):
        images_keys = list(old_data["images"].keys())
        images = []

        for key, value in new_data.items():
            if key not in images_keys or old_data["images"][key]["value"] == value:
                continue 

            images.append({
                "name": key,
                "value": value.replace("data:image/jpeg;base64,", ""),
            })

        if not images:
            return

        for img in images:
            name = img.get("name")
            value = img.get("value")
            storage.upload_base64_image(name=name, base64_img=value)

    def get_site_data(self): 
        return admin_database.hget("site_data", {})

    def get_save_to_data(self, name):
        site_data = self.get_site_data()
        return site_data.get(name, {})


    def validate(self, username, email, password, confirm):
        if None in [username, email, password, confirm] or \
            password != confirm or \
            len(confirm) < 8:
            return False

        return True
