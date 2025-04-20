import networkx as nx

def kruskal_example():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('A', 'B', 4), ('A', 'H', 8),
        ('B', 'H', 11), ('B', 'C', 8),
        ('C', 'I', 2), ('C', 'D', 7),
        ('C', 'F', 4), ('D', 'F', 14),
        ('D', 'E', 9), ('E', 'F', 10),
        ('F', 'G', 2), ('G', 'H', 1),
        ('G', 'I', 6), ('H', 'I', 7)
    ])
    mst = list(nx.minimum_spanning_edges(G, algorithm='kruskal', data=True))
    return mst

if __name__ == "__main__":
    mst_edges = kruskal_example()
    print("Kruskal's MST Edges (CLRS Fig 23.4):")
    for u, v, data in mst_edges:
        print(f"{u} - {v}, weight: {data['weight']}")
