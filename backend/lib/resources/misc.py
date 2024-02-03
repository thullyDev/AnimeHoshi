import re
import random
import uuid
import json

def valid_email(email):
    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return re.match(email_regex, email) is not None

def hide_text(text, limit=3): return text[:limit] + "..."

def get_data_from_string(rawdata):
    return json.loads(rawdata)

def generate_random_code(length=6): return ''.join(random.choices('0123456789', k=length))

def generate_unique_id(length=6): return str(uuid.uuid4())