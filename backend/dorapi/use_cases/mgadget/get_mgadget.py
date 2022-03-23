from commons import exceptions
from commons.use_case import BaseUseCase
from dorapi.models import MUser, MGadget, GadgetLink


class GetMGadget(BaseUseCase):

    mgadget_class = MGadget
    gadgetlink_class = GadgetLink

    def execute(self, muser: MUser, id_: str):

        mgadget = self.mgadget_class.objects.get_by_id(id_)

        if mgadget is None:
            raise exceptions.NotFound({'id': 'Not found'})
        
        gadgetlinks = self.gadgetlink_class.objects.filter_eq_mgadget(mgadget)

        mgadget.links = gadgetlinks

        return mgadget
