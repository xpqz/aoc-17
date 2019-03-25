def read_data(filename="data/input18.data"):
    with open(filename) as f:
        return f.read().splitlines()

def parse_data(lines):
    data = [line.split(" ") for line in lines]
    for instr in data:
        try:
            instr[2] = int(instr[2])
        except (ValueError, IndexError):
            pass
    return data

class ProgramTerminated(Exception):
    pass

class Machine:
    def __init__(self, instructions):
        self.data = instructions
        self.regs = {}
        self.ip = 0
        self.snd = -1

        for instr in self.data:
            self.regs[instr[1]] = 0

    def iset(self, instr):
        (reg, opr) = instr
        if isinstance(opr, int):
            self.regs[reg] = opr
        else:
            self.regs[reg] = self.regs[opr]
        self.ip += 1

    def imul(self, instr):
        (reg, opr) = instr
        if isinstance(opr, int):
            self.regs[reg] *= opr
        else:
            self.regs[reg] *= self.regs[opr]
        self.ip += 1

    def iadd(self, instr):
        (reg, opr) = instr
        if isinstance(opr, int):
            self.regs[reg] += opr
        else:
            self.regs[reg] += self.regs[opr]
        self.ip += 1

    def imod(self, instr):
        (reg, opr) = instr
        if isinstance(opr, int):
            self.regs[reg] %= opr
        else:
            self.regs[reg] %= self.regs[opr]
        self.ip += 1

    def isnd(self, opr):
        if isinstance(opr[0], int):
            self.snd = opr[0]
        else:
            self.snd = self.regs[opr[0]]
        self.ip += 1

    def ircv(self, opr):
        if isinstance(opr[0], int):
            if opr[0] != 0:
                raise ProgramTerminated
        elif self.regs[opr[0]] != 0:
            raise ProgramTerminated
        self.ip += 1

    def ijgz(self, instr):
        (reg_or_val1, reg_or_val2) = instr
        if isinstance(reg_or_val1, int):
            cnd = reg_or_val1
        else:
            cnd = self.regs[reg_or_val1]

        if cnd > 0:
            if isinstance(reg_or_val2, int):
                offset = reg_or_val2
            else:
                offset = self.regs[reg_or_val2]

            self.ip += offset
        else:
            self.ip += 1

    def execute(self):
        try:
            while self.ip >= 0 and self.ip < len(self.data):
                instr = self.data[self.ip]
                # print(self.ip, instr, self.snd)
                getattr(self, f"i{instr[0]}")(instr[1:])
        except ProgramTerminated:
            return self.snd

if __name__ == "__main__":

    data = read_data()
    # data = [
    #     "set a 1",
    #     "add a 2",
    #     "mul a a",
    #     "mod a 5",
    #     "snd a",
    #     "set a 0",
    #     "rcv a",
    #     "jgz a -1",
    #     "set a 1",
    #     "jgz a -2",
    # ]
    machine = Machine(parse_data(data))

    d = machine.execute()

    print(d)
