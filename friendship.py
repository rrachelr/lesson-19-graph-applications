import networkx as nx
import matplotlib.pyplot as plt

'''
Made by Rachel Robins, rrobins@udel.edu

The problem: You are a student who has just entered Sparc Lab 
in Smith Hall. The room is full of familiar faces from your 
classes and around campus. Because the department is relatively 
small, you decide you want to find out if there is a connection 
between every student in the room through a friendship with 
someone else.

I used networkx to create the graph and matplotlib to display it.
'''

graph = {
    'Rachel': {'Jonathon': {}, 'Axel': {}},
    'Will': {'Mycah': {}, 'Ocean': {}, 'Tommy': {}},
    'Carley': {'Megan': {}},
    'Mycah': {'Will': {}, 'Abbey': {}},
    'Jonathon': {'Rachel': {}, 'Simon': {}, 'Andrew': {}, 'Max': {}},
    'Ocean': {'Will': {}, 'Tommy': {}},
    'Andrew': {'Jonathon': {}, 'Trevor': {}, 'Max': {}, 'Yasmin': {}},
    'Yasmin': {'Andrew': {}, 'Trevor': {}},
    'Trevor': {'Matt': {}, 'Yasmin': {}, 'Andrew': {}},
    'Max': {'Andrew': {}, 'Jonathon': {}},
    'Axel': {'Rachel': {}},
    'Blade': {'Simon': {}},
    'Simon': {'Blade': {}, 'Jonathon': {}},
    'Evan': {'Megan': {}, 'Minji': {}, 'Sean': {}},
    'Sean': {'Evan': {}},
    'Tommy': {'Abbey': {}, 'Will': {}, 'Ocean': {}},
    'Megan': {'Minji': {}, 'Carley': {}, 'Evan': {}},
    'Abbey': {'Mycah': {}, 'Tommy': {}},
    'Matt': {'Trevor': {}},
    'Minji': {'Evan': {}, 'Megan': {}},
}

G = nx.from_dict_of_dicts(graph)

pos = nx.spring_layout(G, seed=4)
plt.figure(1, figsize=(5,5))
nx.draw_networkx(G, pos, node_size=60, with_labels=True)
plt.savefig("init_graph.png")

#Solution
def DFS(graph, visited, v):
    visited.append(v)
    for i in graph[v].keys():
        if i not in visited:
            visited.append(i)
            DFS(graph, visited, i)

def friendship_circles(graph, n):
    num_circles = 0
    visited = []
    for i in graph.keys():
        if i not in visited:
            DFS(graph, visited, i)
            num_circles += 1
    return num_circles

print(friendship_circles(graph, len(graph)))
