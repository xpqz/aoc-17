
def gen(number, factor):
    while True:
        number = number * factor % 2147483647
        number = yield number


if __name__ == "__main__":
    A = 679
    B = 771

    prev_a = A
    ga = gen(prev_a, 16807)
    ga.send(None)

    prev_b = B
    gb = gen(prev_b, 48271)
    gb.send(None)

    total = 0
    for _ in range(40_000_000):
        prev_a = ga.send(prev_a)
        prev_b = gb.send(prev_b)

        if hex(prev_a & 0xffff) == hex(prev_b & 0xffff):
            total += 1

    print(total)
