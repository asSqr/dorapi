from dataclasses import dataclass, asdict
from dorapi.models import MGadget
from .dora_superdatabase import superdatabase_datas
from commons.seed import Seed
from typing import List
from .utils import gadget_to_mgadget

@dataclass
class SeedMGadget(Seed):

    def create(self) -> List[MGadget]:
        gadgets = superdatabase_datas
        mgadgets = []
        
        for gadget in gadgets:
            mgadget = gadget_to_mgadget(gadget)
            
            mgadgets.append(mgadget)
        
        mgadgets = MGadget.objects.bulk_create(mgadgets)
        
        return mgadgets
