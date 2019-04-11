"""
Helper tool for day23 and similar tasks -- do some jump annotations
as a starting point for disassembly.
"""

def read_data(filename="data/input23.data"):
    with open(filename) as f:
        return f.read().splitlines()


def parse_data(lines):
    code = []
    regs = {}
    for line in lines:
        (op, arg1, arg2) = line.split(" ")
        try:
            arg1 = int(arg1)
        except ValueError:
            regs[arg1] = 0
        try:
            arg2 = int(arg2)
        except ValueError:
            regs[arg2] = 0
        code.append((op, arg1, arg2))

    return code, regs


class Machine:
    def __init__(self, lines):
        self.code, self.regs = parse_data(lines)
        self.ip = 0
        self.muls = 0
        self.labels = {}
        self.statements = []
        self.label_id = 1

    def iset(self, arg1, arg2):
        self.statements.append(f"{arg1} = {arg2}")

    def ijnz(self, arg1, arg2):
        jump_to = self.ip + arg2
        if jump_to not in self.labels:
            label = f"L{self.label_id}"
            self.label_id += 1
            self.labels[jump_to] = label
        else:
            label = self.labels[jump_to]

        cmp = f"{arg1} != 0"

        if cmp == "1 != 0":
            self.statements.append(f"GOTO {label}")
        else:
            self.statements.append(f"IF {arg1} != 0: GOTO {label}")


    def imul(self, arg1, arg2):
        self.statements.append(f"{arg1} *= {arg2}")

    def isub(self, arg1, arg2):
        self.statements.append(f"{arg1} -= {arg2}")

    def compile(self):
        for self.ip, op in enumerate(self.code):
            getattr(self, f"i{op[0]}")(op[1], op[2])

        for self.ip, line in enumerate(self.statements):
            op = f"{self.code[self.ip]}"
            op = op.replace("(", "")
            op = op.replace("'", "")
            op = op.replace(")", "")
            op = op.replace(",", "")

            l = ""
            if self.ip in self.labels:
                l = self.labels[self.ip]
            elif line.startswith("IF") or line.startswith("GOTO"):
                l = line
            print("{0:>2}: {1:<17} {2:<18}".format(self.ip, op, l))

if __name__ == "__main__":
    machine = Machine(read_data())

    machine.compile()
