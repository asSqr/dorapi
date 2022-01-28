from rest_framework.schemas import openapi


class SchemaGenerator(openapi.SchemaGenerator):
    """
    SchemaGenerator
    https://github.com/encode/django-rest-framework/blob/master/rest_framework/schemas/openapi.py
    """

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)

        schema['components']['securitySchemes'] = self.get_secutiry_schemes()

        return schema

    def get_secutiry_schemes(self, request=None, public=False):
        schemes = {}

        paths, view_endpoints = self._get_paths_and_endpoints(request)
        if not paths:
            return schemes

        self._set_security_schemes_from_views(view_endpoints, schemes)
        self._set_security_schemes_from_headers(schemes)

        return schemes

    def _set_security_schemes_from_headers(self, schemes):
        pass

    def _set_security_schemes_from_views(self, view_endpoints, schemes):

        for _, _, view in view_endpoints:
            for auth_class in view.authentication_classes:
                if hasattr(auth_class, 'security_schema'):
                    schemes.update(auth_class.security_schema)
