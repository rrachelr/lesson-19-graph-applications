import networkx as nx
import matplotlib.pyplot as plt

'''
Made by Rachel Robins, rrobins@udel.edu

The problem: You are a student who has just entered 
Sparc Lab in Smith Hall. The room is full of unfamiliar 
faces and you nervously sit down in the last empty swivel 
chair. It seems like everyone is already part of a group, 
causing you to feel a little intimidated. While lamenting 
your lack of friends, you decide to find out how just many 
friend groups exist among your fellow students in Sparc.

I used networkx to create the graph and matplotlib to display it.

Disclaimer: The vertices include some names of my real-life friends in Sparc, 
however the friendships in the graph are very inaccurate for the sake of a 
decent solution.
'''

graph = {
    'Rachel': {'Jon': {}, 'Sean': {}, 'Minji': {}},
    'Will': {'Mycah': {}, 'Ocean': {}, 'Tommy': {}},
    'Carley': {'Megan': {}, 'Minji': {}, 'Matt': {}},
    'Mycah': {'Will': {}, 'Abbey': {}},
    'Jon': {'Rachel': {}, 'Simon': {}, 'Andrew': {}, 'Max': {}},
    'Ocean': {'Will': {}},
    'Andrew': {'Jon': {}, 'Trevor': {}, 'Max': {}, 'Sarah': {}, 'Rachel': {}},
    'Sarah': {'Andrew': {}, 'Trevor': {}},
    'Trevor': {'Matt': {}, 'Sarah': {}, 'Andrew': {}, 'Minji':{}},
    'Max': {'Andrew': {}, 'Jon': {}},
    'Axel': {'Lucas': {}},
    'James': {'Simon': {}},
    'Simon': {'James': {}, 'Jon': {}},
    'Evan': {'Megan': {}, 'Minji': {}, 'Sean': {}},
    'Sean': {'Evan': {}, 'Rachel': {}},
    'Tommy': {'Abbey': {}, 'Will': {}},
    'Megan': {'Minji': {}, 'Carley': {}, 'Evan': {}},
    'Abbey': {'Mycah': {}, 'Tommy': {}},
    'Matt': {'Trevor': {}},
    'Minji': {'Evan': {}, 'Megan': {}, 'Carley': {}, 'James': {}, 'Rachel': {}},
    'James': {'Minji': {}},
    'Ryan': {'Shreya': {}, 'Sam': {}},
    'Sam': {'Shreya': {}, 'Ryan': {}},
    'Shreya': {'Ryan': {}, 'Mercedes': {}, 'Sam': {}},
    'Mercedes': {'Shreya': {}},
    'Lucas': {'Axel': {}},
    'You': {}
}

G = nx.from_dict_of_dicts(graph)

pos = nx.spring_layout(G, seed=2)
plt.figure(1, figsize=(12,12))
nx.draw_networkx(G, pos, node_size=60, node_color='yellow', with_labels=True)
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
