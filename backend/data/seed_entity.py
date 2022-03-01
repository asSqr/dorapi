from django.db import transaction

from seeds import (
    SeedMBook,
    SeedMGadget,
)

with transaction.atomic():
    # stocks
    mbooks = SeedMBook().create()
    print(f'created {len(mbooks)} books')

    mgadgets = SeedMGadget().create()
    print(f'created {len(mgadgets)} mgadgets')
