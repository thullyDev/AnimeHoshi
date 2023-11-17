from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import ResponseHandler, generate_unique_id, timing_decorator
from ...database import Cache
from ...scraping import TioanimeScraper, LatanimeScraper
from pprint import pprint

tioanime = TioanimeScraper()
latanime = LatanimeScraper()
cache = Cache()

class AnimeAjax(APIView, ResponseHandler):
    @timing_decorator
    def home(self, request):
        cache_id = "home_data"
        cache_data = cache.dcget(name=cache_id)

        if cache_data:
            return self.successful_response(data={"data": cache_data})

        tioanime_rawdata = tioanime.get_home()
        latanime_rawdata = latanime.get_home()

        data = {
            "tioanime": {
                "episodes": [],
                "animes": [],
            },
            "latanime": {
                "episodes": [],
                "features": [],
            }
        }

        latest_episodes = tioanime_rawdata.get("latest_episodes")
        latest_animes = tioanime_rawdata.get("latest_animes")

        for episode in latest_episodes:
            data["tioanime"]["episodes"].append({
                "image_url": f"https://{tioanime.base}/" + episode.get("image").get("url"),
                "title": episode.get("image").get("title"),
                "episode_slug": episode.get("episode_slug").get("slug").replace("/ver", ""),
            })

        for anime in latest_animes:
            data["tioanime"]["animes"].append({
                "image_url": f"https://{tioanime.base}/" + anime.get("image").get("url"),
                "title": anime.get("image").get("title"),
                "slug": anime.get("anime_slug").get("slug").replace("/anime", ""),
            })

        latest_episodes = latanime_rawdata.get("latest_episodes")
        sliders = latanime_rawdata.get("slider")

        for episode in latest_episodes:
            data["latanime"]["episodes"].append({
                "image_url": episode.get("image").get("url"),
                "title": episode.get("image").get("title"),
                "episode_slug": episode.get("episode_slug").get("slug").replace(f"https://{latanime.base}/ver", ""),
            })

        for slider in sliders:
            data["latanime"]["features"].append({
                "background_image_url": slider.get("background_image").get("url"),
                "preview_image_url": slider.get("preview_image").get("url"),
                "title": slider.get("background_image").get("title"),
                "slug": slider.get("anime_slug").get("slug").replace(f"https://{latanime.base}/anime", ""),
                "description": slider.get("description").get("text"),
            })

        cache.dcset(name=cache_id, data=data)
        return self.successful_response(data={"data": data})

    @timing_decorator
    def filter(self, request, site):
        filter_data = {}
        for key, value in request.GET.items():
            if value: filter_data[key] = value

        rawdata = tioanime.get_filter(data=filter_data)
        animes = rawdata.get("animes")
        pages = rawdata.get("pages")[0]

        data = {
            "page": int(rawdata.get("page")[0].get("page").get("text")),
            "pages": int(pages[len(pages) - 2]),
            "animes": []
        }

        for anime in animes:
            data["animes"].append({
                "image_url": f"https://{tioanime.base}/" + anime.get("image").get("url"),
                "title": anime.get("title").get("text"),
                "slug": anime.get("anime_slug").get("slug").replace("/anime", ""),
            })

        return self.successful_response(data=data)

    @timing_decorator
    def schedule(self, request):
        data = tioanime.get_schedule()
        return self.successful_response(data=data)