from ...resources import ( ApiHandler )
from bs4 import BeautifulSoup

class Scraper(ApiHandler):
    def get_data(self, base, endpoint, passings, https_safe=True, params={}):
        html = self.request(base=base, endpoint=endpoint, https_safe=https_safe, params=params)

        if not html: return None

        soup = BeautifulSoup(html, 'html.parser')
        data = {}

        for key, val in passings.items():
            data = self.get(
                soup=soup, 
                selector=val.get("selector"), 
                selector_type=val.get("selector_type"),
                tag=val.get("tag"),
            )
            data[key] = data

        return data
        
    def get(self, soup, selector, selector_type, tag):
        if not tag and not selector and not selector_type: return None

        eles = []     
        
        if selector_type == "class": eles = soup.find_all(class_=selector) if not tag else soup.find_all(tag, class_=selector) 
        if selector_type == "tag": eles = soup.find_all(selector)
        if selector_type == "id": eles = [ soup.find(id=selector) ] 

        if not eles: return None
 
        data = {}
        for i, v in enumerate(eles):
            text_content = target_element.text
            attributes = target_element.attrs
            href = target_element.get('href')
            inner_html = str(target_element)
            src_value = target_element.get('src')

            data_id = f"{selector}_*_{i}"
            data[data_id] = {
                "text_content": text_content,
                "attributes": attributes,
                "href": href,
                "inner_html": inner_html,
                "src_value": src_value,
            }

        return data
