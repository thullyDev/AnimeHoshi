from ..resources import REDIS_PORT, REDIS_HOST, REDIS_PASSWORD
from redis import Redis
import ast
import json

redis = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT, 
    password=REDIS_PASSWORD,
)

class Cache:
    def get(self, name): 
        raw_data = redis.get(name)
        
        if not raw_data: return None
        
        return raw_data.decode()
        
    def dget(self, name):
        raw_data = redis.get(name)
        if not raw_data: return None
        raw_data =  raw_data.decode()
        data = json.loads(raw_data)

        return data

    def set(self, name, value, exp=86400):
        if exp: redis.set(name, value, exp)
        else: redis.set(name, value)
        
    def dset(self, name, data, exp=86400):
        raw_data = json.dumps(data)
        
        if exp: redis.set(name, raw_data, exp)
        else: redis.set(name, raw_data)
        
        
    def mset(self, data): redis.mset(data)
        
    def delete(self, name): redis.delete(name)