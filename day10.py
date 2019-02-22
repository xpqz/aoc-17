from itertools import cycle, islice

def rot(l, pos, length, skip):
    p = pos
    ll = len(l)
    selection = list(islice(cycle(l), pos, pos+length))
    for i in reversed(selection):
        l[p%ll] = i
        p += 1
    return (pos + length + skip) % ll, skip + 1

if __name__ == "__main__":
    lengths = [147, 37, 249, 1, 31, 2, 226, 0, 161, 71, 254, 243, 183, 255, 30, 70]
    numbers = list(range(256))

    skip, pos = 0, 0
    for length in lengths:
        pos, skip = rot(numbers, pos, length, skip)

    print(numbers[0]*numbers[1])
