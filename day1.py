def read_data(filename="data/input1.data"):
    with open(filename) as f:
        return f.read()

if __name__ == "__main__":
    captcha = [int(x) for x in read_data()]
    captcha.append(captcha[0])
    print(sum([captcha[i] for i in range(1, len(captcha)) if captcha[i-1] == captcha[i]]))
