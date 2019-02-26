from day10 import knot
import networkx as nx

def hexbin(data, row):
    return bin(int(knot(f"{data}-{row}"), 16))[2:].zfill(128)

if __name__ == "__main__":
    data = "jzgqcdpd"
    total = 0
    for y in range(128):
        total += sum(int(i) for i in hexbin(data, y))
    print(total)

    # Part 2
    G = nx.Graph()
    for y in range(128):
        for x, v in enumerate(hexbin(data, y)):
            if v == "1":
                G.add_node((x, y))
                if (x-1, y) in G:
                    G.add_edge((x-1, y), (x, y))
                if (x, y-1) in G:
                    G.add_edge((x, y-1), (x, y))

    print(nx.number_connected_components(G))
