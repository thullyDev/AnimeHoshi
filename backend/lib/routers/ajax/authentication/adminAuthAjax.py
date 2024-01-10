from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ....resources import valid_email, hide_text, generate_unique_id
from ....database import Database
from ....handlers import ResponseHandler
from ....decorators import timing_decorator
from ...base import Base


class AdminAuthAjax(Base):
    @timing_decorator
    def login(self, request):
        if not request.POST: return redirect("/")

        data = self.process_request(request.POST.get("data", "{}"))
        email = data.get("email")
        password = data.get("password")
        
        return self.successful_response()

        if not valid_email(email): 
            return self.bad_request_response(data={
                    "message": "this email is not a valid email"
                })

        if not email and not username: return self.forbidden_response()

        temporary_id = generate_unique_id()
        data = db.get_admin(email=email, temporary_id=temporary_id) 
        if not data:
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })

        del data["deleted"]
        del data["password"]

        return self.successful_response(data=data, no_cookies=False, cookies={
            "email": data["email"],
            "username": data["username"],
            "temporary_id": data["temporary_id"],
        })
    