# Experiment 1: BFS and DFS Algorithms

## What is Graph Traversal?
Graph traversal means visiting all vertices (nodes) in a graph systematically. There are two main methods:
- **DFS (Depth-First Search)**: Go as deep as possible, then backtrack
- **BFS (Breadth-First Search)**: Visit all neighbors first, then move to next level

## DFS Algorithm (Depth-First Search)

### How it works:
1. Start from a vertex
2. Mark it as visited
3. Visit an unvisited neighbor
4. Repeat step 3 until no unvisited neighbors
5. Backtrack and try other paths

### Algorithm Steps:
```
DFS(graph, start_vertex):
1. Mark start_vertex as visited
2. Print/store start_vertex
3. For each neighbor of start_vertex:
   - If neighbor is not visited:
     - Call DFS(graph, neighbor)
```

### Example Traversal:
For graph: 0-1-3, 0-2-5-6, 1-4
**DFS Order**: 0 → 1 → 3 → 4 → 2 → 5 → 6

---

## BFS Algorithm (Breadth-First Search)

### How it works:
1. Start from a vertex, add to queue
2. Mark it as visited
3. Remove vertex from queue, visit it
4. Add all unvisited neighbors to queue
5. Repeat until queue is empty

### Algorithm Steps:
```
BFS(graph, start_vertex):
1. Create empty queue
2. Mark start_vertex as visited
3. Add start_vertex to queue
4. While queue is not empty:
   - Remove vertex from front of queue
   - Print/store vertex
   - For each unvisited neighbor:
     - Mark neighbor as visited
     - Add neighbor to queue
```

### Example Traversal:
For same graph: 0-1-3, 0-2-5-6, 1-4
**BFS Order**: 0 → 1 → 2 → 3 → 4 → 5 → 6

---

## Key Differences

| DFS | BFS |
|-----|-----|
| Uses recursion (or stack) | Uses queue |
| Goes deep first | Goes wide first |
| Memory: O(height) | Memory: O(width) |
| Good for: path finding, cycle detection | Good for: shortest path, level-wise traversal |

## Running the Code
```bash
python Exp_1_BFS_DFS.py
```

## Sample Output
```
Adjacency list:
0: [1, 2]
1: [0, 3, 4]
2: [0, 5]
3: [1]
4: [1]
5: [2, 6]
6: [5]

DFS visit order: [0, 1, 3, 4, 2, 5, 6]
BFS visit order: [0, 1, 2, 3, 4, 5, 6]
```