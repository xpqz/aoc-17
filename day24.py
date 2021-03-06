def read_data(filename="data/input24.data"):
    with open(filename) as f:
        return [list(map(int, line.split("/"))) for line in f]

def strongest_path(components, last):
    strongest = 0
    best_path = []
    for i, comp in enumerate(components):
        if comp[0] == last or comp[1] == last:
            path = comp + strongest_path(components[:i] + components[i+1:], comp[1] if comp[0] == last else comp[0])
            strength = sum(path)
            if strength > strongest:
                strongest = strength
                best_path = path

    return best_path


def longest_path(components, last):
    longest = 0
    best_path = []
    for i, comp in enumerate(components):
        if comp[0] == last or comp[1] == last:
            path = comp + \
                longest_path(
                    components[:i] + components[i+1:], comp[1] if comp[0] == last else comp[0])
            length = len(path)
            if length > longest:
                longest = length
                best_path = path
            elif length == longest:
                if sum(path) > sum(best_path):
                    best_path = path


    return best_path

if __name__ == "__main__":
    data = read_data()
    print(sum(strongest_path(data, 0)))
    print(sum(longest_path(data, 0)))
