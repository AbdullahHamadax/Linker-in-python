"""This is the Object file class"""


class ObjectFile:
    """This is a doctring to improve our code quality """

    def __init__(self, name, code, symbols):
        """This is a doctring to improve our code quality """
        self.name = name
        self.code = code
        self.symbols = symbols

    def __str__(self):
        """This is a doctring to improve our code quality """
        return f"ObjectFile(name={self.name}, symbols={self.symbols})"
