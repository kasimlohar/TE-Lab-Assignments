# AI Lab Practical Quick Learning Guide

## 📋 Table of Contents
1. [Lab 1: Tic-Tac-Toe with Minimax](#lab-1)
2. [Lab 2: Constraint Satisfaction (8-Queens)](#lab-2)
3. [Lab 3: Greedy Best First Search](#lab-3)
4. [Lab 4: A* Algorithm](#lab-4)
5. [Lab 6: Expert System](#lab-6)
6. [Viva Questions & Answers](#viva)

---

## Lab 1: Tic-Tac-Toe with Minimax Algorithm {#lab-1}

### Core Concept
Minimax is a decision-making algorithm for two-player zero-sum games. It minimizes the possible loss for a worst-case scenario.

### Key Points
- **Maximizer**: AI player trying to maximize score
- **Minimizer**: Opponent trying to minimize score
- **Terminal States**: Win (+10), Loss (-10), Draw (0)
- **Recursion**: Explores all possible game states

### Algorithm Steps
1. Check if game is in terminal state (win/loss/draw)
2. If maximizer's turn: choose move with maximum score
3. If minimizer's turn: choose move with minimum score
4. Recursively evaluate all possible moves
5. Return best move based on scores

### Code Structure
```python
def minimax(board, depth, isMax):
    score = evaluate(board)
    if score != 0 or no_moves_left:
        return score
    
    if isMax:
        return max(minimax for all moves)
    else:
        return min(minimax for all moves)
```

---

## Lab 2: Constraint Satisfaction Problem (8-Queens) {#lab-2}

### Core Concept
Place 8 queens on a chessboard such that no two queens attack each other (no same row, column, or diagonal).

### Key Points
- **Backtracking**: Try placing queens column by column
- **Constraint Checking**: Verify no conflicts before placing
- **Pruning**: Abandon branches that violate constraints early

### Conflict Checking
- Same column: `board[i] == board[col]`
- Same diagonal: `abs(board[i] - board[col]) == abs(i - col)`

### Algorithm Steps
1. Start from leftmost column
2. Try placing queen in each row
3. Check if placement is safe
4. If safe, recursively solve for next column
5. If not safe or recursive call fails, backtrack
6. Return solution when all queens placed

### Time Complexity
- Worst case: O(N!)
- With pruning: Much better in practice

---

## Lab 3: Greedy Best First Search {#lab-3}

### Core Concept
Informed search algorithm that uses a heuristic function to select the most promising node to explore next.

### Key Points
- **Heuristic Function (h(n))**: Estimates cost from current node to goal
- **Priority Queue**: Explores nodes with lowest h(n) first
- **Not Optimal**: May not find shortest path
- **Fast**: Often finds solution quickly

### Common Heuristics
- **Manhattan Distance**: |x1-x2| + |y1-y2|
- **Euclidean Distance**: √[(x1-x2)² + (y1-y2)²]

### Algorithm Steps
1. Add start node to priority queue with h(n) value
2. Pop node with minimum h(n)
3. If goal reached, return path
4. Generate neighbors
5. Add unvisited neighbors to queue with their h(n) values
6. Repeat until goal found or queue empty

### Comparison
| Feature | GBFS | A* |
|---------|------|-----|
| Uses h(n) | Yes | Yes |
| Uses g(n) | No | Yes |
| Optimal | No | Yes |
| Complete | No (can get stuck) | Yes |

---

## Lab 4: A* Search Algorithm {#lab-4}

### Core Concept
Optimal pathfinding algorithm combining actual cost and heuristic estimate: **f(n) = g(n) + h(n)**

### Key Components
- **g(n)**: Actual cost from start to current node
- **h(n)**: Heuristic estimate from current node to goal
- **f(n)**: Total estimated cost through current node

### Key Properties
- **Admissible Heuristic**: h(n) never overestimates actual cost
- **Consistent Heuristic**: h(n1) ≤ cost(n1,n2) + h(n2)
- **Optimal**: Finds shortest path if heuristic is admissible
- **Complete**: Always finds solution if one exists

### Algorithm Steps
1. Add start node to open list with f(n) = h(n)
2. While open list not empty:
   - Pop node with minimum f(n)
   - If goal, reconstruct path
   - For each neighbor:
     - Calculate g(n) = current g + edge cost
     - Calculate f(n) = g(n) + h(n)
     - Add to open list if not visited or better path found
3. Return path or failure

### Data Structures
- **Open List**: Priority queue of nodes to explore
- **Closed List**: Set of already explored nodes
- **Parent Map**: Track path for reconstruction

---

## Lab 6: Expert System (Medical Diagnosis) {#lab-6}

### Core Concept
Knowledge-based system that emulates decision-making of a human expert using IF-THEN rules.

### Components
1. **Knowledge Base**: Collection of rules and facts
2. **Inference Engine**: Applies rules to facts to derive conclusions
3. **User Interface**: Collects symptoms and displays diagnosis

### Rule Structure
```
IF symptom1 AND symptom2 AND symptom3
THEN disease_name
```

### Types of Inference
- **Forward Chaining**: Data-driven (symptoms → diagnosis)
- **Backward Chaining**: Goal-driven (hypothesis → verify symptoms)

### Implementation Steps
1. Define disease-symptom rules dictionary
2. Get symptoms from user
3. Match symptoms against rules
4. Count matching symptoms for each disease
5. Suggest disease with highest match
6. Provide confidence level or treatment advice

### Advantages
- Preserves expert knowledge
- Consistent decision-making
- Explains reasoning
- Available 24/7

### Limitations
- Limited to coded knowledge
- Cannot learn from experience (unless ML added)
- May struggle with uncertain/incomplete data

---

## Viva Questions & Answers {#viva}

### General AI Concepts

**Q: What is Artificial Intelligence?**
A: AI is the simulation of human intelligence in machines programmed to think, learn, and solve problems. It includes machine learning, natural language processing, computer vision, and expert systems.

**Q: What are search algorithms in AI?**
A: Systematic methods to explore problem spaces to find solutions. Two types: Uninformed (BFS, DFS) and Informed (A*, GBFS).

**Q: What is a heuristic?**
A: A rule of thumb or estimate that guides search toward the goal without guaranteeing optimality. Example: straight-line distance in pathfinding.

---

### Lab 1: Minimax

**Q: What is the Minimax algorithm?**
A: Decision-making algorithm for two-player games where one player maximizes their advantage while the other minimizes it.

**Q: What is alpha-beta pruning?**
A: Optimization technique for Minimax that eliminates branches that won't affect final decision, reducing computation.

**Q: Time complexity of Minimax?**
A: O(b^d) where b is branching factor and d is depth. With alpha-beta pruning: O(b^(d/2)) best case.

**Q: Why is it called "zero-sum" game?**
A: One player's gain equals other player's loss; total payoff is zero.

---

### Lab 2: CSP & Backtracking

**Q: What is a Constraint Satisfaction Problem?**
A: Problem defined by variables, domains, and constraints. Goal is to find assignment satisfying all constraints.

**Q: How does backtracking work?**
A: Incremental approach that builds solution step by step and abandons path when constraint violated.

**Q: What is the N-Queens problem?**
A: Place N queens on N×N chessboard so no two queens attack each other.

**Q: What are forward checking and constraint propagation?**
A: Techniques to detect failures early by checking constraints before making assignments.

---

### Lab 3: Greedy Best First Search

**Q: How does GBFS differ from BFS?**
A: GBFS uses heuristic to prioritize promising nodes; BFS explores all nodes at current level first.

**Q: Is GBFS complete and optimal?**
A: Not complete (can get stuck in loops) and not optimal (may miss shorter paths).

**Q: When to use GBFS?**
A: When fast solution is more important than optimal solution, and good heuristic is available.

**Q: What happens if heuristic is poor?**
A: Performance degrades, may explore many unnecessary nodes or fail to find solution.

---

### Lab 4: A* Algorithm

**Q: How does A* differ from GBFS?**
A: A* uses f(n) = g(n) + h(n), considering both actual and estimated cost. GBFS only uses h(n).

**Q: What makes a heuristic admissible?**
A: Never overestimates actual cost to goal (h(n) ≤ actual cost).

**Q: What is monotonicity/consistency?**
A: h(n1) ≤ cost(n1,n2) + h(n2) for all nodes. Ensures h(n) doesn't decrease faster than actual cost.

**Q: Why is A* optimal?**
A: With admissible heuristic, it always finds lowest-cost path because it explores nodes in order of total cost.

**Q: Difference between Dijkstra and A*?**
A: Dijkstra is A* with h(n) = 0. A* is faster with good heuristic.

---

### Lab 6: Expert Systems

**Q: What is an Expert System?**
A: AI program that uses knowledge base and inference rules to solve complex problems in specific domain.

**Q: Components of Expert System?**
A: Knowledge Base, Inference Engine, User Interface, Explanation Facility.

**Q: Forward vs Backward Chaining?**
A: Forward: data-driven, starts with facts → conclusions. Backward: goal-driven, starts with hypothesis → verify facts.

**Q: Advantages of Expert Systems?**
A: Preserve expertise, consistent decisions, explain reasoning, available 24/7, handle uncertainty.

**Q: Limitations?**
A: Limited to coded knowledge, expensive to build, cannot learn without update, difficulty with common sense.

---

### Comparison Questions

**Q: Compare uninformed vs informed search**
| Uninformed | Informed |
|------------|----------|
| No domain knowledge | Uses heuristics |
| BFS, DFS, UCS | A*, GBFS |
| Slower, explores more | Faster, goal-directed |
| Complete (BFS) | Not always complete |

**Q: When to use which algorithm?**
- **Minimax**: Two-player games
- **Backtracking**: Constraint satisfaction, puzzles
- **GBFS**: Quick solutions, good heuristic available
- **A***: Optimal pathfinding needed
- **Expert Systems**: Domain-specific diagnosis/decisions

---

## 🎯 Quick Tips for Practical Exam

1. **Time Management**: Understand all algorithms but master 3-4 thoroughly
2. **Code Structure**: Write clean, commented code with clear function names
3. **Test Cases**: Prepare sample inputs/outputs for each algorithm
4. **Debugging**: Know common errors (index errors, infinite loops, wrong heuristics)
5. **Explanation**: Be ready to explain each line of important code
6. **Complexity**: Know time/space complexity of each algorithm
7. **Modifications**: Be prepared to modify algorithms (different heuristics, constraints)

## 📝 Common Practical Tasks

- Implement algorithm from scratch
- Modify existing code (change heuristic, add feature)
- Debug given code
- Explain algorithm working on given example
- Compare two algorithms
- Trace algorithm execution step-by-step

---

## 🔑 Key Formulas to Remember

- **A***: f(n) = g(n) + h(n)
- **Manhattan Distance**: |x₁-x₂| + |y₁-y₂|
- **Euclidean Distance**: √[(x₁-x₂)² + (y₁-y₂)²]
- **Minimax Depth**: Depth affects search space exponentially
- **CSP Variables**: Variables × Domain size = Search space

---

**Good luck with your practical exam! Focus on understanding concepts, not just memorizing code.**