from .base_filterset import BaseFilterSet


class BlankFilterSet(BaseFilterSet):
    pass

    @classmethod
    def get_schema_operation_parameters(cls):
        return []
