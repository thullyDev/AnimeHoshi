from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from ..resources import ROOT_FILE
from ..database import Database
from ..handlers import ResponseHandler
import json

database = Database()

class Base(APIView, ResponseHandler):
    def root(self, request, context={}, template=ROOT_FILE): 
        path = request.path.split("/")
        full_path = request.path_info
        paths = full_path.split('/')
        length = len(paths)
        page = paths[length - 2]

        context["page"] = page if page != "" else context["site_data"]["values"]["inputs"]["site_name"]["value"]

        return render(request, template, context=context)

    def process_request(self, data):
        if not data: return {}

        return json.loads(data)

    def set_context(self, data, context):
        for key, value in data.items():
            context[key] = value

