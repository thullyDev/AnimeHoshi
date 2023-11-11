from decouple import config
import re
import random

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
SITE_EMAIL = config("SITE_EMAIL")
SITE_EMAIL_PASS = config("SITE_EMAIL_PASS")

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email): return True

    return False

def hide_text(text, limit=3): return text[:limit] + "..."

def generate_random_code(length=6): return ''.join(random.choices('0123456789', k=length))
