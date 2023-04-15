import networkx as nx
import matplotlib.pyplot as plt

# make a graph named G
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([
    ("A", "C"), ("A", "F"), 
    ("B", "E"), ("B", "F"), ("B", "D"), 
    ("C", "A"), ("C", "D"), ("C", "F"), ("C", "E"),
    ("D", "B"), ("D", "C"), ("D", "F"),
    ("E", "C"), ("E", "B"), ("E", "F"),
    ("F", "A"), ("F", "B"), ("F", "C"), ("F", "D"), ("F", "E")
])
print("Graph Nodes: ", G.nodes)
print("Graph Edges: ")
for edge in G.edges:
    print(edge)
print()
# get the degree of each node
print("Degree of each node: ")
degree_dict = dict(G.degree())
for node, degree in degree_dict.items():
    print(f"Node {node} has degree {degree}")
print()

# define function to get all paths between two nodes
# use a graph traversal algorithm named Depth-First Search (DFS)
def get_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = get_all_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

All_path = get_all_paths(G, "A", "D")
print("All possible paths between node A and D: ")
[print (path) for path in All_path]
print()

def shortest_path(All_path):
    sp = All_path[0]
    for path in All_path:
        if len(path) < len(sp):
            sp = path
    sps = []
    for path in All_path:
        if len(path) == len(sp):
            sps.append(path)
    return sps

shortest_paths = shortest_path(All_path)
print("Shortest path(s): " ,shortest_paths)
print()

#calculate maximum edges
def max_edge():
    n = len(G.nodes)
    Max_edge = n * (n - 1) / 2
    return Max_edge

print("Maximum possible edges: ", max_edge())
print()

# calculate density
def density():
    n = len(G.nodes)
    m = len(G.edges)
    Density = 2 * m / (n * (n-1))
    return Density
print("Density of the graph: ", density())
print()

# find clique in the graph
def clique():
    cliques = list(nx.algorithms.clique.find_cliques(G))
    if len(cliques) > 0:
        print("Clique Found!")
        return print("Clique(s): ", cliques)
    else:
        return print("No Clique!")
clique()
print()

#Adjacency Matrix
def adjacency_matrix():
    nodes = list(G.nodes())
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]
    for x, y in G.edges:
        i, j = nodes.index(x), nodes.index(y)
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1
    return adj_matrix
print("Adjacency Matrix:")
for row in adjacency_matrix():
    print(row)
print()

#Adjacency list
def adjacency_list():
    adj_list = {}
    for u, v in G.edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list
print("Adjacency list:")
for node, neighbors in adjacency_list().items():
    print(f"{node}: {neighbors}")
print()

#Distance Matrix
def distance_matrix():
    nodes = list(G.nodes)
    n = len(nodes)
    dist = [[float('inf')]*n for _ in range(n)] #build a n*n infinity matrix 
    for i in range(n):
        dist[i][i] = 0
    for x, y in G.edges:
        i, j = nodes.index(x), nodes.index(y)
        dist[i][j] = 1
        dist[j][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
print("Distance Matrix:")
for row in distance_matrix():
    print(row)
print()

#Diameter of Network
diameter = max(max(row) for row in distance_matrix())
print("Diameter of the graph:", diameter)
print()

#Average Path Length
def average_path_length():
    num_paths = 0
    total_path_length = 0
    
    nodes = list(G.nodes)
    n = len(nodes)
    
    for i in range(n):
        for j in range(i+1, n):
            path = get_all_paths(G, nodes[i], nodes[j])
            num_paths += len(path)
            for z in path:
                total_path_length += len(z)-1
    
    return (total_path_length / num_paths)
print("Average Path Length: ", average_path_length())
print()

#Degree Distribution Plot
plt.bar(degree_dict.keys(), degree_dict.values())
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")
plt.title("Degree Distribution")
plt.show()

distribution = {}
for i in degree_dict.values():
    if i in distribution:
        distribution[i] += 1
    else:
        distribution[i] = 1
plt.bar(distribution.keys(), distribution.values())
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degree Distribution")
plt.show()

#Clustering Coefficient
def clustering_coefficient(node):
    neighbors = G[node]
    k = len(neighbors)
    if k < 2:
        return 0
    else:
        num_actual_edges = 0
        for i, ni in enumerate(neighbors):
            for j, nj in enumerate(neighbors):
                if i < j and ni in G[nj]:
                    num_actual_edges += 1
        num_possible_edges = k * (k - 1) / 2
        return num_actual_edges / num_possible_edges
print("Clustring Coefficient of Node F: ", clustering_coefficient("F"))