from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import ROOT_FILE, ResponseHandler

class UsersAjax(APIView, ResponseHandler):
    def login(self, request):
        if request.POST:
            post_data = request.POST
            email = post_data.get("email")
            username = post_data.get("username")
            password = post_data.get("password")
            temporary_id = post_data.get("temporary_id")

            if not email and not username: return self.forbidden_response()
            #TODO: get user
            #TODO: check user is valid, whether if user exist or the password is correct
            data = {}
            return self.json_response(data)
        else:
            return redirect("/")

    def signup(self, request): pass
