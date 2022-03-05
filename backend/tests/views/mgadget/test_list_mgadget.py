from commons.test import TestCase, Client
from tests.test_seeds import TestSeed
from dorapi.enums import BookSeriesEnum

import logging


logger = logging.getLogger(__name__)


class TestListMGadget(TestCase):

    URL = '/api/v1/mgadgets/'

    @classmethod
    def setUpTestData(cls):
        cls.seeds = TestSeed()
        cls.seeds.setUp()
        cls.request = Client()

    def test_list_mgadgets(self):
        """
        全取得
        """
        
        mgadget_dict = {}
        
        for mgadget in self.seeds.mgadgets:
            mgadget_dict[mgadget.name] = mgadget
        
        url = self.get_url()

        result_json = self.request.get(url).json()

        def check_response():
            datas = result_json['datas']
            extras = result_json['extras']
            
            for data in datas:
                name = data['name']
                mgadget = mgadget_dict[name]
                
                self.assertEqual(data['name'], mgadget.name)
                self.assertEqual(data['ruby'], mgadget.ruby)
                self.assertEqual(data['desc'], mgadget.desc)
                
                for book, mbook in zip(data['mbooks'], mgadget.mbooks.all()):
                    self.assertEqual(BookSeriesEnum[book['series']].value, mbook.series)
                    self.assertEqual(book['volume'], mbook.volume)
                
            self.assertEqual(extras['count'], len(self.seeds.mgadgets))

        check_response()
