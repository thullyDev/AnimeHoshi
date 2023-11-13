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
    def cget(self, name): 
        raw_data = redis.get(name)
        
        if not raw_data: return None
        
        return raw_data.decode()
        
    def dcget(self, name):
        raw_data = redis.get(name)
        if not raw_data: return None
        raw_data =  raw_data.decode()
        data = json.loads(raw_data)

        return data

    def cset(self, name, value, expiry=86400):
        if exp: redis.set(name, value, exp)
        else: redis.set(name, value)
        
    def dcset(self, name, data, expiry=86400):
        raw_data = json.dumps(data)
        
        if exp: redis.set(name, raw_data, exp)
        else: redis.set(name, raw_data)
        
        
    def cmset(self, data): redis.mset(data)
        
    def cdelete(self, name): redis.delete(name)