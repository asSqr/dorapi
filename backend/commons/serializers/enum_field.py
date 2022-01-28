from enum import Enum
from typing import Type

from .base_field import BaseField


class EnumField(BaseField):

    initial = ""

    default_error_messages = {
        'invalid_choice': '"{input}" is not a valid choice.'
    }

    def __init__(self, enum_class: Type, **kwargs):

        default = kwargs.get('default')
        if default:
            if isinstance(default, Enum):
                kwargs['default'] = default.value

        super().__init__(**kwargs)
        self.enum_class = enum_class

    def to_internal_value(self, data):
        try:
            return self.enum_class[data].value
        except KeyError:
            self.fail('invalid_choice', input=data)

    def to_representation(self, value):
        return self.enum_class(value).name

    def get_default_schema(self):
        return {
            'type': 'string',
            'default': list(self.enum_class)[0].name,
        }
