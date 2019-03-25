
def ins(circle, value, current, step):
    c = (current + step) % len(circle) + 1
    if c >= len(circle):
        circle.append(value)
    else:
        circle.insert(c, value)

    return c

if __name__ == "__main__":

    circle = [0]
    step = 356
    current = 0

    for value in range(1, 2018):
        current = ins(circle, value, current, step)

    print(circle[(current+1)%len(circle)])

    current = 0
    size = 1
    result = -1
    for value in range(1, 50_000_000):
        current = (current + step) % size + 1
        if current == 1:
            result = size
        size += 1

    print(result)
