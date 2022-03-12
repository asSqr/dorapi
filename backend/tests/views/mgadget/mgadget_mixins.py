from dorapi.models import MGadget
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
