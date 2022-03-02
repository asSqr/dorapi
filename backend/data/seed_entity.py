from django.db import transaction

from seeds import (
    SeedMBook,
    SeedMGadget,
    SeedGadgetBook,
)

with transaction.atomic():
    mbooks = SeedMBook().create()
    print(f'created {len(mbooks)} books')

    mgadgets = SeedMGadget().create()
    print(f'created {len(mgadgets)} mgadgets')

    gadget_books = SeedGadgetBook(mgadgets, mbooks).create()
    print(f'created {len(gadget_books)} gadget_books')
