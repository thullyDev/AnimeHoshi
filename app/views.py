from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .services.resources import Resources
import json
import time
import urllib

resources = Resources(cache=cache)

def landing(requests):
    pass



def home(request):
    context = {
        "page": "home",
    }

    return render(request, "app/pages/home.html", context)
