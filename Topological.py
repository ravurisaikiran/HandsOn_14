import networkx as nx

def topological_sort_example():
    G = nx.DiGraph()
    G.add_edges_from([
        ('undershorts', 'pants'), ('undershorts', 'shoes'),
        ('pants', 'belt'), ('pants', 'shoes'),
        ('belt', 'jacket'), ('shirt', 'belt'), ('shirt', 'tie'),
        ('tie', 'jacket'), ('socks', 'shoes')
    ])
    G.add_node('watch')
    return list(nx.topological_sort(G))

if __name__ == "__main__":
    order = topological_sort_example()
    print("Topological Sort Order (CLRS Fig 22.4):")
    for item in order:
        print(item)
