def read_data(filename="data/input4.data"):
    with open(filename) as f:
        return [l.split(" ") for l in f.read().splitlines()]

if __name__ == "__main__":
    data = read_data()

    count = 0
    for l in data:
        if len(set(l)) == len(l):
            count += 1

    print(count)