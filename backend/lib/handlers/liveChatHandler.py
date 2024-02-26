from .apiHandler import ApiHandler
from ..resources import LIVECHAT_API_URL as live_base, CRASH, SUCCESSFUL

class LiveChat(ApiHandler):
    _instance = None  
    create_room_endpoint = "/room/create/"

    def __new__(self):
        if not self._instance:
            self._instance = super(LiveChat, self).__new__(self)
        return self._instance
        
    def create_room(self):
        data = self.request(base=live_base, endpoint=self.create_room_endpoint, https_safe=False)

        if not data: return None

        status_code = data.get("status_code", CRASH)

        if status_code != SUCCESSFUL:
            return None

        return data

    def room_sweeper(self):
        pass
