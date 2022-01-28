from django.test.client import Client as BaseClient
from django.test import TestCase as BaseTestCase
from uuid import UUID
from typing import List, Dict, Optional, Any, Union, Type
from commons.models import BaseModel
from commons import authentication, middlewares


class Client(BaseClient):

    def __init__(self, mwarehouse_id: str = '', muser_id: str = '', machine_api_key: str = '', *args, **kwargs):
        self._mwarehouse_id = mwarehouse_id
        self._muser_id = muser_id
        self._machine_api_key = machine_api_key
        super().__init__(*args, **kwargs)

    def request(self, **request):
        return super().request(**request)


class TestCase(BaseTestCase):

    url: str = ''

    def get_url(self, *args, **kwargs):
        return self.URL.format(*args, **kwargs)
