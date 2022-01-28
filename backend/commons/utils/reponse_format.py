from dataclasses import dataclass
from typing import List, Any
from types import SimpleNamespace

from commons.models import BaseModel

def attr_dict_to_object(obj: BaseModel, attrs: List[str]) -> BaseModel:
    for attr in attrs:
        assert isinstance(getattr(obj, attr), dict), f'{obj.__class__.__name__} attribute: {attr} is not a Dict'
        setattr(obj, attr, SimpleNamespace(**getattr(obj, attr)))
    return obj

class ResponseFormat:

    @classmethod
    def format(cls, obj: Any) -> Any:
        if isinstance(obj, list):
            return cls.format_queryset(obj)
        else:
            return cls.format_obj(obj)

    @classmethod
    def format_obj(cls, obj: BaseModel) -> BaseModel:
        fields = [k for k, v in vars(obj).items() if isinstance(v, dict) and v]
        return attr_dict_to_object(obj, fields)

    @classmethod
    def format_queryset(cls, obj_list: List[BaseModel]) -> List[BaseModel]:
        if not len(obj_list):
            return []
        
        x = obj_list[0]
        fields = [k for k, v in vars(x).items() if isinstance(v, dict) and v]

        return [attr_dict_to_object(obj, fields) for obj in obj_list]

