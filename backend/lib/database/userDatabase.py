from .database import Database

class UserDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_user(self, email):
        if not email: return 
        return self.get(unit="user", key="email", unique_id=email)
        
    def set_user(self, email, data):
        return self.set(unit="user", unique_id=email, data=data)

    def update_user(self, data):
        email = self.get_email(data)
        if not email: return 
        return self.update(unit="user", data=data, unique_id=email, key="email")

    def get_email(self, data):
        return data.get("email")
