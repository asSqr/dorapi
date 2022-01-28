import random
import string
from typing import Optional, List

from dorapi.enums import MUserTypeEnum
from django.db import models
from commons.models import BaseModel, QuerySet


def random_char():
    return ''.join(random.choice(string.ascii_letters) for x in range(10))


class MUserQuerySet(QuerySet):

    def get_by_id(self, id_: str) -> Optional['MUser']:
        try:
            return self.get(id=id_)
        except MUser.DoesNotExist:
            return None

    def get_by_sub(self, sub: str) -> Optional['MUser']:
        try:
            return self.get(sub=sub)
        except MUser.DoesNotExist:
            return None

    def filter_id_in(self, id_list: List[str]) -> 'MUserQuerySet':
        return self.filter(id__in=id_list)

    def filter_eq_mcompany(self, id_: str) -> 'MUserQuerySet':
        return self.filter(mcompany=id_)

    def filter_eq_mwarehouse(self, id_: str) -> 'MUserQuerySet':
        return self.filter(mwarehouse=id_)

    def filter_eq_id(self, id_: str) -> 'MUserQuerySet':
        return self.filter(id=id_)

    def filter_eq_email(self, email: str) -> 'MUserQuerySet':
        return self.filter(email=email)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class MUser(BaseModel):
    sub = models.CharField(max_length=8192, unique=True, default=random_char)
    name = models.CharField(max_length=8192, blank=True)
    email = models.CharField(max_length=8192)
    authority = models.IntegerField()
    active = models.BooleanField(default=True)
    type = models.IntegerField(
        choices=MUserTypeEnum.choices(), default=MUserTypeEnum.user.value)

    class META:
        unique_together = ('email')

    USERNAME_FIELD = 'sub'
    REQUIRED_FIELDS: List[str] = []

    objects = MUserQuerySet.as_soft_manager()
    object_all = MUserQuerySet.as_manager()

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_machine(self):
        return self.type == MUserTypeEnum.machine.value

    @property
    def is_active(self):
        return self.active

    def log_error_info(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
        }
