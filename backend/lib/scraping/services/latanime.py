class Latanime:
    base = "latanime.org"
    animes_endpoint = "animes/"
    anime_endpoint = "anime/"
    watch_endpoint = "ver/"
    calandar_endpoint = "calendario/"
    latanime_home_blueprint = { 
            "slider": {
                "parent_selector": ".carousel-item",
                "children": { 
                    "anime_slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "preview_image": {
                        "selector": ".lozad.preview-image",
                        "attributes": {
                            "url": "data-src",
                        }
                    },
                    "background_image": {
                        "selector": ".lozad.d-block.w-100",
                        "attributes": {
                            "url": "data-src",
                            "title": "alt"
                        }
                    },
                    "description": {
                        "selector": ".p-slider",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
            "latest_episodes": {
                "parent_selector": ".col-6.col-md-6.col-lg-3.mb-3",
                "children": {
                    "episode_slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".lozad.nxtmainimg",
                        "attributes": {
                            "url": "data-src",
                            "title": "alt"
                        }
                    },
                }
            },
        }
    blueprints = {
    	"latanime_home": latanime_home_blueprint,
    }
