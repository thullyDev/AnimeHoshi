from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ...resources import (
    ROOT_FILE, 
    ResponseHandler, 
    valid_email, 
    generate_random_code,
    hide_text, 
    SITE_EMAIL, 
    SITE_EMAIL_PASS
    generate_unique_id,
)
from ...database import Database
import yagmail

db = Database()

class UsersAjax(APIView, ResponseHandler):
    def login(self, request):
        if request.POST:
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
        
        return redirect("/")

    def signup(self, request):
        if request.POST:
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

            db.set(name=f"vf_code_{code}", data, exp=300) # expires in 5 minues

            del data["isfor"]


            return self.successful_response(data={
                    "message": message,
                    "data": data,
                })
        
        return redirect("/")

    def resend_code(self, request):
        if request.POST:
            post_data = request.POST
            email = post_data.get("email")
            old_code = db.dset(name=f"vf_email_{email}")

            if not old_code: return self.forbidden_response(data={ "message": "unsigthed email" })


            message, code = self.send_verification(email=email, username=username, host=host)
            data = db.dget(f"vf_code_{old_code}"); db.delete(f"vf_code_{old_code}")

            db.set(name=f"vf_code_{code}", data, exp=300) # expires in 5 minues

            return message
        
        return redirect("/")

    def verify(self, request)
        if request.POST:
            post_data = request.POST
            code = post_data.get("code")
            data = db.dget(f"vf_code_{code}")

            if not data: return self.forbidden_response(data={ "message": "invalid code" })

            isfor = data.get("isfor")

            data["temporary_id"] = generate_random_code()

            del data["isfor"]

            if isfor == "signup": 
                db.set_user(unit="user", data=data)
                db.delete(f"vf_code_{code}")
                return self.successful_response(data={ "message": "created account sucessfully" }, cookies=data, no_cookies=False)

            return self.successful_response(data={ 
                "message": "sucessfully verified",
                "data": {
                    "code": code,
                }
             })

        return redirect("/")

    def forgot_password(self, request):
        if request.POST:
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

            db.set(name=f"vf_code_{code}", data, exp=300) # expires in 5 minues

            del data["isfor"]

            return self.successful_response(data={
                    "message": message,
                    "data": data
                })

        return redirect("/")

    def renew_password(self, request):
        if request.POST:
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

            data = db.dget(f"vf_code_{code}")
            email = data.get("email")
            username = data.get("username")
            temporary_id = generate_unique_id()
            data = {
                "email": email,
                "username": username,
                "temporary_id": temporary_id,
            }

            res = db.update_user(data=data)

            db.delete(f"vf_code_{code}")

            del data["isfor"]
            
            return self.successful_response(data={ "message": "sucessfully renew password", "data": data, }, cookies=data, no_cookies=False)


        return redirect("/")

    def send_email(self, subject, body, to_email):
        yag = yagmail.SMTP(SITE_EMAIL, SITE_EMAIL_PASS)

        yag.send(
            to=to_email,
            subject=subject,
            contents=body
        )

        yag.close()

    def send_verification(self, email, username, host)
        hidden_email = hide_string(text=email, limit=3)
        original_host = request.get_host()
        code = generate_random_code()
        body = f"user with the username of {username} registed on {host} with this email, please verify by inputting the code {code}, this code expires in 5 minutes"
        subject = f"{host} verification"

        self.send_email(subject=subject, body=body, to_email=email)

        db.set(name=f"vf_email_{email}", code, exp=300) # expires in 5 minues

        return f"sent verification code to {hidden_email}", code

    def handle_tempory_id(self, unit, save=True, **kwargs):
        data["temporary_id"] = temporary_id
        cache_data = self.update_user(temporary_id=temporary_id, **kwargs)

        if not cache_data:
            pass

        temporary_id = generate_unique_id()
        model = user if unit == "user" else admin
        data["temporary_id"] = temporary_id

        if save:
            pass


        return data

