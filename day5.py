import re

def read_data(filename="data/input5.data"):
    with open(filename) as f:
        return [int(l) for l in f.read().splitlines()]


if __name__ == "__main__":
    data = read_data()
    ip = 0
    count = 0
    while ip < len(data):
        # fetch
        jmp = data[ip]

        # modify
        data[ip] += 1

        ip = ip + jmp
        count += 1

    print(count)

    # Part 2
    data = read_data()
    ip = 0
    count = 0
    while ip < len(data):
        # fetch
        jmp = data[ip]

        if jmp >= 3:
            data[ip] -= 1
        else:
            data[ip] += 1

        ip = ip + jmp
        count += 1

    print(count)
