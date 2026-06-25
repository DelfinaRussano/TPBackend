import re
import unicodedata

from django.contrib.auth import get_user_model

User = get_user_model()


def normalize_name(value):
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^a-zA-Z0-9]+', '.', value).strip('.')
    return value.lower()


def generate_unique_email(nombre, apellido):
    base = f"{normalize_name(nombre)}.{normalize_name(apellido)}"
    email = f"{base}@centergym.com"
    suffix = 0
    while User.objects.filter(email=email).exists():
        suffix += 1
        email = f"{base}{suffix}@centergym.com"
    return email
