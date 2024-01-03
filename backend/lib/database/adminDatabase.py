from .database import Database

class AdminDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_admin(self, **kwargs):
        return self.get(unit="admin", data=kwargs)
        
    def set_admin(self, data):
        return self.set(unit="admin", data=data)

    def update_admin(self, data):
        return self.update(unit="admin", data=data)
