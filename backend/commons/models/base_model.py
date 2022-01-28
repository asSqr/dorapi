from datetime import datetime, timedelta
import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        super().delete()
