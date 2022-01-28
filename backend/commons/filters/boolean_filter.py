from .base_filter import Filter


class BoolFilter(Filter):

    filter_name = 'bool'

    def __init__(self):
        pass

    def get(self, request):
        v = request.GET.get(self.key)
        if v == 'true':
            return True
        elif v == 'false':
            return False
        else:
            return None

    def validator(self, value):
        return isinstance(value, bool)
