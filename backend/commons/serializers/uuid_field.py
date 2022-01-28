from rest_framework import serializers

from django.db import models
from commons.models import BaseModel


class UUIDField(serializers.UUIDField):

    def to_representation(self, value):

        if isinstance(value, str):
            return value
        elif isinstance(value, models.UUIDField):
            return str(value)
        elif isinstance(value, BaseModel):
            return str(value.id)
        elif self.uuid_format == 'hex_verbose':
            return str(value)
        else:
            return getattr(value, self.uuid_format)
