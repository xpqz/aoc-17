from itertools import cycle
import re


def read_data(filename="data/input6.data"):
    with open(filename) as f:
        return [int(n) for n in re.findall(r"-?\d+", f.read())]


def maxindex(data):
    m = data[0], 0
    for i in range(len(data)):
        if data[i] > m[0]:
            m = data[i], i

    return m

def bank_order(dlen, pivot):
    spread = list(range(dlen))
    if pivot == dlen:
        return spread
    return spread[pivot+1:] + spread[:pivot+1]

if __name__ == "__main__":
    d = read_data()

    count = 0
    states = {tuple(d)}
    while True:
        m, pivot = maxindex(d)

        d[pivot] = 0
        for bank in cycle(bank_order(len(d), pivot)):
            if m == 0:
                break
            d[bank] += 1
            m -= 1

        count += 1
        state = tuple(d)
        if state in states:
            break

        states.add(state)

    print(count)
