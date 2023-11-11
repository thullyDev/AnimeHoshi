from decouple import config

ROOT_FILE = "index.html"
SUCESSFUL = 200;
NOT_FOUND = 404;
FORBIDEEN = 403;
CRASH = 503;
SUCESSFUL_MSG = "sucessful";
NOT_FOUND_MSG = "not found";
FORBIDEEN_MSG = "request forbidden";
CRASH_MSG = "unexpected issue";
REDIS_PORT = config("REDIS_PORT")
REDIS_HOST = config("REDIS_HOST")
REDIS_PASSWORD = config("REDIS_PASSWORD")
