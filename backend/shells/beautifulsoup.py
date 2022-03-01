from bs4 import BeautifulSoup
import functools
from typing import List, Dict, Any

def generate_soup(html_text: str) -> BeautifulSoup:
    return BeautifulSoup(html_text, 'html.parser')

def selector_parse(selector: str, class_key: str = 'class_') -> Dict[str, Any]:
    
    def reduce_func(acc: Dict[str, Any], tag: str) -> Dict[str, Any]:
        if len(tag) == 0:
            return acc
        
        key = None
        value = None
            
        if tag[0] == '.':
            key = class_key
            value = tag[1:]
        else:
            key = 'name'
            value = tag

        acc.update({
            key: value,
        })
            
        return acc
    
    options = functools.reduce(
        reduce_func,
        selector.split(' '),
        {}
    )
    
    if options.get('name') is None:
        options['name'] = 'div'
        
    return options

def soup_find_extended(
    soup: BeautifulSoup, attr: str,
    path: str, **kwargs) -> BeautifulSoup:
    '''
        ・ネストされたパスを > 区切りで指定できる
        ・クラスを .~~ で指定できる (タグのデフォルトは `div`)
        
        soup.find 系の拡張
    '''

    selectors = path.split('>')
    
    for selector in selectors:
        soup_options = kwargs
    
        soup_options.update(
            **selector_parse(selector)
        )
        
        soup = getattr(soup, attr)(**soup_options)
        
    return soup

def soup_find(soup: BeautifulSoup, 
    path: str, **kwargs) -> BeautifulSoup:
    
    return soup_find_extended(soup, 'find', path, **kwargs)

def soup_find_all(soup: BeautifulSoup, 
    selector: str, **kwargs) -> List[BeautifulSoup]:
    
    soup_options = kwargs
    
    soup_options.update(
        **selector_parse(selector, 'attrs')
    )
    
    return soup.find_all(**soup_options)

# 結果として inner_text だけが欲しい場合の options
inner_text_options = {
    'text': True,
    'recursive': True,
}
