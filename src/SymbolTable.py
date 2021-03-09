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
        table = self
        result = None
        while result is None and table is not None:
            result = table[symbol]
            table = table.parent
        return result

    def add_symbol(self, symbol):
        """
        Adds a symbol to the symbol table
        @params: symbol = IdentifierNode
        """
<<<<<<< HEAD
        self.symbols[symbol.name] = symbol

    
    def enter_scope(self):
        self.parent = self
        self.symbols = dict()


    def exit_scope(self):
        if (self.parent)
            self.symbols = self.parent.symbols
            self.parent = self.parent.parent
        else:
            self.symbols = None
            self.parent = None
=======
        if self.symbols[symbol.name]:
            print("Warning: shadow declaration")
        self.symbols[symbol.name] = symbol
>>>>>>> ab5bc4a0f054e69c21a7b294e589bec0744478b4
