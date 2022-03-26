"""
本番環境用 settings.py
"""

from .base import *     # noqa
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']  # 環境によっては変更可能性アリ

# CORS設定
# TODO: 本番ビルド時はlocalhost等を無効化する
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://earth-bird.vercel.app',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-warehouse-id',
]

CORS_ALLOW_CREDENTIALS = True


DATABASES = {}

DATABASES['default'] = dj_database_url.config()


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(name)s %(funcName)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'alpha_hatchu': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'alpha_hatchu_v2': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'commons': {    # noqa
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        'commons': {    # noqa
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        }
    },
}
