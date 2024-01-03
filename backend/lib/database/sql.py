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

	def sql_update(self, unit, data, **kwargs):
	    instance = self.get_instance(unit=unit, **kwargs)

	    if not instance: return None

	    instance.__dict__.update(data)
	    instance.save()

	    return self.get_instance_as_dict(instance)

	def sql_delete(self, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return None
		instance.delete()

		return True

	def sql_shallow_delete(self, data, **kwargs):
		data["deleted"] = True
		return self.sql_update(unit=unit, data=data, **kwargs)

	def get_instance(self, unit, unique_id, key=None): 
		model = self.get_valid_model(unit)

		if not key: return None

		if key == "email":
			return model.objects.get(email=unique_id)

		if key == "temporary_id":
			return model.objects.get(temporary_id=unique_id)

		if key == "username":
			return model.objects.get(username=unique_id)


		return model.objects.get(id=unique_id)

	def get_valid_model(self, unit):
		return user if unit == "user" else admin

	def get_instance_as_dict(self, instance):
		return model_to_dict(instance)

	