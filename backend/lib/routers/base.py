from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from ..resources import ROOT_FILE
from ..database import Database
from ..handlers import ResponseHandler
import json
from pprint import pprint

database = Database()

class Base(APIView, ResponseHandler):
    def root(self, request, context={}, template=ROOT_FILE, titled=False): 
        if "page" in context: return render(request, template, context=context)

        path = request.path.split("/")
        full_path = request.path_info
        paths = full_path.split('/')
        length = len(paths)
        page = paths[length - 2]

        context["page"] = page 
        context["titled"] = titled 

        return render(request, template, context=context)

    def redirect_to_alert(self, raw_message, raw_description):
        url = reverse('alert')
        message = quote(raw_message)
        description = quote(raw_description)

        url = f"{url}?message={message}&description={description}"
        
        return redirect(url)

    def process_request(self, data):
        if not data: return {}

        return json.loads(data)

    def set_context(self, data, context):
        for key, value in data.items():
            context[key] = value

    def logout(self, request):
        return self.successful_response(data={ "message": "successful logout" }, cookies=True, cookies_data={
            "email": None,
            "username": None,
            "temporary_id": None,
        })
    
    def paginate(self, data, page, limit=20):
        paginator = Paginator(data, limit) 

        try:
            paginated = paginator.page(page)
        except EmptyPage:
            paginated = paginator.page(paginator.num_pages)

        return paginated, paginator.num_pages

    def filter_url_data(self, data, valids):
        return {
            key: value
            for key, value in data.items()
            if key in valids
        }
