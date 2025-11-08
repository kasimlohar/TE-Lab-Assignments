# 🧠 Experiment 5: Selection Sort & Kruskal's Algorithm (MST)

## 🎯 Aim
To implement **Selection Sort** algorithm for sorting arrays and **Kruskal's Algorithm** for finding the **Minimum Spanning Tree (MST)** using **Disjoint Set (Union-Find)** data structure.

---

## 📘 Theory (For Viva)

### 1️⃣ Selection Sort
- **Concept:**  
  Selection Sort is a simple comparison-based sorting algorithm that repeatedly finds the minimum element from the unsorted portion and places it at the beginning.
- **Strategy:** Divide array into sorted and unsorted portions, repeatedly select minimum
- **Applications:** Small datasets, educational purposes, situations requiring minimal swaps.

**Key Steps:**
1. Find the smallest element in the unsorted array
2. Swap it with the first element of unsorted portion
3. Move the boundary between sorted and unsorted portions
4. Repeat until the entire array is sorted

**Algorithm:**
```
SELECTION_SORT(arr):
1. n = length(arr)
2. FOR i = 0 to n-1:
   a. min_index = i
   b. FOR j = i+1 to n-1:
      IF arr[j] < arr[min_index]:
        min_index = j
   c. SWAP arr[i] with arr[min_index]
3. RETURN arr
```

---

### 2️⃣ Kruskal's Algorithm for MST
- **Concept:**  
  Kruskal's Algorithm is a greedy algorithm that finds the Minimum Spanning Tree by selecting edges in order of increasing weight while avoiding cycles.
- **Strategy:** Sort edges by weight, use Union-Find to detect cycles
- **Applications:** Network design, clustering, transportation planning.

**Key Steps:**
1. Sort all edges by weight in ascending order
2. Initialize disjoint set for all vertices
3. For each edge, check if it connects different components
4. If yes, add edge to MST and union the components
5. Stop when MST has (V-1) edges

**Algorithm:**
```
KRUSKAL(vertices, edges):
1. SORT edges by weight in ascending order
2. Initialize disjoint_set for all vertices
3. mst = empty list
4. total_weight = 0

5. FOR each edge (u, v, weight) in sorted_edges:
   a. IF find(u) != find(v):  // Different components
      i. union(u, v)
      ii. ADD (u, v, weight) to mst
      iii. total_weight += weight
6. RETURN mst, total_weight

UNION-FIND Operations:
FIND(u): Return root of component containing u (with path compression)
UNION(u, v): Merge components containing u and v
```

---

## 💻 Python Code

```python
# Selection Sort and Kruskal's Algorithm Implementation

# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current element is the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the min_index if a smaller element is found
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum element with the first element
    return arr

# Take input from the user for Selection Sort
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# Kruskal's Algorithm using Disjoint Set (Union-Find)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(n)
    mst, total_weight = [], 0
    
    for u, v, w in edges:
        if ds.find(u) != ds.find(v):  # Different components, no cycle
            ds.union(u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

# Take input from the user for Kruskal's Algorithm
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = [tuple(map(int, input("Enter edge (u, v, weight): ").strip().split())) for _ in range(m)]
mst, total_weight = kruskal(n, edges)

print("\nEdges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u}-{v} (weight: {w})")
print(f"\nTotal weight of MST: {total_weight}")
```

---

## 🧾 Sample Output

```
Enter the array elements separated by space: 64 25 12 22 11 90
Sorted array: [11, 12, 22, 25, 64, 90]

Enter the number of vertices: 4
Enter the number of edges: 5
Enter edge (u, v, weight): 0 1 4
Enter edge (u, v, weight): 0 2 3
Enter edge (u, v, weight): 1 2 1
Enter edge (u, v, weight): 1 3 2
Enter edge (u, v, weight): 2 3 4

Edges in the Minimum Spanning Tree:
1-2 (weight: 1)
1-3 (weight: 2)
0-2 (weight: 3)

Total weight of MST: 6
```

---

## 🧠 Viva Tips

* **Selection Sort** has **O(n²)** time complexity but uses **minimal swaps** O(n).
* **Kruskal's algorithm** uses **greedy approach** - always pick minimum weight edge that doesn't create cycle.
* **Union-Find** data structure efficiently detects cycles with **path compression** optimization.
* **MST properties**: Exactly **(V-1) edges** for V vertices, **no cycles**, **minimum total weight**.
* **Time complexity** of Kruskal's: **O(E log E)** dominated by edge sorting.
* **Space complexity**: O(1) for Selection Sort, **O(V)** for Union-Find in Kruskal's.
* **Cut property**: Minimum weight edge crossing any cut is always in some MST.

---

## ✅ Conclusion

Both algorithms demonstrate different paradigms: **Selection Sort** uses simple comparison-based approach while **Kruskal's Algorithm** employs greedy strategy with sophisticated data structures.
Selection Sort is educational for understanding basic sorting, while Kruskal's is practical for **network design** and **optimization problems**.
They showcase the evolution from **brute force** to **intelligent algorithmic techniques**.