# Experiment 4: N-Queens Problem

## Overview

The N-Queens problem is a classic constraint satisfaction problem in computer science and artificial intelligence. The challenge is to place N chess queens on an N×N chessboard such that no two queens attack each other.

## Problem Statement

Given an N×N chessboard, place N queens such that:
- No two queens are in the same row
- No two queens are in the same column  
- No two queens are on the same diagonal

## Theory and Algorithm

### Backtracking Algorithm

The N-Queens problem is solved using **backtracking**, which is a systematic method for solving constraint satisfaction problems by:

1. **Incremental Construction**: Build solution step by step
2. **Constraint Checking**: Verify constraints at each step
3. **Backtrack**: Undo choices when constraints are violated
4. **Explore Alternatives**: Try different possibilities systematically

### Algorithm Steps

```
function solveNQueens(n):
    board = array of size n, initialized to -1
    solutions = empty list
    
    function backtrack(row):
        if row == n:
            add current board to solutions
            return
        
        for col from 0 to n-1:
            if isSafe(board, row, col):
                place queen at (row, col)
                backtrack(row + 1)
                remove queen (implicit backtrack)
    
    backtrack(0)
    return solutions
```

### Constraint Checking

The [`is_safe`](Exp_4_nQeens.py) function checks three types of conflicts:

#### 1. Column Conflict
```python
board[i] == col
```
Checks if any queen in previous rows is in the same column.

#### 2. Main Diagonal Conflict
```python
board[i] - i == col - row
```
Queens on the main diagonal (top-left to bottom-right) have the property that `row - col` is constant.

#### 3. Anti-Diagonal Conflict
```python
board[i] + i == col + row
```
Queens on the anti-diagonal (top-right to bottom-left) have the property that `row + col` is constant.

## Implementation Details

### Board Representation
- **1D Array**: `board[row] = col` means queen at position (row, col)
- **Space Efficient**: O(n) space instead of O(n²)
- **Fast Access**: Direct indexing for constraint checking

### Key Functions

#### [`solve_n_queens`](Exp_4_nQeens.py)
- Main solving function using backtracking
- Returns list of all valid solutions
- Uses nested [`backtrack`](Exp_4_nQeens.py) function for recursion

#### [`print_solution`](Exp_4_nQeens.py)
- Converts board representation to visual format
- Uses 'Q' for queens and '.' for empty squares
- Displays each solution clearly

## Complexity Analysis

### Time Complexity
- **Worst Case**: O(N!)
- **Average Case**: Much better due to early pruning
- **Pruning Factor**: Constraint checking eliminates many branches early

### Space Complexity
- **Recursion Stack**: O(N) for recursive calls
- **Board Storage**: O(N) for board representation
- **Total**: O(N)

## Mathematical Properties

### Number of Solutions

| N | Solutions |
|---|-----------|
| 1 | 1 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 8 | 92 |
| 10 | 724 |

### Symmetries
- Each solution has up to 8 symmetric variants
- Rotations: 0°, 90°, 180°, 270°
- Reflections: horizontal, vertical, diagonal

## Running the Code

```bash
python Exp_4_nQeens.py
```

### Sample Execution

```
Enter the number of queens (e.g., 4): 4
Found 2 solution(s) for 4-queens problem:
Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .
```

## Optimization Techniques

### 1. Early Constraint Checking
- Check constraints before placing queen
- Avoid invalid placements entirely
- Reduces search tree significantly

### 2. Heuristic Improvements
- **Most Constrained Variable**: Choose row/column with fewest options
- **Least Constraining Value**: Choose placement that eliminates fewest future options

### 3. Symmetry Breaking
- Fix first queen position to reduce equivalent solutions
- Can reduce search space by factor of 8

## Applications and Extensions

### Real-World Applications
- **VLSI Design**: Component placement on circuit boards
- **Task Scheduling**: Resource allocation with conflicts
- **Graph Coloring**: Conflict-free assignment problems
- **Facility Location**: Placing facilities to avoid interference

### Problem Variations
- **Minimum Queens**: Find minimum queens to attack all squares
- **Super Queens**: Queens that also move like knights
- **Toroidal Board**: Wrap-around edges
- **3D N-Queens**: Extension to three dimensions

## Educational Value

### Concepts Demonstrated
- **Backtracking Algorithm**: Systematic search with pruning
- **Constraint Satisfaction**: Managing multiple constraints
- **Recursion**: Clean recursive problem decomposition
- **State Space Search**: Exploring solution space efficiently

### Learning Objectives
- Understand backtracking paradigm
- Learn constraint satisfaction techniques
- Practice recursive problem solving
- Analyze algorithmic complexity

## Historical Context

- **Origin**: First studied by chess player Max Bezzel in 1848
- **8-Queens**: Classic version with 92 solutions
- **Computer Science**: Became standard AI problem in 1960s
- **Modern Usage**: Benchmark for constraint satisfaction algorithms

## Error Handling

The implementation includes robust error handling:

```python
try:
    n = int(input("Enter the number of queens (e.g., 4): "))
    if n < 4:
        print("The number of queens must be at least 4.")
        return
except ValueError:
    print("Invalid input. Please enter a valid integer.")
```

## Conclusion

The N-Queens problem elegantly demonstrates the power of backtracking algorithms in solving constraint satisfaction problems. It provides an excellent introduction to systematic search techniques while being simple enough to understand and implement, yet complex enough to showcase important algorithmic concepts.

The backtracking solution efficiently prunes the search space by checking constraints early, making it practical for reasonable values of N while providing all possible solutions to the problem.