from django.core.mail import send_mail
from datetime import date, datetime, timedelta
from spacy.lang.en import English
from bs4 import BeautifulSoup
import requests
import json
import uuid
import ast
import re
import random
import difflib
import urllib.parse
import pyrebase

# TODO: save tempid to firebase database so that the temp_id is still valid after 24 hours or server restart

class Resources:
    firebase_config = {
        "apiKey": "AIzaSyDYU06_XQ0LYTTyXykkU5aGhR_DBQPrpso",
        "authDomain": "animehoshitest.firebaseapp.com",
        "databaseURL": "https://animehoshitest-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "animehoshitest",
        "storageBucket": "animehoshitest.appspot.com",
        "messagingSenderId": "244056481341",
        "appId": "1:244056481341:web:fef5dcd4b3f077f1d51454",
        "measurementId": "G-YBXD7B11DW"
    };
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    scraper_base = "https://animehoshiapi.onrender.com/"

    def __init__(self, cache):
        #? MAKING INITIAL CACHE
        try:
            temp = self.db.child("app").get().val()
            temp_admins = temp.get("admins")
            temp_users = temp.get("users")
            site_settings = temp.get("site_settings", {})
            users = {} if temp_users == None else temp_users
            admins = {} if temp_admins == None else temp_admins
            # TODO: setup site settings in the database
            database = {
                "users": users,
                "admins": admins,
                "site_settings": site_settings,
            }
        except Exception as e:
            database = {
                "users": {},
                "admins": {},
                "site_settings": {
                    "page_scripts": {
                        "global_scripts": "",
                        "home_scripts": "",
                        "landing_scripts": "",
                        "browsing_scripts": "",
                        "watch_scripts": "",
                        "profile_scripts": "",
                        "donate_scripts": "",
                        "global_foot_scripts": "",
                        "home_foot_scripts": "",
                        "landing_foot_scripts": "",
                        "browsing_foot_scripts": "",
                        "watch_foot_scripts": "",
                        "profile_foot_scripts": "",
                        "donate_foot_scripts": "",
                        "home_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "landing_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "browsing_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "watch_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "watch_popup_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "profile_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "donate_ad": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "home_ad_second": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "landing_ad_second": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "browsing_ad_second": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "watch_ad_second": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "profile_ad_second": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                        "donate_ad_second": {
                            "script": "",
                            "fluid": True,
                            "height": 0,
                        },
                    },
                    "site_attributes": {
                        "user": True, #* global
                        "preload": True, #* global
                        "maintanance": False, #* global
                        "landing_page": True, #* landing
                        "donate_page": True, #* donate
                        "home_slider": True, #* home
                        "home_schedule": True, #* schedule
                        "top_animes": True, #* global
                        "coming_sections": True, #* home
                        "watch_player_buttons": True, #* watch
                        "watch_comments": True, #* watch
                        "player_poster": True, #* watch
                        "manual_slider": False, #* home
                        "base_footer": True, #* global
                        "socials": True, #* global
                        "episode_notice": True, #* watch
                        "dark_mode": False, #* global
                        "page_ads": True, #* global
                        "adblock_detector": True, #* global
                        "alert": True, #* global
                        "related_animes": True, #* global
                     },
                    "site_data": {
                        "title": "As2anime - Watch Anime Online in High Quality For free", #* global
                        "description": "As2anime - Watch Anime Online in High Quality For free. You can watch anime online free in HD without Ads. Best place for free find and one-click anime", #* global
                        "donate": "", #* global
                        "facebook": "", #* global
                        "discord": "", #* global
                        "twitter": "", #* global
                        "reddit": "", #* global
                        "instagram": "", #* global
                        "site_logo": "", #* global
                        "shortcut_logo": "", #* global
                        "landing_background_image": "", #* landing
                        "landing_image": "", #* landing
                        "footer_background_image": "", #* global
                        "profile_background_image": "", #* profile
                        "player_image": "", #* watch
                        "schedule_background_image": "", #* home
                        "default_image": "", #* profile
                        "anime_sliders": "None", #* home
                        "watch_notice": "", #* watch
                        "home_notice": "", #* home
                        "primary_color": "181414", #* global
                        "secondary_color": "dadada", #* global
                        "secondary_highlight_color": "202020", #* global
                        "third_color": "cb0000", #* global
                        "accent_color": "969696", #* global
                        "highlight_color": "252525", #* global
                        "highlight_accent_color": "cb000070", #* global
                        "as2server_name": "As2server", #* watch
                        "backup_server_name": "Backup", #* watch
                        "redirect_url": "", #* global
                        "contact_us": "", #* global
                        "swipe_servers": False, #* watch
                        "recaptcha_site_key": "", #* global
                        "recaptcha_secrete_key": "", #* global
                        "google_verification_code": "", #* global
                        "bing_verification_code": "", #* global
                        "yandex_verification_code": "", #* global
                    },
                },
            }
        site_data = {
            "resources": {},
            "database": database,
        }
        cache.set("site_data", site_data)
        self.cache = cache

    def get_home_data(self):
        slider_data = self.get_silder_resources()
        recent_data = self.get_recent_animes()
        recent_latino_data = self.get_recent_latino_animes()
        movies_data = self.get_movies_animes()
        specials_data = self.get_specials_animes()

        return {
           "slider_data": slider_data,
           "recent_data": recent_data,
           "recent_latino_data": recent_latino_data,
           "movies_data": movies_data,
           "specials_data": specials_data,
        }

    def get_silder_resources(self):
        slider_data = self.get_data(name="slider_data", unit="resources")

        if slider_data == None:
            url_end_point = f"{self.scraper_base}anime/2/sliders/"
            res = requests.get(url_end_point)

            if res.status_code == 200:
                data: list = res.json()["data"]["sliders"]
            else:
                return {
                    "error": "some thing went wrong...",
                    "status_code": res.status_code,
                }

            if res.status_code == 200: self.set_data(name="slider_data", unit="resources", data=data)

            return {
                "data": data,
                "status_code": res.status_code,
            }

        else:

            return {
                "data": slider_data,
                "status_code": 200,
            }

    def get_recent_animes(self, auto_slider=False):
        url_end_point = f"{self.scraper_base}anime/1/recent/"
        res = requests.get(url_end_point)

        if res.status_code == 200:
            data: list = res.json()["data"]["animes"]
        else:
            return {
                "data": [],
                "status_code": res.status_code,
            }

        return {
            "data": data,
            "status_code": res.status_code,
        }

    def get_recent_latino_animes(self, auto_slider=False):
        url_end_point = f"{self.scraper_base}anime/2/recent/"
        res = requests.get(url_end_point)

        if res.status_code == 200:
            data: list = res.json()["data"]["animes"]
        else:
            return {
                "data": [],
                "status_code": res.status_code,
            }

        return {
            "data": data,
            "status_code": res.status_code,
        }

    def get_movies_animes(self, auto_slider=False):
        movies_data = self.get_data(name="movies_data", unit="resources")

        if movies_data == None:
            url_end_point = f"{self.scraper_base}anime/1/?type=1"
            res = requests.get(url_end_point)

            if res.status_code == 200:
                data: list = res.json()["data"]["animes"]
            else:
                return {
                    "data": [],
                    "status_code": res.status_code,
                }

            if res.status_code == 200: self.set_data(name="movies_data", unit="resources", data=data)

            return {
                "data": data,
                "status_code": res.status_code,
            }
        else:
            return {
                "data": movies_data,
                "status_code": 200,
            }

    def get_specials_animes(self, auto_slider=False):
        specials_data = self.get_data(name="specials_data", unit="resources")

        if specials_data == None:
            url_end_point = f"{self.scraper_base}anime/1/?type=3"
            print(url_end_point)
            res = requests.get(url_end_point)

            if res.status_code == 200:
                data: list = res.json()["data"]["animes"]
            else:
                return {
                    "data": [],
                    "status_code": res.status_code,
                }

            if res.status_code == 200: self.set_data(name="specials_data", unit="resources", data=data)

            return {
                "data": data,
                "status_code": res.status_code,
            }
        else:
            return {
                "data": specials_data,
                "status_code": 200,
            }

    def get_data(self, unit, name):
        site_data = self.cache.get("site_data")

        if site_data != None:
            data = site_data.get(unit, {}).get(name)
        else:
            database = self.db.child("app").get().val()
            site_data = {
                "resources": {},
                "database": database,
            }
            data = site_data.get(unit, {}).get(name)
            self.cache.set("site_data", site_data)

        return data

    def set_data(self, data, name, unit):
        site_data = self.cache.get("site_data")
        site_data[unit][name] = data
        self.cache.set("site_data", site_data)
