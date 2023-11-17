from ..scraper import Scraper
from ..services.tioanime import Tioanime

class TioanimeScraper(Scraper, Tioanime):
    def get_home(self):
    	return self.get(base=self.base, blueprint=self.blueprints["tioanime_home"])