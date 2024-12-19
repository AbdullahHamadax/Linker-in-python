"""This is the utils class"""


def parse_object_file(filename):
    """This is a doctring to improve our code quality """
    with open(filename, 'r') as f:
        lines = f.readlines()

    code = []
    symbols = {}
    in_sym_section = False

    for line in lines:
        line = line.strip()

        if line.startswith("SYM"):
            in_sym_section = True
            continue

        if in_sym_section and line:
            parts = line.split()
            if len(parts) == 2:
                symbol_name, symbol_address = parts

                try:
                    if symbol_address.startswith(("0x", "0X")):
                        address = int(symbol_address, 16)
                    else:
                        address = int(symbol_address)
                    symbols[symbol_name] = address
                except ValueError:
                    print(f"Warning: Could not parse symbol address '{symbol_address}'")
        elif not in_sym_section and line:
            code.append(line)

    return code, symbols
