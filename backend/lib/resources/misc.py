import re
import random
import uuid

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email): return True

    return False

def hide_text(text, limit=3): return text[:limit] + "..."

def generate_random_code(length=6): return ''.join(random.choices('0123456789', k=length))

def generate_unique_id(length=6): return str(uuid.uuid4())