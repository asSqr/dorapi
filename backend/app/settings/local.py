"""
ローカル環境用 settings.py
"""

from .base import *     # noqa

INSTALLED_APPS += [
    'rest_framework_swagger',
]

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
ALLOWED_HOSTS = ['*']  # 環境によっては変更可能性アリ

# CORS設定
# TODO: 本番ビルド時はlocalhost等を無効化する
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
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
]

CORS_ALLOW_CREDENTIALS = True
