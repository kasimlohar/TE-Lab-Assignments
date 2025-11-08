# Experiment 2: A* (A-Star) Algorithm

## What is A* Algorithm?

A* (pronounced "A-star") is a graph traversal and path search algorithm that finds the optimal path from a start node to a goal node. It's widely used in pathfinding and graph traversal because it combines the benefits of Dijkstra's algorithm (guarantees shortest path) with the efficiency of greedy best-first search (uses heuristics).

## How A* Works

A* uses a **cost function** f(n) = g(n) + h(n) where:
- **g(n)**: Actual cost from start to current node
- **h(n)**: Heuristic (estimated cost from current node to goal)
- **f(n)**: Total estimated cost of path through node n

### Algorithm Steps:
1. Initialize open set with start node
2. While open set is not empty:
   - Select node with lowest f(n) from open set
   - If it's the goal, reconstruct path
   - Move node from open to closed set
   - For each neighbor:
     - Calculate tentative g score
     - If better path found, update scores and parent

## Key Components in Our Implementation

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

## A* vs Other Algorithms

| Algorithm | Optimality | Time Complexity | Space Complexity |
|-----------|------------|-----------------|------------------|
| BFS | ✅ (unweighted) | O(b^d) | O(b^d) |
| DFS | ❌ | O(b^m) | O(bm) |
| Dijkstra | ✅ | O((V+E)logV) | O(V) |
| **A*** | ✅ (with admissible heuristic) | O(b^d) | O(b^d) |

**b** = branching factor, **d** = depth of solution, **m** = maximum depth

## Advantages of A*

1. **Optimal**: Guarantees shortest path if heuristic is admissible
2. **Efficient**: Uses heuristic to guide search toward goal
3. **Complete**: Will find solution if one exists
4. **Flexible**: Can work with different heuristics and cost functions

## Properties of Good Heuristics

### Admissible Heuristic
- Never overestimates the actual cost to reach goal
- h(n) ≤ actual cost from n to goal
- Ensures A* finds optimal solution

### Consistent Heuristic
- h(n) ≤ cost(n, n') + h(n') for every edge (n, n')
- Stronger than admissibility
- Ensures optimal substructure

## Running the Code

```bash
python Exp_2_AStar.py
```

### Sample Input/Output:
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

## Applications

- **Game AI**: NPC pathfinding in games
- **Robotics**: Robot navigation and motion planning
- **GPS Navigation**: Route finding in maps
- **Network Routing**: Finding optimal paths in networks
- **Puzzle Solving**: 8-puzzle, 15-puzzle solutions

## Implementation Notes

- Uses sets for open and closed lists for O(1) lookup
- Reconstructs path by backtracking through parent pointers
- Handles grid boundaries and obstacles
- Returns both optimal path and total cost

The A* algorithm is fundamental in AI and computer science, providing an excellent balance between optimality and efficiency for pathfinding problems.