def read_data(filename="data/input21.data"):
    with open(filename) as f:
        return f.read().splitlines()

def fold(pattern):
    return [list(l) for l in pattern.split("/")]

def unfold(matrix):
    list_of_strings = ["".join(row) for row in matrix]
    return "/".join(list_of_strings)

def flipx(matrix):
    return [list(reversed(row)) for row in matrix]

def flipy(matrix):
    return list(reversed(matrix))

def rotate(matrix):
    rot = matrix
    for _ in range(4):
        rot = list(zip(*reversed(rot)))
        yield unfold([list(e)[::-1] for e in rot][::-1])

def transforms(pattern):
    matrix = fold(pattern)
    yield from rotate(matrix)
    yield from rotate(flipx(matrix))
    yield from rotate(flipy(matrix))

def count(matrix):
    total = 0
    for row in matrix:
        for elem in row:
            if elem == "#":
                total += 1

    return total

def tile(matrix):
    if len(matrix) == 3:
        return [[matrix]]

    if len(matrix) % 2 == 0:
        step = 2
    else:
        step = 3

    data = []
    for y in range(0, len(matrix), step):
        row = []
        for x in range(0, len(matrix[y]), step):
            row.append([matrix[y+j][x:x+step] for j in range(step)])
        data.append(row)
    return data

def untile(matrices):
    result = []
    for row in matrices:
        ddata = []
        for yy in range(len(row[0])):
            data = []
            for box in row:
                data.extend(box[yy])
            ddata.append(data)
        result.extend(ddata)

    return result

def parse_data(lines):
    result = {}
    for line in lines:
        (source, dest) = line.split(" => ")
        for p in transforms(source):  # expand all rules
            result[p] = dest
    return result

def run(state, rules, generations):
    for _ in range(generations):
        new_state = []
        for row in tile(state):
            new_row = []
            for matrix in row:
                rewrite = rules[unfold(matrix)]
                new_row.append(fold(rewrite))
            new_state.append(new_row)
        state = untile(new_state)

    return state

if __name__ == "__main__":
    rules = parse_data(read_data())
    state = fold(".#./..#/###")
    p1 = run(state, rules, 5)
    print(count(p1))
    p2 = run(state, rules, 18)
    print(count(p2))
