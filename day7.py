from collections import Counter, deque, defaultdict
from itertools import groupby

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
    build_graph(G, read_data())
    start = [n for n, d in G.in_degree() if d == 0][0]
    print(start)

    queue = deque([(start, "")])
    weights = []
    while queue:
        (cur, parent) = queue.popleft()
        total = G.node[cur]["weight"] + sum([G.node[d]["weight"] for d in nx.descendants(G, cur)])
        queue.extend([(n, cur) for n in G.neighbors(cur)])
        weights.append({"node": cur, "sum": total, "parent": parent})

    result = sorted(weights, key=lambda x: x["parent"])

    # Group nodes by predecessors
    for _k, group in groupby(result, lambda x: x["parent"]):
        c = defaultdict(list)
        for row in group:
            c[row["sum"]].append(row["node"])

        if len(c) == 2:
            ic = iter(c)
            a, b = next(ic), next(ic)
            if len(c[a]) == 1:
                diff = b-a
                print(c[a][0], G.node[c[a][0]]["weight"] + diff)
            else:
                diff = a-b
                print(c[b][0], G.node[c[b][0]]["weight"] + diff)

            break
