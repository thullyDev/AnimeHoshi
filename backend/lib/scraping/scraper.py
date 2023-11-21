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
                    if return_type != "list": data[key][attr_key] = select_element.get(attr_value) if attr_value != "text_content" else select_element.text.strip()
                    else: 
                        temp = select_element.get(attr_value) if attr_value != "text_content" else select_element.text
                        data.append(temp)

        return data

    def process(self, soup, blueprint):
        parent_selector = blueprint.get("parent_selector")
        single_select = blueprint.get("single_select")

        data = {}
        if single_select:
            elements = soup.select(parent_selector)
            attribute = blueprint.get("attribute")
            key = blueprint.get("key")

            for element in elements:
                if attribute == "html": data[key] = str(element); continue
                
                value = element.get(attribute).strip() if attribute != "text_content" else element.text.replace("\n", " ").strip()
                data[key] = value
            
            return data

        elements = soup.select(parent_selector)

        data = [self.extract(element, blueprint["children"]) for element in elements]

        return data
