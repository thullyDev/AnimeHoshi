from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from ..resources import ROOT_FILE
from ..database import Database
from ..handlers import ResponseHandler

database = Database()

class Base(APIView, ResponseHandler):
    def root(self, request, context={}, template=ROOT_FILE): 
        user = self.GET_CREDITIALS(data=request.COOKIES, user_type="admin")
        path = request.path.split("/")
        full_path = request.path_info
        paths = full_path.split('/')
        length = len(paths)
        page = paths[length - 2]

        if page != "login" and not user: 
            return redirect("admin_login") if "admin" in path else redirect("/")

        context["page"] = page

        return render(request, template, context=context)

    def GET_CREDITIALS(self, data, user_type, update=False):
        # return True #? remove this later
        creditials = self.get_safe_creditials(data)
        email = creditials.get("email")
        username = creditials.get("username")
        temporary_id = creditials.get("temporary_id")

        return True

        if (not email and not username) or not temporary_id: 
            return None

        user = database.get_user(email=email, username=username) if user_type == 'user' else database.get_admin(email=email, username=username) 

        if not user: return None

        is_valid = self.is_valid_temporary_id(old_temporary_id=user.get("temporary_id"), temporary_id=temporary_id)

        if not is_valid: return None
        
        new_temporary_id = generate_unique_id()
        email = user.get("email")

        # if update:  
        #     print(f"update ===> {update}")
        #     print(f"user_type ===> {user_type}")
        #     if user_type == 'user': database.update_user(email=email, temporary_id=new_temporary_id)
        #     else: database.update_admin(email=email, temporary_id=new_temporary_id)

        # user["temporary_id"] = new_temporary_id

        return user

    def get_safe_creditials(self, data):
        return { key: value for key, value in data.items() if key in { "username", "email", "temporary_id" } }
