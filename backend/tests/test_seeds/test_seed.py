from seeds import (
    SeedMBook,
    SeedMGadget,
    SeedGadgetBook,
)


class TestSeed:
    
    def setUp(self):

        self.mbooks = SeedMBook().create()
        print(f'created {len(self.mbooks)} mbooks')

        self.mgadgets = SeedMGadget().create()
        print(f'created {len(self.mgadgets)} mgadgets')

        self.gadget_books = SeedGadgetBook(self.mgadgets, self.mbooks).create()
        print(f'created {len(self.gadget_books)} gadget_books')
