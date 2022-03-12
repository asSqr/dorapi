from commons import exceptions
from commons.use_case import BaseUseCase
from dorapi.models import MUser, MGadget


class GetMGadget(BaseUseCase):

    mgadget_class = MGadget

    def execute(self, muser: MUser, id_: str):

        mgadget = self.mgadget_class.objects.get_by_id(id_)

        if mgadget is None:
            raise exceptions.NotFound({'id': 'Not found'})

        return mgadget
