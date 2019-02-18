
def read_data(filename="data/input1.data"):
    with open(filename) as f:
        return f.read()


def rot(l, i):
    offset = len(l) // 2
    pos = (i+offset) % len(l)
    return l[pos] if l[pos] == l[i] else 0

if __name__ == "__main__":
    captcha = [int(x) for x in read_data()]
    captcha.append(captcha[0])
    print(sum([captcha[i] for i in range(1, len(captcha)) if captcha[i-1] == captcha[i]]))

    captcha = [int(x) for x in read_data()]

    total = 0
    for i in range(len(captcha)):
        total += rot(captcha, i)

    print(total)
