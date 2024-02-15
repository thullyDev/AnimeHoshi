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
from ...decorators import userValidator
from ...scraping import TioanimeScraper, LatanimeScraper
from ..base import Base

tioanime = TioanimeScraper()
latanime = LatanimeScraper()

storage = Storage()
database = UserDatabase()

class UserAjax(Base):
    @userValidator
    def add_to_list(self, request, user, **kwargs):
        if not request.POST: return redirect("/")

        post_data = request.POST
        slug = post_data.get("slug")
        watch_type = post_data.get("watch_type")

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
    def delete_list_item(self, request, user, **kwargs):
        if not request.POST: return redirect("/")

        POST = request.POST
        anime_title = POST.get("anime_title")
        slug = POST.get("slug")

        res = database.delete_list_item(slug=slug)

        if not res: return self.crash_response()

        return self.successful_response(data={ "message": f"removed {anime_title}"})

    @userValidator
    def change_user_details(self, request, user, **kwargs):
        if not request.POST: return redirect("/")

        post_data = request.POST
        change_type = post_data.get("type")
        value = post_data.get("value")

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
        data = self.anime_processing(rawdata=rawdata, base=tioanime.base)
        return {
            "slug": slug,
            "anime_title": data["title"],
            "anime_image": data["poster_image"],
        }

    def anime_processing(self, rawdata, base=None):
        poster = rawdata.get("poster_image").get("poster_image")
        poster = f"https://{base}/" + poster
        data = {
            "title": rawdata.get("title").get("title"),
            "poster_image": poster,
        }
        return data
