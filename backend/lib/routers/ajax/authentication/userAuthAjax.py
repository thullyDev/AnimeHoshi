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
from ....handlers import ResponseHandler
from ....decorators import timer
from ...base import Base
import yagmail

db = UserDatabase()

class UserAuthAjax(Base):
    @timer
    def login(self, request):
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

        data = db.get_user({"email": email})

        if not data:
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })

        del data["id"]
        del data["password"]
        del data["deleted"]

        temporary_id = self.update_user(email)

        return self.successful_response(data=data, cookies=True, cookies_data={
            "email": data["email"],
            "username": data["username"],
            "temporary_id": temporary_id,
        })
    
    @timer
    def signup(self, request):
        if not request.POST: return redirect("/")

        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        username = post_data.get("user")
        password = post_data.get("password")
        confirm = post_data.get("confirm")

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

        valid_user = db.get_user({ "email":email }) 

        if valid_user: 
            return self.forbidden_response(data={
                    "message": "user already exist, please make sure username and email unique"
                })

        message, code = self.send_verification(email=email, username=username, host=request.get_host())
        data = {
            "email": email,
            "username": username,
            "password": password,
            "isfor": "signup",
        }

        db.hset(name=f"vf_code_{code}", data=data, expiry=1500) # expires in 15 minues

        del data["isfor"]

        return self.successful_response(data={
                "message": message,
                "data": data,
            })
    
    @timer
    def resend_code(self, request):
        if not request.POST: return redirect("/")
        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        old_code = db.hset(name=f"vf_email_{email}")

        if not old_code: return self.forbidden_response(data={ "message": "unsigthed email" })

        message, code = self.send_verification(email=email, username=username, host=host)
        data = db.hget(f"vf_code_{old_code}"); db.cdelete(f"vf_code_{old_code}")

        db.cset(name=f"vf_code_{code}", data=data, expiry=1500) # expires in 5 minues

        return message
    
    @timer
    def verify(self, request):
        if not request.POST: return redirect("/")
        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        code = post_data.get("code")
        data = db.hget(f"vf_code_{code}")

        if not data: return self.forbidden_response(data={ "message": "invalid code" })

        isfor = data.get("isfor")

        data["temporary_id"] = generate_unique_id()

        del data["isfor"]

        if isfor == "signup": 
            db.set_user(data=data)
            del data["password"]
            db.cdelete(f"vf_code_{code}")
            return self.successful_response(data={ "message": "created account sucessfully" }, cookies_data=data, cookies=True)

        return self.successful_response(data={ 
            "message": "sucessfully verified",
            "data": {
                "code": code,
            }
         })

    @timer
    def forgot_password(self, request):
        if not request.POST: return redirect("/")

        post_data = request.POST
        post_data = get_data_from_string(post_data.get("data"))
        email = post_data.get("email")
        
        if not valid_email(email): 
            return self.bad_request_response(data={ "message": "this email is not a valid email" })

        data = db.get_user({"email": email})

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

        db.hset(name=f"vf_code_{code}", data=data, expiry=1500) # expires in 15 minues

        return self.successful_response(data={
                "message": message,
                "data": data
            })

    @timer
    def renew_password(self, request):
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

        data = db.hget(f"vf_code_{code}")
        email = data.get("email")
        username = data.get("username")
        temporary_id = generate_unique_id()
        data = {
            "email": email,
            "username": username,
            "temporary_id": temporary_id,
            "password": password,
        }

        res = db.update_user(data=data)

        db.cdelete(f"vf_code_{code}")

        del data["password"]
        
        return self.successful_response(data={ "message": "sucessfully renew password", "data": data, }, cookies_data=data, cookies=True)

    def send_email(self, subject, body, to_email):
        yag = yagmail.SMTP(SITE_EMAIL, SITE_EMAIL_PASS)

        yag.send(
            to=to_email,
            subject=subject,
            contents=body
        )

        yag.close()

    def send_verification(self, email, username, host):
        hidden_email = hide_text(text=email, limit=3)
        code = generate_random_code()
        body = f"user with the username of {username} registed on {host} with this email, please verify by inputting the code {code}, this code expires in 15 minutes"
        subject = f"{host} verification"

        self.send_email(subject=subject, body=body, to_email=email)
        db.cset(name=f"vf_email_{email}", value=code, expiry=1500) # expires in 15 minutes 

        return f"sent verification code to {email}, may take 60 seconds to reflect", code

    def update_user(self, email):
        temporary_id = generate_unique_id()
        data = db.get_user({ "email": email, "temporary_id": temporary_id })

        return temporary_id
