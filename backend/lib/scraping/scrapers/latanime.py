from ..scraper import Scraper
from ..services.latanime import Latanime

class LatanimeScraper(Scraper, Latanime):
    def get_home(self):
    	return self.get(base=self.base, blueprint=self.blueprints["latanime_home"])