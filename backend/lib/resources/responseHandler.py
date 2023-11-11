from django.http import JsonResponse, HttpResponse
from . import FORBIDDEN, CRASH, SUCCESSFUL, NOT_FOUND_MSG, NOT_FOUND, FORBIDDEN_MSG, CRASH_MSG, SUCCESSFUL_MSG

class ResponseHandler:
	def json_response(self, data, status_code=None, safe=False):
		return (JsonResponse(json.dumps(data), status=status_code, safe=False) 
				if status_code == None else 
				JsonResponse(json.dumps(data), safe=False))

	def http_response(self, text, status_code=None):
		return (HttpResponse(text, status=status_code)
				if status_code == None else 
				HttpResponse(text))	

	def forbidden_response(self, data=None, safe=False):
		data = data if data else { "message": FORBIDDEN_MSG }
		data["status_code"] = FORBIDDEN
		return self.json_response(data=data, status_code=FORBIDDEN)

	def successful_response(self, data=None, safe=False):
		data = data if data else { "message": SUCCESSFUL_MSG }
		data["status_code"] = SUCCESSFUL
		return self.json_response(data, status_code=SUCCESSFUL)

	def not_found_response(self, data=None, safe=False):
		data = data if data else { "message": NOT_FOUND_MSG }
		data["status_code"] = NOT_FOUND
		return self.json_response(data, NOT_FOUND)

	def crash_response(self, data=None, safe=False):
		data = data if data else { "message": CRASH_MSG }
		data["status_code"] = CRASH
		return self.json_response(data, CRASH)