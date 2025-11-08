# Experiment 5: Selection Sort & Kruskal's Algorithm (MST)

## Overview

This experiment demonstrates two fundamental algorithms:
1. **Selection Sort** - A simple comparison-based sorting algorithm
2. **Kruskal's Algorithm** - A greedy algorithm for finding Minimum Spanning Trees (MST)

---

## Part 1: Selection Sort

### Theory

**Selection Sort** is one of the simplest sorting algorithms that works by repeatedly finding the minimum element from the unsorted portion and placing it at the beginning.

### Algorithm Principle

The algorithm divides the input list into two parts:
- **Sorted portion**: Elements at the beginning (initially empty)
- **Unsorted portion**: Remaining elements

### Working Steps

1. Find the smallest element in the unsorted array
2. Swap it with the first element of unsorted portion
3. Move the boundary between sorted and unsorted portions
4. Repeat until the entire array is sorted

### Pseudocode

```
function selectionSort(arr):
    n = length(arr)
    for i = 0 to n-1:
        min_index = i
        for j = i+1 to n-1:
            if arr[j] < arr[min_index]:
                min_index = j
        swap arr[i] with arr[min_index]
    return arr
```

### Example Execution

```
Initial: [64, 25, 12, 22, 11, 90]

Pass 1: Find min in [64, 25, 12, 22, 11, 90] → 11
Result: [11, 25, 12, 22, 64, 90]

Pass 2: Find min in [25, 12, 22, 64, 90] → 12  
Result: [11, 12, 25, 22, 64, 90]

Pass 3: Find min in [25, 22, 64, 90] → 22
Result: [11, 12, 22, 25, 64, 90]

Pass 4: Find min in [25, 64, 90] → 25
Result: [11, 12, 22, 25, 64, 90]

Pass 5: Find min in [64, 90] → 64
Result: [11, 12, 22, 25, 64, 90]

Final: [11, 12, 22, 25, 64, 90]
```

### Complexity Analysis

| Metric | Complexity |
|--------|------------|
| **Time Complexity** | O(n²) in all cases |
| **Space Complexity** | O(1) - in-place sorting |
| **Best Case** | O(n²) |
| **Average Case** | O(n²) |
| **Worst Case** | O(n²) |

### Characteristics

- **✅ Advantages:**
  - Simple implementation
  - In-place sorting (O(1) extra space)
  - Minimizes number of swaps (O(n) swaps)
  - Performance doesn't depend on input order

- **❌ Disadvantages:**
  - Poor time complexity O(n²)
  - Not suitable for large datasets
  - Not stable (doesn't preserve relative order of equal elements)

---

## Part 2: Kruskal's Algorithm for MST

### Theory

**Kruskal's Algorithm** is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

### Minimum Spanning Tree (MST)

An MST is a subset of edges that:
- Connects all vertices in the graph
- Has no cycles (forms a tree)
- Has minimum total edge weight among all possible spanning trees

### Key Concepts

#### 1. Disjoint Set (Union-Find) Data Structure

Used to efficiently detect cycles during MST construction:

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)  # Union operation
```

#### 2. Path Compression Optimization

In the `find` operation, we compress paths to make future operations faster by making every node point directly to the root.

### Kruskal's Algorithm Steps

1. **Sort all edges** by weight in ascending order
2. **Initialize** disjoint set for all vertices
3. **For each edge** in sorted order:
   - Check if edge connects vertices in different components
   - If yes, add edge to MST and union the components
   - If no, skip edge (would create cycle)
4. **Stop** when MST has (V-1) edges

### Pseudocode

```
function kruskal(vertices, edges):
    sort edges by weight
    initialize disjoint_set
    mst = []
    total_weight = 0
    
    for each edge (u, v, weight) in sorted_edges:
        if find(u) != find(v):  // Different components
            union(u, v)
            add (u, v, weight) to mst
            total_weight += weight
    
    return mst, total_weight
```

### Example Execution

```
Graph with edges: [(0,1,4), (0,2,3), (1,2,1), (1,3,2), (2,3,4)]

Step 1: Sort edges by weight
Sorted: [(1,2,1), (1,3,2), (0,2,3), (0,1,4), (2,3,4)]

Step 2: Process edges
Edge (1,2,1): Components {1}, {2} → Union → Add to MST
Edge (1,3,2): Components {1,2}, {3} → Union → Add to MST  
Edge (0,2,3): Components {0}, {1,2,3} → Union → Add to MST
Edge (0,1,4): Components {0,1,2,3} → Skip (would create cycle)
Edge (2,3,4): Components {0,1,2,3} → Skip (would create cycle)

MST: [(1,2,1), (1,3,2), (0,2,3)]
Total weight: 6
```

### Complexity Analysis

| Operation | Time Complexity |
|-----------|----------------|
| **Sorting edges** | O(E log E) |
| **Union-Find operations** | O(E α(V)) |
| **Overall** | **O(E log E)** |

Where:
- E = number of edges
- V = number of vertices  
- α = inverse Ackermann function (practically constant)

### Space Complexity
- O(V) for disjoint set data structure
- O(E) for storing edges

### Kruskal's vs Other MST Algorithms

| Algorithm | Time Complexity | Best For |
|-----------|----------------|----------|
| **Kruskal's** | O(E log E) | Sparse graphs |
| **Prim's** | O(E log V) | Dense graphs |

### Applications of MST

1. **Network Design**
   - Minimum cost to connect all computers in network
   - Optimal cable/fiber layout

2. **Transportation**
   - Minimum cost road network
   - Airline route optimization

3. **Clustering**
   - Data mining and machine learning
   - Image segmentation

4. **Approximation Algorithms**
   - Traveling Salesman Problem (TSP)
   - Steiner Tree problems

### Greedy Choice Property

Kruskal's algorithm works because of the **greedy choice property**:
- At each step, choosing the minimum weight edge that doesn't create a cycle leads to optimal solution
- This is proven using the **cut property** of MSTs

### Cut Property

For any cut in a graph, the minimum weight edge crossing the cut is always in some MST.

## Implementation Notes

### Error Handling Considerations

```python
# Validate input
if n <= 0:
    print("Number of vertices must be positive")
    
# Check for valid edge format
try:
    u, v, w = map(int, input().split())
except ValueError:
    print("Invalid edge format")
```

### Memory Optimization

- Use adjacency list for sparse graphs
- Implement union by rank for better Union-Find performance

### Practical Considerations

1. **Input validation** for graph connectivity
2. **Handling disconnected graphs** (forest of MSTs)
3. **Dealing with negative weights** (algorithm still works)
4. **Multiple MSTs** with same total weight

## Conclusion

This experiment demonstrates:
- **Selection Sort**: Simple O(n²) sorting with minimal swaps
- **Kruskal's Algorithm**: Efficient O(E log E) MST algorithm using greedy approach and Union-Find

Both algorithms showcase different algorithmic paradigms:
- Selection sort uses **brute force** approach
- Kruskal's uses **greedy** strategy with sophisticated data structures

The combination illustrates the evolution from simple algorithms to more sophisticated ones that solve complex graph problems efficiently.