from commons.test import TestCase, Client
from tests.test_seeds import TestSeed

from dorapi.enums import BookSeriesEnum
from dorapi.models import MGadget

from typing import Dict, Any

import logging


logger = logging.getLogger(__name__)


class MGadgetMixin:
    def assertMGadget(self, data: Dict[str, Any], mgadget: MGadget):
        self.assertEqual(data['name'], mgadget.name)
        self.assertEqual(data['ruby'], mgadget.ruby)
        self.assertEqual(data['desc'], mgadget.desc)
        
        for book, mbook in zip(data['mbooks'], mgadget.mbooks.all()):
            self.assertEqual(BookSeriesEnum[book['series']].value, mbook.series)
            self.assertEqual(book['volume'], mbook.volume)


class TestListMGadget(TestCase, MGadgetMixin):

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
                
                self.assertMGadget(data, mgadget)
                
            self.assertEqual(extras['count'], len(self.seeds.mgadgets))

        check_response()

    def test_list_mgadgets_keyword(self):
        """
        キーワードによる検索
        """
        
        keywords = ['めがね', 'くすり', 'ばくだん', 'らいと']
        
        for keyword in keywords:
        
            def keyword_filter_func(mgadget):
                mbooks = mgadget.mbooks.all()
                
                return keyword in mgadget.name\
                    or keyword in mgadget.ruby\
                    or keyword in mgadget.desc\
                    or keyword in map(lambda mbook: mbook.series, mbooks)\
                    or keyword in map(lambda mbook: mbook.volume, mbooks)
            
            filtered_mgadgets = list(filter(keyword_filter_func, self.seeds.mgadgets))
            
            mgadget_dict = {}
            
            for mgadget in filtered_mgadgets:
                mgadget_dict[mgadget.name] = mgadget
            
            url = f'{self.get_url()}?keyword={keyword}'

            result_json = self.request.get(url).json()

            def check_response():
                datas = result_json['datas']
                extras = result_json['extras']
                
                for data in datas:
                    name = data['name']
                    mgadget = mgadget_dict[name]
                
                    self.assertMGadget(data, mgadget)
                    
                self.assertEqual(extras['count'], len(filtered_mgadgets))

            check_response()
