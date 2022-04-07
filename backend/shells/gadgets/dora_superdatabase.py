import sys

sys.path.append('./backend/seeds/gadgets')
sys.path.append('./backend/shells')

from superbase_texts import html_texts      # noqa

from bs4 import (      # noqa
    BeautifulSoup, Tag,      # noqa
    NavigableString      # noqa
)      # noqa

from beautifulsoup import (      # noqa
    generate_soup,      # noqa
    soup_find,      # noqa
    soup_find_all,      # noqa
    inner_text_options,      # noqa
)      # noqa

from data_struct import (      # noqa
    Gadget,      # noqa
    Link,      # noqa
    BookSeriesEnum,      # noqa
)      # noqa

from typing import List, Tuple      # noqa

sys.path.append('backend/seeds/gadgets')

from custom_search import worker        # noqa


GADGET_ARTICLE_PATH = 'article'


def convert_database_href_typo(href):
    if href == '/gadget/ta#chiisaku-naru-musi-megane-tsui':
        return '/gadget/ta#chiisaku-naru-musi-megane'
    
    if href == '/gadget/ka#tesou-catalog':
        return '/gadget/ta#tesou-catalog'
    
    if href == '/gadget/a#ningen-setsudan-ki':
        return '/gadget/na#ningen-setsudan-ki'
    
    if href == '/gadget/sa#shakkuri-tome-bikkuri-hako':
        return '/gadget/sa#shakkuri-tome-bikkuri-bako'
    
    if href == '/gadget/sa#jidou-hanbai-timemachine':
        return '/gadget/sa#jidou-hanbai-time-machine'
    
    if href == '/gadget/ra#robot-tree-no-tane':
        return '/gadget/ra#robot-tree'
    
    if href == '/gadget/ka#katachi-dake-hansen-no-motor-bort':
        return '/gadget/ka#katachi-dake-hansen-de-honto-ha-motor-bort'
    
    if href == '/gadget/ma#mizu-kakou-furikake':
        return '/gadget/ma#mizu-kakou-you-furikake'
    
    if href == '/gadget/ha#baumkuchenman':
        return '/gadget/ha#baumkuchenman-cassette'
    
    if href == '/gadget/a#otoshimono-tsuribori-to-tsurizao':
        return '/gadget/a#otoshimono-tsuribori'
    
    return href


def get_gadget_info(
    soup: BeautifulSoup
) -> Tuple[Gadget, List[Link]]:
    
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
        
        HREF_PATH = 'span .copy-link'
        href = soup_find(
            caption,
            HREF_PATH
        ).attrs['data-link']
        
        href = convert_database_href_typo(href)
        
        return gadget_dict.update({
            'name': name,
            'ruby': ruby,
            'href': href,
        })
        
    desc_link_list = []
        
    def get_desc():
        
        DESCRIPTION_PATH = '.desc'
        content_list = soup_find(
            soup,
            DESCRIPTION_PATH
        ).contents
        
        desc = ''
        index = 0
        
        for content in content_list:
            
            BR_TAG = 'br'
            ANCHOR_TAG = 'a'
            GADGET_ANCHOR_HREF = '/gadget/'
            DIV_TAG = 'div'
            STYLE_TAG = 'style'
            SPAN_TAG = 'span'
            TABLE_TAG = 'table'
            EM_TAG = 'em'
            
            if isinstance(content, NavigableString) or content.name == DIV_TAG:
                
                desc += str(content)
                
                continue
            
            if isinstance(content, Tag):
                
                if content.name == BR_TAG:
                    
                    desc += '\n'
                    index += 1
                    
                    continue
                
                if content.name == ANCHOR_TAG and content.attrs['href'].startswith(GADGET_ANCHOR_HREF):
                    
                    linked_gadget = (
                        content.renderContents().decode('utf-8')
                    )
                    
                    linked_gadget_href = (
                        convert_database_href_typo(content.attrs['href'])
                    )
                    
                    IGNORE_PREFIX_LIST = [
                        '[別名] ',
                        '[参照] ',
                    ]
                    
                    for prefix in IGNORE_PREFIX_LIST:
                        
                        if linked_gadget.startswith(prefix):
                            
                            linked_gadget = linked_gadget[len(prefix):]
                    
                    desc += linked_gadget
                    
                    length = len(linked_gadget)
                    
                    desc_link_list.append({
                        'from_gadget_href': gadget_dict['href'],
                        'to_gadget_href': linked_gadget_href,
                        'begin_index': index,
                        'end_index': index + length,
                    })
                    
                    index += length
                    
                    continue
                
                # TODO: 未対応のリンク (例: /misc/a, /place/a)
                if content.name == ANCHOR_TAG:
                    
                    render_content = (
                        content.renderContents().decode('utf-8')
                    )
                    
                    desc += render_content
                    
                    continue
                
                if content.name == STYLE_TAG or content.name == SPAN_TAG:
                    
                    continue
                
                # TODO: 要対応
                if content.name == TABLE_TAG:
                    
                    continue
                
                if content.name == EM_TAG:
                    
                    render_content = (
                        content.renderContents().decode('utf-8')
                    )
                    
                    desc += render_content
                    
                    continue
            
            raise ValueError(f'Unexpected Content: {content} (type: {type(content)})')
        
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

    return (
        Gadget(**gadget_dict),
        map(lambda link_dict: Link(**link_dict), desc_link_list)
    )


def unique_gadgets(gadgets: List[Gadget]) -> List[Gadget]:
    '''
        ひみつ道具リストの重複を除く
        "大きくなる虫めがね" 等が重複しているよう
    '''
    
    ret_gadgets = []
    used_gadgets = {}
    
    for gadget in gadgets:
        if gadget.href in used_gadgets:
            continue
        
        used_gadgets[gadget.href] = True
        
        ret_gadgets.append(gadget)
    
    return ret_gadgets


def get_gadgets() -> Tuple[List[Gadget], List[Link]]:
    
    gadgets = []
    links = []
    
    for text in html_texts:
        soup = generate_soup(text)
        articles = soup_find_all(soup, GADGET_ARTICLE_PATH)
        
        for article in articles:
            (gadget, gadget_links) = get_gadget_info(article)
            gadgets.append(gadget)
            links.extend(gadget_links)
            
    gadgets = unique_gadgets(gadgets)
        
    return (gadgets, links)


(gadgets, links) = get_gadgets()

print(f'#gadgets: {len(gadgets)}', file=sys.stderr)

if len(gadgets) < 3000:
    # image_url 等取得
    worker(gadgets)


gadget_links = map(lambda link: link.to_gadget_link(gadgets), links)

prelude_str = '''from .data_struct import Gadget, Book, Link
from dorapi.enums import BookSeriesEnum

gadget_datas = '''

content_str = f'[{", ".join(map(str, gadgets))}]'

print(prelude_str + content_str)

prelude_str = '''

link_datas = '''

content_str = f'[{", ".join(gadget_links)}]'

print(prelude_str + content_str)
