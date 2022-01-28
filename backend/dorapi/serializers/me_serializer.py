from commons import serializers
from dorapi.enums import MUserTypeEnum


class MWarehouseSerailizers(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class MeSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    sub = serializers.CharField(max_length=8192, read_only=True)
    name = serializers.CharField(max_length=8192, allow_blank=True)
    email = serializers.CharField(max_length=8192)
    authority = serializers.IntegerField(required=False)


class MeDataSerializer(serializers.DataSerializer):
    data = MeSerializer(many=False)


class MeUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(required=False, allow_blank=True)


class MeUpdateDataSerializer(serializers.Serializer):
    data = MeUpdateSerializer(many=False)
