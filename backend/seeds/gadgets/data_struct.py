import sys

sys.path.append('./backend')

from dataclasses import dataclass
from dorapi.enums import BookSeriesEnum
from typing import List

'''
登場する単行本 情報 
'''
@dataclass
class Book:
    series: BookSeriesEnum
    volume: str

'''
ドラえもんひみつ道具 情報
'''
@dataclass
class Gadget:
    name: str
    ruby: str
    desc: str
    books: List[Book]

    def __str__(self):
        book_list = []
        
        for book in self.books:
            book_list.append(f"Book(\
series=BookSeriesEnum('{book['series'].value}'), \
volume='{book['volume']}')")
            
        books_str = f"[{', '.join(book_list)}]"
        
        return f"Gadget(name='{self.name}', ruby='{self.ruby}', \
desc='{self.desc}', \
books={books_str})"
