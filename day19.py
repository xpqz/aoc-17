from collections import defaultdict

def read_data(filename="data/input19.data"):
    with open(filename) as f:
        return [list(line) for line in f.read().splitlines()]

def direction(pos, prev):
    """
    Determine the direction of travel given current and previous position, as
    a unit vector and magnitude.
    """
    dx, dy = pos[0] - prev[0], pos[1] - prev[1]
    mag = 1

    if abs(dx) > 1:
        mag = 2
        dx /= abs(dx)

    if abs(dy) > 1:
        mag = 2
        dy /= abs(dy)

    return int(dx), int(dy), mag


def step(stripped, pos, prev):
    """
    Move along the path one or two steps (if ducking under), at location pos, and previous given.
    Return new location, plus the number of steps (1 or 2) that was taken.
    """
    (x, y) = pos
    tile = stripped[pos]

    dx, dy, steps = direction(pos, prev)
    if tile == "-":
        new_pos = (x+dx, y)
        if not stripped.get(new_pos):
            return None, 0             # end of the line

        if stripped[new_pos] in "-+":  # carry on in direction of travel
            return new_pos, steps
        return (x+2*dx, y), steps      # underpass; skip one

    if tile == "|":
        new_pos = (x, y+dy)
        if not stripped.get(new_pos):
            return None, 0             # end of the line

        if stripped[new_pos] in "|+":  # carry on in direction of travel
            return new_pos, steps
        return (x, y+2*dy), steps      # underpass; skip one

    if tile == "+":                    # execute a turn
        if dx != 0:
            new_pos = (x, y+1)         # down
            if stripped.get(new_pos, " ") == "|":
                return new_pos, steps
            return (x, y-1), steps     # up

        new_pos = (x+1, y)
        if stripped.get(new_pos, " ") == "-":  # right (absolute)
            return new_pos, steps
        return (x-1, y), steps                 # left (absolute)

def strip_letters(data):
    letters = {}
    stripped = {}
    for y, row in enumerate(data):
        for x, tile in enumerate(row):
            if tile == " ":
                continue
            if tile in "|-+":
                stripped[x, y] = tile
                continue

            # Deduce what's under a letter. No letter is on a "+".
            if x > 0 and data[y][x-1] in "+|-":
                stripped[x, y] = "-"
            elif x < len(row) - 1 and data[y][x+1] in "+|-":
                stripped[x, y] = "-"
            elif y > 0 and data[y-1][x] in "+|-":
                stripped[x, y] = "|"
            elif y < len(data) - 1 and data[y+1][x+1] in "+|-":
                stripped[x, y] = "|"

            letters[x, y] = tile

    return stripped, letters

if __name__ == "__main__":
    data = read_data()
    stripped, letters = strip_letters(data)

    pos = (len(data[0])-1, 0)
    prev = (pos[0], -1)

    moves = 1

    while True:
        new_pos, steps = step(stripped, pos, prev)
        if new_pos is None:
            break
        if new_pos in letters:
            print(letters[new_pos], end="")
        prev = pos
        pos = new_pos
        moves += steps

    print()
    print(moves)
