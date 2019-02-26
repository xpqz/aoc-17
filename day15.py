
def gen(number, factor):
    while True:
        number = number * factor % 2147483647
        number = yield number


def gen2(number, factor, divisor):
    while True:
        number = number * factor % 2147483647
        if number % divisor == 0:
            number = yield number

def match(iterations, ga, prev_a, gb, prev_b):
    total = 0
    for _ in range(iterations):
        prev_a = ga.send(prev_a)
        prev_b = gb.send(prev_b)

        if hex(prev_a & 0xffff) == hex(prev_b & 0xffff):
            total += 1

    return total

if __name__ == "__main__":
    A = 679
    B = 771

    prev_a = A
    ga = gen(prev_a, 16807)
    ga.send(None)

    prev_b = B
    gb = gen(prev_b, 48271)
    gb.send(None)

    print(match(40_000_000, ga, prev_a, gb, prev_b))

    # Part 2
    prev_a = A
    ga = gen2(prev_a, 16807, 4)
    ga.send(None)

    prev_b = B
    gb = gen2(prev_b, 48271, 8)
    gb.send(None)

    print(match(5_000_000, ga, prev_a, gb, prev_b))
