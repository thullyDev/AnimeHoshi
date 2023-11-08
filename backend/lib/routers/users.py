from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from ..utilities import ROOT_FILE

class Users(APIView):
    def root(self, request):
        context = {}

        return render(request, ROOT_FILE, context)
