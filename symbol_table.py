"""This is the SymbolTable class"""


class SymbolTable:
    """This is a doctring to improve our code quality """
    def __init__(self):
        """This is a doctring to improve our code quality """
        self.symbols = {}

    def add_symbol(self, name, address):
        """This is a doctring to improve our code quality """
        self.symbols[name] = address

    def resolve(self, name):
        """This is a doctring to improve our code quality """
        return self.symbols.get(name, None)

    def _str_(self):
        """This is a doctring to improve our code quality """
        return str(self.symbols)
