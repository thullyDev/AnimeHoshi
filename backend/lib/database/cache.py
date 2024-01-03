from ..resources import REDIS_PORT, REDIS_HOST, REDIS_PASSWORD
from redis import Redis
import ast
import json
# port 6379
redis = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT, 
    # password=REDIS_PASSWORD,
)

class Cache:
    _instance = None  
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance
        
    default_expiry = 86400

    def cget(self, name): 
        raw_data = redis.get(name)
        
        if not raw_data: return None
        
        return raw_data.decode()
        
    def hget(self, name, default=None):
        raw_data = redis.get(name)
        if not raw_data: return default
        raw_data =  raw_data.decode()
        data = json.loads(raw_data)

        return data

    def cset(self, name, value, expiry=default_expiry):
        if expiry: 
            redis.set(name, value, expiry)
            return 

        redis.set(name, value)
        
    def hset(self, name, data, expiry=default_expiry):
        value = json.dumps(data)
        
        if expiry: 
            redis.set(name, value, expiry)
            return
        
        redis.set(name, value)

    def cmset(self, data): redis.mset(data)
        
    def cdelete(self, name): redis.delete(name)