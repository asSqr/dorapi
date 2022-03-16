import sys

sys.path.append('./backend')        # noqa

from dataclasses import dataclass        # noqa
from dorapi.enums import BookSeriesEnum        # noqa
from typing import List        # noqa


@dataclass
class Book:
    '''
    登場する単行本 情報
    '''
    
    series: BookSeriesEnum
    volume: str


@dataclass
class Gadget:
    '''
    ドラえもんひみつ道具 情報
    '''
    
    name: str
    ruby: str
    href: str
    desc: str
    books: List[Book]

    def __str__(self) -> str:
        book_list = []
        
        for book in self.books:
            book_list.append(f"Book(\
series=BookSeriesEnum('{book['series'].value}'), \
volume='{book['volume']}')")
            
        books_str = f"[{', '.join(book_list)}]"
        
        return f"Gadget(name='{self.name}', ruby='{self.ruby}', \
desc='{self.desc}', \
books={books_str})".replace('\n', '\\n')


@dataclass
class Link:
    '''
    ドラえもんひみつ道具 リンク
    '''

    from_gadget_href: str
    to_gadget_href: str
    begin_index: int
    end_index: int
    
    def to_gadget_link(self, gadgets: List[Gadget]) -> str:
        gadget_href_dict = {}
        
        for gadget in gadgets:
            gadget_href_dict[gadget.href] = gadget
            
        assert gadget_href_dict.get(self.from_gadget_href) is not None, (
            f'{self.from_gadget_href} is not found')
        
        assert gadget_href_dict.get(self.to_gadget_href) is not None, (
            f'{self.to_gadget_href} is not found')

        from_gadget = gadget_href_dict.get(self.from_gadget_href)
        to_gadget = gadget_href_dict.get(self.to_gadget_href)
        
        return f'Link(from_gadget={str(from_gadget)}, to_gadget={str(to_gadget)}, \
begin_index={self.begin_index}, end_index={self.end_index})'
