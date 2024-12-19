"""This is the Linker class implementation
it contains methods necessary for the linking process """


import os
from symbol_table import SymbolTable
from object_file import ObjectFile
from utils import parse_object_file


class Linker:
    """This is a doctring to improve our code quality """

    def __init__(self):
        """This is a doctring to improve our code quality """
        self.symbol_table = SymbolTable()
        self.linked_code = []

    def load_object_file(self, filename):
        """This is a doctring to improve our code quality """
        code, symbols = parse_object_file(filename)
        obj_file = ObjectFile(filename, code, symbols)
        for symbol, address in obj_file.symbols.items():
            self.symbol_table.add_symbol(symbol, address)
        return obj_file

    def link(self, object_files):
        """This is a doctring to improve our code quality """
        for obj_file in object_files:
            for line in obj_file.code:
                resolved_line = self.resolve_symbols(line)
                self.linked_code.append(resolved_line)
        return self.linked_code

    def resolve_symbols(self, line):
        """This is a doctring to improve our code quality """
        for symbol, address in self.symbol_table.symbols.items():
            line = line.replace(symbol, str(address))
        return line

    def save_output(self, output_filename):
        """This is a doctring to improve our code quality """
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        with open(output_filename, 'w') as f:
            for line in self.linked_code:
                f.write(line + '\n')
