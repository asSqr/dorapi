from .config import GoogleAPIConfig
from .utils import generate_query

from dotenv import load_dotenv
import time
import os
import sys
from urllib.parse import quote
from dataclasses import dataclass
import requests
from typing import List

sys.path.append('./backend/seeds/gadgets')

from data_struct import Gadget      # noqa


load_dotenv()


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
    
    url = f'{GoogleAPIConfig.GOOGLE_BASE_URL}{GoogleAPIConfig.GOOGLE_CUSTOM_SEARCH_PATH}?{query}'
    
    resp = requests.get(url).json()
    images = resp.get('items', [{'link': None}])
    infos = resp.get('searchInformation', {})
    
    image_url = images[0]['link']
    total_results = infos.get('totalResults')
    
    return SearchInfo(
        image_url=image_url,
        total_results=total_results,
    )


def process(gadget: Gadget) -> None:
    search_keyword = f'{gadget.name}{GoogleAPIConfig.GOOGLE_CUSTOM_DORA_SUFFIX}'
    search_info = get_image_url_from_google(search_keyword)
    gadget.image_url = search_info.image_url
    
    print(f'{search_info.total_results} {search_info.image_url}', file=sys.stderr)
    
    gadget.total_results = search_info.total_results
    
    time.sleep(GoogleAPIConfig.WAIT_SECONDS)
    
    return gadget


def worker(gadgets: List[Gadget]) -> List[Gadget]:
    gadget_list = []
    
    for gadget in gadgets:
        gadget_list.append(process(gadget))
    
    return gadget_list
