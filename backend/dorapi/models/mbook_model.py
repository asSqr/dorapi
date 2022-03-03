from typing import Optional, List

from dorapi.enums import BookSeriesEnum
from django.db import models
from commons.models import BaseModel, QuerySet


class MBookQuerySet(QuerySet):

    def get_by_id(self, id_: str) -> Optional['MBook']:
        try:
            return self.get(id=id_)
        except MBook.DoesNotExist:
            return None

    def filter_id_in(self, id_list: List[str]) -> 'MBookQuerySet':
        return self.filter(id__in=id_list)

    def filter_eq_id(self, id_: str) -> 'MBookQuerySet':
        return self.filter(id=id_)


class MBook(BaseModel):    
    '''
    掲載単行本
    '''
    
    series = models.CharField(
        max_length=8192,
        choices=BookSeriesEnum.choices()
    )
    volume = models.CharField(max_length=8192)
    mgadgets = models.ManyToManyField(
        'dorapi.MGadget',
        related_name='mgadgets',
        related_query_name='mgadget',
        through='dorapi.GadgetBook',
    )

    objects = MBookQuerySet.as_soft_manager()
    object_all = MBookQuerySet.as_manager()
