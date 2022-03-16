from typing import Optional, List

from django.db import models
from django.core.paginator import Paginator, Page

from commons.models import BaseModel, QuerySet


class MGadgetQuerySet(QuerySet):

    def get_by_id(self, id_: str) -> Optional['MGadget']:
        try:
            return self.get(id=id_)
        except MGadget.DoesNotExist:
            return None

    def filter_id_in(self, id_list: List[str]) -> 'MGadgetQuerySet':
        return self.filter(id__in=id_list)

    def filter_eq_id(self, id_: str) -> 'MGadgetQuerySet':
        return self.filter(id=id_)
    
    def filter_or_keyword(self, keyword: str) -> 'MGadgetQuerySet':
        q = models.Q()
        search_keywords = ['name', 'ruby', 'desc', 'mbooks__series', 'mbooks__volume']
        
        for k in keyword.strip().split():
            for c in search_keywords:
                q = q | models.Q(**{f'{c}__icontains': k})
        
        return self.filter(q)

    def sort_by_key(self, sort_key: str, sort_order: bool = True) -> 'MGadgetQuerySet':
        sgn = '' if sort_order else '-'
        return self.order_by(sgn + sort_key)

    def paginate(self, page_size: int, page: int) -> 'Page':
        return Paginator(self, page_size).get_page(page)

    def select_msku_related(self) -> 'MGadgetQuerySet':
        return self.select_related('mbooks')


class MGadget(BaseModel):
    '''
    ドラえもんひみつ道具
    '''
    
    name = models.CharField(max_length=8192)
    ruby = models.CharField(max_length=8192)
    desc = models.CharField(max_length=8192)
    mbooks = models.ManyToManyField(
        'dorapi.MBook',
        related_name='mbooks',
        related_query_name='mbook',
        through='dorapi.GadgetBook',
    )
    linked_gadgets = models.ManyToManyField(
        'self',
        related_name='mgadget',
        related_query_name='mgadget',
        through='dorapi.GadgetLink',
        symmetrical=False,
    )
    
    objects = MGadgetQuerySet.as_soft_manager()
    object_all = MGadgetQuerySet.as_manager()
