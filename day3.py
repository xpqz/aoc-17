from math import sqrt
import itertools

def dist(val):
    """
    The side of nested square containing "val" is defined by the
    smallest odd number greater than the square root of "val", unless
    the square root is an integer
    """

    width = int(sqrt(val))
    if int(val**0.5)**2 != width:
        # Non-perfect square; find the next odd number up from "width"
        width += (width % 2) + 1

    # The target edge is 0, 1, 2, or 3 == S, W, N, E respectively
    target = ((width * width) - val) // (width - 1)

    # We start at the nearest corner, anti-clockwise
    current = width*width - target*(width - 1)

    size = width//2
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    pos = [[size, -size], [-size, -size], [-size, size], [size, size]][target]

    while current > val:
        pos[0] += delta[target][0]
        pos[1] += delta[target][1]
        current -= 1

    return abs(pos[0]) + abs(pos[1])

def adj(pos):
    x, y = pos
    for n in [
        (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1),
        (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1)
    ]:
        yield n

def coords(side):
    cur = side//2, -(side//2) + 1
    for _ in range(1, side-1):  # E face, travelling N
        yield cur
        cur = cur[0], cur[1]+1

    for _ in range(side-1):  # N face, travelling W
        yield cur
        cur = cur[0]-1, cur[1]

    for _ in range(side-1):  # W face, travelling S
        yield cur
        cur = cur[0], cur[1]-1

    for _ in range(side-1):  # S face, travelling E
        yield cur
        cur = cur[0]+1, cur[1]

    yield cur

def part2(target):
    values = {(0, 0): 1}
    for square in itertools.count(start=3, step=2):
        for pos in coords(square):
            value = 0
            for n in adj(pos):
                value += values.get(n, 0)
            if value > target:
                return value
            values[pos] = value


if __name__ == "__main__":
    data = 325489

    print(dist(data))
    print(part2(data))
