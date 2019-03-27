from collections import deque

def read_data(filename="data/input18.data"):
    with open(filename) as f:
        return f.read().splitlines()

def parse_data(lines):
    data = [line.split(" ") for line in lines]
    for instr in data:
        try:
            instr[1] = int(instr[1])
        except (ValueError, IndexError):
            pass
        try:
            instr[2] = int(instr[2])
        except (ValueError, IndexError):
            pass

    return data

class ProgramTerminated(Exception):
    pass

class Machine:
    def __init__(self, pid, instructions):
        self.pid = pid
        self.data = instructions
        self.regs = {}
        self.ip = 0
        self.snd = -1
        self.receive_buffer = deque([])
        self.other = None
        self.send_count = 0
        self.blocked = False
        self.terminated = False

        for instr in self.data:
            if isinstance(instr[1], int):
                continue
            self.regs[instr[1]] = 0

        self.regs["p"] = pid  # part 2

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

    def isnd(self, instr):
        reg = instr[0]
        self.other.receive_buffer.append(self.regs[reg])
        self.ip += 1
        self.send_count += 1

    def ircv(self, instr):
        reg = instr[0]
        if len(self.receive_buffer):
            data = self.receive_buffer.popleft()
            self.regs[reg] = data
            self.ip += 1
            self.blocked = False
        else:
            self.blocked = True

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

    def step(self):
        if self.terminated:
            return

        if self.ip < 0 or self.ip >= len(self.data):
            self.terminated = True
            return

        instr = self.data[self.ip]
        getattr(self, f"i{instr[0]}")(instr[1:])


if __name__ == "__main__":

    data = read_data()
    instr = parse_data(data)

    m0 = Machine(0, instr)
    m1 = Machine(1, instr)

    m0.other = m1
    m1.other = m0

    while True:
        m0.step()
        m1.step()

        if m0.terminated and m1.terminated:
            print("Terminated normally")
            break

        if m0.blocked and m1.blocked:
            print("Deadlock detected")
            break

    print(m1.send_count)
