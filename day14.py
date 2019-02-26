from day10 import knot

if __name__ == "__main__":
    data = "jzgqcdpd"
    total = 0
    for y in range(128):
        total += sum(int(i) for i in bin(int(knot(f"{data}-{y}"), 16))[2:].zfill(128))
    print(total)
