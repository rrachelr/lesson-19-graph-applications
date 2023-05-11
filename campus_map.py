import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# the campus buildings
G.add_edge('SP', 'CO', weight = 5)
G.add_edge('SP', 'PE', weight = 10)
G.add_edge('PE', 'IS', weight = 10)
G.add_edge('CO', 'IS', weight = 10)
G.add_edge('PE', 'AL', weight = 20)
G.add_edge('CO', 'AL', weight = 50)
G.add_edge('IS', 'AL', weight = 15)
G.add_edge('AL', 'ME', weight = 20)
G.add_edge('AL', 'BR', weight = 10)
G.add_edge('DU', 'BR', weight = 5)
G.add_edge('BR', 'GO', weight = 10)
G.add_edge('MI', 'GO', weight = 5)
G.add_edge('SM', 'GO', weight = 15)
G.add_edge('GO', 'KI', weight = 20)
G.add_edge('PU', 'SM', weight = 10)
G.add_edge('PU', 'GO', weight = 20)
G.add_edge('PU', 'KI', weight = 15)
G.add_edge('SP', 'SH', weight = 60)
G.add_edge('SM', 'KI', weight = 5)
G.add_edge('KI', 'WI', weight = 30)
G.add_edge('WI', 'SH', weight = 45)
G.add_edge('AL', 'SH', weight = 30)



# where to start and end
start = input("Enter the first building using the first two letters of building name: ")
finish = input("Enter the second building using the first two letters of building name: ")

# marking the edges, nodes, and labels
nx.draw_edges(G, position, width = 1)
nx.draw_labels(G, position, font_size = 15)

pos = nx.spring_layout(G, seed=2)
plt.figure(1, figsize=(12,12))
nx.draw_networkx(G, pos, node_size = 60, node_color='pink', with_labels = True)
plt.savefig("init_map.png")

plt.show()

def BFS(G):
    distance = []
    tree = nx.bfs_tree(G, start.upper())
    path = nx.shortest(tree, source = start.upper())

    for i in range(0, len(path) - 1):
        distance.append(path[i])
        distance.append(path[i + 1])
    return distance