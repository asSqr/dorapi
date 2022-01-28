from rest_framework.response import Response
from rest_framework import status
from dorapi import serializers
from commons.viewsets import SingleViewSet
from rest_framework.permissions import AllowAny


class HealthCheckView(SingleViewSet):

    TAG = ['HealthCheck']

    permission_classes = (AllowAny,)

    serializer_class_dict = {
        'default': serializers.HealthCheckSerializers,
    }

    def get(self, request, *args, **kwargs) -> Response:
        alias = 'result'
        result = 'healthy'
        serializer = self.get_serializer_response({alias: result})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
