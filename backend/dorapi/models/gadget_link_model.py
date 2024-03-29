from typing import Optional, List

from django.db import models

from commons.models import BaseModel, QuerySet


class GadgetLinkQuerySet(QuerySet):

    def get_by_id(self, id_: str) -> Optional['GadgetLink']:
        try:
            return self.get(id=id_)
        except GadgetLink.DoesNotExist:
            return None

    def filter_id_in(self, id_list: List[str]) -> 'GadgetLinkQuerySet':
        return self.filter(id__in=id_list)

    def filter_eq_id(self, id_: str) -> 'GadgetLinkQuerySet':
        return self.filter(id=id_)
    
    def filter_eq_mgadget(self, mgadget) -> 'GadgetLinkQuerySet':
        return self.filter(from_mgadget=mgadget)
    
    def filter_mgadget_in(self, mgadgets) -> 'GadgetLinkQuerySet':
        return self.filter(from_mgadget__in=mgadgets)


class GadgetLink(BaseModel):
    '''
    ドラえもんひみつ道具 説明リンク
    '''
    
    from_mgadget = models.ForeignKey(
        'dorapi.MGadget', db_column='from_mgadget_id', related_name='to_gadgetlinks',
        related_query_name='to_gadgetlink', on_delete=models.CASCADE
    )
    to_mgadget = models.ForeignKey(
        'dorapi.MGadget', db_column='to_mgadget_id', related_name='from_gadgetlinks',
        related_query_name='from_gadgetlink', on_delete=models.CASCADE
    )
    begin_index = models.IntegerField()
    end_index = models.IntegerField()
    
    objects = GadgetLinkQuerySet.as_soft_manager()
    object_all = GadgetLinkQuerySet.as_manager()
