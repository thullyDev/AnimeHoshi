from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from ...utilities import ROOT_FILE

class UsersAjax(APIView):
    def login(self, request):
        if request.POST:
            data = {}
            return JsonResponse(json.dumps(data), safe = False)
        else:
            return redirect("/")