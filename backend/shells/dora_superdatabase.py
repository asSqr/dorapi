from superbase_texts import html_texts

from bs4 import BeautifulSoup

from beautifulsoup import (
    generate_soup,
    soup_find,
    soup_find_all,
    inner_text_options,
)

from data_struct import (
    Gadget,
    GadgetBrick,
    BookSeriesEnum,
)
from typing import List

import pickle
import sys

GADGET_ARTICLE_PATH = 'article'

def get_gadget_info(soup: BeautifulSoup) -> Gadget:
    
    gadget_dict = {}
    
    def get_caption_info():
        
        CAPTION_PATH = '.caption > .name'
        caption = soup_find(soup, CAPTION_PATH)
        
        GADGET_NAME_PATH = 'h3'
        name = soup_find(
            caption,
            GADGET_NAME_PATH
        ).find(
            **inner_text_options
        )
        
        RUBY_PATH = 'span .ruby'
        ruby = soup_find(
            caption,
            RUBY_PATH
        ).find(
            **inner_text_options
        )
        
        return gadget_dict.update({
            'name': name, 
            'ruby': ruby,
        })
        
    def get_desc():
        
        DESCRIPTION_PATH = '.desc'
        desc = soup_find(
            soup,
            DESCRIPTION_PATH
        ).find(
            **inner_text_options
        )
        
        return gadget_dict.update({
            'desc': desc,
        })
        
    def get_books_info():
        
        BOOKS_PATH = '.books'
        books = soup_find(
            soup,
            BOOKS_PATH
        )
        
        if books is None:
            return gadget_dict.update({
                'books': []
            })
        
        BOOK_PATH = '.book'
        books = soup_find_all(
            books,
            BOOK_PATH
        )
        
        book_list = []
        
        for book in books:
            SERIES_PATH = 'span .book-series'
            series = soup_find(
                book,
                SERIES_PATH
            ).find(
                **inner_text_options
            )
            series_enum = BookSeriesEnum(series)
            
            VOLUME_PATH = 'span .volume-name'
            volume = soup_find(
                book,
                VOLUME_PATH
            ).find(
                **inner_text_options
            )
            
            book_list.append({
                'series': series_enum,
                'volume': volume,
            })

        return gadget_dict.update({
            'books': book_list
        })

    get_caption_info()
    get_desc()
    get_books_info()

    return Gadget(**gadget_dict)

def get_gadgets() -> List[GadgetBrick]:
    
    for text in html_texts:
        soup = generate_soup(text)
        articles = soup_find_all(soup, GADGET_ARTICLE_PATH)
        
        gadgets = []
        
        for article in articles:
            gadget = get_gadget_info(article)
            brick = GadgetBrick(gadget)
            gadgets.append(brick)
        
    return gadgets

gadgets = get_gadgets()

sys.setrecursionlimit(10000)

with open('../seeds/seed_gadgets.pickle', 'wb') as f:
    pickle.dump(gadgets, f, -1)
