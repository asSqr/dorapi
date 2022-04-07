from typing import Optional, List

from django.db.models import (
    Q,
    Case, When, Value,
    IntegerField, CharField, ManyToManyField,
    BigIntegerField,
)
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
        q1 = Q()
        q2 = Q()
        search_keywords = ['name', 'ruby', 'desc', 'mbooks__series', 'mbooks__volume']
        
        for k in keyword.strip().split():
            for c in search_keywords:
                q1 = q1 | Q(**{f'{c}': k})
        
        for k in keyword.strip().split():
            for c in search_keywords:
                q2 = q2 | Q(**{f'{c}__icontains': k})
                
        # exact な一致を優先
        ret_q = (
            self.filter(q1 | q2).annotate(
                search_type_ordering=Case(
                    When(q1, then=Value(1)),
                    When(q2, then=Value(0)),
                    default=Value(-1),
                    output_field=IntegerField(),
                )
            )
            .order_by('-search_type_ordering')
        )
        
        return ret_q

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
    
    name = CharField(max_length=8192)
    ruby = CharField(max_length=8192)
    desc = CharField(max_length=8192)
    href = CharField(max_length=8192)
    image_url = CharField(max_length=8192, null=True)
    total_results = BigIntegerField(null=True)
    mbooks = ManyToManyField(
        'dorapi.MBook',
        related_name='mbooks',
        related_query_name='mbook',
        through='dorapi.GadgetBook',
    )
    linked_gadgets = ManyToManyField(
        'self',
        related_name='linked_mgadgets',
        related_query_name='linked_mgadget',
        through='dorapi.GadgetLink',
        symmetrical=False,
    )
    
    objects = MGadgetQuerySet.as_soft_manager()
    object_all = MGadgetQuerySet.as_manager()
