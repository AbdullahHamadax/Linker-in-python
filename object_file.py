class ObjectFile:
    def __init__(self, name, code, symbols):
        self.name = name
        self.code = code
        self.symbols = symbols

    def __str__(self):
        return f"ObjectFile(name={self.name}, symbols={self.symbols})"