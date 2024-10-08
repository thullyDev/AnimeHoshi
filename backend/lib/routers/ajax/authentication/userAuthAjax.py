from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ....resources import (
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
    generate_unique_id,
    get_data_from_string
)
from ....database import UserDatabase
from ....handlers import SiteHandler, ResponseHandler, send_email
from ....decorators import timer, captchaValidator
from ...base import Base
import yagmail

site = SiteHandler()
database = UserDatabase()

class UserAuthAjax(Base):
    @captchaValidator
    def login(self, request, *args, **kwargs):
        if not request.POST: return redirect("/")

        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        password = post_data.get("password")

        if not valid_email(email): 
            return self.bad_request_response(data={
                    "message": "this email is not a valid email"
                })

        if not email: return self.forbidden_response()

        data = database.get_user({"email": email})

        if not data:
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })

        if data["deleted"] == True: return self.forbidden_response({ "message": "login" })

        del data["id"]
        del data["password"]
        del data["deleted"]

        temporary_id = self.update_user(email)

        return self.successful_response(data=data, cookies=True, cookies_data={
            "email": data["email"],
            "username": data["username"],
            "profile_image": data["profile_image"],
            "temporary_id": temporary_id,
        })
    
    @captchaValidator
    def signup(self, request, *args, **kwargs):
        if not request.POST: return redirect("/")

        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        username = post_data.get("user")
        password = post_data.get("password")
        confirm = post_data.get("confirm")
        site_data = site.get_site_data() # site_data.values.images.favicon_logo.value
        profile_image = site_data.get("values").get("images").get("default_account_image").get("value")

        if None in [email, username, confirm, password]: return self.bad_request_response()

        if not valid_email(email): 
            return self.bad_request_response(data={
                    "message": "this email is not a valid email"
                })

        if confirm != password: 
            return self.bad_request_response(data={
                    "message": "password and confirm should be the same"
                })

        if len(password) <= 10:
            return self.bad_request_response(data={
                    "message": "password should be atleast 10 characters long"
                })

        valid_user = database.get_user({ "email":email }) 

        if valid_user: 
            return self.forbidden_response(data={
                    "message": "user already exist, please make sure username and email unique"
                })

        message, code = self.send_verification(email=email, username=username, host=request.get_host())
        data = {
            "email": email,
            "username": username,
            "password": password,
            "profile_image": profile_image,
            "isfor": "signup",
        }

        database.hset(name=f"vf_code_{code}", data=data, expiry=1500) # expires in 15 minues

        del data["isfor"]

        return self.successful_response(data={
                "message": message,
                "data": data,
            })
    
    @captchaValidator
    def resend_code(self, request, *args, **kwargs):
        if not request.POST: return redirect("/")
        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        old_code = database.hset(name=f"vf_email_{email}")

        if not old_code: return self.forbidden_response(data={ "message": "unsigthed email" })

        message, code = self.send_verification(email=email, username=username, host=host)
        data = database.hget(f"vf_code_{old_code}"); database.cdelete(f"vf_code_{old_code}")

        database.cset(name=f"vf_code_{code}", data=data, expiry=1500) # expires in 5 minues

        return message
    
    @captchaValidator
    def verify(self, request, *args, **kwargs):
        if not request.POST: return redirect("/")
        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        code = post_data.get("code")
        data = database.hget(f"vf_code_{code}")

        if not data: return self.forbidden_response(data={ "message": "invalid code" })

        isfor = data.get("isfor")

        data["temporary_id"] = generate_unique_id()

        del data["isfor"]

        if isfor == "signup": 
            database.set_user(data=data)
            del data["password"]
            database.cdelete(f"vf_code_{code}")
            return self.successful_response(data={ "message": "created account sucessfully" }, cookies_data=data, cookies=True)

        return self.successful_response(data={ 
            "message": "sucessfully verified",
            "data": {
                "code": code,
            }
         })

    @captchaValidator
    def forgot_password(self, request, *args, **kwargs):
        if not request.POST: return redirect("/")

        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        
        if not valid_email(email): 
            return self.bad_request_response(data={ "message": "this email is not a valid email" })

        data = database.get_user({"email": email})

        if not data: 
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })
        username = data["username"]

        message, code = self.send_verification(email=email, username=username, host=request.get_host())
        data = {
            "email": email,
            "username": username,
            "isfor": "forgot_password",
        }

        database.hset(name=f"vf_code_{code}", data=data, expiry=1500) # expires in 15 minues

        return self.successful_response(data={
                "message": message,
                "data": data
            })

    @captchaValidator
    def renew_password(self, request, *args, **kwargs):
        if request.POST: return redirect("/")

        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        code = post_data.get("code")
        password = post_data.get("password")
        confirm = post_data.get("confirm")

        if confirm != password: 
            return self.bad_request_response(data={
                    "message": "password and confirm should be the same"
                })

        if len(password) >= 10:
            return self.bad_request_response(data={
                    "message": "password should be atleast 10 characters long"
                })

        data = database.hget(f"vf_code_{code}")
        email = data.get("email")
        username = data.get("username")
        temporary_id = generate_unique_id()
        data = {
            "email": email,
            "username": username,
            "temporary_id": temporary_id,
            "password": password,
        }

        res = database.update_user(data=data)

        database.cdelete(f"vf_code_{code}")

        del data["password"]
        
        return self.successful_response(data={ "message": "sucessfully renew password", "data": data, }, cookies_data=data, cookies=True)

    def send_verification(self, email, username, host):
        hidden_email = hide_text(text=email, limit=3)
        code = generate_random_code()
        body = f"user with the username of {username} registed on {host} with this email, please verify by inputting the code {code}, this code expires in 15 minutes"
        subject = f"{host} verification"

        send_email(subject=subject, body=body, to_email=email)
        database.cset(name=f"vf_email_{email}", value=code, expiry=1500) # expires in 15 minutes 

        return f"sent verification code to {email}, may take 60 seconds to reflect", code

    def update_user(self, email):
        temporary_id = generate_unique_id()
        data = database.update_user({ "email": email, "temporary_id": temporary_id })

        return temporary_id
