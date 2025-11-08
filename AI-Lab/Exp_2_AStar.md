# 🧠 Experiment 2: A* (A-Star) Algorithm for Optimal Pathfinding

## 🎯 Aim
To implement the **A* (A-Star) search algorithm** for finding the **optimal path** from a start node to a goal node in a **grid-based environment** with obstacles.

---

## 📘 Theory (For Viva)

### 🌟 A* Algorithm Overview
- **Concept:**  
  A* is an **informed search algorithm** that finds the optimal path by combining the benefits of Dijkstra's algorithm (guarantees shortest path) with the efficiency of greedy best-first search (uses heuristics).
- **Key Feature:** Uses both **actual cost** and **heuristic estimation** to guide search
- **Applications:** Game AI pathfinding, robotics navigation, GPS routing, puzzle solving.

### 🧮 Cost Function
A* uses a **cost function** f(n) = g(n) + h(n) where:
- **g(n)**: Actual cost from start to current node
- **h(n)**: Heuristic (estimated cost from current node to goal)
- **f(n)**: Total estimated cost of path through node n

**Key Steps:**
1. Initialize open set with start node
2. While open set is not empty:
   - Select node with lowest f(n) from open set
   - If it's the goal, reconstruct path
   - Move node from open to closed set
   - For each neighbor: calculate costs and update if better

**Algorithm:**
```
A_STAR(start, goal):
1. Initialize open_set = {start}
2. Initialize closed_set = {}
3. Initialize g[start] = 0
4. Initialize f[start] = g[start] + heuristic(start, goal)

5. WHILE open_set is not empty:
   a. current = node in open_set with lowest f[node]
   b. IF current == goal:
      RETURN reconstruct_path()
   
   c. Remove current from open_set
   d. Add current to closed_set
   
   e. FOR each neighbor of current:
      IF neighbor in closed_set: CONTINUE
      
      tentative_g = g[current] + distance(current, neighbor)
      
      IF neighbor not in open_set:
         Add neighbor to open_set
      ELSE IF tentative_g >= g[neighbor]:
         CONTINUE
      
      parent[neighbor] = current
      g[neighbor] = tentative_g
      f[neighbor] = g[neighbor] + heuristic(neighbor, goal)

6. RETURN failure (no path found)
```

---

## 🔍 Key Components in Our Implementation

### 1. Heuristic Function
```python
def heuristic(self, start, goal):
    D = 1
    D2 = 1
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
```
This implements **Manhattan distance with diagonal movement** allowed.

### 2. Movement Directions
The algorithm allows 5 types of movements:
- Up, Down, Left, Right (cost = 1)
- Diagonal (cost = 1)

### 3. Barriers
Positions marked as barriers have a high movement cost (100), making the algorithm avoid them when possible.

### 4. Grid Boundaries
The implementation works on a 6x6 grid (0 to 5 in both dimensions).

---

## 🧩 Algorithm Summary

| Aspect | A* | BFS | Dijkstra |
|--------|----|----- |----------|
| Data Structure | Priority Queue | Queue | Priority Queue |
| Approach | Best-first with heuristic | Level-order | Shortest path |
| Uses | Optimal pathfinding | Unweighted shortest path | Weighted shortest path |
| Time Complexity | O(b^d) | O(V + E) | O((V+E)logV) |
| Space Complexity | O(b^d) | O(V) | O(V) |
| Optimality | ✅ (with admissible heuristic) | ✅ (unweighted) | ✅ |

**b** = branching factor, **d** = depth of solution

---

## 💻 Python Code

```python
# A* Algorithm Implementation for Grid-Based Pathfinding

class AStarGraph(object):
    def __init__(self):
        self.barriers = []  # List to hold the barrier coordinates
        t = int(input("Enter total number of barriers: "))
        for i in range(t):
            # Collecting the coordinates for each barrier
            x = int(input(f"Enter row number for barrier point {i+1}: "))
            y = int(input(f"Enter column number for barrier point {i+1}: "))
            self.barriers.append((x, y))

    def heuristic(self, start, goal):
        # Heuristic function to estimate the cost from start to goal
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def get_vertex_neighbours(self, pos):
        # Get the valid neighbouring positions from the current position
        n = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 5 or y2 < 0 or y2 > 5:
                continue  # Skip out-of-bounds positions
            n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        # Return the movement cost from position a to position b
        if b in self.barriers:
            return 100  # High cost for barriers
        return 1  # Normal cost for free space

def AStarSearch(start, end, graph):
    G = {}  # Actual movement cost to each position from the start position
    F = {}  # Estimated movement cost from start to end going through the position

    G[start] = 0  # Cost from start to start is zero
    F[start] = graph.heuristic(start, end)  # Initial estimated cost

    closedVertices = set()  # Set of evaluated positions
    openVertices = set([start])  # Set of positions to be evaluated
    cameFrom = {}  # Map of navigated positions

    while len(openVertices) > 0:
        current = None
        currentFscore = None
        for pos in openVertices:
            # Find the position with the lowest F score
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        if current == end:
            # If the goal is reached, reconstruct the path
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[end]

        openVertices.remove(current)
        closedVertices.add(current)

        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue  # Ignore already evaluated neighbours
            candidateG = G[current] + graph.move_cost(current, neighbour)

            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue  # This is not a better path

            # Record the best path to the neighbour
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    raise RuntimeError("A* failed to find a solution")

if __name__ == "__main__":
    graph = AStarGraph()
    s1 = int(input("Enter row number for start point: "))
    s2 = int(input("Enter column number for start point: "))
    g1 = int(input("Enter row number for goal point: "))
    g2 = int(input("Enter column number for goal point: "))
    result, cost = AStarSearch((s1, s2), (g1, g2), graph)
    print("Route:", result)
    print("Cost:", cost)
```

---

## 🧾 Sample Output

```
Enter total number of barriers: 2
Enter row number for barrier point 1: 1
Enter column number for barrier point 1: 1
Enter row number for barrier point 2: 2
Enter column number for barrier point 2: 2
Enter row number for start point: 0
Enter column number for start point: 0
Enter row number for goal point: 3
Enter column number for goal point: 3

Route: [(0, 0), (1, 0), (2, 0), (3, 1), (3, 2), (3, 3)]
Cost: 5
```

---

## 🧠 Viva Tips

* A* uses **f(n) = g(n) + h(n)** cost function for optimal pathfinding.
* **g(n)** is actual cost, **h(n)** is heuristic estimation.
* **Admissible heuristic** never overestimates actual cost → guarantees optimal solution.
* Uses **priority queue** (open set) and **closed set** for efficient search.
* **Manhattan distance** is commonly used heuristic for grid-based pathfinding.
* **Time Complexity:** O(b^d) where b = branching factor, d = depth.
* **Space Complexity:** O(b^d) for storing open and closed sets.

---

## ✅ Conclusion

**A* algorithm** is a powerful pathfinding technique that combines optimality with efficiency.
It uses heuristics to guide search toward the goal while guaranteeing the shortest path.
Widely used in **game AI**, **robotics navigation**, and **GPS routing systems**.