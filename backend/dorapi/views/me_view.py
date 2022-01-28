from rest_framework.response import Response

from dorapi import serializers
from dorapi.use_cases import me as use_case_me
from commons.viewsets import SingleViewSet


class MeView(SingleViewSet):

    TAG = ['Me']

    serializer_class_dict = {
        'default': serializers.MeDataSerializer,
    }

    serializer_alias_dict = {
        'default': 'data',
    }

    use_case_dict = {
        'default': use_case_me.GetMe,
    }

    def get(self, request, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        obj = case.execute(request.mwarehouse, request.muser)

        serializer = self.get_serializer_response({alias: obj})
        return Response(serializer.data)
