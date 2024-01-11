from .database import Database

class AdminDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_admin(self, data={}):
        email = self.get_email(data)
        if not email: return 
        return self.get(unit="admin", key="email", unique_id=email, data=data)
        
    def set_admin(self, data):
        return self.set(unit="admin", data=data)

    def update_admin(self, data, **kwargs):
        email = self.get_email(kwargs)
        if not email: return 
        return self.update(unit="admin", data=data, unique_id=email, key="email")

    def get_email(self, data)
        return data.get("email")
