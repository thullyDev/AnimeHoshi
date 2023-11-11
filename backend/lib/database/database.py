from . import Cache
from .. import user, admin
from django.forms.models import model_to_dict

class Database(Cache):
	modelset = {"user", "admin"}

	def get_user(self, **kwargs): return self.db_get(unit="user", **kwargs)

	def db_get(self, unit, **kwargs):
		if unit not in self.modelset: return None 

		cache_data = self.dget(name=unit + "_*_" + **kwargs[0])
		
		if cache_data: return cache_data

		model = user if unit == "user" else admin
		data = {}

	    try:
	        rawdata = model.objects.get(**kwargs)
	        data = model_to_dict(rawdata)
	    except mode.DoesNotExist:
	        return None

		self.dset(name=unit + "_*_" + **kwargs[0], data=data)

		return data
