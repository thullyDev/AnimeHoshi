import json
import requests

class ApiHandler:
    def build_url(self, base, endpoint, https_safe=True):
        head = "https" if https_safe else "http"
        url = f"{head}://{base}{endpoint}"
        return url
        
    def request(self, base, endpoint, params={}, html=False, post=False, **kwargs):
        url = self.build_url(base, endpoint, **kwargs)
        resp = self.post_request(url, params, **kwargs) \
            if post else self.get_request(url, params, **kwargs)

        if resp.status_code != 200: return
        return resp.text if html else resp.json()


    def get_request(self, url, params={}, headers={}, **kwargs):
        response = requests.get(url=url, params=params)

        return response

    def post_request(self, url, params={}, headers={}, **kwargs):
        response = requests.post(url=url, data=params)

        return response

