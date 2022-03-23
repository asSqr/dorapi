from commons.test import TestCase, Client
from tests.test_seeds import TestSeed

from .mgadget_mixins import MGadgetMixin

import logging


logger = logging.getLogger(__name__)


class TestGetMGadget(TestCase, MGadgetMixin):

    URL = '/api/v1/mgadgets/{id}/'

    @classmethod
    def setUpTestData(cls):
        cls.seeds = TestSeed()
        cls.seeds.setUp()
        cls.request = Client()

    def test_get_mgadget(self):
        """
        取得
        """
        
        mgadget = self.seeds.mgadgets[8]
        target_id = str(mgadget.id)

        url = self.get_url(id=target_id)
        
        result_json = self.request.get(url).json()

        def check_response():
            data = result_json['data']
            
            self.assertMGadget(data, mgadget)

        check_response()
