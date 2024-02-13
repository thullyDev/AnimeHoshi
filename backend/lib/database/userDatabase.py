from .database import Database
from ..resources import get_email

class UserDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_user(self, data):
        email = get_email(data)
        if not email: return 
        return self.get(unit="user", key="email", unique_id=email)
        
    def set_user(self, data):
        email = get_email(data)
        if not email: return 
        return self.set(unit="user", unique_id=email, data=data)

    def update_user(self, data):
        email = get_email(data)
        if not email: return 
        return self.update(unit="user", data=data, unique_id=email, key="email")

    def change_user_details(self, data):
        email = get_email(data)
        if not email: return False

        sqldata = self.sql_update(unit="user", data=data, unique_id=email, key="email")

        return sqldata != None

    def add_to_list(self, data):
        email = get_email(data)
        if not email: return False

        sqldata = self.sql_set(unit="lists", data=data)
        cache_data = self.get_cached_user_list(email)
        cache_data.append(sqldata)

        self.save_cached_user_list(email=email, data=cache_data)
        
        return sqldata != None

    def get_list(self, data):
        email = get_email(data)

        if not email: return 

        cache_data = self.get_cached_user_list(email)

        if cache_data: 
            return cache_data

        sqldata = self.sql_get_query(unit="lists", email=email, query=email, be_dynmc=True)
        list_query = [
            {
                'slug': obj.slug,
                'user': obj.user,
                'email': obj.email,
                'anime_title': obj.anime_title,
                'watch_type': obj.watch_type,
                'anime_image': obj.anime_image,
                'created_at': obj.created_at.isoformat(),
                'updated_at': obj.updated_at.isoformat(),
            }
            for obj in sqldata
        ]

        self.save_cached_user_list(email=email, data=list_query)
        return list_query

    def get_cached_user_list(self, email): 
        name = f"{email}_list"
        return self.hget(name=name)

    def save_cached_user_list(self, email, data): 
        name = f"{email}_list"
        self.hset(name=name, data=data)
