# Campus Life Graph Applications

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Rachel Robins (rrobins@udel.edu)
* Shreya Pamulapati (shrey@udel.edu)

Description of project

We chose the theme "Campus Life" for our graph applications because 
the topic is relatable to us and provides an endless number of 
related problems to solve. Our first problem, done by Rachel Robins, is
a friendship graph of students in Sparc.

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
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
3
```

**Interpretation of Results**:

