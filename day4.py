class PhraseInvalidException(Exception):
    pass

def read_data(filename="data/input4.data"):
    with open(filename) as f:
        return [l.split(" ") for l in f.read().splitlines()]

if __name__ == "__main__":
    data = read_data()

    count = 0
    for l in data:
        if len(set(l)) == len(l):
            count += 1

    print(count)

    count = 0
    for l in data:
        try:
            for i, word1 in enumerate(l):
                for j, word2 in enumerate(l):
                    if i != j:
                        if sorted(word1) == sorted(word2):
                            raise PhraseInvalidException
        except PhraseInvalidException:
            continue
        count += 1

    print(count)
