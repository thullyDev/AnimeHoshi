from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .services.resources import Resources
import json
import time
import urllib

resources = Resources(cache=cache)

def sitemap(request): 
    sitemap_response = '<?xml version="1.0" encoding="UTF-8"?>\
           <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\
                <sitemap>\
                    <loc>https://as2anime.com/sitemap-page.xml</loc>\
                </sitemap>\
                <sitemap>\
                    <loc>https://as2anime.com/sitemap-lists.xml</loc>\
                </sitemap>\
            </sitemapindex>\
        '
    return HttpResponse(sitemap_response, content_type="text/xml")
    
    # return render(request, 'app/sitemaps/sitemap.html', content_type="text/xml")

def sitemap_page(request): 
    sitemap_response = '<?xml version="1.0" encoding="UTF-8"?>\
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\
            <url>\
                <loc>https://as2anime.com/</loc>\
                <changefreq>daily</changefreq>\
                <priority>1.0</priority>\
            </url>\
            <url>\
                <loc>https://as2anime.com/home</loc>\
                <changefreq>daily</changefreq>\
                <priority>1.0</priority>\
            </url>\
            <url>\
                <loc>https://as2anime.com/browsing</loc>\
                <changefreq>daily</changefreq>\
                <priority>1.0</priority>\
            </url>\
            <url>\
                <loc>https://as2anime.com/alert</loc>\
                <changefreq>daily</changefreq>\
                <priority>1.0</priority>\
            </url>\
            <url>\
                <loc>https://as2anime.com/profile</loc>\
                <changefreq>daily</changefreq>\
                <priority>1.0</priority>\
            </url>\
        </urlset>\
        '
    return HttpResponse(sitemap_response, content_type="text/xml")
    
    # return render(request, 'app/sitemaps/sitemap-page.html', content_type="text/xml")

def sitemap_lists(request):
    sitemap_response = '<?xml version="1.0" encoding="UTF-8"?>\
    <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\
        <sitemap>\
            <loc>https://as2anime.com/sitemap-browses.xml</loc>\
        </sitemap>\
        <sitemap>\
            <loc>https://as2anime.com/sitemap-watches.xml</loc>\
        </sitemap>\
    </sitemapindex>\
    '
    return HttpResponse(sitemap_response, content_type="text/xml")
    
    # return render(request, 'app/sitemaps/sitemap-lists.html', content_type="text/xml")
    
def sitemap_browses(request): 
    page = request.GET.get("page", 1)
    data = resources.get_sitemap_list_data(page)
    
    routes = ""
    for i in data:
        title = urllib.parse.quote(i["animeTitle"]) if i["animeTitle"] != "" else urllib.parse.quote("one piece")
        routes += '\
            <url>\
                <loc>https://as2anime.com/browsing?keyword='+ title +'</loc>\
                <changefreq>daily</changefreq>\
                <priority>0.8</priority>\
            </url>\
        '
    
    sitemap_response = '<?xml version="1.0" encoding="UTF-8"?>\
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">' + routes + '</urlset>'        
    
    return HttpResponse(sitemap_response, content_type="text/xml")
    # return render(request, 'app/sitemaps/sitemap-browses.html', context, content_type="text/xml")
    
def sitemap_watches(request): 
    routes = ""
    count = 1
    for i in range(504):
        routes += '\
            <sitemap>\
                <loc>https://as2anime.com/sitemap-watches-list.xml?page=' + str(count) + '</loc>\
            </sitemap>\
        '
        count += 1

    sitemap_response = '<?xml version="1.0" encoding="UTF-8"?>\
        <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + routes + '</sitemapindex>'
    
    return HttpResponse(sitemap_response, content_type="text/xml")
    
    # return render(request, 'app/sitemaps/sitemap-watches.html', context, content_type="text/xml")

def sitemap_watches_list(request):
    page = request.GET.get("page", 1)
    data = resources.get_sitemap_list_data(page)
    
    routes = ""
    for i in data:
        title = urllib.parse.quote(i["animeTitle"]) if i["animeTitle"] != "" else urllib.parse.quote("one piece")
        routes += '\
            <url>\
                <loc>https://as2anime.com/watch/'+ title +'</loc>\
                <changefreq>daily</changefreq>\
                <priority>0.7</priority>\
            </url>\
        '
    
    sitemap_response = '<?xml version="1.0" encoding="UTF-8"?>\
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">' + routes + '</urlset>'
    
    return HttpResponse(sitemap_response, content_type="text/xml")
    
    #return render(request, 'app/sitemaps/sitemap-watches-list.html', context, content_type="text/xml")

def admin_login(request): context = {}; return render(request, "app/pages/admin_login.html", context)

def landing(request):
    site_attributes = resources.get_site_attributes()
    landing_page = site_attributes.get("landing_page")
    maintanance = site_attributes.get("maintanance")
    if maintanance == True: return redirect("/maintenance")
    if landing_page == False: return redirect("/home")
    user = resources.get_user_with_cookies(request.COOKIES)
    
    context = {
        "page": "landing",
        "global_data": resources.get_global_data(site_attributes),
        "site_data": resources.get_landing_site_data(),
        "data": {
            "user": user,
        }
    }
    
    return render(request, "app/pages/landing.html", context)
  
    
def maintenance(request):
    site_attributes = resources.get_site_attributes()
    context = {
        "page": "maintenance",
        "global_data": resources.get_global_data(site_attributes),
        "site_data": resources.get_landing_site_data(),
    }
    
    return render(request, "app/pages/maintenance.html", context)
    
def alert(request):
    site_attributes = resources.get_site_attributes()
    alert = site_attributes.get("alert")
    if alert == False: return redirect("/")
    message = request.GET.get("message", "What do you want...")
    sub_message = request.GET.get("sub_message", "")
    context = {
        "page": "alert",
        "global_data": resources.get_global_data(site_attributes),
        "data": {
            "message": message,
            "sub_message": sub_message,
        }
    }
    
    return render(request, "app/pages/alert.html", context)

def home(request):
    site_attributes = resources.get_site_attributes()
    maintanance = site_attributes.get("maintanance")
    if maintanance == True: return redirect("/maintenance")
    user = resources.get_user_with_cookies(request.COOKIES)
    
    context = {
        "page": "home",
        "global_data": resources.get_global_data(site_attributes),
        "site_data": resources.get_home_site_data(),   
        "data": {
            "user": user,
        }
        
    }

    return render(request, "app/pages/home.html", context)

def get_home_data(request):
    if request.POST: 
        start = time.time()
        day_int = int(request.POST.get("day"))
        data = resources.get_home_data(day_int=day_int)
        end = time.time()
        print(f"get_home_data TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)
    else: 
        return redirect("/")

def get_schedule_data(request):
    start = time.time()
    tz_offset = request.GET.get("tz_offset")
    day = request.GET.get("day", False)
    data = resources.get_schedule_data(tz_offset=tz_offset, day=day)
    end = time.time()
    print(f"get_schedule_data TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)

def authenticate(request):
    if request.POST: 
        start = time.time()
        auth_type = request.POST.get("auth")
        
        if auth_type == "logout":
            response = JsonResponse(json.dumps({
                "status_code": 200,
            }), safe = False)
            response.delete_cookie('username')
            response.delete_cookie('user_email')
            response.delete_cookie('temporary_id')
            end = time.time()
            print(f"AUTHENTICATE TIME ==> {end-start}")
            return response
        
        auth_data = request.POST.get("data")
        data = resources.authenticate(auth_type, auth_data)
        end = time.time()
        print(f"AUTHENTICATE TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)
    else: 
        return redirect("/")
        
def admin_authenticate(request):
    if request.POST: 
        start = time.time()
        auth_data = request.POST.get("data")
        data = resources.admin_authenticate(json.loads(auth_data))
        
        if data.get("status_code") == 200:
            response =  JsonResponse(json.dumps(data), safe = False)
            name = data.get("data").get("name")
            email = data.get("data").get("email")
            temporary_id = data.get("data").get("temporary_id")
            response.set_cookie(key='admin_email', value=email, max_age=86400)
            response.set_cookie(key='admin_name', value=name, max_age=86400)
            response.set_cookie(key='admin_temporary_id', value=temporary_id, max_age=86400)
        else: response = JsonResponse(json.dumps(data), safe = False)
        end = time.time()
        print(f"ADMIN_AUTHENTICATE TIME ==> {end-start}")
        return response
    else: 
        return redirect("/")
        
def logout_admin(request):
    if request.POST: 
        start = time.time()
        response = JsonResponse(json.dumps({"status_code": 200, "message": "Admin logged out"}), safe = False)
        response.delete_cookie('admin_email')
        response.delete_cookie('admin_name')
        response.delete_cookie('admin_temporary_id')
        end = time.time()
        print(f"LOGOUT_ADMIN TIME ==> {end-start}")
        return response
    else: 
        return redirect("/")

def get_anime(request):
    if request.POST: 
        start = time.time()
        slug = request.POST.get("slug")
        anime_slug = request.POST.get("anime_slug")
        server_id = int(request.POST.get("server_id"))
        data = resources.get_anime(slug=slug, server_id=server_id, anime_slug=anime_slug)
        end = time.time()
        print(f"GET_ANIME TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)
    else: 
        return redirect("/")
      
def search_for_anime(request, query):
    start = time.time()
    data = resources.search_for_anime(query)
    end = time.time()
    print(f"SEARCH_FOR_ANIME TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)
   
def add_to_list(request, playlist, query):
    start = time.time()
    temporary_id = request.COOKIES.get('temporary_id')
    email = request.COOKIES.get('user_email')
    data = resources.add_to_list(email=email, temporary_id=temporary_id, playlist=playlist, query=query)
    
    if data.get("status_code") == 200:
        response =  JsonResponse(json.dumps(data), safe = False)
        username = data.get("data").get("username")
        email = data.get("data").get("email")
        temporary_id = data.get("data").get("temporary_id")
        response.set_cookie(key='email', value=email, max_age=31536000)
        response.set_cookie(key='username', value=username, max_age=31536000)
        response.set_cookie(key='temporary_id', value=temporary_id, max_age=31536000)
    else: response = JsonResponse(json.dumps(data), safe = False)
    end = time.time()
    print(f"ADD_TO_LIST TIME ==> {end-start}")
    return response
   
def delete_list_item(request, playlist, slug):
    start = time.time()
    temporary_id = request.COOKIES.get('temporary_id')
    email = request.COOKIES.get('user_email')
    data = resources.delete_list_item(email=email, temporary_id=temporary_id, playlist=playlist, slug=slug)
    
    if data.get("status_code") == 200:
        response =  JsonResponse(json.dumps(data), safe = False)
        username = data.get("data").get("username")
        email = data.get("data").get("email")
        temporary_id = data.get("data").get("temporary_id")
        response.set_cookie(key='email', value=email, max_age=31536000)
        response.set_cookie(key='username', value=username, max_age=31536000)
        response.set_cookie(key='temporary_id', value=temporary_id, max_age=31536000)
        
    else: response = JsonResponse(json.dumps(data), safe = False)
    end = time.time()
    print(f"ADD_TO_LIST TIME ==> {end-start}")
    return response

def profile(request):
    site_attributes = resources.get_site_attributes()
    maintanance = site_attributes.get("maintanance")
    if maintanance == True: return redirect("/maintenance")
    user = resources.get_user_with_cookies(request.COOKIES)
    
    context = {
        "page": "profile",
        "global_data": resources.get_global_data(site_attributes),
        "site_data": resources.get_profile_site_data(),
        "data": {
            "user": user,
        }
    }
    
    return render(request, "app/pages/profile.html", context)

def admin(request): return redirect("/as2_admin/login")

def users(request):
    raw_users = resources.get_data(name="users", unit="database") 
    temp_user_dict = {}
    for i in raw_users.values():
        email = i.get("email")
        username = i.get("username")
        temp_user = {
            "email": email,
            "username": username,
        }
        temp_user_dict[email] = temp_user
        
    users = {i: raw_users[i] for i in list(raw_users)}
    admin_email, admin_username, admin_temp_id = resources.get_current_admin(request.COOKIES)
    if admin_email == None: return redirect("/as2_admin/login")
    
    context = {
        "page": "users",
        "page_column": "users",
        "data": {
            "users": raw_users,
            "num_users": len(raw_users),
            "num_animes": 10083,
            "admin_email": admin_email,
            "admin_username": admin_username,
            "temp_user_dict": temp_user_dict,
        }
    }
    
    response = render(request, "app/pages/users.html", context)
    response.set_cookie(key='admin_email', value=admin_email, max_age=86400)
    response.set_cookie(key='admin_name', value=admin_username, max_age=86400)
    response.set_cookie(key='admin_temporary_id', value=admin_temp_id, max_age=86400)

    return response

def dashboard(request):
    raw_users = resources.get_data(name="users", unit="database") 
    users = {i: raw_users[i] for i in list(raw_users)[:5]}
    admin_email, admin_username, admin_temp_id = resources.get_current_admin(request.COOKIES)
    if admin_email == None: return redirect("/as2_admin/login")
    
    jikan_anime = resources.get_jikan_anime()
    total = jikan_anime.get("jikan_anime", {}).get("pagination", {}).get("items", {}).get("total", 0)
    context = {
        "page": "dashboard",
        "page_column": "dashboard",
        "data": {
            "users": users,
            "num_users": len(raw_users),
            "num_animes": total,
            "admin_email": admin_email,
            "admin_username": admin_username,
        }
    }
    
    response = render(request, "app/pages/dashboard.html", context)
    
    response.set_cookie(key='admin_email', value=admin_email, max_age=86401)
    response.set_cookie(key='admin_name', value=admin_username, max_age=86401)
    response.set_cookie(key='admin_temporary_id', value=admin_temp_id, max_age=86401)

    return response

def general_settings(request):
    raw_users = resources.get_data(name="users", unit="database") 
    users = {i: raw_users[i] for i in list(raw_users)[:5]}
    admin_email, admin_username, admin_temp_id = resources.get_current_admin(request.COOKIES)
    if admin_email == None: return redirect("/as2_admin/login")
    site_settings = resources.get_site_settings()
    context = {
        "page": "general_settings",
        "page_column": "settings",
        "site_data": site_settings.get("site_data"),
        "data": {
            "users": users,
            "num_users": len(raw_users),
            "num_animes": 10083,
            "admin_email": admin_email,
            "admin_username": admin_username,
        }
    }
    response = render(request, "app/pages/general_settings.html", context)
    response.set_cookie(key='admin_email', value=admin_email, max_age=86400)
    response.set_cookie(key='admin_name', value=admin_username, max_age=86400)
    response.set_cookie(key='admin_temporary_id', value=admin_temp_id, max_age=86400)

    return response

def advance_settings(request):
    raw_users = resources.get_data(name="users", unit="database") 
    users = {i: raw_users[i] for i in list(raw_users)[:5]}
    admin_email, admin_username, admin_temp_id = resources.get_current_admin(request.COOKIES)
    if admin_email == None: return redirect("/as2_admin/login")
    site_settings = resources.get_site_settings()
    data = resources.get_admin_anime_sliders()
    data["users"] = users
    data["num_users"] = len(raw_users)
    data["num_animes"] = 10083
    data["admin_email"] = admin_email
    data["admin_username"] = admin_username
    context = {
        "page": "advance_settings",
        "page_column": "settings",
        "site_attributes": site_settings.get("site_attributes"),
        "data": data,
    }
    
    response = render(request, "app/pages/advance_settings.html", context)
    
    response.set_cookie(key='admin_email', value=admin_email, max_age=86400)
    response.set_cookie(key='admin_name', value=admin_username, max_age=86400)
    response.set_cookie(key='admin_temporary_id', value=admin_temp_id, max_age=86400)

    return response

def scripts(request):
    raw_users = resources.get_data(name="users", unit="database") 
    users = {i: raw_users[i] for i in list(raw_users)[:5]}
    admin_email, admin_username, admin_temp_id = resources.get_current_admin(request.COOKIES)

    if admin_email == None: return redirect("/as2_admin/login")
    site_settings = resources.get_site_settings()
    context = {
        "page": "scripts",
        "page_column": "settings",
        "site_scripts": site_settings.get("page_scripts"),
        "data": {
            "users": users,
            "num_users": len(raw_users),
            "num_animes": 10083,
            "admin_email": admin_email,
            "admin_username": admin_username,
        }
    }
    
    response = render(request, "app/pages/scripts.html", context)
    
    response.set_cookie(key='admin_email', value=admin_email, max_age=86400)
    response.set_cookie(key='admin_name', value=admin_username, max_age=86400)
    response.set_cookie(key='admin_temporary_id', value=admin_temp_id, max_age=86400)
    
    return response

def confirm_email(request):
    context = {}

    return render(request, "app/pages/confirm_email.html", context)

def renew_password(request):
    context = {}

    return render(request, "app/pages/renew_password.html", context)

def forgot_password(request):
    context = {}

    return render(request, "app/pages/forgot_password.html", context)

def browsing(request):
    site_attributes = resources.get_site_attributes()
    maintanance = site_attributes.get("maintanance")
    if maintanance == True: return redirect("/maintenance")
    user = resources.get_user_with_cookies(request.COOKIES)
    context = {
        "page": "browsing",
        "global_data": resources.get_global_data(site_attributes),
        "site_data": resources.get_browsing_site_data(),     
        "data": {
            "genres": resources.second_genres,
            "seasons": resources.seasons,
            "type": resources.type,
            "status": resources.status,
            "years": resources.years,
            "languages": resources.languages,
            "data": {
                "user": user,
            }
        }
    }

    return render(request, "app/pages/browsing.html", context)

def get_browsing_data(request):
    if request.POST:
        start = time.time()
        request_data = request.POST.get("data", "{}")
        data = resources.get_browsing_data(request_data=request_data)
        end = time.time()
        print(f"GET_BROWSING_DATA TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)
        
def act_user(request):
    if request.POST:
        start = time.time()
        email = request.POST.get("email", )
        act_type = request.POST.get("type")
        if act_type == "delete":
            data = resources.act_user(email=email)
            response = JsonResponse(json.dumps(data), safe = False)
        else:
            response =  JsonResponse(json.dumps({"status_code": 200}), safe = False)
            response.set_cookie(key='view_user', value=email, max_age=31536000)
        end = time.time()
        print(f"ACT_USER TIME ==> {end-start}")
        return response

def get_user_profile_image(request):
    if request.POST:
        start = time.time()
        email = request.COOKIES.get("user_email")
        temporary_id = request.COOKIES.get("temporary_id")
        data = resources.get_user_profile_image(email=email, temporary_id=temporary_id)
        end = time.time()
        print(f"GET_USER_PROFILE_IMAGE TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)


def get_menu_genre(request):
    if request.POST:
        start = time.time()
        data = resources.get_menu_genre()
        end = time.time()
        print(f"GET_MENU_GENRE TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)
        
def change_user_details(request):
    if request.POST:
        start = time.time()
        temporary_id = request.COOKIES.get('temporary_id')
        email = request.COOKIES.get('user_email')
        change_type = request.POST.get("type")
        user_input = request.POST.get("user_input")
        data = resources.change_user_details(email=email, temporary_id=temporary_id, change_type=change_type, user_inp=user_input)
        if data.get("status_code") == 200:
            response =  JsonResponse(json.dumps(data), safe = False)
            username = data.get("data").get("username")
            email = data.get("data").get("email")
            temporary_id = data.get("data").get("temporary_id")
            response.set_cookie(key='email', value=email, max_age=31536000)
            response.set_cookie(key='username', value=username, max_age=31536000)
            response.set_cookie(key='temporary_id', value=temporary_id, max_age=31536000)
        else: response = JsonResponse(json.dumps(data), safe = False)
        end = time.time()
        print(f"CHANGE_USER_DETAILS TIME ==> {end-start}")
        return response


def watch(request, slug):
    start = time.time()
    site_attributes = resources.get_site_attributes()
    maintanance = site_attributes.get("maintanance")
    if maintanance == True: return redirect("/maintenance")
    user = resources.get_user_with_cookies(request.COOKIES)
    data = resources.get_watch_anime(slug=slug)
    data["user"] = user
    raw_user_settings = request.COOKIES.get("user_settings", "{}")
    user_settings = json.loads(raw_user_settings)
    
    context = {
        "data": data,
        "user_settings": user_settings,
        "episode_num": 1,
        "page": "watch",
        "global_data": resources.get_global_data(site_attributes),
        "site_data": resources.get_watch_site_data(),     
    }
    
    end = time.time()
    print(f"WATCH TIME ==> {end-start}")
    return render(request, "app/pages/watch.html", context)
    

def random(request):
    response = resources.random()
    slug = response.get("data", {}).get("slug", "one-piece")
    
    return redirect(f"/watch/{slug}") if response.get("status_code") == 200 else redirect(f"/watch/one-piece")

def anime(request, slug):
    start = time.time()
    data = resources.anime(slug)
    end = time.time()
    print(f"ANIME TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)


def get_watch_data(request):
    if request.POST:
        start = time.time()
        genres = request.POST.get("genres")
        data = resources.get_watch_data(genres)
        end = time.time()
        print(f"GET_WATCH_DATA TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)

def parse_data(request):
    if request.POST:
        start = time.time()
        sources = request.POST.get("sources")
        backup_sources = request.POST.get("backup_sources")
        data = resources.parse_data(sources=sources, backup_sources=backup_sources)
        end = time.time()
        print(f"PARSE_DATA TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)

def get_watch_type(request):
    if request.POST:
        start = time.time()
        slug = request.POST.get("slug")
        watch_type = request.POST.get("watch_type")
        anime_title = request.POST.get("anime_title")
        data = resources.get_watch_type(slug=slug, watch_type=watch_type, anime_title=anime_title)
        end = time.time()
        print(f"GET_WATCH_TYPE TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)


def get_next_episode_data(request):
    if request.POST:
        start = time.time()
        anime_title = request.POST.get("anime_title")
        data = resources.get_next_episode_data(anime_title=anime_title)
        end = time.time()
        print(f"GET_WATCH_DATA TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)

def stream(request, source_id):
    start = time.time()
    site_attributes = resources.get_site_attributes()
    autoskip_intro = request.GET.get("auto_skip_intro", "False")
    autoskip_outro = request.GET.get("auto_skip_outro", "False")
    autoskip_outro = request.GET.get("auto_skip_outro", "False")
    autostart = request.GET.get("autostart", "False")
    autonext = request.GET.get("auto_next", "False")
    title = request.GET.get("title", "")
    image = request.GET.get("image", "")
    episode = request.GET.get("episode", "")
    watch_type = request.GET.get("type", "")
    site_settings = resources.get_site_settings()
    site_data = site_settings.get("site_data")
    context = {
        "global_data": resources.get_global_data(site_attributes),
        "page": "stream",
        "source_id": source_id,
        "title": urllib.parse.unquote(title), 
        "image": image, 
        "episode": episode, 
        "watch_type": watch_type,
        "autostart": autostart,
        "autonext": autonext,
        "autoskip_intro": autoskip_intro,
        "autoskip_outro": autoskip_outro,
        "controls": "True",
        "displaytitle": "True",
        "displaydescription": "True",
    }
    end = time.time()
    print(f"STREAM TIME ==> {end-start}")
    return render(request, "app/pages/stream.html", context)

def get_watch_list_data(request):
    start = time.time()
    temporary_id = request.COOKIES.get('temporary_id')
    email = request.COOKIES.get('user_email')
    data = resources.get_watch_list_data(email=email, temporary_id=temporary_id)
    end = time.time()
    print(f"GET_WATCH_LIST_DATA TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)

def get_likes_list_data(request):
    start = time.time()
    temporary_id = request.COOKIES.get('temporary_id')
    email = request.COOKIES.get('user_email')
    data = resources.get_likes_list_data(email=email, temporary_id=temporary_id)
    end = time.time()
    print(f"GET_LIKES_LIST_DATA TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)

def get_coming_data(request, coming_id):
    start = time.time()
    data = resources.get_coming_data(coming_id)
    end = time.time()
    print(f"GET_COMING_DATA TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)

def get_landing_data(request):
    start = time.time()
    data = resources.get_landing_data()
    end = time.time()
    print(f"GET_LANDING_DATA TIME ==> {end-start}")
    return JsonResponse(json.dumps(data), safe = False)

def get_profile_data(request):
    if request.POST:
        start = time.time()
        view_user = request.COOKIES.get('view_user')
        if view_user == None:
            temporary_id = request.COOKIES.get('temporary_id')
            email = request.COOKIES.get('user_email')
            data = resources.get_profile_data(email=email, temporary_id=temporary_id)

            if data.get("status_code") == 200:
                response =  JsonResponse(json.dumps(data), safe = False)
                username = data.get("data").get("username")
                email = data.get("data").get("email")
                temporary_id = data.get("data").get("temporary_id")
                response.set_cookie(key='email', value=email, max_age=31536000)
                response.set_cookie(key='username', value=username, max_age=31536000)
                response.set_cookie(key='temporary_id', value=temporary_id, max_age=31536000)
            else: response = JsonResponse(json.dumps(data), safe = False)
            end = time.time()
            print(f"GET_PROFILE_DATA TIME ==> {end-start}")
            return response
        else:
            data = resources.get_profile_data(view_user=view_user)
            if data.get("status_code") == 200:
                response =  JsonResponse(json.dumps(data), safe = False)
                response.delete_cookie('view_user')
            else: response = JsonResponse(json.dumps(data), safe = False)
            end = time.time()
            print(f"GET_PROFILE_DATA TIME ==> {end-start}")
            return response 
    else:
        return redirect("/")

def get_trending_data(request):
    if request.POST:
        start = time.time()
        data = resources.get_trending_animes()
        end = time.time()
        print(f"GET_TRENDING_DATA TIME ==> {end-start}")
        return JsonResponse(json.dumps(data), safe = False)
    else:
        return redirect("/")


def save_site_settings(request):
    if request.POST:
        start = time.time()
        admin_temp_id = request.COOKIES.get('admin_temporary_id')
        admin_email = request.COOKIES.get('admin_email')
        admin_username = request.COOKIES.get('admin_username')
        save_type = request.POST.get("type")
        save_data = request.POST.get("data")
        data = resources.save_site_settings(save_type=save_type, data=json.loads(save_data), admin_email=admin_email, admin_temp_id=admin_temp_id, cookies=request.COOKIES)
        response = JsonResponse(json.dumps(data), safe = False)
        if data.get("status_code") == 200:
            email = data.get("data").get("email")
            temporary_id = data.get("data").get("temporary_id")
            response.set_cookie(key='admin_email', value=email, max_age=86400)
            response.set_cookie(key='admin_name', value=admin_username, max_age=86400)
            response.set_cookie(key='admin_temporary_id', value=temporary_id, max_age=86400)
            
        end = time.time()
        print(f"SAVE_SITE_SETTINGS TIME ==> {end-start}")
        return response 
    else:
        return redirect("/")

