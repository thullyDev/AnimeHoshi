from ..scraper import Scraper
from ..services.tioanime import Tioanime

class TioanimeScraper(Scraper, Tioanime):
    def get_home(self):
    	return self.get(base=self.base, blueprint=self.blueprints["tioanime_home"])

    def get_filter(self, data):
        # ?type%5B%5D=0&genero%5B%5D=accion&year=1960%2C1993&status=2&sort=recent&p=2&q=s
    	params = {}
    	for key, value in data.items():
    		if key == "type": 
    			params["type%5B%5D"] = value
    			continue

    		if key == "genre": 
    			params["genero%5B%5D"] = value
    			continue

    		if key == "keywords": 
    			params["q"] = value
    			continue

    		if key == "page": 
    			params["p"] = value
    			continue

    		params[key] = value

    	return self.get(base=self.base, endpoint=self.animes_endpoint, blueprint=self.blueprints["tioanime_filter"], params=params)