
import re
import json


class Turing:

    def __init__(self):
        self.tape = {}
        self.cursor = 0
        self.state = 'A'
        self.steps = 0
        self.state_transitions = {}

    def get(self):
        return self.tape.get(self.cursor, 0)

    def set(self, value):
        self.tape[self.cursor] = value

    def move(self, step):
        self.cursor += step

    def checksum(self):
        return sum(list(self.tape.values()))

    def exec(self, opcode):
        value, move, state = opcode
        self.set(value)
        self.move(move)
        self.state = state
        self.steps += 1

    def run(self, halt):
        while self.steps < halt:
            self.exec(self.state_transitions[self.state][self.get()])

    def compile(self, lines):
        """
        [trigger, (value, move, state), (value, move, state)]
        """
        program = []
        current_op = []
        for line in lines:
            match = re.search(r'In state (A|B|C|D|E|F)', line)
            if match:
                trigger = match.group(1)
                if current_op:
                    program.append(current_op)
                current_op = [trigger]
                continue
            match = re.search(r'If the current value is (0|1)', line)
            if match:
                continue  # assume both conds are present with 0 before 1
            match = re.search(r'- Write the value (0|1)', line)
            if match:
                value = int(match.group(1))
                continue
            match = re.search(r'- Move one slot to the (left|right)', line)
            if match:
                move = -1 if match.group(1) == "left" else 1
                continue
            match = re.search(r'- Continue with state (A|B|C|D|E|F)', line)
            if match:
                state = match.group(1)
                current_op.append((value, move, state))

        program.append(current_op)
        self.state_transitions = {
            instruction[0]: [instruction[1], instruction[2]]
            for instruction in program
        }


def read_program(filename="input25.data"):
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == "__main__":

    data = read_program()

    machine = Turing()

    machine.compile(data)

    machine.run(12919244)

    print(machine.checksum())
