class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, address):
        self.symbols[name] = address

    def resolve(self, name):
        return self.symbols.get(name, None)

    def _str_(self):
        return str(self.symbols)
