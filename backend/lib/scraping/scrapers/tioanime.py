from ..scraper import Scraper
from ..services.tioanime import Tioanime

class TioanimeScraper(Scraper, Tioanime):
    def get_home_data(self):
    	blueprint = {
            "animes": {
                "parent_selector": ".col-6.col-sm-4.col-md-3",
                "children": { #*important> the first children go first, then after the deeper children go
                    "slug": {
                        "selector": ".episode > a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                            "title": "alt"
                        }
                    },
                }
            },
        }
    	data = self.get_data(base=self.base, blueprint=blueprint, cache_id="tioanime_home")
    	return data