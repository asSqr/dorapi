from dataclasses import dataclass
from dorapi.models import MGadget, MBook, GadgetBook
from commons.seed import Seed
from typing import List
from .gadgets.utils import (
    generate_book_key,
    generate_mbook_key,
    generate_gadget_key,
    generate_mgadget_key,
)
from .gadgets.dora_superdatabase import superdatabase_datas as gadget_superdatabase_datas


@dataclass
class SeedGadgetBook(Seed):
    
    mgadgets: List[MGadget]
    mbooks: List[MBook]

    def create(self) -> List[GadgetBook]:
        mbook_dict = {}
        
        for mbook in self.mbooks:
            book_key = generate_mbook_key(mbook)
            
            mbook_dict[book_key] = mbook
        
        mgadget_dict = {}
        gadget_books = []
        
        for mgadget in self.mgadgets:
            gadget_key = generate_mgadget_key(mgadget)
            mgadget_dict[gadget_key] = mgadget
            
        for gadget in gadget_superdatabase_datas:
            gadget_key = generate_gadget_key(gadget)
            mgadget = mgadget_dict[gadget_key]
            
            for book in gadget.books:
                book_key = generate_book_key(book)

                mbook = mbook_dict[book_key]
                
                gadget_books.append(GadgetBook(
                    mgadget=mgadget,
                    mbook=mbook,
                ))
        
        gadget_books = GadgetBook.objects.bulk_create(gadget_books)
        
        return gadget_books
