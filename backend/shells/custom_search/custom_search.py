from constants import (
    GOOGLE_BASE_URL,
    GOOGLE_CUSTOM_SEARCH_PATH,
    GOOGLE_CUSTOM_DORA_SUFFIX,
    WAIT_SECONDS,
)
from utils import generate_query
from dataclasses import dataclass

import dotenv

import os
import requests
from urllib.parse import quote

import time
import sys

sys.path.append('backend/seeds/gadgets')

from dora_superdatabase import gadget_datas, link_datas      # noqa


dotenv.load_dotenv()


@dataclass
class SearchInfo:
    image_url: str
    total_results: int


def get_image_url_from_google(gadget_name: str) -> SearchInfo:
    
    CSE_ID = os.getenv('CSE_ID')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    search_keyword = f'{gadget_name} コミック'
    encoded_keyword = quote(search_keyword.replace(' ', '+'))
    
    query_dict = {
        'q': encoded_keyword,
        'searchType': 'image',
        'cx': CSE_ID,
        'key': GOOGLE_API_KEY,
        'start': 1,
        'lr': 'lang_ja',
        'num': 1,
    }
    
    query = generate_query(query_dict)
    
    url = f'{GOOGLE_BASE_URL}{GOOGLE_CUSTOM_SEARCH_PATH}?{query}'
    
    resp = requests.get(url).json()
    images = resp.get('items', [{'link': ''}])
    infos = resp.get('searchInformation', {})
    
    image_url = images[0]['link']
    total_results = infos.get('totalResults')
    
    return SearchInfo(
        image_url=image_url,
        total_results=total_results,
    )


def crawler() -> None:
    for gadget in gadget_datas:
        search_keyword = f'{gadget.name}{GOOGLE_CUSTOM_DORA_SUFFIX}'
        search_info = get_image_url_from_google(search_keyword)
        gadget.image_url = search_info.image_url
        gadget.total_results = search_info.total_results
        
        time.sleep(WAIT_SECONDS)
        
    prelude_str = '''from data_struct import Gadget, Book, Link
from dorapi.enums import BookSeriesEnum

gadget_datas = '''

    content_str = str(gadget_datas)

    print(prelude_str + content_str)

    prelude_str = '''

    link_datas = '''

    content_str = str(link_datas)

    print(prelude_str + content_str)


if __name__ == '__main__':
    crawler()
