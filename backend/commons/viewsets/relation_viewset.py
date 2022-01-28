from typing import Any, Dict, Tuple, Union
from rest_framework.response import Response

from .base_viewset import BaseViewSet

def format_payload(alias: str, objs: Union[Any, Tuple]) -> Dict[str, Any]:
    return {alias: objs[0], 'extras': objs[1]} if isinstance(objs, tuple) else {alias: objs}

class RelationViewSet(BaseViewSet):
    """
    Relation ViewSet

    注意：
        - _id: を指定すること
        - Nested 使用すると、(Nested の lookup_field)_(Viewset の lookup_field) が引数になる
        - Nested の lookup_field '', Viewset の lookup_field がidだと、''+'_'+'id'
    """

    # LookUp
    lookup_field = 'id'

    def _list(self, request, _id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()
        filter_set = self.get_filter_set(request)

        objs = case.execute(request.mwarehouse,
                            request.muser, _id, filter_set.data)

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _connect(self, request, _id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(request.mwarehouse, request.muser, _id,
                            serializer.validated_data[alias], serializer.validated_data.get(option_alias, {}))

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _disconnect(self, request, _id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(request.mwarehouse, request.muser, _id,
                            serializer.validated_data[alias], serializer.validated_data.get(option_alias, {}))

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _retrieve(self, request, _id: str, detail_id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        objs = case.execute(request.mwarehouse, request.muser, _id, detail_id)

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _update(self, request, _id: str, detail_id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(request.mwarehouse, request.muser, _id, detail_id,
                            serializer.validated_data[alias], serializer.validated_data.get(option_alias))

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _bulk_create(self, request, _id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(request.mwarehouse, request.muser, _id,
                            serializer.validated_data[alias], serializer.validated_data.get(option_alias))

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)

    def _bulk_replace(self, request, _id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        option_alias = self.get_serializer_option_alias()
        case = self.get_use_case()

        serializer = self.get_serializer_request(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(request.mwarehouse, request.muser, _id,
                            serializer.validated_data[alias], serializer.validated_data.get(option_alias))

        payload = format_payload(alias, objs)

        serializer = self.get_serializer_response(payload)
        return Response(serializer.data)
