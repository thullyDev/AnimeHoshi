from .. import User as user, Admin as admin
from django.forms.models import model_to_dict
from ..resources import ( 
	generate_unique_id, 
	NOT_FOUND,
	SUCCESSFUL
)

class Sql:
	def sql_get(self, unit, as_dict=True, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return None
		if not as_dict: return instance
		data = model_to_dict(instance)

		return data

	def sql_set(self, unit, data):
		model = user if unit == "user" else admin
		instance = model.objects.create(**data)
		instance.save()

		return instance.to_dict()

	def sql_update(self, unit, data):
	    instance = self.get_instance(unit=unit, data=data)

	    if not instance: return None

	    instance.__dict__.update(data)
	    instance.save()

	    return instance.to_dict()

	def sql_delete(data):
		instance = self.get_instance(unit=unit, data=data)

		if not instance: return None
		instance.delete()

		return True

	def sql_shallow_delete(data):
		data["deleted"] = True
		return self.sql_update(unit=unit, data=data)

	def get_instance(self, unit, data): 
		model =user if unit == "user" else admin
		email = data.get("email")
		temporary_id = data.get("temporary_id")
		user_id = data.get("user_id")
		username = data.get("username")

		if user_id: return model.objects.get(id=user_id)
		if email: return model.objects.get(id=email)
		if temporary_id: return model.objects.get(id=temporary_id)
		if username: return model.objects.get(id=username)

		return None

	def get_safe_id(self, data):
		email = data.get("email")
		temporary_id = data.get("temporary_id")
		user_id = data.get("user_id")
		username = data.get("username")

		if user_id: return user_id
		if email: return email
		if temporary_id: return temporary_id
		if username: return username

		return None
