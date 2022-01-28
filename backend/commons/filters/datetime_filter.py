from dateutil import parser as dateutil_parser
import datetime
from .base_filter import Filter


class DateTimeFilter(Filter):

    filter_name = 'datetime'

    def get(self, request):
        v = request.GET.get(self.key)
        return dateutil_parser.parse(v) if v is not None else v

    def validator(self, value):
        return isinstance(value, datetime.datetime)

    def get_default(self):
        return self.default.name if self.default else None
