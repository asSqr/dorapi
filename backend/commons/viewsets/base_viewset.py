from typing import Dict, List, Tuple, Any, Union, Type
from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission

from commons.use_case import BaseUseCase
from commons.filters import BaseFilterSet, BlankFilterSet
from commons.enums import RequestType


class BaseViewSet(viewsets.GenericViewSet):
    """
    ViewSet
    各クラス dict にて、action に対応した serializer etcが取得できる

    ```py
    serializer_class_dict = {
        'list': ListSerializer, # list 時に動作
        'retrieve': RetrieveSerializer, # retrieve 時に動作
        'default': GenericSerializer, # 上記その他で取得
    }
    ```

    action -> default -> list の順で取得

    serializer_class_dict のみ request, response Dict 可能
    serializer_class_dict = {
        'default': {
            'request': RequestSerializer,
            'response': RequestSerializer,
        }
    }

    """

    # Open API
    TAG = []

    class Meta:
        abstract = True

    # Permissions
    permission_classes_dict: Dict[str, Tuple] = {}

    # Serializer
    serializer_class_dict: Dict[str, Union[Type[serializers.Serializer],
                                           Dict[str, Type[serializers.Serializer]]]] = {}

    # Alias
    serializer_alias_dict: Dict[str, str] = {
        'list': 'datas', 'default': 'data'}
    serializer_option_alias_dict: Dict[str, str] = {'default': 'options'}

    # UseCase
    use_case_dict: Dict[str, Type[BaseUseCase]] = {}

    # Filter
    filter_set_dict: Dict[str, Type[BaseFilterSet]] = {}

    # LookUp
    lookup_field = 'id'

    def get_permissions(self) -> List[BasePermission]:
        permission_classes = (
            self.permission_classes_dict.get(self.action) or
            self.permission_classes_dict.get('default') or
            self.permission_classes
        )
        return [permission() for permission in permission_classes]

    def get_serializer_request(self, *args, **kwargs):
        serializer_class = self.get_serializer_class('request')
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_response(self, *args, **kwargs):
        serializer_class = self.get_serializer_class('response')
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_alias(self) -> str:
        return (
            self.serializer_alias_dict.get(self.action) or
            self.serializer_alias_dict.get('default') or
            self.serializer_alias_dict['list']
        )

    def get_serializer_option_alias(self) -> str:
        # main: default. If required, will add.
        return (
            self.serializer_option_alias_dict['default']
        )

    def get_use_case(self, *args, **kwargs) -> Any:
        cls = (
            self.use_case_dict.get(self.action) or
            self.use_case_dict.get('default') or
            self.use_case_dict['list']
        )
        return cls(*args, **kwargs)  # type: ignore

    def get_filter_set(self, request) -> BaseFilterSet:
        filter_set_class = self.get_filter_set_class()
        return filter_set_class(request)

    def _get_serializer_class_from_action(self) -> Union[Type[serializers.Serializer], Dict[str, Type[serializers.Serializer]]]:
        return (
            self.serializer_class_dict.get(self.action) or
            self.serializer_class_dict.get('default') or
            self.serializer_class_dict['list']
        )

    def get_serializer_class(self, type_: str = 'request') -> Type[serializers.Serializer]:
        """also required open api"""
        serializer_class_dict_value = self._get_serializer_class_from_action()

        if isinstance(serializer_class_dict_value, dict):
            return serializer_class_dict_value[RequestType[type_].name]
        else:
            return serializer_class_dict_value

    def get_filter_set_class(self) -> Type[BaseFilterSet]:
        """also required for open api"""
        return (
            self.filter_set_dict.get(self.action) or
            self.filter_set_dict.get('default') or
            BlankFilterSet
        )
