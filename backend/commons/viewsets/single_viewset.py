from typing import Any, Dict, Tuple, Union
from rest_framework import status
from rest_framework.response import Response

from .base_viewset import BaseViewSet


def format_payload(alias: str, objs: Union[Any, Tuple]) -> Dict[str, Any]:
    return {alias: objs[0], 'extras': objs[1]} if isinstance(objs, tuple) else {alias: objs}


class SingleViewSet(BaseViewSet):
    """
    Single ViewSet
    """

    # LookUp
    lookup_field = 'id'

    def _list(self, request, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()
        filterset = self.get_filter_set(request)

        objs = case.execute(request.muser, filterset.data)

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _create(self, request, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = case.execute(request.muser,
                           serializer.validated_data[alias], serializer.validated_data.get(option_alias, {}))

        payload = format_payload(alias, obj)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def _retrieve(self, request, id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        obj = case.execute(request.muser, id)

        payload = format_payload(alias, obj)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _update(self, request, id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = case.execute(request.muser, id,
                           serializer.validated_data[alias], serializer.validated_data.get(option_alias, {}))

        payload = format_payload(alias, obj)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _destroy(self, request, id: str, *args, **kwargs) -> Response:
        case = self.get_use_case()

        case.execute(request.muser, id)

        return Response(status=status.HTTP_204_NO_CONTENT)
