from .constants import (
    GOOGLE_BASE_URL,
    GOOGLE_CUSTOM_SEARCH_PATH,
    GOOGLE_CUSTOM_DORA_SUFFIX,
    WAIT_SECONDS,
)
from .utils import generate_query
from .async_request import get

import dotenv
import time
import os
import sys
from urllib.parse import quote
from dataclasses import dataclass
import asyncio
from typing import List

sys.path.append('./backend/seeds/gadgets')

from data_struct import Gadget      # noqa


dotenv.load_dotenv()


@dataclass
class SearchInfo:
    image_url: str
    total_results: int


async def get_image_url_from_google(gadget_name: str) -> SearchInfo:
    
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
    
    resp = get(url)
    images = resp.get('items', [{'link': None}])
    infos = resp.get('searchInformation', {})
    
    image_url = images[0]['link']
    total_results = infos.get('totalResults')
    
    return SearchInfo(
        image_url=image_url,
        total_results=total_results,
    )


async def process(gadget: Gadget) -> None:
    search_keyword = f'{gadget.name}{GOOGLE_CUSTOM_DORA_SUFFIX}'
    search_info = await get_image_url_from_google(search_keyword)
    gadget.image_url = search_info.image_url
    
    print(f'#{search_info.total_results}: {search_info.image_url}', file=sys.stderr)
    
    if gadget.image_url is None:
        time.sleep(WAIT_SECONDS)
        await process(gadget)
        return
    
    gadget.total_results = search_info.total_results
    
    if gadget.total_results is None:
        time.sleep(WAIT_SECONDS)
        await process(gadget)
        return


def worker(gadgets: List[Gadget]) -> None:
    loop = asyncio.get_event_loop()
    gather = asyncio.gather(
        *[process(gadget) for gadget in gadgets]
    )
    loop.run_until_complete(gather)
