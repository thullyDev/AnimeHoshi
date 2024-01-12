from django.http import JsonResponse, HttpResponse
from ..resources import (
	FORBIDDEN, 
	CRASH, 
	SUCCESSFUL, 
	NOT_FOUND_MSG, 
	NOT_FOUND, 
	FORBIDDEN_MSG, 
	CRASH_MSG, 
	SUCCESSFUL_MSG,
	BAD_REQUEST_MSG,
	BAD_REQUEST,
)

class ResponseHandler:
	def json_response(self, data, status_code, safe=False, cookies=False, cookies_data={}):
		response = JsonResponse(data=data, status=status_code, safe=False) 

		if cookies:
			SIXTY_DAYS = 2_592_000 * 3 #* 30 days (in seconds) * 3

			for key, val in cookies_data.items():
				response.set_cookie(
					key=key, 
					value=val, 
					max_age=SIXTY_DAYS, 
					secure=True, 
					httponly=True
				)

		return response

	def http_response(self, text, status_code):
		return HttpResponse(text, status=status_code)

	def forbidden_response(self, data=None, safe=False, cookies=False, cookies_data={}):
		data = data if data else {}
		data["status_code"] = FORBIDDEN
		if not data.get("message"): data["message"] = FORBIDDEN_MSG
		
		return self.json_response(data=data, status_code=FORBIDDEN, cookies=cookies, cookies_data=cookies_data)

	def successful_response(self, data=None, safe=False, cookies=False, cookies_data={}):
		data = data if data else {}
		data["status_code"] = SUCCESSFUL
		if not data.get("message"): data["message"] = SUCCESSFUL_MSG

		return self.json_response(data=data, status_code=SUCCESSFUL, cookies=cookies, cookies_data=cookies_data)

	def not_found_response(self, data=None, safe=False, cookies=False, cookies_data={}):
		data = data if data else {}
		data["status_code"] = NOT_FOUND
		if not data.get("message"): data["message"] = NOT_FOUND_MSG
		
		return self.json_response(data=data, status_code=NOT_FOUND, cookies=cookies, cookies_data=cookies_data)

	def crash_response(self, data=None, safe=False, cookies=False, cookies_data={}):
		data = data if data else {}
		data["status_code"] = CRASH
		if not data.get("message"): data["message"] = CRASH_MSG
		
		return self.json_response(data=data, status_code=CRASH, cookies=cookies, cookies_data=cookies_data)

	def bad_request_response(self, data=None, safe=False, cookies=False, cookies_data={}):
		data = data if data else {}
		data["status_code"] = BAD_REQUEST
		if not data.get("message"): data["message"] = BAD_REQUEST_MSG
		
		return self.json_response(data=data, status_code=BAD_REQUEST, cookies=cookies, cookies_data=cookies_data)