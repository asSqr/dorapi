import logging
from .base_filter import Filter
from commons import exceptions

logger=logging.getLogger(__name__)
class FilterSetMetaclass(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        setattr(new_class, '_filters', cls.get_filters(attrs))
        return new_class

    @classmethod
    def get_filters(cls, attrs):
        filters = []
        for k, v in attrs.items():
            if isinstance(v, Filter):
                v.set_key(k)
                filters.append((k, v))
        return filters


class BaseFilterSet(metaclass=FilterSetMetaclass):

    search_param_name = '検索'
    search_description = ''

    def __init__(self, request):
        self._data = {}
        self.get_data_from_request(request)

    def get_data_from_request(self, request):
        for k, f in getattr(self, '_filters'):  # nopa
            try:
                v = f.get(request)
            except Exception as e:
                logger.error(e, exc_info=True)
                raise exceptions.BadRequestError({
                    'query params': f"Field {k} is class {f.__class__.__name__} but something went wrong. msg: {str(e)}",
                })

            if v is None and f.has_default():
                v = f.get_default()

            if v is None and not f.required:
                continue

            if not f.validator(v):
                raise exceptions.BadRequestError({
                    'query params': f"Field {k} is class {f.__class__.__name__} but got {v}",
                })
            self._data[k] = v

    @property
    def data(self):
        return self._data

    @classmethod
    def get_schema_operation_parameters(cls):

        filters = []

        for k, f in getattr(cls, '_filters'):  # nopa
            filters += f.get_schema(k)

        return filters
