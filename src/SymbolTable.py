class SymbolTable:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = dict()


    def get_symbol(self, symbol):
        """
        Returns the Node corresponding to a symbol of the smallest scope possible
        Returns None f the symbol was not previously declared
        @params: symbol = String
        """



    def add_symbol(self, symbol):
        """
        Adds a symbol to the symbol table
        @params: symbol = IdentifierNode
        """
        if self.symbols[symbol.name]:
            print("Warning: shadow declaration")
        self.symbols[symbol.name] = symbol