from dataclasses import dataclass
from dorapi.models import MGadget
from .gadgets.dora_superdatabase import superdatabase_datas as gadget_superdatabase_datas
from .gadgets.utils import gadget_to_mgadget
from commons.seed import Seed
from typing import List

@dataclass
class SeedMGadget(Seed):

    def create(self) -> List[MGadget]:
        gadgets = gadget_superdatabase_datas
        mgadgets = []
        
        for gadget in gadgets:
            mgadget = gadget_to_mgadget(gadget)
            
            mgadgets.append(mgadget)
        
        mgadgets = MGadget.objects.bulk_create(mgadgets)
        
        return mgadgets
