import networkx as nx

def dfs_example():
    G = nx.DiGraph()
    G.add_edges_from([
        ('undershorts', 'pants'), ('undershorts', 'shoes'),
        ('pants', 'belt'), ('pants', 'shoes'),
        ('belt', 'jacket'), ('shirt', 'belt'), ('shirt', 'tie'),
        ('tie', 'jacket'), ('socks', 'shoes')
    ])
    G.add_node('watch')
    return list(nx.dfs_preorder_nodes(G))

if __name__ == "__main__":
    traversal = dfs_example()
    print("DFS Traversal Order (CLRS Fig 22.4):")
    for node in traversal:
        print(node)
