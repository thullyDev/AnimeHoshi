from .apiHandler import ApiHandler
from ..database import Database
from ..resources import LIVECHAT_API_URL as live_base, CRASH, SUCCESSFUL, get_time_difference
from pprint import pprint
import datetime

database = Database()

class LiveChat(ApiHandler):
    _instance = None  
    create_room_endpoint = "/room/create/"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # cls._instance.room_sweeper()
        return cls._instance

    def __init__(self, *args, **kwargs):
        self.room_sweeper()

        
    def create_room(self):
        data = self.request(base=live_base, endpoint=self.create_room_endpoint, https_safe=False)

        if not data:
            return None

        status_code = data.get("status_code", CRASH)

        if status_code != SUCCESSFUL:
            return None

        return data

    def room_sweeper(self):
        rooms = database.get_all(unit="rooms")
        current_time = datetime.datetime.now(datetime.timezone.utc)

        for room in rooms:
            created_at = room.get("created_at")
            if not created_at:
                return

            time_difference = get_time_difference(current_time, created_at)

            if time_difference.total_seconds() < 24 * 3600: return

            # self.delete_room(room)

    def delete_room(self, room):
        database.delete(unit="rooms", unique_id=room["room_id"], key="room_id")