from django.urls import path
from django.core.exceptions import ValidationError

def produce_urlpatterns(routes):
	hashnames = set()

	for route in routes:
		name = route.get("name")

		if not name: 
			continue

		if name in hashnames:
			raise ValidationError(f"Duplicate URL name: {name}")

		hashnames.add(name)
		
	hashnames.clear()
	return [ path(request["route"], request["view"], name=request.get("name")) for request in routes ]