from django.db import models


class SoftManager(models.Manager):

    def get_queryset(self):
        return self._queryset_class(model=self.model, using=self._db, hints=self._hints).filter(deleted_at=None)
