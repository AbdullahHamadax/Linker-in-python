def parse_object_file(filename):
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
        elif in_sym_section and line:
            parts = line.split()
            if len(parts) == 2:
                symbol_name, symbol_address = parts
                symbols[symbol_name] = int(symbol_address)
        elif not in_sym_section and line:
            code.append(line)  

    return code, symbols