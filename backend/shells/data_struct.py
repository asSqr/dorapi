from dataclasses import dataclass
from enum import Enum
from typing import List

'''
単行本 Enum
'''
class BookSeriesEnum(Enum):
    # てんとう虫コミックス
    tencomi = 'てんコミ'
    # 大長編ドラえもん
    chohen = '大長編'
    # 藤子不二雄ランド
    f_land = 'FFランド'
    # カラー作品集
    col_collect = 'カラー'
    # ドラえもんプラス
    plus = 'プラス'
    # 藤子・F・不二雄大全集
    f_collect = '大全集'
    # 映画版ドラえもん
    movie = '映ドラ'

    @classmethod
    def choices(cls):
        return tuple((c.value, c.name) for c in cls)

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
