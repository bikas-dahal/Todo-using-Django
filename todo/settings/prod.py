from .base import *
from decouple import config
from django.conf import settings


DEBUG = False

ADMINS = [
    ('Bikas Dahal', 'bikkydahal@gmail.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',

        'NAME': config('POSTGRES_DB'),

        'USER': config('POSTGRES_USER'),

        'PASSWORD': config('POSTGRES_PASSWORD'),

        'HOST': 'db',

        'PORT': 5432,

    }
}



from django.conf import settings

# Define the Redis URL
REDIS_URL = 'redis://cache:6379'

# Configure CACHES
settings.CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Configure CHANNEL_LAYERS
settings.CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}
