# Campus Life

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Rachel Robins (rrobins@udel.edu)
* Shreya Pamulapati (shrey@udel.edu)

Description of project

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

# Friendship Graph

**Informal Description**:

> **Formal Description**:
>  * Input:
>  * Output: 

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:


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