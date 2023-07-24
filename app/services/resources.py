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
            "resources": {
                "schedule_data": {}
            },
            "database": database,
        }
        cache.set("site_data", site_data)
        self.cache = cache
