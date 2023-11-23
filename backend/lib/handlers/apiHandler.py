import json
import requests

class ApiHandler:
    def build_url(self, base, endpoint, params, https_safe):
        head = "https" if https_safe else "http"
        url = f"{head}://{base}/{endpoint}"
        count = 0
        for key, value in params.items():
            url += f"?{key}={value}" if not count else f"&{key}={value}"
            count += 1
        
        return url
        
    def request(self, base, endpoint, params={}, headers={}, https_safe=True, html=False):
        url = self.build_url(base=base, endpoint=endpoint, params=params, https_safe=True)
        print(url)
        response = requests.get(url)
        
        if html:
            return response.text if response.status_code == 200 else None

        return response.json() if response.status_code == 200 else None 
                    

