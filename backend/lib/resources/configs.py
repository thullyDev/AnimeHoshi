from decouple import config

ROOT_FILE = "index.html"

REDIS_PORT = config("REDIS_PORT")
REDIS_HOST = config("REDIS_HOST")
REDIS_PASSWORD = config("REDIS_PASSWORD")
SITE_EMAIL = config("SITE_EMAIL")
SITE_EMAIL_PASS = config("SITE_EMAIL_PASS")
SITE_KEY = config("SITE_KEY")


