from django.urls import path

def produce_urlpatterns(routes):
	return [ path(request["route"], request["view"], name=request.get("name")) for request in routes ]