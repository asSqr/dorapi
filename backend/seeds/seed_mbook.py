from dataclasses import dataclass, asdict
from dorapi.models import MBook
from .dora_superdatabase import superdatabase_datas
from .utils import generate_book_key, book_to_mbook
from commons.seed import Seed
from typing import List


@dataclass
class SeedMBook(Seed):

    def create(self) -> List[MBook]:
        book_dict = {}
        
        for gadget in superdatabase_datas:
            for book in gadget.books:
                book_key = generate_book_key(book)
                book_dict[book_key] = book_to_mbook(book)
                
        mbooks = MBook.objects.bulk_create(book_dict.values())
        
        return mbooks
