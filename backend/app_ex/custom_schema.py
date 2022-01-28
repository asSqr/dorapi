from typing import Dict, Any
import warnings
from rest_framework.schemas.openapi import AutoSchema
from rest_framework import serializers, exceptions
from rest_framework.schemas.utils import is_list_view
from rest_framework.fields import empty
from commons import serializers


class CustomSchema(AutoSchema):

    def get_tags(self, path, method):
        tag = getattr(self.view, 'TAG', [])

        # super().get_tags(path, method)
        return tag if len(tag) else ['/'.join(path.split('/')[1:3]) + '/']

    def get_operation(self, path, method):
        operation = super().get_operation(path, method)
        operation['security'] = self._get_securities(path, method)

        return operation

    def _get_securities(self, path, method):
        view = self.view

        schemas = []
        
        securities = [{key: [] for key in s.keys()} for s in schemas]
        for auth_class in view.authentication_classes:
            if hasattr(auth_class, 'security_schema'):
                securities.append({key: []
                                  for key in auth_class.security_schema.keys()})

        return securities

    def get_filter_parameters(self, path, method):

        if not self.allows_filters(path, method):
            return []

        if hasattr(self.view, 'filter_set_dict'):
            filter_set_class = self.view.get_filter_set_class()
            return filter_set_class.get_schema_operation_parameters()
        else:
            return []

    # def get_request_serializer(self, path, method):
    #     return self._get_serializer(
    #         path, method, 'request')

    # def get_response_serializer(self, path, method):
    #     return self._get_serializer(
    #         path, method, 'response')

    def get_request_body(self, path, method):
        """
        Need to override get_serializer
        """
        if method not in ('PUT', 'PATCH', 'POST'):
            return {}

        self.request_media_types = self.map_parsers(path, method)

        serializer = self._get_serializer(
            path, method, 'request')

        if not isinstance(serializer, serializers.Serializer):
            item_schema = {}
        else:
            item_schema = self._get_reference(serializer)
        return {
            'content': {
                ct: {'schema': item_schema}
                for ct in self.request_media_types
            }
        }

    def get_responses(self, path, method):
        """
        Need to override get_serializer
        """
        if method == 'DELETE':
            return {
                '204': {
                    'description': ''
                }
            }

        self.response_media_types = self.map_renderers(path, method)

        serializer = self._get_serializer(
            path, method, 'response')

        if not isinstance(serializer, serializers.Serializer):
            item_schema = {}
        else:
            item_schema = self._get_reference(serializer)

        if is_list_view(path, method, self.view):
            response_schema = {
                'type': 'array',
                'items': item_schema,
            }
            paginator = self.get_paginator()
            if paginator:
                response_schema = paginator.get_paginated_response_schema(
                    response_schema)
        else:
            response_schema = item_schema
        status_code = '201' if method == 'POST' else '200'

        return {
            status_code: {
                'content': {
                    ct: {'schema': response_schema}
                    for ct in self.response_media_types
                },
                # description is a mandatory property,
                # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#responseObject
                # TODO: put something meaningful into it
                'description': ""
            }
        }

    def _get_serializer(self, path, method, type_=''):
        view = self.view

        # BaseViewSet checker
        if not hasattr(view, 'serializer_alias_dict'):
            return super().get_serializer(path, method)
        else:
            try:
                serializer_class = view.get_serializer_class(type_)
                return serializer_class()
            except exceptions.APIException:
                warnings.warn('{}.get_serializer() raised an exception during '
                              'schema generation. Serializer fields will not be '
                              'generated for {} {}.'
                              .format(view.__class__.__name__, method, path))
                return None

    def get_operation_id(self, path, method):
        """
        Needed to avoid warning for operation ID
        """
        method_name = getattr(self.view, 'action', method.lower())
        if is_list_view(path, method, self.view):
            action = 'list'
        elif method_name not in self.method_mapping:
            action = self._to_camel_case(method_name)
        else:
            action = self.method_mapping[method.lower()]

        name = self.view.__class__.__name__

        return action + name

    def map_field(self, field):

        if isinstance(field, serializers.BaseField):
            return field.get_default_schema()

        return super().map_field(field)

    def map_serializer(self, serializer):
        """
        Needed to override
        """
        # Assuming we have a valid serializer instance.
        required = []
        properties = {}
        

        for field in serializer.fields.values():
            if isinstance(field, serializers.HiddenField):
                continue

            if field.required:
                required.append(field.field_name)

            schema: Dict[str, Any] = self.map_field(field)
            if field.read_only:
                schema['readOnly'] = True
            if field.write_only:
                schema['writeOnly'] = True
            if field.allow_null:
                schema['nullable'] = True

            super_class_default_cond = field.default is not None and field.default != empty and not callable(field.default)
            custom_cond = not isinstance(field, serializers.BaseField)

            if super_class_default_cond and custom_cond:
                schema['default'] = field.default
            if field.help_text:
                schema['description'] = str(field.help_text)
            self.map_field_validators(field, schema)

            properties[field.field_name] = schema

        result = {
            'type': 'object',
            'properties': properties
        }
        if required:
            result['required'] = required

        return result
