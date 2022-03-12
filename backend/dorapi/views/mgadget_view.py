from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from commons.viewsets import SingleViewSet

from dorapi import serializers, filters
from dorapi.use_cases import mgadget as use_case_mgadget


class MGadgetView(SingleViewSet):

    TAG = ['v1/MGadget']
    
    permission_classes = (AllowAny,)

    serializer_class_dict = {
        'list': serializers.MGadgetReadDataListSerializer,
        'retrieve': serializers.MGadgetReadDataSerializer,
    }

    use_case_dict = {
        'list': use_case_mgadget.ListMGadget,
        'retrieve': use_case_mgadget.GetMGadget,
    }

    serializer_alias_dict = {
        'list': 'datas',
        'default': 'data',
    }

    filter_set_dict = {
        'list': filters.ListMGadgetFilterSet,
    }

    def list(self, request, *args, **kwargs) -> Response:
        return self._list(request, *args, **kwargs)

    def retrieve(self, request, id: str, *args, **kwargs) -> Response:
        return self._retrieve(request, id, *args, **kwargs)
