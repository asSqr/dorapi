from rest_framework import serializers


class DataListSerializer(serializers.Serializer):
    options = serializers.DictField(required=False)  # for request
    extras = serializers.DictField(required=False)  # for response
