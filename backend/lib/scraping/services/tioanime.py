class Tioanime:
    base = "tioanime.com"
    animes_endpoint = "directorio"
    anime_endpoint = "anime/"
    watch_endpoint = "ver/"
    tioanime_home_blueprint = { 
            "latest_episodes": {
                "parent_selector": ".episodes > .col-6.col-sm-4.col-md-3",
                "children": { 
                    "episode_slug": {
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
            "latest_animes": {
                "parent_selector": ".col-6.col-sm-4.col-md-3.col-xl-2",
                "children": {
                    "anime_slug": {
                        "selector": ".anime > a",
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
    tioanime_filter_blueprint = { 
            "animes": {
                "parent_selector": ".col-6.col-sm-4.col-md-3.col-xl-2",
                "children": {
                    "anime_slug": {
                        "selector": ".anime > a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
            "page": {
                "parent_selector": ".pagination",
                "children": {
                    "page": {
                        "selector": ".page-item.active",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
            "pages": {
                "parent_selector": ".pagination",
                "children": {
                    "page": {
                        "selector": ".page-item",
                        "return_type": "list",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
        }
    tioanime_schedule_blueprint = { 
            "monday": {
                "parent_selector": "#monday",
                "children": {
                    "animes": {
                        "selector": ".anime > a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                }
            },
        }
    blueprints = {
        "tioanime_home": tioanime_home_blueprint,
    	"tioanime_filter": tioanime_filter_blueprint,
    }