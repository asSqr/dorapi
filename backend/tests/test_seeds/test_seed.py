from seeds import (
    SeedMBook,
    SeedMGadget,
    SeedGadgetBook,
    SeedGadgetLink,
)


class TestSeed:
    
    def setUp(self):

        self.mbooks = SeedMBook().create()
        
        self.mgadgets = SeedMGadget().create()
        
        self.gadget_books = SeedGadgetBook(self.mgadgets, self.mbooks).create()
        
        self.gadget_links = SeedGadgetLink(self.mgadgets).create()
