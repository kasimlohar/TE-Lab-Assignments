# Experiment 3: Alpha-Beta Pruning Algorithm

## What is Alpha-Beta Pruning?

Alpha-Beta pruning is an optimization technique for the **Minimax algorithm** used in game theory and decision-making. It significantly reduces the number of nodes evaluated in the search tree by eliminating branches that cannot possibly influence the final decision.

## How Alpha-Beta Pruning Works

The algorithm maintains two values:
- **Alpha (α)**: The best value that the **maximizing player** can guarantee so far
- **Beta (β)**: The best value that the **minimizing player** can guarantee so far

### Key Principle: Pruning Condition
**If α ≥ β, prune the remaining branches**

This happens because:
- Maximizing player will choose a value ≥ α
- Minimizing player will choose a value ≤ β
- If α ≥ β, no better solution exists in this branch

## Algorithm Steps

```
function alphabeta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node is terminal:
        return heuristic_value(node)
    
    if maximizing_player:
        max_eval = -∞
        for each child of node:
            eval = alphabeta(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # β cutoff (prune)
        return max_eval
    else:
        min_eval = +∞
        for each child of node:
            eval = alphabeta(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # α cutoff (prune)
        return min_eval
```

## Tic-Tac-Toe Implementation Details

### Game Representation
- **Board**: 3x3 matrix with values:
  - `1`: Player X (Human)
  - `-1`: Player O (Computer)
  - `0`: Empty cell

### Evaluation Function
```python
if winner == 1: return 10 - depth    # Player wins (minimize computer's advantage)
if winner == -1: return depth - 10   # Computer wins (maximize computer's advantage)
if no moves: return 0                # Draw
```

The depth factor ensures:
- **Faster wins are preferred** (lower depth = higher score)
- **Delayed losses are preferred** (higher depth = less negative score)

### Movement Strategy
- **Computer (Minimizing Player)**: Seeks lowest score (best for computer)
- **Player (Maximizing Player)**: Algorithm assumes player seeks highest score

## Alpha-Beta vs Pure Minimax

| Aspect | Minimax | Alpha-Beta |
|--------|---------|------------|
| **Optimality** | ✅ Optimal | ✅ Optimal (same result) |
| **Time Complexity** | O(b^d) | O(b^(d/2)) in best case |
| **Space Complexity** | O(d) | O(d) |
| **Pruning** | ❌ None | ✅ Significant branch elimination |

Where:
- **b** = branching factor (average moves per position)
- **d** = maximum depth of search tree

## Pruning Efficiency

### Best Case Scenario
- Nodes are ordered optimally (best moves first)
- Time complexity reduces from O(b^d) to O(b^(d/2))
- **Up to 50% reduction** in nodes evaluated

### Worst Case Scenario
- Nodes are ordered poorly (worst moves first)
- No pruning occurs
- Performance equals standard Minimax

## Key Features in Our Implementation

### 1. Game State Evaluation
```python
def check_winner():
    # Check all rows, columns, and diagonals
    # Returns: 1 (Player wins), -1 (Computer wins), 0 (No winner yet)
```

### 2. Alpha-Beta Pruning Logic
```python
if player == 1:  # Maximizing
    alpha = max(alpha, eval)
    if beta <= alpha: break  # β cutoff
else:  # Minimizing  
    beta = min(beta, eval)
    if beta <= alpha: break  # α cutoff
```

### 3. Computer Move Selection
```python
def computer_move():
    best_score = inf  # Computer wants minimum score
    for each possible move:
        score = minimax(0, 1, -inf, inf)  # Start with α=-∞, β=+∞
        if score < best_score:
            best_score = score
            best_move = current_move
```

## Advantages of Alpha-Beta Pruning

1. **Significant Performance Improvement**: Reduces search space dramatically
2. **Maintains Optimality**: Same result as Minimax, but faster
3. **Memory Efficient**: No additional memory overhead
4. **Widely Applicable**: Works with any zero-sum game

## Applications

- **Game AI**: Chess, Checkers, Go, Tic-Tac-Toe
- **Decision Trees**: Business and financial decision making
- **Resource Allocation**: Optimization problems
- **Strategic Planning**: Military and competitive scenarios

## Running the Code

```bash
python Exp_3_Alpa_beta_prun.py
```

### Sample Game Session:
```
Tic-Tac-Toe (You: X, Computer: O)
Positions: 1-9 (left to right, top to bottom)
Play first? (y/n): y

|   |   |   |
-----------
|   |   |   |
-----------
|   |   |   |
-----------
Enter position (1-9): 5

| X |   |   |
-----------
|   | X |   |
-----------
|   |   |   |
-----------
Computer's move:
| X |   |   |
-----------
|   | X |   |
-----------
| O |   |   |
-----------
```

## Complexity Analysis

### Time Complexity
- **Average Case**: O(b^(3d/4))
- **Best Case**: O(b^(d/2))
- **Worst Case**: O(b^d)

### Space Complexity
- **O(d)** where d is maximum depth
- Same as Minimax (recursive call stack)

## Optimization Techniques

### 1. Move Ordering
- Evaluate promising moves first
- Increases pruning effectiveness
- Can use domain knowledge or heuristics

### 2. Iterative Deepening
- Search incrementally deeper levels
- Provides early results
- Better move ordering for deeper searches

### 3. Transposition Tables
- Cache previously computed positions
- Avoid redundant calculations
- Significant speedup in practice

## Conclusion

Alpha-Beta pruning is a crucial optimization that makes game-playing algorithms practical for real-world applications. It demonstrates how intelligent pruning strategies can dramatically improve algorithm efficiency without