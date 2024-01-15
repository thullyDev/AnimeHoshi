from django.shortcuts import render, redirect
from ...decorators import timer
from ...database import AdminDatabase
from ..base import Base
from ...resources import SITE_KEY 
import json

admin_database = AdminDatabase()

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