from collections.abc import Iterable

from .base_filter import Filter


class StringEnumListFilter(Filter):

    filter_name = 'str_enum_list'

    def __init__(self, enum, *args, **kwargs):
        self.enum = enum
        self.names = tuple(c.name for c in enum)
        super().__init__(*args, **kwargs)

    def get(self, request):
        enum_list = request.GET.getlist(self.key)
        if not enum_list:
            return None
        res = []
        for k in enum_list:
            if k not in self.names:
                return [None]
            res.append(self.enum[k].value)
        return res

    def validator(self, value):
        if isinstance(value, Iterable):
            return all(isinstance(v, int) for v in value)
        else:
            return False

    def get_default(self):
        return None

    def get_filter_desc(self):
        return self.filter_name + f": List[{str(list(self.names))}]"
