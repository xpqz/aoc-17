
def read_data(filename="data/input9.data"):
    with open(filename) as f:
        return f.read()

def ffwd(stream, i):
    pos = i+1
    while pos < len(stream):
        c = stream[pos]
        if c == "!":
            pos += 1
        elif c == ">":
            return pos

        pos += 1

if __name__ == "__main__":
    stream = read_data()
    stack = []
    i = 0
    nesting_level = -1
    score = 0
    while i < len(stream):
        c = stream[i]
        if c == "{":
            stack.append(c)
            nesting_level += 1
        elif c == "}":
            stack.pop()
            score += nesting_level + 1
            nesting_level -= 1
        elif c == "<":
            i = ffwd(stream, i)
        elif c == "!":
            i += 1

        i += 1

    print(score)
