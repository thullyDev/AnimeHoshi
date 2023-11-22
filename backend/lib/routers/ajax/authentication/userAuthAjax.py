from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ....resources import (
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS,
    generate_unique_id,
)
from ....database import Database
from ....handlers import ResponseHandler
from ....decorators import timing_decorator
import yagmail

db = Database()

class UserAuthAjax(APIView, ResponseHandler):
    @timing_decorator
    def login(self, request):
        if not request.POST: return redirect("/")

        post_data = request.POST
        email = post_data.get("email")
        username = post_data.get("username")
        password = post_data.get("password")
        temporary_id = post_data.get("temporary_id")

        if not valid_email(email): 
            return self.crash_response(data={
                    "message": "this email is not a valid email"
                })

        if not email and not username: return self.forbidden_response()

        data = db.get_user(email=email) if email else db.get_user(username=username)

        if not data:
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })

        del data["id"]
        del data["wachlist"]
        del data["likeslist"]

        return self.successful_response(data=data, no_cookies=False, cookies={
            "email": data.get("email"),
            "username": data.get("username"),
        })
    
    @timing_decorator
    def signup(self, request):
        if not request.POST: return redirect("/")

        post_data = request.POST
        email = post_data.get("email")
        username = post_data.get("username")
        password = post_data.get("password")
        confirm = post_data.get("confirm")

        if not valid_email(email): 
            return self.crash_response(data={
                    "message": "this email is not a valid email"
                })

        if not email and not username: return self.forbidden_response()

        if confirm != password: 
            return self.crash_response(data={
                    "message": "password and confirm should be the same"
                })

        if len(password) >= 10:
            return self.crash_response(data={
                    "message": "password should be atleast 10 characters long"
                })

        valid_user = db.get_user(email=email) if email else db.get_user(username=username)

        if valid_user: 
            return self.forbidden_response(data={
                    "message": "user already exist, please make sure username and email unique"
                })

        message, code = self.send_verification(email=email, username=username, host=host)
        data = {
            "email": email,
            "username": username,
            "password": password,
            "isfor": "signup",
        }

        db.cset(name=f"vf_code_{code}", data=data, expiry=300) # expires in 5 minues

        del data["isfor"]


        return self.successful_response(data={
                "message": message,
                "data": data,
            })
    
    @timing_decorator
    def resend_code(self, request):
        if not request.POST: return redirect("/")
        post_data = request.POST
        email = post_data.get("email")
        old_code = db.dcset(name=f"vf_email_{email}")

        if not old_code: return self.forbidden_response(data={ "message": "unsigthed email" })


        message, code = self.send_verification(email=email, username=username, host=host)
        data = db.dcget(f"vf_code_{old_code}"); db.cdelete(f"vf_code_{old_code}")

        db.cset(name=f"vf_code_{code}", data=data, expiry=300) # expires in 5 minues

        return message
    
    @timing_decorator
    def verify(self, request):
        if not request.POST: return redirect("/")
        post_data = request.POST
        code = post_data.get("code")
        data = db.dcget(f"vf_code_{code}")

        if not data: return self.forbidden_response(data={ "message": "invalid code" })

        isfor = data.get("isfor")

        data["temporary_id"] = generate_unique_id()

        del data["isfor"]

        if isfor == "signup": 
            db.set_user(unit="user", data=data)
            db.cdelete(f"vf_code_{code}")
            return self.successful_response(data={ "message": "created account sucessfully" }, cookies=data, no_cookies=False)

        return self.successful_response(data={ 
            "message": "sucessfully verified",
            "data": {
                "code": code,
            }
         })

    @timing_decorator
    def forgot_password(self, request):
        if request.POST: return redirect("/")

        post_data = request.POST
        email = post_data.get("email")
        username = post_data.get("username")

        if not valid_email(email): 
            return self.crash_response(data={ "message": "this email is not a valid email" })

        data = db.get_user(email=email) if email else db.get_user(username=username)

        if not data: 
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })

        message, code = self.send_verification(email=email, username=username, host=host)
        data = {
            "email": email,
            "username": username,
            "isfor": "forgot_password",
        }

        db.cset(name=f"vf_code_{code}", data=data, expiry=300) # expires in 5 minues

        del data["isfor"]

        return self.successful_response(data={
                "message": message,
                "data": data
            })

    @timing_decorator
    def renew_password(self, request):
        if request.POST: return redirect("/")

        post_data = request.POST
        code = post_data.get("code")

        if confirm != password: 
            return self.crash_response(data={
                    "message": "password and confirm should be the same"
                })

        if len(password) >= 10:
            return self.crash_response(data={
                    "message": "password should be atleast 10 characters long"
                })

        data = db.dcget(f"vf_code_{code}")
        email = data.get("email")
        username = data.get("username")
        temporary_id = generate_unique_id()
        data = {
            "email": email,
            "username": username,
            "temporary_id": temporary_id,
        }

        res = db.update_user(data=data)

        db.cdelete(f"vf_code_{code}")

        del data["isfor"]
        
        return self.successful_response(data={ "message": "sucessfully renew password", "data": data, }, cookies=data, no_cookies=False)

    def send_email(self, subject, body, to_email):
        yag = yagmail.SMTP(SITE_EMAIL, SITE_EMAIL_PASS)

        yag.send(
            to=to_email,
            subject=subject,
            contents=body
        )

        yag.close()

    def send_verification(self, email, username, host):
        hidden_email = hide_string(text=email, limit=3)
        original_host = request.get_host()
        code = generate_random_code()
        body = f"user with the username of {username} registed on {host} with this email, please verify by inputting the code {code}, this code expires in 5 minutes"
        subject = f"{host} verification"

        self.send_email(subject=subject, body=body, to_email=email)

        db.cset(name=f"vf_email_{email}", data=code, expiry=300) # expires in 5 minues

        return f"sent verification code to {hidden_email}", code

