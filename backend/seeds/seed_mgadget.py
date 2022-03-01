from dataclasses import dataclass
from typing import List
from dorapi.models import MGadget, MBook
from .dora_superdatabase import superdatabase_datas
from commons.seed import Seed


@dataclass
class SeedMGadget(Seed):

    def create(self):
        gadget_datas = superdatabase_datas
                
        gadgets = []
        
        for gadget_data in gadget_datas:
            mgadget = MGadget(gadget_data)
            
            for mbook in gadget.books:
                mgadget.mbook = mbook

                gadgets.append(mgadget)
        
        mgadgets = MGadget.objects.bulk_create(gadgets)
        
        return mgadgets
