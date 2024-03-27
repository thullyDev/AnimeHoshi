from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.urls import reverse
from base64 import b64decode, b64encode
from ..decorators import recorder
from ..resources import generate_unique_id
from ..database import Cache, Database
from ..scraping import TioanimeScraper, LatanimeScraper
from ..handlers import ResponseHandler, SiteHandler, LiveChat
from .base import Base
from pprint import pprint
import ast
import random

tioanime = TioanimeScraper()
latanime = LatanimeScraper()
site = SiteHandler()
cache = Cache()
database = Database()
live_chat = LiveChat()

class Anime(Base):
    @recorder
    def random(self, request, **kwargs):
        site_data = site.get_site_data()
        random = site_data.get("settings", {}).get("random", {}).get("value")

        if not random: return redirect("home")
        
        page = random.randint(1, 196) # it gets random page between 1 and 196
        anime_index = random.randint(1, 20) - 1 # gets a random anime between the 20 shown
        rawdata = tioanime.get_filter(data={ "page": str(page) })
        data = self.filter_data_processing(rawdata=rawdata, base=tioanime.base)
        animes = data["animes"]
        anime = animes[anime_index]
        slug = anime.get("slug")

        return redirect(f"/main/anime{slug}")

    @recorder
    def home(self, request, context, **kwargs):
        cache_id = "home_data"
        cache_data = cache.hget(name=cache_id)

        if cache_data:
            context["data"] = cache_data 
            context["page"] = "index"
            return self.root(request=request, context=context, template="pages/anime/home.html")

        tioanime_rawdata = tioanime.get_home()
        latanime_rawdata = latanime.get_home()

        if None in [ tioanime_rawdata, latanime_rawdata ]:
            return self.redirect_to_alert(
                raw_message="Something Went Wrong", 
                raw_description="the site received an internal server crash, please try again"
                )


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
                "slug": episode.get("episode_slug").get("slug").replace("/ver", ""),
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
                "slug": episode.get("episode_slug").get("slug").replace(f"https://{latanime.base}/ver", ""),
            })

        for slider in sliders:
            data["latanime"]["features"].append({
                "background_image_url": slider.get("background_image").get("url"),
                "preview_image_url": slider.get("preview_image").get("url"),
                "title": slider.get("background_image").get("title"),
                "slug": slider.get("anime_slug").get("slug").replace(f"https://{latanime.base}/anime", ""),
                "description": slider.get("description").get("text"),
            })

        self.cache_data(cache_id=cache_id, data=data)

        context["data"] = data
        context["page"] = "index"
        return self.root(request=request, context=context, template="pages/anime/home.html")

    @recorder
    def watch_room(self, request, room_id, GET, context, **kwargs):
        ep_num = GET.get("ep_num", "1")

        try:
            ep_num = int(ep_num)
        except ValueError:
            ep_num = 1            

        cache_id = room_id.replace("room:*", "room_data:*")

        room_data = database.get(unit="rooms", key="room_id", unique_id=room_id)
        room_code = room_data["room_code"]
        slug = room_data["slug"]
        watch_type = room_data["watch_type"]
        scraper = tioanime if watch_type == "main" else latanime
        rawdata = scraper.get_anime(slug=slug)

        if not rawdata: return redirect("not_found")

        cache_data = cache.hget(name=cache_id)
        data = None

        if cache_data:
            data = cache_data 
        else: 
            data = self.anime_processing(rawdata=rawdata, base=scraper.base)
            cache.hset(name=cache_id, data=data, expiry=86400) # 24 hours 

        # just a mess
        watch_room_data = {}
        episodes = data["episodes"]
        episodes_length = len(episodes)
        ep_num = episodes_length if ep_num >= episodes_length else ep_num
        watch_room_data["episodes"] = episodes
        watch_room_data["anime_slug"] = slug
        watch_room_data["anime_title"] = data["title"]
        watch_room_data["type"] = watch_type
        episode_slug = episodes[ep_num - 1]
        if type(episode_slug) is dict: episode_slug = episode_slug['slug']
        episode_num = episode_slug.split("-")[-1]
        rawdata = scraper.get_episode(slug=episode_slug.replace("/", ""))
        episodes_data = self.watch_processing(rawdata=rawdata, base=scraper.base)
        embed_links = episodes_data.get("embed_links", [])
        first_embed = {} if not embed_links else embed_links[0]
        watch_room_data["data"] = episodes_data
        watch_room_data["first_embed"] = first_embed
        watch_room_data["page"] = "watch"
        watch_room_data["room_id"] = room_id
        context["is_watch_room"] = True
        context["room_data"] = room_data
        context["room_code"] = room_code
        context["room_inputs"] = self.get_watch_room_inputs(
            slug=slug, 
            watch_type=watch_type
        )
        # just a mess [end]
        data = {**context, **watch_room_data}
        data["episode_num"] = ep_num

        return self.root(request=request, context=data, template="pages/anime/watch.html", titled=True)

    @recorder
    def chat_room(self, request, room_id, GET, COOKIES, context, **kwargs):
        context["room_code"] = GET.get("room_code", "")
        context["room_id"] = room_id
        context["page"] = "chat_room"
        context["no_layout"] = True
        user_live_chat_id = COOKIES.get("user_live_chat_id")

        if user_live_chat_id: 
            context["user_live_chat_id"] = user_live_chat_id
            return self.root(request=request, context=context, template="pages/anime/chat_room.html")

        key = "user_live_chat_id"
        user_live_chat_id = generate_unique_id()
        response = self.root(request=request, context=context, template="pages/anime/chat_room.html")
        response.set_cookie(
            key=key, 
            value=user_live_chat_id, 
            max_age=86_400, # 24 hours
            secure=True, 
            httponly=True
        )
        return response

    @recorder
    def watch_rooms(self, request, GET, COOKIES, context, **kwargs):
        mine = GET.get("mine", "false")
        page = GET.get("page", "1")
        query = GET.get("keywords")
        rooms = None

        if mine == "true":
            email = COOKIES.get("email")
            rooms = database.sql_get_query(
                unit="rooms", 
                creator_email=email, 
                be_dynmc=True
            )        
        elif query:
            rooms = database.sql_get_query(
                unit="rooms", 
                room_name__icontains=query, 
                be_dynmc=True
            )
        else:
            rooms = database.sql_get_all(unit="rooms")

        paginated_rooms, pages = self.paginate(data=list(reversed(rooms)), page=page, limit=12)
        pagination = {
            "page": page,
            "pages": pages,
        }
        context["rooms"] = paginated_rooms
        context["query"] = "" if not query else f"&keywords={query}"
        context["pagination"] = pagination

        return self.root(request=request, context=context, template="pages/anime/watch_rooms.html")

    @recorder
    def tioanime_filter(self, request, GET, context, **kwargs):
        filter_data = {}
        for key, value in GET.items():
            if value: filter_data[key] = value

        rawdata = tioanime.get_filter(data=filter_data)
        data = self.filter_data_processing(rawdata=rawdata, base=tioanime.base)
        context["current_page"] = filter_data.get("page", "1")
        if "page" in filter_data: del filter_data["page"]
        
        query = tioanime.build_query(filter_data)
        context["data"] = data
        context["query"] = query.replace("?", "&")
        context["type"] = "main"
        return self.root(request=request, context=context, template="pages/anime/filter.html")

    @recorder
    def latanime_filter(self, request, GET, context, **kwargs):
        filter_data = {}
        for key, value in GET.items():
            if value: filter_data[key] = value

        rawdata = latanime.get_filter(data=filter_data)
        data = self.filter_data_processing(rawdata=rawdata, base=latanime.base)
        context["current_page"] = filter_data.get("page", "1")
        if "page" in filter_data: del filter_data["page"]
        
        query = latanime.build_query(filter_data)
        context["data"] = data
        context["query"] = query.replace("?", "&")
        context["type"] = "latino"
        return self.root(request=request, context=context, template="pages/anime/filter.html")

    @recorder
    def tioanime_schedule(self, request, context, **kwargs):
        cache_id = "tioanime_schedule"
        cache_data = cache.hget(name=cache_id)

        if cache_data:
            context["data"] = cache_data 

        rawdata = tioanime.get_schedule()
        data = self.schedule_data_processing(rawdata=rawdata)
        context["data"] = data
        context["type"] = "main"
        self.cache_data(cache_id=cache_id, data=data)
        return self.root(request=request, context=context, template="pages/anime/schedule.html")

    @recorder
    def latanime_schedule(self, request, context, **kwargs):
        cache_id = "latanime_schedule"
        cache_data = cache.hget(name=cache_id)

        if cache_data:
            context["data"] = cache_data 

        rawdata = latanime.get_schedule()
        data = self.schedule_data_processing(rawdata=rawdata, base=latanime.base)
        context["data"] = data
        context["type"] = "latino"
        self.cache_data(cache_id=cache_id, data=data)
        return self.root(request=request, context=context, template="pages/anime/schedule.html")

    @recorder
    def latanime_search(self, request, GET, context, **kwargs):
        search_data = {}
        for key, value in GET.items():
            if value: search_data[key] = value

        rawdata = latanime.get_search(data=search_data)

        if not rawdata["animes"]: return redirect("home")

        data = self.filter_data_processing(rawdata=rawdata, base=latanime.base)
        if "page" in search_data: del search_data["page"]

        query = latanime.build_query(search_data)
        context["data"] = data
        context["query"] = query.replace("?", "&")
        context["type"] = "latino"
        context["page"] = "filter"
        return self.root(request=request, context=context, template="pages/anime/filter.html")

    @recorder
    def tioanime_anime(self, request, slug, context, **kwargs):
        rawdata = tioanime.get_anime(slug=slug)

        if not rawdata: return redirect("not_found")

        data = self.anime_processing(rawdata=rawdata, base=tioanime.base)
        watch_type = "main"
        context["anime_slug"] = slug
        context["type"] = watch_type
        context["data"] = data
        context["page"] = "anime"
        context["room_inputs"] = self.get_watch_room_inputs(
            slug=slug, 
            watch_type=watch_type
        )

        return self.root(request=request, context=context, template="pages/anime/anime.html", titled=True)

    @recorder
    def latanime_anime(self, request, slug, context, **kwargs):
        rawdata = latanime.get_anime(slug=slug)

        if not rawdata: return redirect("not_found")

        data = self.anime_processing(rawdata=rawdata, base=latanime.base)
        watch_type = "latino"
        context["anime_slug"] = slug
        context["type"] = watch_type
        context["data"] = data
        context["page"] = "anime"
        context["room_inputs"] = self.get_watch_room_inputs(
            slug=slug, 
            watch_type=watch_type
        )

        return self.root(request=request, context=context, template="pages/anime/anime.html", titled=True)

    @recorder
    def latanime_watch(self, request, slug, context, **kwargs):
        rawdata = latanime.get_episode(slug=slug)
        data = self.watch_processing(rawdata=rawdata, base=latanime.base)
        anime_slug = slug.split("-episodio")[0]
        context["anime_slug"] = anime_slug
        context["anime_title"] = anime_slug.replace("-", " ").title()
        episodes = self.get_episodes(anime_slug, latanime)
        del data["recommandations"]
        context["data"] = data
        embed_links = data.get("embed_links", [])
        first_embed = {} if not embed_links else embed_links[0]
        episode_num = slug.split("-")[-1]
        context["episode_num"] = episode_num
        context["first_embed"] = first_embed
        context["episodes"] = episodes
        watch_type = "latino"
        context["next_episode_slug"], context["prev_episode_slug"] = self.get_anchor_episodes(
            episode_slug=slug, 
            watch_type=watch_type, 
            episodes=episodes
        )
        context["type"] = watch_type    
        context["page"] = "watch"
        context["room_inputs"] = self.get_watch_room_inputs(
            slug=anime_slug, 
            watch_type=watch_type
        )

        return self.root(request=request, context=context, template="pages/anime/watch.html", titled=True)

    @recorder
    def tioanime_watch(self, request, slug, context, **kwargs):
        rawdata = tioanime.get_episode(slug=slug)
        temp = slug.split("-")
        anime_slug = "-".join(temp[:-1])
        episodes = self.get_episodes(anime_slug, tioanime)
        data = self.watch_processing(rawdata=rawdata, base=tioanime.base)
        episode_num = slug.split("-")[-1]
        context["episode_num"] = episode_num
        context["data"] = data
        context["anime_slug"] = anime_slug
        context["anime_title"] = anime_slug.replace("-", " ").title()
        embed_links = data.get("embed_links", [])
        first_embed = {} if not embed_links else embed_links[0]
        context["first_embed"] = first_embed
        context["episodes"] = episodes
        context["episodes_amount"] = str(len(episodes))
        watch_type = "main"
        context["type"] = watch_type
        context["page"] = "watch"
        context["next_episode_slug"], context["prev_episode_slug"] = self.get_anchor_episodes(
            episode_slug=slug, 
            watch_type=watch_type, 
            episodes=episodes
        )
        context["room_inputs"] = self.get_watch_room_inputs(
            slug=anime_slug, 
            watch_type=watch_type
        )

        return self.root(request=request, context=context, template="pages/anime/watch.html", titled=True)

    @recorder
    def stream(self, request, encrypted_link, GET, context, **kwargs):
        link = b64decode(encrypted_link.replace("b'", "").replace("'", "")).decode("utf-8")
        site = link.replace("https://", "").split("/")[0]
        valid_sites = {
            "ok.ru",
            "sfastwish.com",
            "www.mp4upload.com",
            "denisegrowthwide.com",
            "www.yourupload.com",
        }

        if site not in valid_sites:
            return self.bad_request_response()

        blueprint = {
            "body": {
                "parent_selector": "body",
                "attribute": "html",
                "single_select": True,
                "key": "html",
            },
        }
        data = tioanime.get(base=site, endpoint=link.replace(f"https://{site}/", ""), blueprint=blueprint)

        file = data.get("body").get("html").split("file: ")[1].replace('.mp4', ".mp4***cut_here***").split("***cut_here***")[0].replace("'", '')
        return self.successful_response(data={ "data": data })

    @recorder
    def alert(self, request, GET, context, **kwargs):
        message = GET.get("message")
        description = GET.get("description")

        if None in [message, description]: return redirect("home")

        context["message"] = message
        context["description"] = description

        return self.root(request=request, context=context, template="pages/anime/alert.html")

    @recorder
    def maintenance(self, request, context, **kwargs):
        return self.redirect_to_alert(
            raw_message="Under Construction", 
            raw_description="we are currently doing maintenance to the site"
            )

    @recorder
    def not_found(self, request, context, **kwargs):
        return self.redirect_to_alert(
            raw_message="404 - Page Not Found", 
            raw_description="The requested page could not be found."
            )

    #*** helper functions START ***#
    def get_episodes(self, slug, instance):
        rawdata = instance.get_anime(slug)
        data = self.anime_processing(rawdata=rawdata, base=instance.base)
        return data["episodes"]

    def filter_data_processing(self, rawdata, base):
        if not rawdata: return {
            "page": 1,
            "page": 0,
            "animes": [],
        } 
        animes = rawdata.get("animes")
        pages = rawdata.get("pages")[0]
        data = {
            "page": int(rawdata.get("page")[0].get("page", {}).get("text", "1")),
            "pages": "1" if not pages else int(pages[len(pages) - 2]),
            "animes": []
        }

        disabled_animes = site.get_save_to_data("disabled_animes")

        if base == tioanime.base:
            for anime in animes:
                slug = anime.get("anime_slug").get("slug").replace("/anime", "")
                data["animes"].append({
                    "image_url": f"https://{base}/" + anime.get("image").get("url"),
                    "title": anime.get("title").get("text"),
                    "slug": slug,
                    "disabled": False if slug not in disabled_animes else True,
                })

            return data

        for anime in animes:
            title = anime.get("title").get("text")
            temp = title.split(" ")
            watch_type = temp[len(temp) - 1]
            slug = anime.get("anime_slug").get("slug").replace(f"https://{latanime.base}/anime", "")
            data["animes"].append({
                "image_url": anime.get("image").get("url"),
                "title": title,
                "slug": slug,
                "year": anime.get("year").get("text").strip(),
                "type": watch_type,
                "disabled": False if slug not in disabled_animes else True,
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

    def anime_processing(self, rawdata, base=None):
        if base == tioanime.base:
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

            return data

        data = {
            "title": rawdata.get("title").get("title"),
            "description": rawdata.get("description").get("description"),
            "synopsis": rawdata.get("synopsis").get("synopsis"),
            "poster_image": rawdata.get("poster_image").get("poster_image"),
            "genres": [],
            "episodes": [],
        }
        chapters_html = rawdata.get("chapters").get("chapters_html")

        for item in rawdata.get("genres"):
            data["genres"].append({
                "genre_id":item.get("slug").get("text"),
                "genre":item.get("slug").get("text").lower(),
                })

        for item in chapters_html.split('href='):
            found = item.find("https://latanime.org/ver")

            if found == 1:
                temp = item.split(">")[0]
                data["episodes"].append(temp.replace('\"', "").replace("https://latanime.org/ver", ""))

        return data

    def cache_data(self, cache_id, data):
        twelve_hours = 43_200
        cache.hset(name=cache_id, data=data, expiry=twelve_hours)

    def watch_processing(self, rawdata, base):
        data = {
            "episode_title": rawdata.get("episode_title").get("title"),
            "safe_links": [],
            "embed_links": [],
        }

        if base == tioanime.base:
            script = rawdata.get("script").get("embed_script")
            rawlist = script.split("var videos = ")[1].split(";")[0].strip()
            embed_links = ast.literal_eval(rawlist)

            for item in embed_links:
                link =  item[1].replace('\\/', '/')
                name = item[0].lower()

                data["embed_links"].append({
                        "name": name,
                        "link": link,
                    })

                if name in { "yourupload", "sfastwish", "uqload", "mp4upload", "okru" }:
                    data["safe_links"].append({
                            "name": name,
                            "embed_id": str(b64encode(link.encode('utf-8'))),
                            # "id": b64decode(link.encode('utf-8')),
                            "id": link,
                        })
            return data

        data["recommandations"] =[]

        for item in rawdata.get("embed_links"):
            item = item.get("link")
            name = item.get("name")
            link = b64decode(item.get("embed_link")).decode('utf-8')

            data["embed_links"].append({
                    "name": name,
                    "link": link,
                })

            if name in { "sfastwish", "uqload", "mp4upload" }:
                link = item.get("embed_link")
                data["safe_links"].append({
                        "name": name,
                        "id": str(link.encode("utf-8")),
                    })

        for item in rawdata.get("recommendations"):
            title = item.get("title").get("text")
            slug = item.get("slug").get("slug")
            date = item.get("date").get("text")
            episode = item.get("episode").get("text")

            data["recommandations"].append({
                    "title": title,
                    "slug": slug,
                    "date": date,
                    "episode": episode,
                })

        return data

    def get_watch_room_inputs(self, slug, watch_type):
        watch_room_inputs = [
                {
                    "input": "hidden",
                    "key": "slug",
                    "value": slug,
                },
                {
                    "input": "hidden",
                    "key": "type",
                    "value": watch_type,
                },
            ]

        return watch_room_inputs

    def get_anchor_episodes(self, episode_slug, watch_type, episodes):
        prev_episode_slug = ""
        next_episode_slug = ""
        episodes_amount = len(episodes)

        if episodes_amount <= 1:
            prev_episode_slug = episodes[0]
            next_episode_slug = episodes[0]

            return next_episode_slug, prev_episode_slug
            
        for index, episode in enumerate(episodes):
            episode = episode if watch_type == "latino" else episode.get("slug", "")
            slug = episode.replace("/", "")

            if slug == episode_slug:
                prev_episode_slug = episodes[index - 1]
                next_episode_slug = episodes[index + 1] if index < episodes_amount - 1 else episodes[-1]
                break

        return next_episode_slug, prev_episode_slug
    #*** helper functions END ***#
