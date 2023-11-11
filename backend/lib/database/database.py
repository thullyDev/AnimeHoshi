from . import Cache, Sql
from ...resources import ( generate_unique_id, NOT_FOUND )

class Database(Cache, Sql):
	modelset = {"user", "admin"}

	def get_user(self, **kwargs): return self.db_get(unit="user", **kwargs[0])

	def set_user(self, **kwargs): return self.db_set(unit="user", **kwargs[0])

	def update_user(self, **kwargs): return self.sql_update(unit="user", **kwargs)

	def db_get(self, unit, uid):
		cache_data = self.dget(name=f"{unit}_*_{uid}")
		
		if cache_data: return cache_data


		self.dset(name=f"{unit}_*_{uid}", data=data)

		return data

	def db_set(self, unit, **kwargs):
		model = user if unit == "user" else admin
		instance = model(**kwargs)
		instance.save()

	def db_update(self, unit, **kwargs):
		model = user if unit == "user" else admin
		instance = model(**kwargs)
		instance.save()

	def handle_tempory_id(self, unit, save=True, **kwargs):
		data["temporary_id"] = temporary_id
		cache_data = self.update_user(temporary_id=temporary_id, **kwargs)

		if not cache_data:
			pass

		temporary_id = generate_unique_id()
		model = user if unit == "user" else admin
		data["temporary_id"] = temporary_id

		if save:
			pass


		return data
