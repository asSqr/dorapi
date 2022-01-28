from django.db import models
from datetime import datetime


class QuerySet(models.QuerySet):

    def as_soft_manager(cls):
        from .manager import SoftManager
        manager = SoftManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager

    as_soft_manager.queryset_only = True
    as_soft_manager = classmethod(as_soft_manager)  # type: ignore

    def delete(self):
        deleted_at = datetime.now()
        objs = list(self)
        for obj in objs:
            obj.deleted_at = deleted_at

        self.bulk_update(objs, ['deleted_at'])
        return objs
