from itertools import cycle, islice, zip_longest
from functools import reduce

def rot(l, pos, length, skip):
    p = pos
    ll = len(l)
    selection = list(islice(cycle(l), pos, pos+length))
    for i in reversed(selection):
        l[p%ll] = i
        p += 1
    return (pos + length + skip) % ll, skip + 1

def chunk16(iterable):
    args = [iter(iterable)] * 16
    return zip_longest(*args)

def knot(data):
    lengths = list(bytearray(data, "ascii")) + [17, 31, 73, 47, 23]

    numbers = list(range(256))

    skip, pos = 0, 0
    for _ in range(64):
        for length in lengths:
            pos, skip = rot(numbers, pos, length, skip)

    dense = [reduce(lambda acc, i: acc^i, j) for j in chunk16(numbers)]

    return "".join([f"{i:02x}" for i in dense])

if __name__ == "__main__":
    lengths = [147, 37, 249, 1, 31, 2, 226, 0, 161, 71, 254, 243, 183, 255, 30, 70]
    numbers = list(range(256))

    skip, pos = 0, 0
    for length in lengths:
        pos, skip = rot(numbers, pos, length, skip)

    print(numbers[0]*numbers[1])

    data = "147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70"

    print(knot(data))
