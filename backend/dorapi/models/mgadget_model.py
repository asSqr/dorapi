from typing import Optional, List

from django.db import models
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
    
    objects = MGadgetQuerySet.as_soft_manager()
    object_all = MGadgetQuerySet.as_manager()
