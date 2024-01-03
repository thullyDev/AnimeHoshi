from .database import Database

class UserDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_user(self, **kwargs):
        return self.get(unit="user", data=kwargs)
        
    def set_user(self, data):
        return self.set(unit="user", data=data)

    def update_user(self, data):
        return self.update(unit="user", data=data)
