from django.http import JsonResponse, HttpResponse
import json

class ResponseHandler:
	def json_response(self, data, safe=False):
		return JsonResponse(json.dumps(data), safe = False)

	def http_response(self, text, safe=False):
		return HttpResponse(text)