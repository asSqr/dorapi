from commons.test import TestCase
from tests.test_seeds import TestSeed
from seeds.gadgets.data_struct import Gadget, Book  # noqa
from dorapi.models import MGadget, MBook    # noqa
from seeds.gadgets.utils import (
    mbook_to_book,
)

import logging


logger = logging.getLogger(__name__)


class TestGadgetUtils(TestCase):

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
                
                self.assertEqual(book.series, mbook.series)
                self.assertEqual(book.volume, mbook.volume)
                
            check_book()
