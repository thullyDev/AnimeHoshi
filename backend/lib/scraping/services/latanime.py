class Latanime:
    base = "latanime.org"
    animes_endpoint = "animes/"
    anime_endpoint = "anime/"
    watch_endpoint = "ver/"
    calandar_endpoint = "calendario/"
    queries = {
        "page",
        "type",
        "genre",
        "year",
    }
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
    latanime_filter_blueprint = { 
            "animes": {
                "parent_selector": ".col-md-4.col-lg-3.col-xl-2.col-6.my-3",
                "children": {
                    "anime_slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".img-fluid2.shadow-sm",
                        "attributes": {
                            "url": "src",
                        }
                    },
                    "title": {
                        "selector": "h3.my-1",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "year": {
                        "selector": "span",
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
    blueprints = {
    	"latanime_home": latanime_home_blueprint,
        "latanime_filter": latanime_filter_blueprint,
    }
