from .base_filter import Filter


class IntFilter(Filter):

    filter_name = 'int'

    def __init__(self):
        pass

    def get(self, request):
        v = request.GET.get(self.key)
        return int(v) if v is not None and v.isdigit() else v

    def validator(self, value):
        return isinstance(value, int)
