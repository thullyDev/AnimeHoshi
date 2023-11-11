from .. import user, admin
from django.forms.models import model_to_dict
from ...resources import ( 
	generate_unique_id, 
	NOT_FOUND,
	SUCCESSFUL
)

class Sql:
	def sql_get(self, unit, as_dict=True, **kwargs):
		instance = self.get_instance(unit=unit, **kwargs[0])

        if not instance: return None
        if as_dict: return instance
        
        data = model_to_dict(instance)

		return data

	def sql_set(self, unit, **kwargs):
		model = user if unit == "user" else admin
		instance = model(**kwargs)
		instance.save()

	def sql_update(self, unit, **kwargs):
		model = self.get_model(unit)
	    instance = self.get_instance(unit=unit, **kwargs[0])

	    if not instance: return NOT_FOUND

        for key, value in kwargs.items():
            setattr(model, key, value)

        model.save()

	def sql_delete(**kwargs):
		instance = self.get_instance(unit=unit, **kwargs[0])

		if not instance: return NOT_FOUND
	    instance.delete()

	def get_instance(self, unit, uid): 
		model =user if unit == "user" else admin
		instance = model.objects.get(uid)

		return instance
