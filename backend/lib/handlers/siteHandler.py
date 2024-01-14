from ...database import Database


database = Database()

class SiteHandler:
    def save_site_data(self, data, name):
        site_data = self.get_site_data()
        site_data[name] =  data
        database.hset(name="site_data", data=site_data, expiry=False)

    def update_data(self, new_data, old_data):
        for key, value in new_data.items():
            if not value and key in old_data: break 
            old_data[key] = value

    def get_site_data(self): 
        return database.hget("site_data", {})

    def get_save_to_data(self, name):
        site_data = self.get_site_data()
        return site_data.get(name, {})