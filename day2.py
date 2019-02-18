import re

def read_data(filename="data/input2.data"):
    with open(filename) as f:
        return [
            [int(n) for n in re.findall(r"-?\d+", l)]
            for l in f.read().splitlines()
        ]

if __name__ == "__main__":
    d = read_data()

    total = 0
    for row in d:
        total += max(row) - min(row)

    print(total)