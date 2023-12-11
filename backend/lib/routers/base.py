from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from ..resources import ROOT_FILE
from ..database import Database
from ..handlers import ResponseHandler

db = Database()

class Base(APIView, ResponseHandler):
    def root(self, request, context={}, template=ROOT_FILE): 
        user = self.GET_CREDITIALS(DATA=request.COOKIES, user_type="admin")

        path = request.path.split("/")

        if not user: return redirect("/admin/login") if "admin" in path else redirect("/")

        return render(request, template, context=context)

    def GET_CREDITIALS(self, DATA, user_type, no_update=False):
        return True #? remove this later
        CREDITIALS = { "username", "email", "temporary_id" }
        CREDITIALS_DATA = {key: value for key, value in DATA.items() if key in CREDITIALS }

        email = CREDITIALS_DATA.get("email")
        username = CREDITIALS_DATA.get("username")
        temporary_id = CREDITIALS_DATA.get("temporary_id")

        if not email and not username and not temporary_id: 
            return None

        user = db.get_user(email=email, username=username) if user_type == 'user' else db.get_admin(email=email, username=username) 

        if not user: return None

        is_valid = self.is_valid_temporary_id(old_temporary_id=user.get("temporary_id"), temporary_id=temporary_id)

        if not is_valid: return None
        
        new_temporary_id = generate_unique_id()
        email = user.get("email")

        if no_update:  
        	if user_type == 'user': db.update_user(email=email, temporary_id=new_temporary_id)
        	else: db.update_admin(email=email, temporary_id=new_temporary_id)

        user["temporary_id"] = new_temporary_id

        return user
