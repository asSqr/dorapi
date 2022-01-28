from enum import Enum


class MUserTypeEnum(Enum):
    admin = 0
    machine = 1
    user = 2

    @classmethod
    def choices(cls):
        return tuple((c.value, c.name) for c in cls)
