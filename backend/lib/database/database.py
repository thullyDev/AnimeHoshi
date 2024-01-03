from .cache import Cache
from .sql import Sql
from ..resources import (generate_unique_id, NOT_FOUND)

class Database(Cache, Sql):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get(self, unit, data):
        uid = self.get_safe_id(data)
        cache_data = self.dget(name=f"{unit}_*_{uid}")
        temporary_id = data.get("temporary_id")

        if not temporary_id and cache_data:
            return cache_data

        data = self.sql_get(data)
        data["temporary_id"] = temporary_id
        
        self.sql_update(data)
        self.dset(name=f"{unit}_*_{uid}", data=data)

        return data

    def set(self, unit, data):
        data = self.sql_set(unit, data)
        uid = data.get("email")
        self.dset(name=f"{unit}_*_{uid}", data=data)

        return data

    def update(self, unit, data):
        data = self.sql_update(**data)

        if not data:
            return data

        uid = data.get("email")
        self.dset(name=f"{unit}_*_{uid}", data=data)

        return data
