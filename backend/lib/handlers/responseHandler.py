from django.http import JsonResponse, HttpResponse
from ..resources import (
	FORBIDDEN, 
	CRASH, 
	SUCCESSFUL, 
	NOT_FOUND_MSG, 
	NOT_FOUND, 
	FORBIDDEN_MSG, 
	CRASH_MSG, 
	SUCCESSFUL_MSG
)

class ResponseHandler:
	def json_response(self, data, status_code, safe=False, no_cookies=True, cookies={}):
		response = JsonResponse(data=data, status=status_code, safe=False) 

		if not no_cookies:
			thirty_days = 2592000 # 30 days in seconds

			for key, val in cookies.items():
				response.set_cookie(val.get("name"), val.get("value"), max_age=val.get("max_age", thirty_days), secure=True, httponly=True)

		return response

	def http_response(self, text, status_code):
		return HttpResponse(text, status=status_code)

	def forbidden_response(self, data=None, safe=False, no_cookies=True, cookies={}):
		data = data if data else {}
		data["status_code"] = FORBIDDEN
		if not data.get("message"): data["message"] = FORBIDDEN_MSG
		
		return self.json_response(data=data, status_code=FORBIDDEN, no_cookies=True, cookies=cookies)

	def successful_response(self, data=None, safe=False, no_cookies=True, cookies={}):
		data = data if data else {}
		data["status_code"] = SUCCESSFUL
		if not data.get("message"): data["message"] = SUCCESSFUL_MSG

		return self.json_response(data=data, status_code=SUCCESSFUL, no_cookies=no_cookies, cookies=cookies)

	def not_found_response(self, data=None, safe=False):
		data = data if data else {}
		data["status_code"] = NOT_FOUND
		if not data.get("message"): data["message"] = NOT_FOUND_MSG
		
		return self.json_response(data=data, status_code=NOT_FOUND)

	def crash_response(self, data=None, safe=False):
		data = data if data else {}
		data["status_code"] = CRASH
		if not data.get("message"): data["message"] = CRASH_MSG
		
		return self.json_response(data=data, status_code=CRASH)