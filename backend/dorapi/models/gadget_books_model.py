from typing import Optional, List

from dorapi.enums import BookSeriesEnum
from django.db import models
from commons.models import BaseModel, QuerySet


class GadgetBookQuerySet(QuerySet):

    def get_by_id(self, id_: str) -> Optional['GadgetBook']:
        try:
            return self.get(id=id_)
        except MBook.DoesNotExist:
            return None

    def filter_id_in(self, id_list: List[str]) -> 'GadgetBookQuerySet':
        return self.filter(id__in=id_list)

    def filter_eq_id(self, id_: str) -> 'GadgetBookQuerySet':
        return self.filter(id=id_)


'''
ひみつ道具ー掲載単行本 中間テーブル
'''
class GadgetBook(BaseModel):
    mgadget = models.ForeignKey('dorapi.MGadget', db_column='mgadget_id', related_name='gadgetbooks',
                               related_query_name='gadgetbook', on_delete=models.CASCADE)
    mbook = models.ForeignKey('dorapi.MBook', db_column='mbook_id', related_name='gadgetbooks',
                               related_query_name='gadgetbook', on_delete=models.CASCADE)

    objects = GadgetBookQuerySet.as_soft_manager()
    object_all = GadgetBookQuerySet.as_manager()
