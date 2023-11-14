from ..scraper import Scraper
from ..services.tioanime import Tioanime

class TioanimeScraper(Scraper, Tioanime):
    def get_home_data(self):
    	blueprint = {
            "animes": {
                "parent_selector": ".episode > a",
                "children": {
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                            "title": "alt"
                        }
                    }
                }
            },
        }
    	data = self.get_data(base=self.base, blueprint=blueprint, cache_id="tioanime_home")
    	return data