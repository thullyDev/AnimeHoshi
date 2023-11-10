from django.http import JsonResponse, HttpResponse
from . import FORBIDDEN, CRASH, SUCCESSFUL, NOT_FOUND_MSG, NOT_FOUND, FORBIDDEN_MSG, CRASH_MSG, SUCCESSFUL_MSG

class ResponseHandler:
	def json_response(self, data, safe=False):
		return JsonResponse(json.dumps(data), safe = False)

	def http_response(self, text, safe=False):
		return HttpResponse(text)	

	def forbidden_response(self, data=None, safe=False):
		data = data if data else {
			"status_code": FORBIDDEN,
			"message": FORBIDDEN_MSG,
		}
		return self.json_response(data)

	def successful_response(self, data=None, safe=False):
		data = data if data else {
			"status_code": SUCCESSFUL,
			"message": SUCCESSFUL_MSG,
		}
		return self.json_response(data)

	def not_found_response(self, data=None, safe=False):
		data = data if data else {
			"status_code": NOT_FOUND,
			"message": NOT_FOUND_MSG,
		}
		return self.json_response(data)

	def crash_response(self, data=None, safe=False):
		data = data if data else {
			"status_code": CRASH,
			"message": CRASH_MSG,
		}
		return self.json_response(data)