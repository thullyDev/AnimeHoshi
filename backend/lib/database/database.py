from . import Cache, Sql
from ...resources import ( generate_unique_id, NOT_FOUND )

class Database(Cache, Sql):
	modelset = {"user", "admin"}

	def get_user(self, **kwargs): return self.db_get(unit="user", **kwargs)

	def set_user(self, data): return self.db_set(unit="user", data)

	def update_user(self, **kwargs): return self.db_update(unit="user", **kwargs)

	def db_get(self, unit, data):
		uid = self.get_safe_id(data)
		cache_data = self.dget(name=f"{unit}_*_{uid}")

		if cache_data: return cache_data

		data = self.sql_get(data)

		self.dset(name=f"{unit}_*_{uid}", data=data)

		return data

	def db_set(self, unit, data):
		data = self.sql_set(unit, data)
		uid = data.get("email")
		self.dset(name=f"{unit}_*_{uid}", data=data)

		return  data

	def db_update(self, unit, data):
		data = self.sql_update(**data)

		if not data: return data

		uid = data.get("email")
		self.dset(name=f"{unit}_*_{uid}", data=data)

		return data
