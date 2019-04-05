def read_data(filename="data/input22.data"):
    with open(filename) as f:
        return f.read().splitlines()

def parse_data(lines):
    data = {}
    for y, line in enumerate(lines):
        for x, item in enumerate(line):
            if item == "#":
                data[x, y] = True
    return data, x, y

def move(infected, pos):
    (x, y, direction) = pos
    right = {"N": "E", "E": "S", "S": "W", "W": "N"}
    left = {"N": "W", "W": "S", "S": "E", "E": "N"}
    delta = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

    if infected.get((x, y), False):
        new_dir = right[direction]
        infected.pop((x, y))
    else:
        new_dir = left[direction]
        infected[x, y] = True

    d = delta[new_dir]

    return (x + d[0], y + d[1], new_dir), infected.get((x, y), False)


if __name__ == "__main__":
    infection_status, xmax, ymax = parse_data(read_data())

    pos = (xmax//2, ymax//2, "N")
    total = 0
    for _burst in range(10000):
        pos, infected = move(infection_status, pos)
        if infected:
            total += 1

    print(total)
