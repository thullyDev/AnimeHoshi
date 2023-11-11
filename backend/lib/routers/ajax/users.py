from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import ROOT_FILE, ResponseHandler
from ...database import Database

db = Database()

class UsersAjax(APIView, ResponseHandler):
    def login(self, request):
        if request.POST:
            post_data = request.POST
            email = post_data.get("email")
            username = post_data.get("username")
            password = post_data.get("password")
            temporary_id = post_data.get("temporary_id")

            if not email and not username: return self.forbidden_response()

            data = db.get_user(email=email) if email else db.get_user(username=username)

            if not data: return self.forbidden_response()

            del data["id"]
            del data["wachlist"]
            del data["likeslist"]

            return self.json_response(data)
        else:
            return redirect("/")

    def signup(self, request): pass
