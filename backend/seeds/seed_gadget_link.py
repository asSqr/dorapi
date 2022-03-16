from dataclasses import dataclass
from dorapi.models import MGadget, GadgetLink
from commons.seed import Seed
from typing import List
from .gadgets.utils import (
    generate_mgadget_key,
)
from .gadgets.dora_superdatabase import link_datas


@dataclass
class SeedGadgetLink(Seed):

    mgadgets: List[MGadget]

    def create(self) -> List[GadgetLink]:

        mgadget_dict = {}
        gadget_links = []

        for mgadget in self.mgadgets:
            gadget_key = generate_mgadget_key(mgadget)
            mgadget_dict[gadget_key] = mgadget

        for link in link_datas:
            from_key = generate_mgadget_key(link.from_gadget_href)
            to_key = generate_mgadget_key(link.to_gadget_href)
            
            from_mgadget = mgadget_dict[from_key]
            to_mgadget = mgadget_dict[to_key]
            
            gadget_links.append(GadgetLink(
                from_mgadget=from_mgadget,
                to_mgadget=to_mgadget,
                begin_index=link.begin_index,
                end_index=link.end_index,
            ))

        gadget_links = GadgetLink.objects.bulk_create(gadget_links)

        return gadget_links
