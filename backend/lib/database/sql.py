from ...models import User as user, Admin as admin
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
		data = self.get_instance_as_dict(instance)

		return data

	def sql_set(self, unit, data):
		model = self.get_valid_model(unit)
		instance = model.objects.create(**data)
		instance.save()

		return self.get_instance_as_dict(instance)

	def sql_update(self, unit, data):
	    instance = self.get_instance(unit=unit, data=data)

	    if not instance: return None

	    instance.__dict__.update(data)
	    instance.save()

	    return self.get_instance_as_dict(instance)

	def sql_delete(self, data):
		instance = self.get_instance(unit=unit, data=data)

		if not instance: return None
		instance.delete()

		return True

	def sql_shallow_delete(self, data):
		data["deleted"] = True
		return self.sql_update(unit=unit, data=data)

	def get_instance(self, unit, data): 
		model = self.get_valid_model(unit)
		unique_id = self.get_safe_id(data)

		return None if not unique_id else model.objects.get(id=unique_id)

	def get_valid_model(self, unit):
		return user if unit == "user" else admin

	def get_instance_as_dict(self, instance):
		return model_to_dict(instance)

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
