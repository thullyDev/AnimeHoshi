from .database import Database

class AdminDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_admin(self, email):
        if not email: return 
        return self.get(unit="admin", key="email", unique_id=email)
        
    def set_admin(self, data):
        return self.set(unit="admin", data=data)

    def update_admin(self, data):
        email = self.get_email(data)
        if not email: return 
        return self.update(unit="admin", data=data, unique_id=email, key="email")

    def get_email(self, data):
        return data.get("email")

    def get_admins(self):
        return self.get_all(unit="admin")

    def get_users(self):
        return self.get_all(unit="users")

    def get_amount(self, model):
        # weird side affect is adding 6 empty admins, they're safe tho
        if model == "admins":
            return len(self.get_admins()) - 6

        if model == "users":
            return len(self.get_users()) - 6

        return 0