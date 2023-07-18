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
    nlp = English()
    # auth = firebase.auth()
    storage = firebase.storage() 
    jikan_base = "https://api.jikan.moe/v4/"
    simkl_base = "https://api.simkl.com/"
    # scraper_base = "https://as2vid.co.in/"
    scraper_base = "https://godsapi.onrender.com/"
    enime_base = "https://api.enime.moe/"
    kitsu_base = "https://kitsu.io/api/edge/"
    
    
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
            # self.db.child("app").child("admins").child(email_hash_code).update(admin)
        site_data = {
            "resources": {
                "schedule_data": {}
            },
            "database": database,
        }
        cache.set("site_data", site_data)
        self.cache = cache  
        #? BROKE GENRES: music, slice-of-Life
        self.genres = [
            "action",
            "adventure",
            "cars",
            "comedy",
            "crime",
            "dementia",
            "demons",
            "drama",
            "dub",
            "ecchi",
            "family",
            "fantasy",
            "game",
            "gourmet",
            "harem",
            "historical",
            "horror",
            "josei",
            "kids",
            "magic",
            "martial-arts",
            "mecha",
            "military",
            "mystery",
            "parody",
            "police",
            "psychological",
            "romance",
            "samurai",
            "school",
            "sci-fi",
            "seinen",
            "shoujo",
            "shoujo-ai",
            "shounen",
            "shounen-ai",
            "space",
            "sports",
            "super-power",
            "supernatural",
            "suspense",
            "thriller",
            "vampire",
            "yaoi",
            "yuri",
            ];
        self.second_genres = [
            "Action",
            "Adventure",
            "Cars",
            "Comedy",
            "Dementia",
            "Demons",
            "Drama",
            "Ecchi",
            "Fantasy",
            "Game",
            "Harem",
            "Historical",
            "Horror",
            "Isekai",
            "Josei",
            "Kids",
            "Magic",
            "Martial Arts",
            "Mecha",
            "Military",
            "Music",
            "Mystery",
            "Parody",
            "Police",
            "Psychological",
            "Romance",
            "Samurai",
            "School",
            "Sci-Fi",
            "Seinen",
            "Shoujo",
            "Shoujo Ai",
            "Shounen",
            "Shounen Ai",
            "Slice of Life",
            "Space",
            "Sports",
            "Super Power",
            "Supernatural",
            "Thriller",
            "Vampire",
            "Yaoi",
            "Yuri",
        ]
        self.seasons = [
            "Spring",
            "Summer",
            "Fall",
            "Winter",
        ]
        self.type = [
            "Movie",
            "TV Series",
            "OVA",
            "ONA",
            "Special",
            "Music",
        ] 
        self.status  = [
            "All",
            "Finished Airing",
            "Currently Airing",
            "Not yet aired",
        ]
        self.years = [
            "2023",
            "2022",
            "2021",
            "2020",
            "2019",
            "2018",
            "2017",
            "2016",
            "2015",
            "2014",
            "2013",
            "2012",
            "2011",
            "2010",
            "2009",
            "2008",
            "2007",
            "2006",
            "2005",
            "2004",
            "2003",
            "2002",
            "2001",
        ]
        self.languages = [
            "sub",
            "dub",
        ]
 
    def get_silder_resources(self, auto_slider=False):
        site_settings = self.get_site_settings()
        site_attributes = site_settings.get("site_attributes")
        manual_slider = site_attributes.get("manual_slider")
        
        if manual_slider == False or auto_slider == True:
            slider_data = self.get_data(name="slider_data", unit="resources")
            
            if slider_data == None:  
                url_end_point = f"{self.scraper_base}anime/3/sliders/"
                res = requests.get(url_end_point)

                if res.status_code == 200:
                    data: list = res.json()["data"]["sliders"]
                else:
                    return {
                        "error": "some thing went wrong...",
                        "status_code": res.status_code,
                    }
                    
                raw_sliders: list = data[:10]
                sliders = []
                
                for i in raw_sliders:
                    temp = {
                        "cover_image": i.get('image_url', ""),
                        "banner_image": i.get('image_url', ""),
                        "season": i.get("date"),  
                        "year": i.get("date").split(",")[1].strip(),       
                        "title": i.get("title"),    
                        "slug": i.get("slug"),    
                        "type": i.get("type"),    
                        "description": i.get("description"),    
                        "status": "releasing",    
                        "duration": i.get("duration"),    
                        "quality": i.get("quality"),    
                    }
                    sliders.append(temp)
                    
                if res.status_code == 200: self.set_data(name="slider_data", unit="resources", data=sliders)
                
                site_attributes = self.get_site_attributes()  
                home_slider = site_attributes.get("home_slider")
                return {
                    "slider_data": sliders,
                    "slider_enabled": home_slider,
                    "status_code": res.status_code,
                }
            else:
                site_attributes = self.get_site_attributes()  
                home_slider = site_attributes.get("home_slider")
                return {
                    "slider_data": slider_data,
                    "slider_enabled": home_slider,
                    "status_code": 200,
                }
        else:
            site_data = site_settings.get("site_data")
            anime_sliders = site_data.get("anime_sliders") 
            if anime_sliders == None: return self.get_silder_resources(True)
            slider_data = [v for k,v in anime_sliders.items()] 
            home_slider = site_attributes.get("home_slider")
            
            return {
                "slider_data": slider_data,
                "slider_enabled": home_slider,
                "status_code": 200,
            }
                
    def get_trending_animes(self):
        url = "https://9animetv.to/home"
        res = requests.get(url)
        
        if res.status_code != 200:
            return {
                "error": "some thing went wrong...",
                "status_code": res.status_code,
            }
            
        html = res.text.replace('<li class="">', '<li class="item-top">')
        soup = BeautifulSoup(html, 'html.parser')
        top_animes_eles = soup.find_all("li", class_="item-top")
        top_animes = []
        
        for i in top_animes_eles:
            item_soup = BeautifulSoup(str(i), 'html.parser')
            link_ele = item_soup.find_all("a", class_="dynamic-name")[0]
            img_ele = item_soup.find_all("img", class_="film-poster-img")[0]
            span_ele = item_soup.find_all("span", class_="fdi-item")[0]
            watched = span_ele.getText()
            slug = link_ele["href"].split("/")[-1]
            title = img_ele["alt"]
            image_url = img_ele["data-src"]
            temp = {
                "title": title,
                "slug": slug,
                "image_url": image_url,
                "watched": watched,
            }
            top_animes.append(temp)
        
        site_attributes = self.get_site_attributes()  
        top_animes_enabled = site_attributes.get("top_animes")
        
        return {
            "trending_data": top_animes,
            "top_animes_enabled": top_animes_enabled,
            "status_code": res.status_code,
        }
     
    def get_genre(self, genre):
        genre_list: list = difflib.get_close_matches(genre, self.genres)
        similar_genre = random.choice(genre_list) if len(genre_list) else random.choice(self.genres) 
        
        return similar_genre

    def get_related_data(self, genres, limit=40):
        genre = self.get_genre(random.choice(genres))
        url_end_point = f"{self.scraper_base}anime/3/genre/{genre}"
        res = requests.get(url_end_point)

        if res.status_code == 200:
            data: list = res.json()["data"]["animes"][:limit]
        
            return {
                "related_data": data,
                "status_code": res.status_code,
            }
        else: 
            return {
                "error": "some thing went wrong...",
                "status_code": res.status_code,
            }
            
    def get_recent_animes(self):
        url_end_point = f"{self.scraper_base}anime/3/recent"
        res = requests.get(url_end_point)

        if res.status_code == 200:
            data: list = res.json()["data"]["animes"]
        else:
            return {
                "error": "some thing went wrong...",
                "status_code": res.status_code,
            }
            
        animes_list = []
        for i in data:
            temp = {
                "title": i.get("title", ""),
                "image_url": i.get("image_url", ""),
                "slug":  i.get("slug", ""),
                "type":  i.get("type", ""),
                "durataion":  i.get("durataion", ""),
                "description":  i.get("description", ""),
                "ticks": i.get("ticks", {}),
            }
            animes_list.append(temp)

        return {
            "recent_data": animes_list,
            "status_code": res.status_code,
        }

    def get_schedule_data(self, tz_offset, day):
        url = "https://aniwatch.to/ajax/schedule/widget?tzOffset="+tz_offset if day == False else "https://aniwatch.to/ajax/schedule/list?tzOffset="+tz_offset+"&date="+day
        res = requests.get(url)
        
        if res.status_code != 200: 
            return {
                "status_code": res.status_code,
            }
            
        data = res.json()
        
        return {
            "data": data,
            "status_code": 200,
        }
         
    def search_for_anime(self, query):
        return None

    def add_to_list(self,email, temporary_id, playlist, query):
        if email != None and temporary_id != None:
            user = self.get_user(email=email)
            temp_user = {} if user == None else user
            old_temp_id = temp_user.get("temporary_id")
            
            if old_temp_id == temporary_id: 
                if playlist == "watch":
                   animes_list = self.search_for_anime(query)
                   
                   if len(animes_list) != 0:
                       anime_item = animes_list[0]
                       slug = anime_item.get("animeId")
                       watch_list = {} if user.get("watch_list") == "None" else user.get("watch_list")
                       email_hash_code = user.get("email_hash_code")
                       watch_list_anime = watch_list.get(slug)
                       
                       if watch_list_anime == None:
                            watch_list[slug] = anime_item
                            new_temporary_id = str(uuid.uuid4())
                            try:
                                self.db.child("app").child("users").child(email_hash_code).update({
                                    "watch_list": watch_list,
                                    "temporary_id": new_temporary_id,
                                })
                            except Exception as e:
                                print(f"WATCH_LIST Error ===> {e}")
                                return {
                                        "status_code": 403,
                                        "message": "something went wrong..." #? Response Message
                                    }
                            else: 
                                user["watch_list"] = watch_list
                                user["temporary_id"] = new_temporary_id
                                users = self.get_data(name="users", unit="database")
                                users[email_hash_code] = user
                                self.set_data(name="users", unit="database", data=users)
                                
                                response = {
                                    "data": {
                                        "email": email,
                                        "username": user.get("username"),
                                        "temporary_id": new_temporary_id,
                                    },
                                    "message": "added the anime successfully", #? Response Message
                                    "status_code": 200,
                                } 
                       else:
                            response = {
                                "message": "this anime is already in watch list", #? Response Message
                                "status_code": 403,
                            } 
                       
                   else:
                       response = {
                            "message": "couldn't find requested",
                            "status_code": 404,
                        } 
                elif playlist == "likes":
                   animes_list = self.search_for_anime(query)
                   
                   if len(animes_list) != 0:
                       anime_item = animes_list[0]
                       slug = anime_item.get("animeId")
                       likes_list = {} if user.get("likes_list") == "None" else user.get("likes_list")
                       email_hash_code = user.get("email_hash_code")
                       likes_list_anime = likes_list.get(slug)
                       
                       if likes_list_anime == None:
                            likes_list[slug] = anime_item
                            new_temporary_id = str(uuid.uuid4())
                            
                            try:
                                self.db.child("app").child("users").child(email_hash_code).update({
                                    "likes_list": likes_list,
                                    "temporary_id": new_temporary_id,
                                })
                            except Exception as e:
                                print(f"LIKES_LIST Error ===> {e}")
                                return {
                                        "status_code": 403,
                                        "message": "something went wrong..." #? Response Message
                                    }
                            else: 
                                user["likes_list"] = likes_list
                                user["temporary_id"] = new_temporary_id
                                users = self.get_data(name="users", unit="database")
                                users[email_hash_code] = user
                                self.set_data(name="users", unit="database", data=users)
                                
                                response = {
                                    "data": {
                                        "email": email,
                                        "username": user.get("username"),
                                        "temporary_id": new_temporary_id,
                                    },
                                    "message": "added the anime successfully", #? Response Message
                                    "status_code": 200,
                                } 
                       else:
                            response = {
                                "message": "this anime is already in likes list", #? Response Message
                                "status_code": 403,
                            } 
                       
                   else:
                       response = {
                            "message": "couldn't find requested",
                            "status_code": 404,
                        } 
                elif playlist == "check":
                   temp = query.split("-**-")
                   query = temp[0]
                   watch_status = temp[1]
                   animes_list = self.search_for_anime(query)
                   
                   if len(animes_list) == 0:
                      return {
                        "message": "anime not found", #? Response Message
                         "status_code": 403,
                      } 
                   
                   anime_item = animes_list[0]
                   slug = anime_item.get("animeId")
                   likes_list = {} if user.get("likes_list") == "None" else user.get("likes_list")
                   watch_list = {} if user.get("watch_list") == "None" else user.get("watch_list")
                   email_hash_code = user.get("email_hash_code")
                   likes_list_anime = likes_list.get(slug)
                   watch_list_anime = watch_list .get(slug)
                   
                   if likes_list_anime != None:
                      likes_list_anime["watch_status"] = watch_status
                      likes_list[slug] = likes_list_anime
                    
                   if watch_list_anime != None:
                      watch_list_anime["watch_status"] = watch_status
                      watch_list[slug] = watch_list_anime
                      
                   if watch_list_anime != None and likes_list_anime != None:
                      new_temporary_id = str(uuid.uuid4())
                      
                      try:
                        self.db.child("app").child("users").child(email_hash_code).update({
                            "likes_list": likes_list,
                            "watch_list": watch_list,
                            "temporary_id": new_temporary_id,
                        })
                      except Exception as e:
                        print(f"LIKES_LIST Error ===> {e}")
                        return {
                                "status_code": 403,
                                "message": "something went wrong..." #? Response Message
                            }
                      else: 
                        user["likes_list"] = likes_list
                        user["watch_list"] = watch_list
                        user["temporary_id"] = new_temporary_id
                        users = self.get_data(name="users", unit="database")
                        users[email_hash_code] = user
                        self.set_data(name="users", unit="database", data=users)
                        
                        response = {
                            "data": {
                                "email": email,
                                "username": user.get("username"),
                                "temporary_id": new_temporary_id,
                                },
                            "message": "added the anime successfully", #? Response Message
                            "status_code": 201,
                        } 
                        
                   if watch_list_anime != None:
                      new_temporary_id = str(uuid.uuid4())
                      
                      try:
                        self.db.child("app").child("users").child(email_hash_code).update({
                            "watch_list": watch_list,
                            "temporary_id": new_temporary_id,
                        })
                      except Exception as e:
                        print(f"LIKES_LIST Error ===> {e}")
                        return {
                                "status_code": 403,
                                "message": "something went wrong..." #? Response Message
                            }
                      else: 
                        user["watch_list"] = watch_list
                        user["temporary_id"] = new_temporary_id
                        users = self.get_data(name="users", unit="database")
                        users[email_hash_code] = user
                        self.set_data(name="users", unit="database", data=users)
                        
                        response = {
                            "data": {
                                "email": email,
                                "username": user.get("username"),
                                "temporary_id": new_temporary_id,
                                },
                            "message": "added the anime successfully", #? Response Message
                            "status_code": 201,
                        } 
                    
                   if likes_list_anime != None:
                      new_temporary_id = str(uuid.uuid4())
                      
                      try:
                        self.db.child("app").child("users").child(email_hash_code).update({
                            "likes_list": likes_list,
                            "temporary_id": new_temporary_id,
                        })
                      except Exception as e:
                        print(f"LIKES_LIST Error ===> {e}")
                        return {
                                "status_code": 403,
                                "message": "something went wrong..." #? Response Message
                            }
                      else: 
                        user["likes_list"] = likes_list
                        user["temporary_id"] = new_temporary_id
                        users = self.get_data(name="users", unit="database")
                        users[email_hash_code] = user
                        self.set_data(name="users", unit="database", data=users)
                        
                        response = {
                            "data": {
                                "email": email,
                                "username": user.get("username"),
                                "temporary_id": new_temporary_id,
                                },
                            "message": "added the anime successfully", #? Response Message
                            "status_code": 201,
                        } 
                    
                   else:
                       response = {
                            "message": "couldn't find requested",
                            "status_code": 404,
                        } 
                else:
                    response = {
                        "message": "request is invalid",
                        "status_code": 403,
                    }
            else:
                response = {
                    "message": "please login...",
                    "status_code": 503,
                }
        else:
             response = {
                    "message": "please login...",
                    "status_code": 404,
                }
                
        return response

    def delete_list_item(self,email, temporary_id, playlist, slug):
        if email != None and temporary_id != None:
            user = self.get_user(email=email)
            temp_user = {} if user == None else user
            old_temp_id = temp_user.get("temporary_id")
            
            if old_temp_id == temporary_id: 
                if playlist == "watch":
                       watch_list = {} if user.get("watch_list") == "None" else user.get("watch_list")
                       email_hash_code = user.get("email_hash_code")
                       
                       new_temporary_id = str(uuid.uuid4())
                       
                       try:
                           del watch_list[slug]
                           self.db.child("app").child("users").child(email_hash_code).update({ "watch_list": watch_list})
                       except Exception as e:
                           print(f"WATCH_LIST Error ===> {e}")
                           return {
                                "status_code": 403,
                                "message": "something went wrong..." #? Response Message
                            }
                       else: 
                            user["watch_list"] = watch_list
                            user["temporary_id"] = new_temporary_id
                            self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temporary_id, "watch_list": watch_list})
                            users = self.get_data(name="users", unit="database")
                            users[email_hash_code] = user
                            self.set_data(name="users", unit="database", data=users)
                        
                            response = {
                                "data": {
                                    "email": email,
                                    "username": user.get("username"),
                                    "temporary_id": new_temporary_id,
                                },
                                "message": "added the anime successfully", #? Response Message
                                "status_code": 200,
                            }
                                
                elif playlist == "likes":
                       likes_list = {} if user.get("likes_list") == "None" else user.get("likes_list")
                       email_hash_code = user.get("email_hash_code")
                       
                       new_temporary_id = str(uuid.uuid4())
                       
                       try:
                           del likes_list[slug]
                           self.db.child("app").child("users").child(email_hash_code).update({ "likes_list": likes_list})
                       except Exception as e:
                           print(f"likes_list Error ===> {e}")
                           return {
                                "status_code": 403,
                                "message": "something went wrong..." #? Response Message
                            }
                       else: 
                            user["likes_list"] = likes_list
                            user["temporary_id"] = new_temporary_id
                            self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temporary_id, "likes_list": likes_list})
                            users = self.get_data(name="users", unit="database")
                            users[email_hash_code] = user
                            self.set_data(name="users", unit="database", data=users)
                        
                            response = {
                                "data": {
                                    "email": email,
                                    "username": user.get("username"),
                                    "temporary_id": new_temporary_id,
                                },
                                "message": "added the anime successfully", #? Response Message
                                "status_code": 200,
                            }
                else:
                    response = {
                        "message": "request is invalid",
                        "status_code": 403,
                    }
            else:
                response = {
                    "message": "please login...",
                    "status_code": 503,
                }
        else:
             response = {
                    "message": "please login...",
                    "status_code": 503,
                }
                
        return response 
   
    def get_home_data(self, day_int):
        slider_data: list = self.get_silder_resources()
        recent_data: list = self.get_recent_animes()
        
        return {
           "slider_data": slider_data, 
           "recent_data": recent_data, 
        }
        
    def get_watch_data(self, raw_genres):
        genres = ast.literal_eval(raw_genres)
        genres = genres if len(genres) != 0 else ["action"]
        related_data: list = self.get_related_data(genres, limit=20)
        trending_data: list = self.get_top_airing(limit=12)
        print(len(trending_data))
        
        return {
           "related_data": related_data, 
           "trending_data": trending_data, 
        }
        
    def get_next_ep_date(self, slug, last_ep):
        url_end_point = f"{self.episodate_base}show-details?q={slug}"
        res = requests.get(url_end_point)

        if res.status_code == 200: 
            data = res.json()
            show_data = data.get("tvShow", {})
            episodes = reversed(show_data.get("episodes", []))
            status = show_data.get("status", {})
            
            if status == "Running":
                for i in episodes:
                    ep = i.get("episode")
                    if last_ep == ep:
                        return {
                            "anime_data": {
                                "anime_status_code": 200,
                                "episode_name": i.get("name", ""),
                                "episode_num": ep,
                                "date": i.get("air_date", None)
                                },
                            "status_code": res.status_code,
                        }
                
                return {
                        "anime_data": {
                            "anime_status_code": 405,
                            "date": None,
                        },
                        "status_code": res.status_code,
                        }

            else:
                return {
                        "anime_data": {
                            "anime_status": status,
                            "anime_status_code": 201,
                            "status_code": res.status_code,
                            },
                        "status_code": res.status_code,
                        }
        else:
            return {
                "error": "some thing went wrong...",
                "status_code": res.status_code,
            }

    def get_user_profile_image(self, email, temporary_id):
        is_auth = False
        if email == None and temporary_id == None:
            profile_image = None
        else:
            user = self.get_user(email)
            email_hash_code = user.get("email_hash_code")
            old_temp_id = user.get("temporary_id")
        
            if old_temp_id != temporary_id:
                profile_image = None
            else: 
                is_auth = True
                profile_image = user.get("profile_image") if user.get("profile_image") != "None" else None
                
        return {
           "profile_image": profile_image,
           "is_auth": is_auth,
        }
        
    def get_menu_genre(self):    
        return {
           "genres": self.second_genres, 
        }

    def get_watch_list_data(self, email, temporary_id):
        if email == None and temporary_id == None:
            data = self.get_popular_anime()
            watch_list_data = data.get("popular_data", [])
            status_code = data.get("status_code", 404)
            is_user = False
        else:
            user = self.get_user(email)
            email_hash_code = user.get("email_hash_code")
            watch_list = user.get("watch_list")
            likes_list = user.get("likes_list")
            old_temp_id = user.get("temporary_id")
        
            if old_temp_id != temporary_id:
                data = self.get_popular_anime()
                watch_list_data = data.get("popular_data", [])
                status_code = data.get("status_code", 404)
                is_user = False
            else:
                data = self.get_popular_anime()
                status_code = 201
                watch_list_data = data.get("popular_data", [])
                if type(watch_list) is dict and len(watch_list) > 0:  
                    watch_list_data = list(watch_list.values())
                    status_code = 200
                is_user = True
                
        return {
           "watch_list_data": watch_list_data, 
           "status_code": status_code, 
           "is_user": is_user,
        }
    
    def get_likes_list_data(self, email, temporary_id):
        if email == None and temporary_id == None:
            data = self.get_top_airing()
            likes_list_data = data.get("current_top_airing_data", [])
            status_code = data.get("status_code", 404)
            is_user = False
        else:
            user = self.get_user(email)
            email_hash_code = user.get("email_hash_code")
            likes_list = user.get("likes_list")
            old_temp_id = user.get("temporary_id")
            
            if old_temp_id != temporary_id:
                data = self.get_top_airing()
                likes_list_data = data.get("current_top_airing_data", [])
                status_code = data.get("status_code", 404)
                is_user = False
            else:
                data = self.get_top_airing()
                status_code = 201
                likes_list_data = data.get("current_top_airing_data", [])
                if type(likes_list) is dict and len(likes_list) > 0:  
                    likes_list_data = list(likes_list.values())
                    status_code = 200
                is_user = True
                
        return {
           "likes_list_data": likes_list_data, 
           "status_code": status_code,
           "is_user": is_user,
        }
        
    def get_top_airing(self, limit=40):
        gogo_topairing_data = self.get_data(name="gogo_top_airing", unit="resources")
        
        if gogo_topairing_data == None:  
            api_url = f"{self.scraper_base}anime/3/top_airing"
            response = requests.get(api_url)

            if response.status_code == 200:    
                temp = response.json()["data"]["animes"]
                anime_list = []
                
                count = 1
                for i in temp:
                    anime_list.append(i)
                    
                    if count == limit: break
                    count += 1
                
                self.set_data(name="gogo_top_airing", unit="resources", data=temp)
                
                return  {
                    "current_top_airing_data": anime_list,
                    "status_code": response.status_code,
                }
            else:
                return {
                    "status_code": response.status_code
                }
            
        else: 
            gogo_topairing_data = gogo_topairing_data
            anime_list = []
            
            count = 1
            for i in gogo_topairing_data:
                anime_list.append(i)
                
                if count == limit: break
                count += 1
            
            return {
                "current_top_airing_data": anime_list,
                "status_code": 200,
            }
   
    def get_popular_anime(self):
        popular_data = self.get_data(name="popular", unit="resources")
        
        if popular_data == None:  
            api_url = f"{self.scraper_base}anime/3/popular"
            print(api_url)
            response = requests.get(api_url)

            if response.status_code == 200:    
                data = response.json()["data"]["animes"]
                    
                self.set_data(name="popular", unit="resources", data=data)
                
                return  {
                    "popular_data": data,
                    "status_code": response.status_code,
                }
            else:
                return {
                    "status_code": response.status_code
                }
            
        else: 
            return {
                "popular_data": popular_data,
                "status_code": 200,
            }
                
    def get_sitemap_list_data(self, page):
        api_url = f"{self.scraper_base}popular?page={page}"
        response = requests.get(api_url)

        return response.json() if response.status_code == 200 else []
            
    def random(self):
        response = self.get_popular_anime()
        
        if response.get("status_code") == 200:
            anime = random.choice(response.get("popular_data"))
            
            return {
                "data": {
                    "slug": anime.get("animeId"),
                },
                "status_code": 200,
            }
        else:
            return {
                "status_code": 503,
            }
                
    def get_landing_data(self): return self.get_popular_anime()
    
    def get_landing_site_data(self):
        site_settings = self.get_site_settings()
        site_data = site_settings.get("site_data", {})
        landing_image = site_data.get("landing_image", "")
        landing_background_image = site_data.get("landing_background_image", "")
        
        return {
            "landing_image": landing_image,
            "landing_background_image": landing_background_image,
            "scripts": self.get_scripts_site_data("landing"),
        }
        
    def get_admin_anime_sliders(self):
        site_settings = self.get_site_settings()
        manual_slider = site_settings.get("site_attributes", {}).get("manual_slider")
        anime_sliders = site_settings.get("site_data", {}).get("anime_sliders", {})
        
        return {
            "manual_slider": manual_slider,
            "anime_sliders": anime_sliders,
        }
        
    def get_home_site_data(self):
        site_settings = self.get_site_settings()
        site_data = site_settings.get("site_data", {})
        schedule_background_image = site_data.get("schedule_background_image", "")
        home_notice = site_data.get("home_notice", "")
        
        return {
            "schedule_background_image": schedule_background_image,
            "home_notice": home_notice,
            "scripts": self.get_scripts_site_data("home"),
        }
        
    def get_profile_site_data(self):
        site_settings = self.get_site_settings()
        site_data = site_settings.get("site_data", {})
        profile_background_image = site_data.get("profile_background_image", "")
        
        return {
            "profile_background_image": profile_background_image,
            "scripts": self.get_scripts_site_data("profile"),
        }
        
    def get_browsing_site_data(self): return {"scripts": self.get_scripts_site_data("browsing")}
        
    def get_watch_site_data(self):
        site_settings = self.get_site_settings()
        site_data = site_settings.get("site_data", {})
        watch_notice = site_data.get("watch_notice", "")
        as2server_name = site_data.get("as2server_name", "")
        backup_server_name = site_data.get("backup_server_name", "")
        swipe_servers = site_data.get("swipe_servers", "")
        
        return {
            "watch_notice": watch_notice,
            "as2server_name": as2server_name,
            "backup_server_name": backup_server_name,
            "swipe_servers": swipe_servers,
            "scripts": self.get_scripts_site_data("watch"),
        }
        
    def get_donate_site_data(self): return {"scripts": self.get_scripts_site_data("donate")}
      
        
    def get_jikan_anime(self, is_browsing=False):
        jikan_anime = self.get_data(name="jikan_anime", unit="resources")
        
        if jikan_anime == None:  
            api_url = f"{self.jikan_base}anime"
            response = requests.get(api_url)
            
            if response.status_code == 200:    
                data = response.json()
                del data["data"]
                
                self.set_data(name="jikan_anime", unit="resources", data=data)
                
                return  {
                    "jikan_anime": data,
                    "status_code": response.status_code,
                }
            else:
                return {
                    "status_code": response.status_code
                }
            
        else: 
        
            return {
                "jikan_anime": jikan_anime,
                "status_code": 200,
            }
      
    def get_scripts_site_data(self, page):
        site_settings = self.get_site_settings()
        site_scripts = site_settings.get("page_scripts", {})
        
        return {
            'page_scripts': site_scripts.get(f"{page}_scripts", ""),
            'page_foot_scripts': site_scripts.get(f"{page}_foot_scripts", ""),
            'page_ad': site_scripts.get(f"{page}_ad", ""),
            'second_page_ad': site_scripts.get(f"{page}_ad_second", ""),
            'page_popup_ad': site_scripts.get(f"{page}_popup_ad", ""),
        }
    
    def get_global_data(self, attributes={}): 
        site_settings = self.get_site_settings()
        page_scripts = site_settings.get("page_scripts", {})
        global_scripts = page_scripts.get("global_scripts", "")
        global_foot_scripts = page_scripts.get("global_foot_scripts", "")
        site_data = site_settings.get("site_data", {})
        title = site_data.get("title", "")
        description = site_data.get("description", "")
        donate = site_data.get("donate", "")
        facebook = site_data.get("facebook", "")
        discord = site_data.get("discord", "")
        twitter = site_data.get("twitter", "")
        Reddit = site_data.get("Reddit", "")
        site_logo = site_data.get("site_logo", "")
        shortcut_logo = site_data.get("shortcut_logo", "")
        footer_background_image = site_data.get("footer_background_image", "")
        primary_color = site_data.get("primary_color", "")
        secondary_color = site_data.get("secondary_color", "")
        secondary_highlight_color = site_data.get("secondary_highlight_color", "")
        third_color = site_data.get("third_color", "")
        accent_color = site_data.get("accent_color", "")
        highlight_color = site_data.get("highlight_color", "")
        highlight_accent_color = site_data.get("highlight_accent_color", "")
        redirect_url = site_data.get("redirect_url", "")
        contact_us = site_data.get("contact_us", "")
        recaptcha_site_key = site_data.get("recaptcha_site_key", "")
        recaptcha_secrete_key = site_data.get("recaptcha_secrete_key", "")
        google_verification_code = site_data.get("google_verification_code", "")
        bing_verification_code = site_data.get("bing_verification_code", "")
        yandex_verification_code = site_data.get("yandex_verification_code", "")
        
        recaptcha_valid = True if len(recaptcha_site_key) > 0 and len(recaptcha_secrete_key) > 0 else False
        
        global_data = {
            "title": title,
            "description": description,
            "donate": donate,
            "facebook": facebook,
            "discord": discord,
            "twitter": twitter,
            "Reddit": Reddit,
            "site_logo": site_logo,
            "shortcut_logo": shortcut_logo,
            "footer_background_image": footer_background_image,
            "redirect_url": redirect_url,
            "contact_us": contact_us,
            "recaptcha_site_key": recaptcha_site_key,
            "google_verification_code": google_verification_code,
            "bing_verification_code": bing_verification_code,
            "yandex_verification_code": yandex_verification_code,
            "recaptcha_valid": recaptcha_valid,
            "colors": {
                "primary-color": primary_color,
                "secondary-color": secondary_color,
                "secondary-highlight_color": secondary_highlight_color,
                "third-color": third_color,
                "accent-color": accent_color,
                "highlight-color": highlight_color,
                "highlight-accent_color": highlight_accent_color,
            },
            "attributes": attributes,
            "scripts": {
                "global_scripts": global_scripts,
                "global_foot_scripts": global_foot_scripts,
            },
        }
        
        return global_data

    def get_profile_data(self, email=None, temporary_id=None, view_user=None):
        if view_user == None:
            if email == None and temporary_id == None:
                return {
                        "message": "please login...",
                        "status_code": 403,
                    }
            
            site_settings = self.get_site_settings()
            site_attributes = site_settings.get("site_settings")
            site_data = site_settings.get("site_data") #player_image    
            default_image = site_data.get("default_image") if site_data.get("default_image") != "" else "/static/images/default.jpg"
            user = self.get_user(email)
            email_hash_code = user.get("email_hash_code")
            username = user.get("username")
            email = user.get("email")
            watch_list = user.get("watch_list")
            likes_list = user.get("likes_list")
            profile_image_url = user.get("profile_image")
            old_temp_id = user.get("temporary_id")
            
            if old_temp_id == temporary_id:
                new_temp_id = str(uuid.uuid4())
                user["temporary_id"] = new_temp_id
                self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temp_id})
                users = self.get_data(name="users", unit="database")
                users[email_hash_code] = user
                self.set_data(name="users", unit="database", data=users)
                response = {
                    "data": {
                        "username": username,
                        "email": email,
                        "temporary_id": new_temp_id,
                        "watch_list": watch_list,
                        "likes_list": likes_list,
                        "profile_image": profile_image_url,
                        "default_image": default_image,
                    },
                    "status_code": 200,
                } 
            else:
                response = {
                    "message": "please login...",
                    "status_code": 403,
                } 
        else:
            site_settings = self.get_site_settings()
            site_attributes = site_settings.get("site_settings")
            site_data = site_settings.get("site_data") #player_image    
            default_image = site_data.get("default_image") if site_data.get("default_image") != "" else "/static/images/default.jpg"
            user = self.get_user(view_user)
            email_hash_code = user.get("email_hash_code")
            username = user.get("username")
            email = user.get("email")
            watch_list = user.get("watch_list")
            likes_list = user.get("likes_list")
            profile_image_url = user.get("profile_image")
            old_temp_id = user.get("temporary_id")
            
            response = {
                    "data": {
                        "username": username,
                        "email": email,
                        "watch_list": watch_list,
                        "likes_list": likes_list,
                        "profile_image": profile_image_url,
                        "default_image": default_image,
                    },
                    "status_code": 200,
                } 
                
        return response
       
    def get_coming_data(self, coming_id):
        coming_data = self.get_data(name=coming_id, unit="resources")
        
        if coming_data == None:
            if coming_id == "premieres": api_url = f"{self.scraper_base}anime/3/new"
            elif coming_id == "upcoming": api_url = f"{self.scraper_base}anime/3/upcoming"
            else: api_url = f"{self.scraper_base}anime/3/complete"
            response = requests.get(api_url)

            if response.status_code == 200:    
                data = response.json()["data"]["animes"][:5] 
                
                self.set_data(name=coming_id, unit="resources", data=data)
                site_attributes = self.get_site_attributes()  
                coming_sections = site_attributes.get("coming_sections")
                
                return {
                    "coming_section_enabled": coming_sections,
                    "data": data,
                }
            else:
                return {
                    "status_code": 403
                }
            
        else:  
            site_attributes = self.get_site_attributes()  
            coming_sections = site_attributes.get("coming_sections")
            
            return {
                "coming_section_enabled": coming_sections,
                "data": coming_data,
            }
        
    def act_user(self, email):
        hash_email = self.nlp.vocab[email] 
        email_hash_code = str(hash_email.orth) 
        try:
            self.db.child("app").child("users").child(email_hash_code).remove()
            pass
        except Exception as e:
            print(f"RENEW_USERNAME Error ===> {e}")
            return {
                    "status_code": 503,
                    "message": "something went wrong..." #? Response Message
                }
        else:
            users = self.get_data(name="users", unit="database")
            del users[email_hash_code]
            try:
                self.db.child("app").child("users").child(email_hash_code).remove()
            except Exception as e:
                print(f"error ==> {e}")
            finally:
                self.set_data(name="users", unit="database", data=users)
            
            return {
                    "status_code": 200,
                    "message": "successfully deleted user..." #? Response Message
                }
        
    def change_user_details(self, change_type, email, temporary_id, user_inp):
        if email == None and temporary_id == None:
            return {
                    "message": "please login...",
                    "status_code": 403,
                } 
        user = self.get_user(email)
        email_hash_code = user.get("email_hash_code")
        username = user.get("username")
        profile_image_url = user.get("profile_image")
        old_temp_id = user.get("temporary_id")
        
        if change_type == "username":
            if old_temp_id == temporary_id:
                try:
                    self.db.child("app").child("users").child(email_hash_code).update({"username": user_inp})
                except Exception as e:
                    print(f"RENEW_USERNAME Error ===> {e}")
                    return {
                            "status_code": 503,
                            "message": "something went wrong..." #? Response Message
                        }
                else: 
                    new_temp_id = str(uuid.uuid4())
                    user["temporary_id"] = new_temp_id
                    user["username"] = user_inp
                    self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temp_id, "username": user_inp})
                    users = self.get_data(name="users", unit="database")
                    users[email_hash_code] = user
                    self.set_data(name="users", unit="database", data=users)
                    response = {
                        "data": {
                            "username": user_inp,
                            "email": email,
                            "temporary_id": new_temp_id,
                            "profile_image": profile_image_url,
                        },
                        "message": "changed the username successfully",
                        "status_code": 200,
                    } 
            else:
                response = {
                    "message": "please login...",
                    "status_code": 403,
                } 
        elif change_type == "profile_image":
            if old_temp_id == temporary_id:
                try:
                    self.db.child("app").child("users").child(email_hash_code).update({"profile_image": user_inp})
                except Exception as e:
                    print(f"profile_image_url Error ===> {e}")
                    return {
                            "status_code": 503,
                            "message": "something went wrong..." #? Response Message
                        }
                else: 
                    new_temp_id = str(uuid.uuid4())
                    user["temporary_id"] = new_temp_id
                    user["profile_image"] = user_inp
                    self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temp_id, "profile_image": user_inp})
                    users = self.get_data(name="users", unit="database")
                    users[email_hash_code] = user
                    self.set_data(name="users", unit="database", data=users)
                    response = {
                        "data": {
                            "profile_image": user_inp,
                            "email": email,
                            "temporary_id": new_temp_id,
                        },
                        "message": "changed the profile_image_url successfully",
                        "status_code": 200,
                    } 
            else:
                response = {
                    "message": "please login...",
                    "status_code": 403,
                }
        else:
            response = {
                "status_code": "this request is invalid",
            }
            
        return response
        
    def get_browsing_data(self, request_data):
        # sort = "default"
        # https://9animetv.to/filter?keyword=&type=&status=all&season=&language=&sort=default&year=&genre=1
        # page == 1
        data = json.loads(request_data)
        genre = data.get("genre", "")
        keyword = urllib.parse.quote(data.get("keyword", ""))
        season = data.get("season", "")
        year = data.get("year", "")
        status = data.get("status", "all")
        language = data.get("language", "")
        status = data.get("status", "")
        page = data.get("page", "")
        anime_type = data.get("type", "")
        url = f"https://9animetv.to/filter?keyword={keyword}&type={anime_type}&status={status}&season={season}&language={language}&sort=default&year={year}&genre={genre}&page={page}"
        res = requests.get(url)
        
        if res.status_code == 200:
            html = res.text
            soup = BeautifulSoup(html, 'html.parser')
            anime_items = soup.find_all("div", class_="flw-item")
            try:
                pager_div = soup.find_all("div", class_="btn-blank")[1]
            except:
                pages = 0
            else:
                pages = int(pager_div.getText().replace("of ", ""))
            anime_list = []
            
            for i in anime_items:
                item_soup = BeautifulSoup(str(i), 'html.parser')
                ticks_ele = item_soup.find_all("div", class_="tick-item")
                img_ele = item_soup.find_all("img", class_="film-poster-img")[0]
                link_ele = item_soup.find_all("a", class_="film-poster-ahref")[0]
                title = img_ele["alt"]
                slug = link_ele["href"].split("/")[-1]
                image_url = img_ele["data-src"]
                attributes = []
                
                for j in ticks_ele:
                    string = str(j).replace('<div class="tick-item tick-eps">', "").replace(' </div>', "").strip()
                    
                    if string.find("Ep ") != -1:
                        eps = string.replace("Ep ", "")
                        attributes.append(eps)
                    else:
                        attributes.append(j.getText())
                                
                    
                anime_list.append({
                    "title": title, 
                    "slug": slug, 
                    "image_url": image_url, 
                    "attributes": attributes, 
                }) 

            browsing_data = {
                "anime_list": anime_list[:19], # TODO: for now this slice list in half, later make proper way to show all the anime_list items
                "pages": pages,
            }    
            
            return {
                "browsing_data": {
                    "status_code": res.status_code,
                    "browsing_data": browsing_data,
                },
            } 
        else:
            return {
                "error": "some thing went wrong...",
                "status_code": res.status_code,
            }

    def get_data(self, unit, name):
        site_data = self.cache.get("site_data")
        
        if site_data != None:
            data = site_data.get(unit, {}).get(name)
        else: 
            database = self.db.child("app").get().val()
            site_data = {
                "resources": {
                    "schedule_data": {}
                },
                "database": database,
            }
            data = site_data.get(unit, {}).get(name)
            self.cache.set("site_data", site_data)
        
        return data
    
    def set_data(self, data, name, unit):
        site_data = self.cache.get("site_data")
        site_data[unit][name] = data
        self.cache.set("site_data", site_data)
        
    def save_site_settings(self, save_type, data, admin_temp_id, admin_email, cookies):
        temp_admin_email, temp_admin_username, temp_admin_temp_id = self.get_current_admin(cookies)
        
        if temp_admin_email == None: 
             return {
                    "status_code": 403,
                    "message": "this is forbidden user",
                }
        
        new_temp_id = temp_admin_temp_id
        
        if save_type == "general_settings":
            site_data = data.get("site_data")
            site_settings = self.get_site_settings()
            site_settings["site_data"] = site_data
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "saved site settings successfully",
            }
        elif save_type == "advance_settings":
            site_attributes = data.get("site_attributes")
            site_settings = self.get_site_settings()
            site_settings["site_attributes"] = site_attributes
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "saved site settings successfully",
            }
        elif save_type == "scripts":
            site_scripts = data.get("site_scripts")
            site_settings = self.get_site_settings()
            site_settings["page_scripts"] = site_scripts
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "saved site settings successfully",
            }
        elif save_type == "anime_slider":
            site_settings = self.get_site_settings()
            data["data"]["created_at"] = str(date.today() - timedelta(1))
            slider_id = str(uuid.uuid4())
            data["data"]["id"]  = slider_id
            site_data = site_settings.get("site_data")
            temp_anime_slider = site_data.get("anime_sliders")
            anime_sliders =  temp_anime_slider if temp_anime_slider != None else {}
            anime_sliders[slider_id] = data["data"]
            site_data["anime_sliders"] = anime_sliders
            site_settings["site_data"] = site_data
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "successfully saved slider",
            }
        elif save_type == "reset_settings":
            site_settings = {
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
                    "third_color": "e22be7", #* global 
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
            }
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            # self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "successfully reset settings",
            }
        elif save_type == "anime_slider_toggle":
            site_settings = self.get_site_settings()
            manual_slider = data.get("value") # if slider_toggle is True use automatic slider else use manual slider
            site_settings["site_attributes"]["manual_slider"] = manual_slider
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "saved site settings successfully",
            }
        elif save_type == "delete_slider":
            site_settings = self.get_site_settings()
            anime_slider_id = data.get("id")
            site_data = site_settings.get("site_data")
            anime_sliders = site_data.get("anime_sliders") if site_data.get("anime_sliders") != "None" else {}
            del anime_sliders[anime_slider_id]
            site_data["anime_sliders"] = anime_sliders
            site_settings["site_data"] = site_data
            self.set_data(name="site_settings", unit="database", data=site_settings)
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "saved site settings successfully",
            }
        elif save_type == "edit_slider":
            site_settings = self.get_site_settings()
            slider_data = data.get("data")
            slider_id = slider_data.get("id")
            site_data = site_settings.get("site_data")
            anime_sliders = site_data.get("anime_sliders") if site_data.get("anime_sliders") != "None" else {}
            anime_sliders[slider_id] = slider_data
            site_data["anime_sliders"] = anime_sliders
            site_settings["site_data"] = site_data
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="site_settings", unit="database", data=site_settings)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"site_settings": site_settings,})
            
            return {
                "data": {
                    "site_settings": site_settings,
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "successfully saved slider",
            }
        elif save_type == "edit_user":
            users = self.get_data(name="users", unit="database")
            email_hash_code = data.get("id")
            user = users[email_hash_code]
            user["profile_image"] = data.get("profile_image")
            user["username"] = data.get("username")
            user["password"] = data.get("password")
            users[email_hash_code] = user
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="users", unit="database", data=users)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"users": users,})
            
            return {
                "data": {
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                },
                "status_code": 200,
                "message": "successfully edited user info",
            }
        elif save_type == "change_vip":
            users = self.get_data(name="users", unit="database")
            email = data.get("email")
            value = data.get("value", False)
            hash_email = self.nlp.vocab[email] 
            email_hash_code = str(hash_email.orth)
            user = users[email_hash_code]
            vip_expiration = datetime.today().strftime('%Y-%m-%d %H:%M:%S') # datetime.strptime(vip_expiration, %Y-%m-%d %H:%M:%S')
            
            if value == False:
                vip_expiration = 0
                user["is_vip"] = value
                user["vip_expiration"] = vip_expiration
            else:
                user["is_vip"] = value
                user["vip_expiration"] = vip_expiration 
                
            users[email_hash_code] = user
            admins = self.get_data(name="admins", unit="database")
            hash_email = self.nlp.vocab[admin_email] 
            email_hash_code = str(hash_email.orth)
            admins[email_hash_code]["temporary_id"] = new_temp_id
            self.set_data(name="users", unit="database", data=users)
            self.set_data(name="admins", unit="database", data=admins)
            self.db.child("app").update({"users": users,})
            
            return {
                "data": {
                    "email": admin_email,
                    "temporary_id": new_temp_id,
                    "vip_expiration": self.exp_parser(vip_expiration),
                },
                "status_code": 200,
                "message": "successfully edited user info",
            }
        else: 
           return {
                "status": 503,
                "message": "this request is invalid",
            } 
                      
    def get_anime(self, slug, server_id, anime_slug): pass
                        
    def get_watch_anime(self, slug): 
        url_end_point = f"{self.scraper_base}anime/1/details/{slug}"
        res = requests.get(url_end_point)
        
        if res.status_code == 200:
            data = res.json()["data"]
            del data["host"]
            del data["referer"]
            del data["url"]
            
            return {
                "anime_data": data,
            }
         
        return {}
    
    def anime(self, slug):
        url = f"{self.enime_base}anime/{slug}"
        res = requests.get(url)
        
        return [] if res.status_code != 200 else res.json()
        
    def authenticate(self, auth_type, data):
        data = json.loads(data)
        if auth_type == "login": 
            email = data.get("email")
            
            if self.check(email) == True: auth_response = self.login_user(data)
            else: 
                auth_response = {
                    "status_code": 403,
                    "message": "The email was invalid"
                }
        elif auth_type == "signup": 
            email = data.get("email")
            token = data.get("token")
            
            res_code = self.verify_grecaptcha(token)
            
            if res_code == 200: 
                if self.check(email) == True: auth_response = self.signup_user(data)
                else: 
                    auth_response = {
                        "status_code": 403,
                        "message": "The email was invalid"
                    }
            else: 
                auth_response = {
                    "status_code": res_code,
                    "message": "The recaptcha couldn't verify the request..."
                }
        elif auth_type == "forgot_password": auth_response = self.forgot_password(data)
        elif auth_type == "renew": auth_response = self.renew_user_password(data)
        elif auth_type == "verify": auth_response = self.verify_user(data=data, auth_type=auth_type)
        else:
            auth_response = {
                "status_code": 403,
                "message": "The authentication request was invalid"
            }
        
        return auth_response
        
    def admin_authenticate(self, data):
        email = data.get("email")
        password = data.get("password")
        admins = self.get_data(name="admins", unit="database")
        hash_email = self.nlp.vocab[email] 
        email_hash_code = str(hash_email.orth)
        admin = admins.get(email_hash_code)
    
        if admin != None:
            admin_password = admin.get("password")
            
            if password == admin_password:
                temp_id = str(uuid.uuid4())
                admin["temporary_id"] = temp_id
                admins[email_hash_code] = admin
                self.set_data(name="admins", unit="database", data=admins)
                auth_response = {
                    "data": {
                        "email": email,
                        "temporary_id": temp_id,
                        "name": admin.get("name"),
                    },
                    "status_code": 200,
                    "message": "Admin login was successful" #? Response Message
                }
            else:
                auth_response = {
                    "status_code": 403,
                    "message": "Password is incorrect" #? Response Message
                }
        else:
            auth_response = {
                "status_code": 403,
                "message": "Email is not registed" #? Response Message
            }
            
        return auth_response        
        
    def send_verification_email(self, email, code, text):
        app_email = "demykunta@gmail.com" # TODO: change this cred 
       
        send_mail("As2anime confirmation", code, app_email, [email])

    def check(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        
        return True if(re.search(regex,email)) else False
                                            
    def renew_user_password(self, data):
        email = data.get("email")
        password = data.get("password")
        confirm = data.get("confirm")
        
        if password == confirm:
            if len(password) >= 8:
                user = self.get_user(email)
                email_hash_code = user.get("email_hash_code")
                new_temp_id = str(uuid.uuid4)
                try:
                    self.db.child("app").child("users").child(email_hash_code).update({"password": password})
                except Exception as e:
                    print(f"RENEW_USER_PASSWORD Error ===> {e}")
                    return {
                            "status_code": 503,
                            "message": "something went wrong..." #? Response Message
                        }
                else: 
                    user["password"] = password
                    user["temporary_id"] = new_temp_id
                    self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temp_id, "password": password})
                    users = self.get_data(name="users", unit="database")
                    users[email_hash_code] = user
                    self.set_data(name="users", unit="database", data=users)
                    
                    return {
                        "data": {
                            "temporary_id": user.get("temporary_id"),
                            "email": user.get("email"),
                            "username": user.get("username"),
                        },
                        "status_code": 200,
                    } 
            else:
                return {
                    "status_code": 503,
                    "message": "password should be aleast 8 characters" #? Response Message
                } 
        else: 
            return {
                "status_code": 503,
                "message": "password and confirm don't match" #? Response Message
            }  

    def forgot_password(self, data):
        email = data.get("email")
        user = self.get_user(email=email)
        
        if user != None:
            code = self.get_verification_code()
            data["verification_time"] = str(date.today() - timedelta(1))
            data["is_verified"] = False
            data["is_for"] = "forgot_password"
            text = "confirmation code"
            self.send_verification_email(email=email, code=code, text=text)
            self.set_data(name="verification_data", unit="resources", data={code: data})
        
            return {
                    "status_code": 200,
                    "data": {
                        "email": email,
                    },
                    "message": "sent the confirmation code to the email you have provided" #? Response Message
                }
        else:
            return {
                "status_code": 403,
                "message": "Email is not registed"
            }
            
    def login_user(self, data):
        email = data.get("email")
        password = data.get("password")
        user = self.get_user(email=email)
    
        if user != None:
            user_password = user.get("password")
            
            if password == user_password:
                temp_id = str(uuid.uuid4())
                email_hash_code = user.get("email_hash_code")
                user["temporary_id"] = temp_id
                self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": temp_id})
                users = self.get_data(name="users", unit="database")
                users[email_hash_code] = user
                self.set_data(name="users", unit="database", data=users)
                auth_response = {
                    "data": {
                        "email": email,
                        "temporary_id": temp_id,
                        "username": user.get("username"),
                    },
                    "status_code": 200,
                    "message": "User login was successful" #? Response Message
                }
            else:
                auth_response = {
                    "status_code": 403,
                    "message": "Password is incorrect" #? Response Message
                }
        else:
            auth_response = {
                "status_code": 403,
                "message": "Email is not registed" #? Response Message
            }
            
        return auth_response
    
    def get_user_with_temp_id(self, data):
        email = data.get("email")
        user = self.get_user(email=email)
        user_temp_id = data.get("temporary_id")
        temporary_id = user.get("temporary_id")
        
        if user_temp_id == temporary_id:
            email_hash_code = user.get("email_hash_code")
            user["temporary_id"] = new_temp_id
            self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temp_id})
            users = self.get_data(name="users", unit="database")
            users[email_hash_code] = user
            self.set_data(name="users", unit="database", data=users)
            auth_response = {
                "data": user,
                "status_code": 200,
                "message": "Got user data" #? Response Message
            }
        else:
            auth_response = {
                "status_code": 404,
                "message": "User is not is logged in" #? Response Message
            }
    
    def signup_user(self, data):
        email = data.get("email")
        password = data.get("password")
        confirm = data.get("confirm")
        
        if len(password) >= 8:
            if confirm == password:
                code = self.get_verification_code()
                data["verification_time"] = str(date.today() - timedelta(1))
                data["is_for"] = "signup"
                email = data.get("email")
                text = "confirmation code"
                self.send_verification_email(email=email, code=code, text=text)
                self.set_data(name="verification_data", unit="resources", data={code: data})
                
                return {
                        "status_code": 200,
                        "data": {
                            "email": email,
                        },
                        "message": "sent the confirmation code to the email you have provided" #? Response Message
                    }
            else:
                return {
                         "status_code": 403,
                          "message": "The password and confirm dont match" #? Response Message
                        }
        else:
            return {
                     "status_code": 403,
                     "message": "The password should have atleast 8 characters" #? Response Message
                    }
        
    def verify_user(self, data, auth_type):
        verify_data = self.get_data(name="verification_data", unit="resources")
        code = data.get("code")
        user = verify_data.get(code)
        
        def check_verification_time(time):
            # TODO: check the verification time for real time
            return True

        if user != None:
            auth = user.get("is_for")
            
            if auth == "signup":
                if check_verification_time(user["verification_time"]) == True:
                    create_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    username = user.get("username")
                    email = user.get("email")
                    confirm = user.get("confirm")
                    password = user.get("password")
                    
                    if confirm == password:
                        temporary_id = str(uuid.uuid4())
                        hash_email = self.nlp.vocab[email] 
                        email_hash_code = str(hash_email.orth)
                        # email = nlp.vocab[email_hash_code].text #? to get the email again 
                        user = {
                            "username": username,
                            "email": email,
                            "email_hash_code": email_hash_code,
                            "password": password,
                            "watch_list": "None",
                            "likes_list": "None",
                            "profile_image": "None",
                            "create_at": create_at,
                        }
                        
                        try:
                            self.db.child("app").child("users").child(email_hash_code).update(user)
                        except Exception as e:
                            print(f"SIGNUP Error ===> {e}")
                            return {
                                "status_code": 503,
                                "message": "something went wrong..." #? Response Message
                            }
                        else:
                            user["temporary_id"] = temporary_id
                            self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": temporary_id})
                            users = self.get_data(name="users", unit="database")
                            users[email_hash_code] = user
                            self.set_data(name="users", unit="database", data=users)
                            
                            return {
                                    "status_code": 200,
                                    "data": {
                                      "email": email,
                                      "temporary_id": temporary_id,
                                      "auth": "signup",
                                      "username": user.get("username"),
                                    },
                                    "message": "User signup was sucessful" #? Response Message
                                }
                    else:
                        auth_response = {
                            "status_code": 400,
                            "message": "The Confirm does not match with the Password" #? Response Message
                        }
                else:
                    auth_response = {
                        "status_code": 403,
                        "message": "The verification has expired" #? Response Message
                    }
            elif auth == "forgot_password":
                email = user.get("email")
                auth_response = {
                    "data": {
                        "email": email
                        },
                    "status_code": 200,
                    "message": "successful" #? Response Message
                }
            else:
                auth_response = {
                    "status_code": 503,
                    "message": "Something went wrong..." #? Response Message
                }
        else: 
            auth_response = {
                "status_code": 501,
                "message": "Confirmation code is incorrect" #? Response Message
            }

                
        return auth_response
                        
    def get_user(self, email):
        hash_email = self.nlp.vocab[email] 
        email_hash_code = str(hash_email.orth)
        users = self.get_data(name="users", unit="database")
        user = users.get(email_hash_code)
        
        return user  
        
    def get_admin(self, email):
        hash_email = self.nlp.vocab[email] 
        email_hash_code = str(hash_email.orth)
        admins = self.get_data(name="admins", unit="database")
        admin = admins.get(email_hash_code)
        
        return admin  
        
    def get_current_admin(self, cookies):
        admin_email = cookies.get("admin_email")
        admin_username = cookies.get("admin_name")
        admin_temporary_id = cookies.get("admin_temporary_id")
        if admin_email == None: return None, None, None
        admins = self.get_data(name="admins", unit="database")
        hash_email = self.nlp.vocab[admin_email] 
        email_hash_code = str(hash_email.orth)
        admin =  admins.get(email_hash_code)
        if admin == None: return None, None, None
        old_temp_id = admin.get("temporary_id")
        if admin_temporary_id != old_temp_id: return None, None, None
        new_temp_id = str(uuid.uuid4())
        admin["temporary_id"] = new_temp_id
        admins[email_hash_code] = admin
        self.set_data(name="admins", unit="database", data=admins)
        email = admin.get("email")
        name = admin.get("name")
        
        return email, name, new_temp_id  
        
    def get_user_with_cookies(self, cookies):
        email = cookies.get("user_email")
        temporary_id = cookies.get("temporary_id")
        if email == None: return {}
        users = self.get_data(name="users", unit="database")
        hash_email = self.nlp.vocab[email] 
        email_hash_code = str(hash_email.orth)
        user = users[email_hash_code]
        user_temporary_id = user.get("temporary_id")
        if user_temporary_id != temporary_id: return {}
        vip_expiration = user.get("vip_expiration")
        
        try:
            if vip_expiration != None:
                is_not_expired = self.exp_filter(vip_expiration)
                
                if is_not_expired == False:
                    del user["is_vip"]
                    users[email_hash_code] = user
        except Exception as e:
            print(e)
        else:
            new_temp_id = str(uuid.uuid4())
            user["temporary_id"] = new_temp_id
            self.db.child("app").child("users").child(email_hash_code).update({"temporary_id": new_temp_id})
            
            del user["watch_list"]
            del user["likes_list"]
            del user["profile_image"]
            
            return user
        
    def get_site_settings(self): return self.get_data(name="site_settings", unit="database")
    
    def get_site_attributes(self): 
        site_settings = self.get_site_settings()
        
        return site_settings.get("site_attributes")
        
    def get_verification_code(self):
        code = ""
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        for counter in range(6):
            random_num = str(random.choice(num_list))
            code = code + random_num
        
        return code
                    
    def verify_grecaptcha(self, token):
        site_settings = self.get_site_settings()
        site_data = site_settings.get("site_data", {})
        recaptcha_site_key = site_data.get("recaptcha_site_key", "")
        recaptcha_secrete_key = site_data.get("recaptcha_secrete_key", "")
        if len(recaptcha_site_key) > 0: return 200
        if len(recaptcha_secrete_key) > 0: return 200
        url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_params = {'secret': recaptcha_secrete_key, 'response': token}
        response = requests.post(url, data=recaptcha_params)

        return response.status_code
            
    def exp_filter(self, exp_time):
        exp_time = str(exp_time)
        if exp_time == "0": return False
        
        current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
        current_date = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') 
        vip_exp_date = datetime.strptime(exp_time, '%Y-%m-%d %H:%M:%S')
        dif = current_date-vip_exp_date
        date_str = str(dif)
        if date_str.find("days") == -1: return True
        temp_list = date_str.split(" days")
        exp_date = int(temp_list[0])
        
        if exp_date < 30: return True
        
        return False
           
    def exp_parser(self, exp_time):
        exp_time = str(exp_time)
        if exp_time == "0": return "No days"
       
        current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
        current_date = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') 
        vip_exp_date = datetime.strptime(exp_time, '%Y-%m-%d %H:%M:%S')
        dif = current_date-vip_exp_date
        date_str = str(dif)
        if date_str.find("days") == -1: return 1
        temp_list = date_str.split(" days")
        exp_date = int(temp_list[0])
        
        if exp_date < 30: return exp_date
        
        return "Expired"
