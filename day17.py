

from collections import deque

def ins(circle, value, current, step):
    c = (current + step) % len(circle) + 1
    if c >= len(circle):
        circle.append(value)
    else:
        circle.insert(c, value)

    return c


if __name__ == "__main__":
    circle = deque([0])
    step = 356
    current = 0

    for value in range(1, 2018):
        current = ins(circle, value, current, step)

    print(circle[(current+1)%len(circle)])
