from dataclasses import dataclass
from dorapi.models import MBook
from .gadgets.dora_superdatabase import superdatabase_datas as gadget_superdatabase_datas
from .gadgets.utils import generate_book_key, book_to_mbook
from commons.seed import Seed
from typing import List


@dataclass
class SeedMBook(Seed):

    def create(self) -> List[MBook]:
        book_dict = {}
        
        for gadget in gadget_superdatabase_datas:
            for book in gadget.books:
                book_key = generate_book_key(book)
                book_dict[book_key] = book_to_mbook(book)
                
        mbooks = MBook.objects.bulk_create(book_dict.values())
        
        return mbooks
