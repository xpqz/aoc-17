import re
import networkx as nx

def read_data(filename="data/input12.data"):
    with open(filename) as f:
        return f.read().splitlines()

def build_graph(G, lines):
    for line in lines:
        nodes = [int(n) for n in re.findall(r"-?\d+", line)]
        for child in nodes[1:]:
            G.add_edge(nodes[0], child)

if __name__ == "__main__":
    G = nx.DiGraph()
    build_graph(G, read_data())

    print(len(list(nx.descendants(G, 0))) + 1)  # add self
