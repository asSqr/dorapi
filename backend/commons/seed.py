from typing import Any
from abc import ABC, abstractmethod


class Seed(ABC):

    @abstractmethod
    def create(self) -> Any:
        """create and return object list that was created"""
