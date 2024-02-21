import json
import requests

class ApiHandler:
    def build_url(self, base, endpoint, params, https_safe=True):
        head = "https" if https_safe else "http"
        query = self.build_query(params);
        url = f"{head}://{base}{endpoint}{query}"
        return url

    def build_query(self, params):
        count = 0
        query = ""
        for key, value in params.items():
            query += f"?{key}={value}" if not count else f"&{key}={value}"
            count += 1
        
        return query
        
    def request(self, base, endpoint, params={}, headers={}, html=False, **kwargs):
        url = self.build_url(base=base, endpoint=endpoint, params=params, **kwargs)
        response = requests.get(url)
        
        if html:
            return response.text if response.status_code == 200 else None

        return response.json() if response.status_code == 200 else None 
                    

