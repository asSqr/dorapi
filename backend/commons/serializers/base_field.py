from rest_framework import serializers


class BaseField(serializers.Field):
    """
    Open API 用
    """

    def get_default_schema(self):
        return {
            'type': 'string',
            'default': '[]',
        }
