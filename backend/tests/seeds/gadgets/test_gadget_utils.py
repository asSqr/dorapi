from commons.test import TestCase
from tests.test_seeds import TestSeed
from seeds.gadgets.data_struct import Gadget, Book
from dorapi.models import MGadget, MBook
from seeds.gadgets.utils import (
    mbook_to_book,
    book_to_mbook,
    mgadget_to_gadget,
    gadget_to_mgadget,
)

import logging


logger = logging.getLogger(__name__)


class GadgetsMixin:

    def assertBookAndMBook(self, book: Book, mbook: MBook):
        
        self.assertEqual(book.series.value, mbook.series)
        self.assertEqual(book.volume, mbook.volume)
          
    def assertGadgetAndMGadget(self, gadget: Gadget, mgadget: MGadget):
        
        self.assertEqual(gadget.name, mgadget.name)
        self.assertEqual(gadget.ruby, mgadget.ruby)
        self.assertEqual(gadget.desc, mgadget.desc)
        
        for book, mbook in zip(gadget.books, mgadget.mbooks.all()):
            self.assertBookAndMBook(book, mbook)


class TestGadgetUtils(TestCase, GadgetsMixin):

    @classmethod
    def setUpTestData(cls):
        cls.seeds = TestSeed()
        cls.seeds.setUp()

    def test_mbook_to_book(self):
        """
        mbook_to_book 関数
        """
        
        mbooks = self.seeds.mbooks

        for mbook in mbooks:
        
            book = mbook_to_book(mbook)
            
            def check_book():
                
                self.assertBookAndMBook(book, mbook)
                
            check_book()

    def test_book_to_mbook(self):
        """
        book_to_mbook 関数 (mbook_to_book の逆関数かチェック)
        """
        
        mbooks = self.seeds.mbooks
        books = []

        for mbook in mbooks:
        
            book = mbook_to_book(mbook)
            books.append(book)
            
        for book in books:
            
            mbook = book_to_mbook(book)
            
            def check_mbook():
                
                self.assertBookAndMBook(book, mbook)
                
            check_mbook()
    
    def test_mgadget_to_gadget(self):
        """
        mgadget_to_gadget 関数
        """
        
        mgadgets = self.seeds.mgadgets

        for mgadget in mgadgets:
        
            gadget = mgadget_to_gadget(mgadget)
            
            def check_gadget():
                
                self.assertGadgetAndMGadget(gadget, mgadget)
                
            check_gadget()
    
    def test_gadget_to_mgadget(self):
        """
        gadget_to_mgadget 関数 (mgadget_to_gadget の逆関数かチェック)
        """
        
        mgadgets = self.seeds.mgadgets
        gadgets = []

        for mgadget in mgadgets:
        
            gadget = mgadget_to_gadget(mgadget)
            gadgets.append(gadget)
            
        for gadget in gadgets:
            
            mgadget = gadget_to_mgadget(gadget)
            
            def check_mgadget():
                
                self.assertGadgetAndMGadget(gadget, mgadget)
                
            check_mgadget()
