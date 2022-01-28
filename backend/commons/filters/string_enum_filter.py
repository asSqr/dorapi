from .base_filter import Filter


class StringEnumFilter(Filter):

    filter_name = 'str_enum'

    def __init__(self, enum, *args, **kwargs):
        self.enum = enum
        self.names = tuple(c.name for c in enum)
        super().__init__(*args, **kwargs)

    def get(self, request):
        k = request.GET.get(self.key)
        return self.enum[k].value if k is not None else None

    def validator(self, value):
        return isinstance(value,int)

    def get_default(self):
        return self.default.name if self.default else None

    def get_filter_desc(self):
        return self.filter_name + f": {str(list(self.names))}"
