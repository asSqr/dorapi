from collections.abc import Iterable

from .base_filter import Filter


class IntListFilter(Filter):

    filter_name = 'int_list'

    def __init__(self, required: bool):
        self.required = required

    def get(self, request):
        return request.GET.getlist(self.key)

    def validator(self, value):
        if isinstance(value, Iterable):
            return all(isinstance(v, int) for v in value)
        else:
            return False
