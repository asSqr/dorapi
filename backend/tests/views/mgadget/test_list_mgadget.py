from commons.test import TestCase, Client
from tests.test_seeds import TestSeed

from .mgadget_mixins import MGadgetMixin

import logging


logger = logging.getLogger(__name__)


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
            mgadget_dict[mgadget.href] = mgadget
        
        url = self.get_url()

        result_json = self.request.get(url).json()

        def check_response():
            datas = result_json['datas']
            extras = result_json['extras']
            
            for data in datas:
                href = data['href']
                mgadget = mgadget_dict[href]
                
                self.assertMGadget(data, mgadget)
                
            self.assertEqual(extras['count'], len(self.seeds.mgadgets))

        check_response()

    def test_list_mgadgets_not_exact_keyword(self):
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
                mgadget_dict[mgadget.href] = mgadget
            
            url = f'{self.get_url()}?keyword={keyword}'

            result_json = self.request.get(url).json()

            def check_response():
                datas = result_json['datas']
                extras = result_json['extras']
                
                for data in datas:
                    href = data['href']
                    mgadget = mgadget_dict[href]
                
                    self.assertMGadget(data, mgadget)
                    
                self.assertEqual(extras['count'], len(filtered_mgadgets))

            check_response()
            
    def test_list_mgadgets_exact_keyword(self):
        """
        キーワードによる検索
        """
        
        keywords = ['どこでもどあ', 'ほんやくこんにゃく']
        
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
                mgadget_dict[mgadget.href] = mgadget
            
            url = f'{self.get_url()}?keyword={keyword}'

            result_json = self.request.get(url).json()

            def check_response():
                datas = result_json['datas']
                extras = result_json['extras']
                
                # 完全一致が優先されているか
                top_data = datas[0]
                self.assertEqual(top_data['ruby'], keyword)
                
                for data in datas:
                    href = data['href']
                    mgadget = mgadget_dict[href]
                
                    self.assertMGadget(data, mgadget)
                    
                self.assertEqual(extras['count'], len(filtered_mgadgets))

            check_response()
    
    def test_list_mgadgets_paginate(self):
        """
        ページネーション
        """
        
        mgadget_dict = {}
        
        page = 1
        page_size = 10
        
        mgadgets = self.seeds.mgadgets
        
        for mgadget in mgadgets:
            mgadget_dict[mgadget.href] = mgadget
        
        url = f'{self.get_url()}?page={page}&page_size={page_size}'

        result_json = self.request.get(url).json()

        def check_response():
            datas = result_json['datas']
            extras = result_json['extras']
            
            for data in datas:
                href = data['href']
                mgadget = mgadget_dict[href]
                
                self.assertMGadget(data, mgadget)
                
            self.assertEqual(extras['count'], page_size)

        check_response()

    def test_list_mgadgets_sort(self):
        """
        ソート
        """
        
        mgadget_dict = {}
        
        sort_order = 'asc'
        sort_key = 'ruby'
        
        def mgadget_compare_func(mgadget):
            return mgadget.ruby
        
        mgadgets = sorted(self.seeds.mgadgets, key=mgadget_compare_func)
        
        for mgadget in mgadgets:
            mgadget_dict[mgadget.href] = mgadget
        
        url = f'{self.get_url()}?sort_order={sort_order}&sort_key={sort_key}'

        result_json = self.request.get(url).json()

        def check_response():
            datas = result_json['datas']
            extras = result_json['extras']
            
            for data in datas:
                href = data['href']
                mgadget = mgadget_dict[href]
                
                self.assertMGadget(data, mgadget)
                
            self.assertEqual(extras['count'], len(mgadgets))

        check_response()
