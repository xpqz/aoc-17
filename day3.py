from math import sqrt

start = 325489

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

if __name__ == "__main__":
    print(dist(325489))
