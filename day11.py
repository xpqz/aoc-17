# cube coordinates for hex grids; see
# https://www.redblobgames.com/grids/hexagons/#coordinates
#
# Map N-S axis to y, NE-SW to z and NW-SE to x
#
# Manhattan distance on the hex grid is half that on the cube grid.

def read_data(filename="data/input11.data"):
    with open(filename) as f:
        return f.read()

def mdist(x, y, z):
    return (abs(x)+abs(y)+abs(z)) // 2

if __name__ == "__main__":
    path = read_data()

    (x, y, z) = 0, 0, 0

    offset = {
        "n":  (0, 1, -1), "ne": (1, 0, -1),
        "se": (1, -1, 0), "s":  (0, -1, 1),
        "sw": (-1, 0, 1), "nw": (-1, 1, 0)
    }

    maxdist = 0
    for step in path.split(","):
        delta = offset[step]
        (x, y, z) = (x+delta[0], y+delta[1], z+delta[2])
        maxdist = max(maxdist, mdist(x, y, z))

    print(mdist(x, y, z))
    print(maxdist)
