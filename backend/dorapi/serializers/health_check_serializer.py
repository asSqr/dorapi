from commons import serializers

class HealthCheckSerializers(serializers.Serializer):
    result = serializers.CharField()
