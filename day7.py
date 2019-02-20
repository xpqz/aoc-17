import re
import networkx as nx


def read_data(filename="data/input7.data"):
    with open(filename) as f:
        return f.read().splitlines()

def build_graph(G, lines):
    for line in lines:
        data = line.split(" -> ")
        root, sweight = data[0].split(" ")
        weight = int(sweight[1:-1])
        G.add_node(root, weight=weight)
        if len(data) > 1:
            children = data[1].split(", ")
            for child in children:
                G.add_edge(root, child)

if __name__ == "__main__":
    G = nx.DiGraph()

    data = read_data()

    build_graph(G, data)

    # print(next(nx.topological_sort(G)))

    print([n for n, d in G.in_degree() if d == 0][0])
