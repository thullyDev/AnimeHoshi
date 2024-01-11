from .cache import Cache
from .sql import Sql
from ..resources import (generate_unique_id, NOT_FOUND)

class Database(Cache, Sql):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get(self, unit, data, unique_id, key):
        cache_data = self.hget(name=f"{unit}_*_{unique_id}")

        if cache_data:
            return cache_data

        sqldata = self.sql_get(unit=unit, key=key, unique_id=unique_id)

        return sqldata

    def set(self, unit, data, uid):
        data = self.sql_set(unit, data)
        self.hset(name=f"{unit}_*_{uid}", data=data)

        return data

    def update(self, unit, data, uid, **kwargs):
        data = self.sql_update(unit=unit, data=data, **kwargs)

        if not data:
            return data

        self.hset(name=f"{unit}_*_{uid}", data=data)

        return data

