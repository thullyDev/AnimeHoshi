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
	def home(self, request):
	    data = tioanime.get_home_data()
	    # print(data)

	    return self.successful_response(data={ "data": data })