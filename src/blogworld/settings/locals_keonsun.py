import json

from django.core.exceptions import ImproperlyConfigured

from .locals_base import *

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(os.path.dirname(BASE_DIR), 'secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable"
        raise ImproperlyConfigured(error_msg)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


SECRET_KEY = get_secret('SECRET_KEY', secrets)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME", secrets),
        'USER': get_secret("DB_USERNAME", secrets),
        'PASSWORD': get_secret("DB_PASSWORD", secrets),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
