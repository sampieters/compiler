from collections import defaultdict
from copy import copy

class SymbolTable:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = defaultdict(lambda: None)

    def get_symbol(self, symbol):
        """
        Returns the Node corresponding to a symbol of the smallest scope possible
        Returns None f the symbol was not previously declared
        @params: symbol = String
        """
        table = self
        result = None
        while result is None and table is not None:
            if symbol in table.symbols:
                result = table.symbols[symbol]
            table = table.parent
        return result

    def get_symbol_curr_scope(self, symbol):
        print("get_symbol_curr_scope")
        try:
            return self.symbols[symbol]
        except KeyError:
            return None

    def add_symbol(self, symbol):
        """
        Adds a symbol to the symbol table
        @params: symbol = IdentifierNode or FunctionNode
        """
        print("add_symbol", symbol)
        self.symbols[symbol.name] = symbol

    def enter_scope(self):
        print("enter_scope")
        self.parent = copy(self)
        self.symbols = defaultdict()

    def exit_scope(self):
        print("exit_scope")
        if self.parent:
            self.symbols = self.parent.symbols
            self.parent = self.parent.parent
        else:
            self.symbols = None
            self.parent = None

    def __str__(self):
        return "\n".join([f"{symbol}: {self.symbols[symbol]}" for symbol in self.symbols])
