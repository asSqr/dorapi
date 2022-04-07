from commons import serializers
from dorapi.enums import BookSeriesEnum


class MGadgetMBookSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    series = serializers.EnumField(BookSeriesEnum)
    volume = serializers.CharField()
    
    
class MGadgetInfoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    ruby = serializers.CharField()
    href = serializers.CharField()
    desc = serializers.CharField()
    image_url = serializers.CharField()
    total_results = serializers.IntegerField()
    mbooks = MGadgetMBookSerializer(read_only=True, many=True)


class MGadgetReadSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    ruby = serializers.CharField()
    href = serializers.CharField()
    desc = serializers.CharField()
    image_url = serializers.CharField()
    total_results = serializers.IntegerField()
    mbooks = MGadgetMBookSerializer(read_only=True, many=True)
    linked_gadgets = MGadgetInfoSerializer(read_only=True, many=True)


class GadgetLinkSerializer(serializers.Serializer):
    to_mgadget_id = serializers.UUIDField(read_only=True)
    begin_index = serializers.IntegerField()
    end_index = serializers.IntegerField()


class MGadgetSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    ruby = serializers.CharField()
    href = serializers.CharField()
    desc = serializers.CharField()
    image_url = serializers.CharField()
    total_results = serializers.IntegerField()
    mbooks = MGadgetMBookSerializer(read_only=True, many=True)
    links = GadgetLinkSerializer(read_only=True, many=True)


class MGadgetReadDataListSerializer(serializers.DataListSerializer):
    datas = MGadgetReadSerializer(many=True)


class MGadgetReadDataSerializer(serializers.DataListSerializer):
    data = MGadgetReadSerializer(many=False)
    

class MGadgetDataListSerializer(serializers.DataSerializer):
    datas = MGadgetSerializer(many=True)


class MGadgetDataSerializer(serializers.DataSerializer):
    data = MGadgetSerializer(many=False)
