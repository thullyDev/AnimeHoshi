from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from ..resources import ROOT_FILE

class Base(APIView):
    def root(self, request): return render(request, ROOT_FILE)
