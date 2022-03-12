from commons import serializers
from dorapi.enums import BookSeriesEnum


class MGadgetMBookSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    series = serializers.EnumField(BookSeriesEnum)
    volume = serializers.CharField()


class MGadgetReadSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    ruby = serializers.CharField()
    desc = serializers.CharField()
    mbooks = MGadgetMBookSerializer(read_only=True, many=True)


class MGadgetReadDataListSerializer(serializers.DataListSerializer):
    datas = MGadgetReadSerializer(many=True)


class MGadgetReadDataSerializer(serializers.DataListSerializer):
    data = MGadgetReadSerializer(many=False)
    

class MGadgetDataListSerializer(serializers.DataSerializer):
    datas = MGadgetReadSerializer(many=True)


class MGadgetDataSerializer(serializers.DataSerializer):
    data = MGadgetReadSerializer(many=False)
