from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import (
    ResponseHandler, 
    generate_unique_id,
)
from ...database import ( Cache )
from ...scraping import ( TioanimeScraper, LatanimeScraper )
import yagmail
from pprint import pprint

tioanime = TioanimeScraper()
latanime = LatanimeScraper()
cache = Cache()

class AnimeAjax(APIView, ResponseHandler):
	def home(self, request):
		cache_id = "home_data"
		cache_data = cache.dget(name=cache_id)

		if cache_data: return self.successful_response(data={ "data": cache_data })

		tioanime_rawdata = tioanime.get_home()
		latanime_rawdata = latanime.get_home()

		data = {
	    	"tioanime": {
	    		"episodes": [],
	    		"animes": [],
	    	},
	    	"latanime":  {
	    		"episodes": [],
	    		"features": [],
	    	}
	    }

	    latest_episodes = tioanime_rawdata.get("latest_episodes")
	    latest_animes = tioanime_rawdata.get("latest_animes")

	    for episosde in latest_episodes:
	    	data["tioanime"]["episodes"].append({
	    		"image_url": f"https://{tioanime.base}/" + episosde.get("image").get("url"),
	    		"title": episosde.get("image").get("title"),
	    		"episode_slug": episosde.get("episode_slug").get("slug").replace("/ver", ""),
	    	})

	    for anime in latest_animes:
	    	data["tioanime"]["animes"].append({
	    		"image_url": f"https://{tioanime.base}/" + anime.get("image").get("url"),
	    		"title": anime.get("image").get("title"),
	    		"slug": anime.get("anime_slug").get("slug").replace("/anime", ""),
	    	})

	    latest_episodes = latanime_rawdata.get("latest_episodes")
	    sliders = latanime_rawdata.get("slider")

	    for episosde in latest_episodes:
	    	print(episosde.get("episode_slug").get("slug"))
	    	data["latanime"]["episodes"].append({
	    		"image_url": episosde.get("image").get("url"),
	    		"title": episosde.get("image").get("title"),
	    		"episode_slug": episosde.get("episode_slug").get("slug").replace(f"https://{latanime.base}/ver", ""),
	    	})

	    for slider in sliders:
	    	data["latanime"]["features"].append({
	    		"background_image_url": slider.get("background_image").get("url"),
	    		"preview_image_url": slider.get("preview_image").get("url"),
	    		"title": slider.get("background_image").get("title"),
	    		"slug": slider.get("anime_slug").get("slug").replace(f"https://{latanime.base}/anime", ""),
	    		"description": slider.get("description").get("text"),
	    	})

	    cache.dset(name=cache_id, data=data)
	    return self.successful_response(data={ "data": data })