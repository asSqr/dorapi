from dataclasses import dataclass
from enum import Enum
from typing import List

class BookSeriesEnum(Enum):
    tencomi = 'てんコミ'
    chohen = '大長編'
    f_land = 'FFランド'
    col_collect = 'カラー'
    plus = 'プラス'
    f_collect = '大全集'
    movie = '映ドラ'

    @classmethod
    def choices(cls):
        return tuple((c.value, c.name) for c in cls)

@dataclass
class Book:
    series: BookSeriesEnum
    volume: str

@dataclass
class Gadget:
    name: str
    ruby: str
    desc: str
    books: List[Book]
