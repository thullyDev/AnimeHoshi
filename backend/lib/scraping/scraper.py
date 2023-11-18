from ..resources import ( ApiHandler )
from ..database import ( Cache )
from bs4 import BeautifulSoup
from lxml import html

cache = Cache()

class Scraper(ApiHandler):
    def get(self, base, blueprint, endpoint="", params={}, https_safe=True, cache_id=""):
        if cache_id:
            data = cache.get(name=cache_id)
            if data: return data

        html = self.request(base=base, endpoint=endpoint, https_safe=https_safe, params=params, html=True)

        if not html: return None

        data = {}
        soup = BeautifulSoup(html, 'html.parser')
        for key, value in blueprint.items():
            data[key] = self.process(soup=soup, blueprint=value)

        if cache_id: cache.set(name=cache_id, data=data)

        return data

    def extract(self, element, config):
        data = {}
        for key, value in config.items():
            data[key] = {}
            selector = value.get("selector")
            return_type = value.get("return_type")
            if return_type == "list": data = []
            selected_elements = element.select(selector)

            for select_element in selected_elements:
                for attr_key, attr_value in value.get("attributes").items():
                    if return_type != "list": data[key][attr_key] = select_element.get(attr_value) if attr_value != "text_content" else select_element.text
                    else: 
                        temp = select_element.get(attr_value) if attr_value != "text_content" else select_element.text
                        data.append(temp)

        return data

    def process(self, soup, blueprint):
        parent_selector = blueprint["parent_selector"]
        parent_elements = soup.select(parent_selector)

        data = []
        for parent_element in parent_elements:
            data.append(self.extract(parent_element, blueprint["children"]))
        
        return data
