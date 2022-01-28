import json

from rest_framework import serializers


class JSONDumpSerializer(serializers.Serializer):

    default_error_messages = {
        'invalid_json': '"{input}" is not a json.'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        try:
            return json.loads(data) if data else {}
        except:
            self.fail('invalid_json', input=data)

    def to_representation(self, value):
        return json.dumps(value) if value else ""

    @property
    def data(self):
        try:
            return json.dumps(self.instance)
        except KeyError:
            self.fail('invalid_json', input=self.instance)
