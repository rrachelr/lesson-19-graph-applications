# Campus Life Graph Applications


**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Rachel Robins (rrobins@udel.edu)
* Shreya Pamulapati (shrey@udel.edu)

Description of project

We chose the theme "Campus Life" for our graph applications because 
the topic is relatable to us and provides an endless number of 
related problems to solve. Our first problem, done by Rachel Robins, is
a graph of the number of friend groups in Sparc. The second and final problem,
done by Shreya Pamulapti, is finding the shorted route between two
locations on a campus map.

## Installation Code

```sh
$> pip install networkx
$> pip install matplotlib
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```


# A Sparc Can Start a Fire

**Informal Description**: 
The problem: You are a student who has just entered Sparc Lab in Smith Hall. The room is full of unfamiliar faces and you nervously sit down in the last empty swivel chair. It seems like everyone is already part of a group, causing you to feel a little intimidated. While lamenting your lack of friends, you decide to find out how just many friend groups exist among your fellow students in Sparc.

> **Formal Description**:
>  * Input: A disconnected, undirected, and unweighted graph with at least 20 vertices. The vertices are students at the University of Delaware currently in Sparc, and the edges are a friendship between
two students.
>  * Output: The number of connected components that exist within the graph.

**Graph Problem/Algorithm**: DFS

**Setup code**:

```
import networkx as nx
import matplotlib.pyplot as plt

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

pos = nx.spring_layout(G, seed=4)
plt.figure(1, figsize=(12,12))
nx.draw_networkx(G, pos, node_size=60, with_labels=True)
plt.savefig("init_graph.png")
```

**Visualization**:

![Alt text](/init_graph.png)

**Solution code:**

```
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
```

**Output**

```
5
```

**Interpretation of Results**:
The result is the number of connected components within
the graph. In this case, the number is 5, because there are
4 connected components and one node on its own, which counts
as a single component.


# Campus Map

**Informal Description**: Find the shortest path to get from Alison Hall (AL) to Willard Hall (WI). Return that path of halls taken.

> **Formal Description**:
>  * Input: start = AL , finish = WI
>  * Output: A list of the halls that were taken.

**Graph Problem/Algorithm**: BFS

**Setup code**:

```python
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
nx.draw_nodes(G, position, width = 300)
nx.draw_labels(G, position, font_size = 15)

plt.show()
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
distance = []
tree = nx.bfs_tree(G, start.upper())
path = nx.shortest(tree, source = start.upper())

for i in range(0, len(path) - 1):
    distance.append(path[i])
    distance.append(path[i + 1])
```

**Output**

```
```

**Interpretation of Results**: