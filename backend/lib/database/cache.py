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
    default_expiry = 86400

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

    def cset(self, name, value, expiry=default_expiry):
        if expiry: redis.set(name, value, expiry)
        else: redis.set(name, value)
        
    def dcset(self, name, data, expiry=default_expiry):
        raw_data = json.dumps(data)
        
        if expiry: redis.set(name, raw_data, expiry)
        else: redis.set(name, raw_data)
        
        
    def cmset(self, data): redis.mset(data)
        
    def cdelete(self, name): redis.delete(name)