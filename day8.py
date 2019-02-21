from collections import defaultdict
import re

def read_data(filename="data/input8.data"):
    with open(filename) as f:
        return f.read().splitlines()

def conditional(c, reg, comp, val):
    regval = c.get(reg, 0)
    return eval(f"{regval}{comp}{val}")

if __name__ == "__main__":
    lines = read_data()

    reg = defaultdict(int)

    for line in lines:
        # eb inc -915 if wf != 0
        match = re.search(r'([a-z]+)\s+(inc|dec)\s+(-?\d+)\s+if\s+([a-z]+)\s+([><!=]+)\s+(-?\d+)', line)
        assert match

        reg1 = match.group(1)
        op = match.group(2)
        val1 = int(match.group(3))
        reg2 = match.group(4)
        comp = match.group(5)
        val2 = int(match.group(6))

        if conditional(reg, reg2, comp, val2):
            if op == "inc":
                reg[reg1] += val1
            else:
                reg[reg1] -= val1

    key = max(reg, key=reg.get)
    print(f"{key}: {reg[key]}")