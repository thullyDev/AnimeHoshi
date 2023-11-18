class Tioanime:
    base = "tioanime.com"
    animes_endpoint = "directorio"
    anime_endpoint = "anime/"
    watch_endpoint = "ver/"
    schedule_endpoint = "programacion"
    queries = {
        "keywords",
        "page",
        "type",
        "genre",
        "status",
        "sort",
        "year",
    }

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
            "saturday": {
                "parent_selector": "#Saturday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "saturday": {
                "parent_selector": "#Saturday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "sunday": {
                "parent_selector": "#Sunday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "monday": {
                "parent_selector": "#Monday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "tuesday": {
                "parent_selector": "#Tuesday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "wednesday": {
                "parent_selector": "#Wednesday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "friday": {
                "parent_selector": "#Friday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
        }
    blueprints = {
        "tioanime_home": tioanime_home_blueprint,
        "tioanime_filter": tioanime_filter_blueprint,
    	"tioanime_schedule": tioanime_schedule_blueprint,
    }