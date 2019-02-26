from copy import copy

class CaughtException(Exception):
    pass

def move(state):
    if state is None:
        return None
    pos, d, size = state
    pos += d
    if pos < 0:
        return 1, 1, size
    if pos >= size:
        return size-2, -1, size
    return pos, d, size

def cost(packet, firewall):
    for layer, state in enumerate(firewall):
        if state is not None and state[0] == 0 and packet == layer:
            return state[2] * layer
    return 0

def caught(packet, firewall):
    for layer, state in enumerate(firewall):
        if state is not None and state[0] == 0 and packet == layer:
            return True
    return False

def read_data(filename="data/input13.data"):
    with open(filename) as f:
        return f.read().splitlines()

def from_data(lines):
    size = int(lines[-1].split(": ")[0])
    firewall = [None] * (size+1)
    for line in lines:
        layer, depth = [int(n) for n in line.split(": ")]
        firewall[layer] = (0, 1, depth)
    return firewall, size

if __name__ == "__main__":
    lines = read_data()

    firewall, size = from_data(lines)

    packet = -1
    total_cost = 0
    while packet <= size:
        packet += 1
        total_cost += cost(packet, firewall)
        firewall = [move(i) for i in firewall]

    print(total_cost)

    # Part 2
    fw, size = from_data(lines)
    delay = 1
    while True:
        fw = [move(i) for i in fw]

        firewall = copy(fw)

        packet = -1
        try:
            while packet <= size:
                packet += 1
                if caught(packet, firewall):
                    raise CaughtException
                firewall = [move(i) for i in firewall]
        except CaughtException:
            delay += 1
            continue

        break

    print(delay)
