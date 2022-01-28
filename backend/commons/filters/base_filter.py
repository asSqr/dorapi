from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Filter(ABC):

    weight = 0
    key = None
    required = False
    filter_name = ''

    def __init__(self, *args, **kwargs):
        default = kwargs.get('default')
        if default:
            self.default = default

    def set_key(self, key):
        self.key = key

    @abstractmethod
    def get(self, request):
        """get request and extract"""

    @abstractmethod
    def validator(self, value):
        """set validator"""

    def has_default(self):
        return hasattr(self, "default")

    def get_default(self):
        return self.default

    def get_filter_desc(self):
        return self.filter_name

    def get_schema(self, key):
        return [
            {
                'name': key,
                'required': False,
                'in': 'query',
                'description': self.get_filter_desc(),
                'schema': {
                    'type': 'string',
                },
            },
        ]

