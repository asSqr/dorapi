import json

from .base_field import BaseField


class JSONField(BaseField):

    initial = "{}"

    default_error_messages = {
        'not_a_json': 'Expected a json of items but got type "{input}".',
        'empty': 'This dictionary may not be empty.',
        'not_a_json_list': 'Expected a json list but got type "{input}".',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        try:
            return json.loads(data) if data else {}
        except json.decoder.JSONDecodeError:
            self.fail('not_a_json', input=data)

    def to_representation(self, value):
        return json.dumps(value) if value else ""

    def get_default_schema(self):
        return {
            'type': 'string',
            'default': '{}',
        }


class JSONListField(JSONField):

    initial = "[]"

    def to_internal_value(self, data):

        data = super().to_internal_value(data)
        if isinstance(data, list):
            return data
        else:
            self.fail('not_a_json_list', input=data)

    def get_default_schema(self):
        return {
            'type': 'string',
            'default': '[]',
        }
