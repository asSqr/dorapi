from dataclasses import dataclass
from dorapi.models import MBook
from .dora_superdatabase import superdatabase_datas
from commons.seed import Seed


@dataclass
class SeedMBook(Seed):

    def create(self):
        book_set = set()
        
        for gadget in superdatabase_datas:
            book_set.update(gadget.books)
        
        mbooks = MBook.objects.bulk_create(list(book_set))
        
        return mbooks
