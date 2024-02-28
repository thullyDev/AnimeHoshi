from django.shortcuts import render, redirect
from ...resources import (
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
    get_data_from_string,
    generate_unique_id,
)
from ...database import UserDatabase, Storage
from ...decorators import userValidator, timer
from ...handlers import LiveChat
from ...scraping import TioanimeScraper, LatanimeScraper
from ..base import Base
from pprint import pprint

tioanime = TioanimeScraper()
latanime = LatanimeScraper()
storage = Storage()
database = UserDatabase()
live_chat = LiveChat()

class UserAjax(Base):
    @userValidator
    def make_watch_room(self, request, POST, user, **kwargs):
        if not POST: return redirect("/")

        data = self.filter_url_data(POST, ["slug", "type", "room_name", "unlimited", "limit", "private"])

        if not data: return self.bad_request_response()

        name = data.get("room_name", "")
        slug = data.get("slug", "")
        watch_type = data.get("type", "")

        if watch_type not in ["latino", "main"]: return self.bad_request_response()

        if len(name) < 10:
            return self.bad_request_response({ "message": "room name should be atleast 10 characters long" })

        anime = self.get_anime_data(watch_type=watch_type, slug=slug)

        if not anime: return self.bad_request_response()

        data["anime_title"] = anime["anime_title"]
        data["anime_image"] = anime["anime_image"]

        room = live_chat.create_room()

        if not room:
            return self.crash_response({ "message": "room was not recreated" })

        room_id = room["data"]["room_id"]
        room_code = None if data["unlimited"] else generate_random_code(7)

        response = database.create_watch_room(data=data, user=user, room_id=room_id, room_code=room_code) 

        if not response: return self.crash_response()
        
        return self.successful_response({ "message": "room was created", "data": {"room_id": room_id} })

    @userValidator
    def add_to_list(self, request, POST, user, **kwargs):
        if not POST: return redirect("/")

        slug = POST.get("slug")
        watch_type = POST.get("watch_type")

        if watch_type not in ["latino", "main"]: return self.bad_request_response()

        data = self.get_anime_data(watch_type=watch_type, slug=slug)

        if not data: return self.bad_request_response()

        data["user"] = user["id"]
        data["email"] = user["email"]
        data["watch_type"] = watch_type

        res = database.add_to_list(data)

        if not res: return self.crash_response()

        return self.successful_response(data={ "message": "added to my list"})

    @userValidator
    def delete_list_item(self, request, POST, user, **kwargs):
        if not POST: return redirect("/")

        anime_title = POST.get("anime_title")
        slug = POST.get("slug")

        res = database.delete_list_item(slug=slug)

        if not res: return self.crash_response()

        return self.successful_response(data={ "message": f"removed {anime_title}"})

    @userValidator
    def change_user_details(self, request, POST, user, **kwargs):
        if not POST: return redirect("/")

        change_type = POST.get("type")
        value = POST.get("value")

        if change_type not in ["username", "profile_image"]: return self.bad_request_response()

        if "profile_image" == change_type: value = storage.upload_base64_image(name=user["username"] + "_profile_image", base64_img=value)

        data = { "email": user["email"] }
        data[change_type] = value
        res = database.change_user_details(data)

        if not res: return self.crash_response()

        return self.successful_response(data={ "message": "successfully changed " + change_type.replace("_", " ") })

    def get_anime_data(self, slug, watch_type):
        scraper = tioanime if "main" == watch_type else latanime
        rawdata = scraper.get_anime(slug=slug)
        if not rawdata: return None
        data = self.anime_processing(rawdata=rawdata, base=scraper.base)
        return {
            "slug": slug,
            "anime_title": data["title"],
            "anime_image": data["poster_image"],
        }

    def anime_processing(self, rawdata, base=None):
        poster = rawdata.get("poster_image").get("poster_image")
        poster = f"https://{base}/" + poster if base == tioanime.base else poster
        data = {
            "title": rawdata.get("title").get("title"),
            "poster_image": poster,
        }
        return data
