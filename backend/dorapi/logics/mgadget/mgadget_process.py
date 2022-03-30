from dataclasses import dataclass
from dorapi.models.mgadget_model import MGadgetQuerySet


@dataclass
class MGadgetProcess:
    
    mgadget_queryset: MGadgetQuerySet

    def filter_or_query_param(self, keyword):
        if keyword is not None:

            self.mgadget_queryset = (
                self.mgadget_queryset.filter_or_keyword(keyword)
            )

    def sort_by_query_param(self, sort_key, sort_order):
        if sort_key is not None:
            self.mgadget_queryset = (
                self.mgadget_queryset.sort_by_key(sort_key, sort_order)
            )

    def count(self):
        return self.mgadget_queryset.count()

    def paginate(self, page_size, page):
        if isinstance(page_size, int) and isinstance(page, int):
            self.mgadget_queryset = self.mgadget_queryset.paginate(page_size, page)

    def distinct(self):
        self.mgadget_queryset = self.mgadget_queryset.distinct()
