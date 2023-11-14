from ..resources import ( ApiHandler )
from ..database import ( Cache )
from bs4 import BeautifulSoup
from lxml import html

cache = Cache()

class Scraper(ApiHandler):
    def get_data(self, base, blueprint, endpoint="", params={}, https_safe=True, cache_id="", as_=list):
        cache_id = ""  #Todo: remove this once we are done and ready to cache
        if cache_id:
            data = cache.get(name=cache_id)
            if data: return data

        html = self.request(base=base, endpoint=endpoint, https_safe=https_safe, params=params, html=True)

        if not html: return None

        data = {}
        soup = BeautifulSoup(html, 'html.parser')
        for key, value in blueprint.items():
            data[key] = self.process_passing(soup=soup, blueprint=value)

        if cache_id: cache.set(name=cache_id, data=data)

        return data

    def extract_data(self, element, config):
        data = {}
        for key, value in config.items():
            data[key] = {}
            selected_elements = element.select(value.get("selector"))

            for element in selected_elements:
                for attribute, attr_value in value.get("attributes").items():
                    data[key][attribute] = element.get(attr_value)

        return data

    def process_passing(self, soup, blueprint):
        parent_elements = soup.select(blueprint["parent_selector"])

        data = []
        for parent_element in parent_elements:
            data.append(self.extract_data(parent_element, blueprint["children"]))
        
        return data
