from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import (
    ResponseHandler, 
    generate_unique_id,
)
from ...scraping import ( TioanimeScraper, LatanimeScraper )
import yagmail

tioanime = TioanimeScraper()
latanime = LatanimeScraper()

class AnimeAjax(APIView, ResponseHandler):
    pass