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
    def get_home_data(self, request):
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
    def tioanime_filter(self, request):
        filter_data = {}
        for key, value in request.GET.items():
            if value: filter_data[key] = value

        rawdata = tioanime.get_filter(data=filter_data)
        data = self.filter_data_processing(rawdata=rawdata, base=tioanime.base, site="tioanime")

        return self.successful_response(data=data)

    @timing_decorator
    def latanime_filter(self, request):
        filter_data = {}
        for key, value in request.GET.items():
            if value: filter_data[key] = value

        rawdata = latanime.get_filter(data=filter_data)
        data = self.filter_data_processing(rawdata=rawdata, base=latanime.base, site="latanime")

        return self.successful_response(data=data)

    @timing_decorator
    def tioanime_schedule(self, request):
        rawdata = tioanime.get_schedule()
        data = self.schedule_data_processing(rawdata=rawdata)

        return self.successful_response(data={ "data": data })

    @timing_decorator
    def latanime_schedule(self, request):
        rawdata = latanime.get_schedule()
        data = self.schedule_data_processing(rawdata=rawdata, base=latanime.base)

        return self.successful_response(data={ "data": data })

    @timing_decorator
    def latanime_search(self, request):
        search_data = {}
        for key, value in request.GET.items():
            if value: search_data[key] = value

        rawdata = latanime.get_search(data=search_data)
        data = self.filter_data_processing(rawdata=rawdata, base=latanime.base, site="latanime")

        return self.successful_response(data={ "data": data })

    @timing_decorator
    def tioanime_anime(self, request, slug):
        rawdata = tioanime.get_anime(slug=slug)
        base = tioanime.base
        data = {
            "title": rawdata.get("title").get("title"),
            "original_title": rawdata.get("original_title").get("original_title"),
            "type": rawdata.get("type").get("type"),
            "year": rawdata.get("year").get("year"),
            "season": rawdata.get("season").get("season"),
            "description": rawdata.get("description").get("description"),
            "status": rawdata.get("status").get("status"),
            "poster_image": f"https://{base}/" + rawdata.get("poster_image").get("poster_image"),
            "background_image": f"https://{base}/" + rawdata.get("background_image").get("background_image"),
            "genres": [],
            "episodes": [],
        }
        genres_hmtl = rawdata.get("genres").get("genres_html").replace("/directorio?genero=", "").replace('</a>', "").replace('</span>', "").replace('</span>', "").replace('<a class="btn btn-sm btn-light rounded-pill"', "").replace('<p class="genres">', "").replace('<span class="btn btn-sm btn-primary rounded-pill">', "")
        rawgenres_list = genres_hmtl.split("href=")
        scripts = rawdata.get("last_scripts").get("episodes_script").replace("var anime_info = ", "").replace("episodesList();", "").replace("var episodes = ", "").replace("$(document).ready(function()", "").replace("{", "").replace("});", "").replace("var episodes_details = ", "").replace(";\r", "").replace("  ", "").strip().replace("] [", "]] [[").split("] [")
        anime_info = eval(scripts[0])
        episodes_num = eval(scripts[1])
        episodes_details = eval(scripts[2])

        for ep_num in episodes_num:
            slug = f"/{anime_info[1]}-{episodes_num[ep_num - 1]}"
            episode_title = f"Episodio {episodes_num[ep_num - 1]}"
            image_url = f"https://{tioanime.base}/uploads/thumbs/{anime_info[0]}.jpg"

            data["episodes"].append({
                "slug": slug,
                "episode_title": episode_title,
                "image_url": image_url,
                })

        for item in rawgenres_list:
            genre_id = item.replace('"', "").strip().split(">")[0]
            if not genre_id: continue
            genre = genre_id.title()
            data["genres"].append({
                "genre_id": genre_id,
                "genre": genre
                })

        return self.successful_response(data={ "data": data })

    @timing_decorator
    def latanime_anime(self, request, slug):
        rawdata = latanime.get_anime(slug=slug)
        data = {
            "title": rawdata.get("title").get("title"),
            "description": rawdata.get("description").get("description"),
            "status": rawdata.get("status").get("status"),
            "poster_image": rawdata.get("poster_image").get("poster_image"),
            "background_image": rawdata.get("background_image"),
            "genres": [],
            "episodes": [],
        }
        des_html = rawdata.get("des_html").get("des_html")

        for item in genres_html.split('href='):
            found = item.find("https://latanime.org/ver")

            print()

            if found == 1:
                temp = item.split(">")[0]
                data["episodes"].append(temp)

        return self.successful_response(data={ "rawdata": rawdata })


    #*** helper functions START ***#
    def filter_data_processing(self, rawdata, site, base):
        animes = rawdata.get("animes")
        pages = rawdata.get("pages")[0]
        data = {
            "page": int(rawdata.get("page")[0].get("page").get("text")),
            "pages": int(pages[len(pages) - 2]),
            "animes": []
        }

        if site not in [ "tioanime", "latanime" ]: return None

        if site == "tioanime":
            for anime in animes:
                data["animes"].append({
                    "image_url": f"https://{base}/" + anime.get("image").get("url"),
                    "title": anime.get("title").get("text"),
                    "slug": anime.get("anime_slug").get("slug").replace("/anime", ""),
                })

            return data

        if site == "latanime": 
            for anime in animes:
                title = anime.get("title").get("text")
                temp = title.split(" ")
                watch_type = temp[len(temp) - 1]

                data["animes"].append({
                    "image_url": anime.get("image").get("url"),
                    "title": title,
                    "slug": anime.get("anime_slug").get("slug").replace(f"https://{latanime.base}/anime", ""),
                    "year": anime.get("year").get("text").strip(),
                    "type": watch_type,
                })

        return data    

    def schedule_data_processing(self, rawdata, base=None):
        data = {}
        for day, animes in rawdata.items():
            data[day] = []
            for anime in animes:
                slug = anime.get("slug").get("slug").strip().replace(f"https://{base}/anime", "")
                title = anime.get("title").get("text")
                image = anime.get("image").get("url")

                data[day].append({
                        "slug": slug if slug != "#" else None,
                        "title": title,
                        "image_url": image,
                    })
        return data
    #*** helper functions END ***#
