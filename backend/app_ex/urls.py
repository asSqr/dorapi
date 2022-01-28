from rest_framework import permissions
from django.urls import path
from django.views.generic.base import TemplateView
from rest_framework.schemas.views import SchemaView
from .schema_generator import SchemaGenerator


urlpatterns = [
    path('openapi-schema/', SchemaView.as_view(
        renderer_classes=None,
        schema_generator=SchemaGenerator(
            title='AlphaHatchu',
            url=None,
            description=None,
            urlconf=None,
            patterns=None,
            version='2.0.0',
        ),
        public=True,
        authentication_classes=(),
        permission_classes=(permissions.AllowAny,),
    ), name='openapi-schema'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
