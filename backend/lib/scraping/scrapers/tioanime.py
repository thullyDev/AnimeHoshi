from ..scraper import Scraper
from ..services.tioanime import Tioanime

class TioanimeScraper(Scraper, Tioanime):
    def get_home(self):
    	return self.get(base=self.base, blueprint=self.blueprints["tioanime_home"])

    def get_filter(self, data):
        params = {}
        for key, value in data.items():
            if key is not self.queries: continue
            
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

    def get_schedule(self):
        return self.get(base=self.base, endpoint=self.schedule_endpoint, blueprint=self.blueprints["tioanime_schedule"])

    def get_anime(self, slug):
        blueprint = {
            "title": {
                "parent_selector": "h1.title",
                "attribute": "text_content",
                "single_select": True,
                "key": "title",
            },
            "original_title": {
                "parent_selector": "p.original-title",
                "attribute": "text_content",
                "single_select": True,
                "key": "original_title",
            },
            "type": {
                "parent_selector": "span.anime-type-peli",
                "attribute": "text_content",
                "single_select": True,
                "key": "type",
            },
            "year": {
                "parent_selector": "span.year",
                "attribute": "text_content",
                "single_select": True,
                "key": "year",
            },
            "season": {
                "parent_selector": "span.season > .season",
                "attribute": "text_content",
                "single_select": True,
                "key": "season",
            },
            "score": {
                "parent_selector": ".mal",
                "attribute": "text_content",
                "single_select": True,
                "key": "score",
            },
            "votes": {
                "parent_selector": ".total > span",
                "attribute": "text_content",
                "single_select": True,
                "key": "votes",
            },
            "description": {
                "parent_selector": ".sinopsis",
                "attribute": "text_content",
                "single_select": True,
                "key": "description",
            },
            "status": {
                "parent_selector": ".btn.btn-block.status",
                "attribute": "text_content",
                "single_select": True,
                "key": "status",
            },
            "poster_image": {
                "parent_selector": ".thumb img",
                "attribute": "src",
                "single_select": True,
                "key": "poster_image",
            },
            "background_image": {
                "parent_selector": ".backdrop > img",
                "attribute": "src",
                "single_select": True,
                "key": "background_image",
            },
            "genres": {
                "parent_selector": ".genres",
                "attribute": "html",
                "single_select": True,
                "key": "genres_html",
            },
            "last_scripts": {
                "parent_selector": "script",
                "attribute": "text_content",
                "single_select": True,
                "key": "episodes_script",
            },
        }
        return self.get(base=self.base, endpoint=f"{self.anime_endpoint}{slug}", blueprint=blueprint)