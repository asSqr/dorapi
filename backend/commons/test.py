from django.test.client import Client as BaseClient
from django.test import TestCase as BaseTestCase


class Client(BaseClient):

    def __init__(self, muser_id: str = '', *args, **kwargs):
        self._muser_id = muser_id
        super().__init__(*args, **kwargs)

    def request(self, **request):
        return super().request(**request)


class TestCase(BaseTestCase):

    url: str = ''

    def get_url(self, *args, **kwargs):
        return self.URL.format(*args, **kwargs)
