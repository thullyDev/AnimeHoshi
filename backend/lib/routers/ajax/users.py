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

            if not data: return self.forbidden_response()

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
                "temporary_id": generate_unique_id(),
            }

            db.set(name=f"vf_code_{code}", data, exp=300) # expires in 5 minues


            return message
        
        return redirect("/")

    def resend_code(self, request):
        if request.POST:
            post_data = request.POST
            old_code = db.dset(name=f"vf_email_{email}")

            if not old_code: return self.forbidden_response(data={ "message": "unsigthed email" })


            message, code = self.send_verification(email=email, username=username, host=host)
            data = db.dget(f"vf_code_{old_code}"); db.delete(f"vf_code_{old_code}")
            # data = db.handle_temporary_id(unit="user", temporary_id=temporary_id, data=data, save=False)

            db.set(name=f"vf_code_{code}", data, exp=300) # expires in 5 minues

            return message
        
        return redirect("/")

    def verify(self, )
        if request.POST:
            post_data = request.POST
            old_code = db.dset(name=f"vf_email_{email}")

            if not old_code: return self.forbidden_response(data={ "message": "unsigthed email" })

            return self.send_verification(email=email, username=username, host=host)
        
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



