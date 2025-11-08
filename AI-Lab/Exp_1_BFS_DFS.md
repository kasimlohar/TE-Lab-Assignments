# 🧠 Experiment: DFS and BFS Traversal of an Undirected Graph

## 🎯 Aim
To implement **Depth First Search (DFS)** and **Breadth First Search (BFS)** algorithms for traversing an **undirected graph** using **adjacency list representation**.

---

## 📘 Theory (For Viva)

### 1️⃣ Depth First Search (DFS)
- **Concept:**  
  DFS explores as far as possible along each branch before backtracking.  
  It uses **recursion** or a **stack** to remember vertices to visit next.
- **Traversal Order:** Deep → Backtrack → Next Path
- **Applications:** Path finding, cycle detection, topological sorting.

**Key Steps:**
1. Pick an unvisited node.
2. Visit it and mark as visited.
3. Recursively visit all its unvisited neighbors.
4. Repeat for disconnected components.

**Algorithm:**
```
DFS(Graph, start_node):
1. Initialize visited = empty set
2. Call DFS_Visit(start_node)

DFS_Visit(node):
1. IF node is in visited THEN return
2. Add node to visited
3. Print/Process node
4. FOR each neighbor of node:
     DFS_Visit(neighbor)
```

---

### 2️⃣ Breadth First Search (BFS)
- **Concept:**  
  BFS explores all neighbors of a vertex before moving to the next level.  
  It uses a **queue** for level-order traversal.
- **Traversal Order:** Level by level
- **Applications:** Shortest path in unweighted graph, web crawling.

**Key Steps:**
1. Pick an unvisited node.
2. Enqueue and mark as visited.
3. Dequeue and visit all its unvisited neighbors.
4. Continue until all nodes are visited.

**Algorithm:**
```
BFS(Graph, start_node):
1. Initialize visited = empty list/set
2. Initialize queue = empty queue
3. Add start_node to visited
4. Add start_node to queue
5. WHILE queue is not empty:
   a. current_node = dequeue from queue
   b. Print/Process current_node
   c. FOR each neighbor of current_node:
      IF neighbor is not in visited:
         Add neighbor to visited
         Add neighbor to queue
```

---

## 🧩 Algorithm Summary

| Aspect | DFS | BFS |
|--------|------|------|
| Data Structure | Stack (or recursion) | Queue |
| Approach | Depth-first | Level-order |
| Uses | Backtracking, Cycle detection | Shortest path, Connectivity |
| Time Complexity | O(V + E) | O(V + E) |

---

## 💻 Python Code

```python
# BFS and DFS Implementation using User Input

# Function for BFS
def bfs(visited, graph, node):
    visited.append(node)
    queue = [node]

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Function for DFS
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


graph = {}  # adjacency list

n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

# Taking node names
print("\nEnter node names:")
nodes = []
for i in range(n):
    node = input(f"Node {i+1}: ")
    nodes.append(node)
    graph[node] = []  # initialize adjacency list

# Taking edges
print("\nEnter edges (u v):")
for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    graph[u].append(v)  # directed graph
    # For undirected graph, also add the reverse edge:
    graph[v].append(u)

print("\nGraph Representation (Adjacency List):")
for node in graph:
    print(f"{node} : {graph[node]}")

start = input("\nEnter starting node: ")

# BFS
visited_bfs = []
print("\nFollowing is the Breadth-First Search:")
bfs(visited_bfs, graph, start)

# DFS
visited_dfs = set()
print("\n\nFollowing is the Depth-First Search:")
dfs(visited_dfs, graph, start)
```

---

## 🧾 Sample Output

```
Adjacency List:
0: [1, 2]
1: [0, 3, 4]
2: [0, 5]
3: [1]
4: [1]
5: [2, 6]
6: [5]

DFS (recursive) Visit Order: [0, 1, 3, 4, 2, 5, 6]
BFS Visit Order: [0, 1, 2, 3, 4, 5, 6]
```

---

## 🧠 Viva Tips

* DFS uses **recursion** → Stack structure internally.
* BFS uses **queue** → First In, First Out (FIFO).
* Both cover **disconnected graphs** by running on every unvisited node.
* **Time Complexity:** O(V + E) for both.
* **Space Complexity:** O(V) for visited list + stack/queue.

---

## ✅ Conclusion

Both **DFS** and **BFS** are fundamental graph traversal techniques.
DFS explores deep paths first, while BFS explores breadth-wise levels.
They are widely used in **AI search**, **network routing**, and **graph analysis**.
