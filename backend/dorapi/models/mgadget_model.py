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

'''
ドラえもんひみつ道具
'''
class MGadget(BaseModel):
    name = models.CharField(max_length=8192)
    ruby = models.CharField(max_length=8192)
    desc = models.CharField(max_length=8192)
    mbook = models.ForeignKey('dorapi.MBook', 
        db_column='mbook_id', related_name='mbooks',
        related_query_name='mbook', on_delete=models.CASCADE)
