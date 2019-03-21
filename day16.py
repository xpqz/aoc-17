import re

class UnknownInstructionException(Exception):
    pass

def read_data(filename="data/input16.data"):
    with open(filename) as f:
        return f.read().split(",")

def spin(state, count):
    return state[-count:] + state[:-count]

def exchange(state, p1, p2):
    d = list(state)
    d[p1], d[p2] = d[p2], d[p1]
    return "".join(d)

def partner(state, name1, name2):
    return exchange(state, state.index(name1), state.index(name2))

def is_sublist(a, b):
    return [(i, i+len(b)) for i in range(len(a)) if a[i:i+len(b)] == b]

def execute(state, instr):
    m = re.search(r'x(\d+)/(\d+)', i)
    if m:
        return exchange(state, int(m.group(1)), int(m.group(2)))

    m = re.search(r's(\d+)', i)
    if m:
        return spin(state, int(m.group(1)))

    m = re.search(r'p(.)/(.)', i)
    if m:
        return partner(state, m.group(1), m.group(2))

    raise UnknownInstructionException

if __name__ == "__main__":
    instr = read_data()
    state = "abcdefghijklmnop"

    for i in instr:
        state = execute(state, i)

    print(state)

    # A beeeellion iterations is obviously too much to brute, so we look for
    # recurring patterns instead. End-of-dance state quickly recurs. The value
    # at 100 is the value at 1_000 is the value at 1_000_000_000...

    for _ in range(2, 101):
        for i in instr:
            state = execute(state, i)

    print(state)
