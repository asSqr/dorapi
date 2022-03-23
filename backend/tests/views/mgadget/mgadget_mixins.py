from dorapi.models import MGadget, GadgetLink
from dorapi.enums import BookSeriesEnum
from typing import Dict, Any


class MGadgetMixin:

    def assertMGadget(self, data: Dict[str, Any], mgadget: MGadget):
        self.assertEqual(data['name'], mgadget.name)
        self.assertEqual(data['ruby'], mgadget.ruby)
        self.assertEqual(data['desc'], mgadget.desc)
        
        for book, mbook in zip(data['mbooks'], mgadget.mbooks.all()):
            self.assertEqual(BookSeriesEnum[book['series']].value, mbook.series)
            self.assertEqual(book['volume'], mbook.volume)
            
        gadgetlinks = (
            GadgetLink.objects
            .filter_eq_mgadget(mgadget)
        )
        
        expected_tuple_list = []
        
        for gadgetlink in gadgetlinks:
            expected_tuple_list.append((str(gadgetlink.to_mgadget.id), gadgetlink.begin_index, gadgetlink.end_index))
            
        check_tuple_list = []
        
        for link in data['links']:
            check_tuple_list.append((link['to_mgadget_id'], link['begin_index'], link['end_index']))
        
        self.assertEqual(set(check_tuple_list), set(expected_tuple_list))
