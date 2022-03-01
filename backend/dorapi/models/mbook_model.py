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


'''
掲載単行本
'''
class MBook(BaseModel):
    series = models.CharField(max_length=8192,
                choices=BookSeriesEnum.choices())
    volume = models.CharField(max_length=8192)
