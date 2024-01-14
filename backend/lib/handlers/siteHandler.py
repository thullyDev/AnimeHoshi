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
        site_data = database.hget("site_data", {})
        if site_data:
            return site_data

        return self.set_default_site_data()

    def get_save_to_data(self, name):
        site_data = self.get_site_data()
        return site_data.get(name, {})

    def get_amount(self, amount_type):
        if amount_type not { "settings", "values", "attributes", "scripts" }:
            raise ValueError(f"Invalid value for amount_type: {amount_type}. It must be one of 'settings', 'values', 'attributes', or 'scripts'") 

        site_data = self.get_site_data()
        return len(site_data.get(amount_type, ""))


    def set_default_site_data(self):
        site_data = self.get_default_site_data()
        database.hset(name="site_data", data=site_data, expiry=False)
        return site_data

    def get_default_site_data(self):
        return {
            "scripts": {
                "head_scripts": [
                    {"name": "global_head", "value": ""},
                    {"name": "home_head", "value": ""},
                    {"name": "landing_head", "value": ""},
                    {"name": "filter_head", "value": ""},
                    {"name": "profile_head", "value": ""},
                    {"name": "anime_head", "value": ""},
                    {"name": "watch_head", "value": ""},
                    {"name": "watch_together_browsing_head", "value": ""},
                    {"name": "watch_together_anime_head", "value": ""},
                ],
                "foot_scripts": [
                    {"name": "global_foot", "value": ""},
                    {"name": "home_foot", "value": ""},
                    {"name": "landing_foot", "value": ""},
                    {"name": "filter_foot", "value": ""},
                    {"name": "profile_foot", "value": ""},
                    {"name": "anime_foot", "value": ""},
                    {"name": "watch_foot", "value": ""},
                    {"name": "watch_together_browsing_foot", "value": ""},
                    {"name": "watch_together_anime_foot", "value": ""},
                ],
                "ads_scripts": {
                    "global": [
                        {"name": "top_advertisement", "value": "", "height": ""},
                        {"name": "bottom_advertisement", "value": "", "height": ""},
                    ],
                    "landing": [
                        {"name": "middle_advertisement", "value": "", "height": ""},
                    ],
                    "watch": [
                        {"name": "under_player_advertisement", "value": "", "height": ""},
                        {"name": "under_suggestions_advertisement", "value": "", "height": ""},
                    ],
                },
            },
            "values": {
                "images": [
                    {"key": "site_logo", "value": "/static/images/site-logo.png"},
                    {"key": "favicon_logo", "value": "/static/images/favicon.png"},
                    {"key": "alert", "value": "/static/images/gifs/alert.gif"},
                    {"key": "maintenance", "value": "/static/images/gifs/maintenance.gif"},
                    {"key": "empty", "value": "/static/images/gifs/empty.gif"},
                ],
                "inputs": [
                    {"value": "AnimeHoshi", "key": "site_name"},
                    {"value": "admin@animehoshi.com", "key": "email"},
                    {"value": "Watch Anime On AnimeHoshi For No ads | AnimeHoshi", "key": "title"},
                    {
                        "value": "AnimeHoshi is a vibrant online platform offering a diverse collection of anime content for free streaming. With an extensive library spanning genres and popular titles, AnimeHoshi provides enthusiasts with an immersive experience. User-friendly navigation and high-quality playback make it a go-to destination for anime lovers seeking free, accessible entertainment.",
                        "key": "site_description",
                        "type": "field",
                    },
                ],
                "socials": [
                    {"value": "https://discord.com/", "key": "discord"},
                    {"value": "https://twitter.com/", "key": "twitter"},
                    {"value": "https://reddit.com/", "key": "reddit"},
                    {"value": "https://ko-fi.com/", "key": "donate"},
                ],
            }
            "settings": [
                {"key": "maintanence", "value": False},
                {"key": "adblocker_detection", "value": True},
                {"key": "alert", "value": True},
                {"key": "authentication", "value": True},
                {"key": "anime", "value": True},
                {"key": "watch", "value": True},
                {"key": "watch_togather", "value": True},
                {"key": "user", "value": True},
                {"key": "schedule", "value": True},
                {"key": "features", "value": True},
                {"key": "footer", "value": True},
                {"key": "landing", "value": True},
                {"key": "donation", "value": True},
                {"key": "socials", "value": True},
                {"key": "contact", "value": True},
                {"key": "dark_mode", "value": True},
            ]
        }

