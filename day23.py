import sys

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

    def iset(self, arg1, arg2):
        if isinstance(arg2, int):
            v = arg2
        else:
            v = self.regs[arg2]
        self.regs[arg1] = v
        self.ip += 1

    def ijnz(self, arg1, arg2):
        if isinstance(arg1, int):
            cmp = arg1
        else:
            cmp = self.regs[arg1]
        if cmp == 0:
            self.ip += 1
            return
        if isinstance(arg2, int):
            v = arg2
        else:
            v = self.regs[arg2]

        self.ip += v


    def imul(self, arg1, arg2):
        if isinstance(arg2, int):
            v = arg2
        else:
            v = self.regs[arg2]
        self.regs[arg1] *= v
        self.ip += 1


    def isub(self, arg1, arg2):
        if isinstance(arg2, int):
            v = arg2
        else:
            v = self.regs[arg2]
        self.regs[arg1] -= v
        self.ip += 1

    def exec(self):
        while True:
            try:
                op = self.code[self.ip]
            except IndexError:
                break
            getattr(self, f"i{op[0]}")(op[1], op[2])
            if op[0] == "mul":
                self.muls += 1


if __name__ == "__main__":
    machine = Machine(read_data())
    machine.exec()
    print(machine.muls)
