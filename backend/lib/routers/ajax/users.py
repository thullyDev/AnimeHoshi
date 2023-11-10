from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...utilities import ROOT_FILE
from ..responseHandler import ResponseHandler

class UsersAjax(APIView, ResponseHandler):
    def login(self, request):
        if request.POST:
            data = {}
            return self.json_response(data)
        else:
            return redirect("/")