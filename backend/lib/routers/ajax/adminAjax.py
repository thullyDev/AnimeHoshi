from django.shortcuts import render, redirect
from ...decorators import timing_decorator
from ...database import Cache
from .authentication.adminAuthAjax import AdminAuthAjax

cache = Cache()

class AdminAjax(AdminAuthAjax):
    @timing_decorator
    def get_scripts(self, request):
        user = GET_CREDITIALS(request.COOKIES)

        if not user: return self.forbidden_response(data={ "message": "login" })

        site_data = self.get_site_data()
        scripts = data.get("scripts")

        return self.successful_response(data={ "data": scripts })

    @timing_decorator
    def get_attributes(self, request):
        user = GET_CREDITIALS(request.COOKIES)

        if not user: return self.forbidden_response(data={ "message": "login" })

        site_data = self.get_site_data()
        attributes = data.get("attributes")

        return self.successful_response(data={ "data": attributes })

    @timing_decorator
    def get_values(self, request):
        user = GET_CREDITIALS(request.COOKIES)

        if not user: return self.forbidden_response(data={ "message": "login" })

        site_data = self.get_site_data()
        values = data.get("values")

        return self.successful_response(data={ "data": values })

    @timing_decorator
    def get_settings(self, request):
        user = GET_CREDITIALS(request.COOKIES)

        if not user: return self.forbidden_response(data={ "message": "login" })

        site_data = self.get_site_data()
        settings = data.get("settings")

        return self.successful_response(data={ "data": settings })

    def save_data(self, request):
    	if not request.POST: return redirect("admin_login")

    	user = GET_CREDITIALS(request.COOKIES)

    	if not user: return self.forbidden_response(data={ "message": "login" })

    	data = json.load(request.POST.get("data"))
    	save_type = request.POST.get("save_type")

    	if save_type not in { "settings", "values", "attributes", "scripts" }:
    		return self.bad_request_response()

    	site_data = self.get_site_data(save_type=save_type, data=data)

    	site_data[save_type] = data

    	cache.dcset(name="site_data", data=site_data, expiry=False)

    def add_admin(self, request):
    	pass

    def GET_CREDITIALS(self, DATA, no_update=False):
        CREDITIALS = { "username", "email", "temporary_id" }
        CREDITIALS_DATA = {key: value for key, value in DATA.items() if key in CREDITIALS }

        email = CREDITIALS_DATA.get("email")
        username = CREDITIALS_DATA.get("username")
        temporary_id = CREDITIALS_DATA.get("temporary_id")

        if not email and not username and not temporary_id: 
            return None

        user = db.get_user(email=email, username=username)

        if not user: return None

        is_valid = self.is_valid_temporary_id(old_temporary_id=user.get("temporary_id"), temporary_id=temporary_id)

        if not is_valid: return None
        
        new_temporary_id = generate_unique_id()
        email = user.get("email")

        if no_update: self.update_user(email=email, temporary_id=new_temporary_id)

        user["temporary_id"] = new_temporary_id

        return user

    def get_site_data(self):
    	return cache.dcget("site_data", {})