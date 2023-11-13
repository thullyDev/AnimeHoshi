from .cache import Cache
from .sql import Sql
from ..resources import ( generate_unique_id, NOT_FOUND )

class Database(Cache, Sql):
	def get_user(self, **kwargs): return self.db_get(unit="user", data=kwargs)

	def set_user(self, data): return self.db_set(unit="user", data=data)

	def update_user(self, **kwargs): return self.db_update(unit="user", data=kwargs)

	def get(self, unit, data):
		uid = self.get_safe_id(data)
		cache_data = self.dget(name=f"{unit}_*_{uid}")

		if cache_data: return cache_data

		data = self.sql_get(data)

		self.dset(name=f"{unit}_*_{uid}", data=data)

		return data

	def set(self, unit, data):
		data = self.sql_set(unit, data)
		uid = data.get("email")
		self.dset(name=f"{unit}_*_{uid}", data=data)

		return  data

	def update(self, unit, data):
		data = self.sql_update(**data)

		if not data: return data

		uid = data.get("email")
		self.dset(name=f"{unit}_*_{uid}", data=data)

		return data
