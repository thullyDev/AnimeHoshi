from ...models import User as user, Admin as admin
from django.forms.models import model_to_dict
from django.db import IntegrityError
from ..resources import ( 
	generate_unique_id, 
	NOT_FOUND,
	SUCCESSFUL
)
import logging

class Sql:
	def sql_get(self, unit, as_dict=True, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return None
		if not as_dict: return instance
		data = self.get_instance_as_dict(instance)

		return data

	def sql_set(self, unit, data):
		model = self.get_valid_model(unit)
		try:
			instance = model.objects.create(**data)
			instance.save()
			return self.get_instance_as_dict(instance)
		except IntegrityError as e:
			# logging.exception(e)
			print(e)
			return None

	def sql_update(self, unit, data, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs)

		if not instance: return self.sql_set(unit=unit, data=data)

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
		if not key: return None

		model = self.get_valid_model(unit)

		try:
			if key == "email":
				return model.objects.get(email=unique_id)

			if key == "temporary_id":
				return model.objects.get(temporary_id=unique_id)

			if key == "username":
				return model.objects.get(username=unique_id)
		except model.DoesNotExist:
			return None

		return model.objects.get(id=unique_id)

	def get_valid_model(self, unit):
		return user if unit == "user" else admin

	def get_instance_as_dict(self, instance):
		return model_to_dict(instance)

		# filtered_data = YourModel.objects.filter(your_field1__condition1='value1', your_field2__condition2='value2')

	def sql_get_all(self, unit):
		model = self.get_valid_model(unit)
		return list(model.objects.values())

	def sql_get_query(self, unit, query):
		model = self.get_valid_model(unit)
		values = model.objects.filter(username=query, email=query)
		return list(values)