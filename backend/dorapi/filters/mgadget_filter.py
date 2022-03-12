from commons import filters
from commons.enums import SortOrderType


class ListMGadgetFilterSet(filters.BaseFilterSet):
    keyword = filters.StringFilter()
    page = filters.IntFilter()
    page_size = filters.IntFilter()
    sort_key = filters.StringFilter()
    sort_order = filters.StringEnumFilter(SortOrderType)
