from django.conf import settings
from .apiHandler import ApiHandler
from ..database import Database
from ..resources import LIVECHAT_API_URL as live_base, CRASH, SUCCESSFUL, get_time_difference
import datetime
import threading

database = Database()

class LiveChat(ApiHandler):
    _instance = None  
    create_room_endpoint = "/room/create/"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.start_room_sweeper()
        return cls._instance


    def create_room(self):
        data = self.request(base=live_base, endpoint=self.create_room_endpoint, https_safe=False)

        if not data:
            return None

        status_code = data.get("status_code", CRASH)

        if status_code != SUCCESSFUL:
            return None

        return data

    def room_sweeper(self):
        print("ROOM_SWEEPER running")
        rooms = database.get_all(unit="rooms")

        if not len(rooms): return 

        current_time = datetime.datetime.now(datetime.timezone.utc)

        for room in rooms:
            created_at = room.get("created_at")
            if not created_at:
                return

            time_difference = get_time_difference(current_time, created_at)

            if time_difference.total_seconds() < 24 * 3600: return # 3600 = 24 hours

            self.delete_room(room)


    def delete_room(self, room): # 3600 = 24 hours
        database.delete(unit="rooms", unique_id=room["room_id"], key="room_id")

    def start_room_sweeper(self):
        self._room_sweeper_loop()

    def stop_room_sweeper(self):
        if hasattr(self, '_room_sweeper_timer') and self._room_sweeper_timer:
            self._room_sweeper_timer.cancel()

    def _room_sweeper_loop(self):
        self.room_sweeper()  

        # this is here to ensure we have a good development 
        # enviroment without the threading slowing the programme down
        if settings.DEBUG: return 

        # Schedule the next execution
        self._room_sweeper_timer = threading.Timer(10, self._room_sweeper_loop) # 3600 = 24 hours
        self._room_sweeper_timer.start()