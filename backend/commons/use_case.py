from django.db import models
from dataclasses import dataclass
from abc import ABC, abstractmethod


class BaseUseCase(ABC):

    main_class: models.Model

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        create a running function
        """
