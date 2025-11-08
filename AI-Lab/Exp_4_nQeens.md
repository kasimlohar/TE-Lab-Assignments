# 🧠 Experiment 4: N-Queens Problem Using Backtracking

## 🎯 Aim
To implement the **N-Queens problem** using **backtracking algorithm** to place N queens on an N×N chessboard such that no two queens attack each other, demonstrating constraint satisfaction problem solving.

---

## 📘 Theory (For Viva)

### 👑 N-Queens Problem Overview
- **Concept:**  
  The N-Queens problem is a classic constraint satisfaction problem where we place N queens on an N×N chessboard such that no two queens can attack each other.
- **Key Challenge:** Queens can attack horizontally, vertically, and diagonally
- **Applications:** Constraint satisfaction, VLSI design, task scheduling, resource allocation.

### 🔄 Backtracking Algorithm
- **Concept:**  
  Backtracking is a systematic method that builds solutions incrementally and abandons candidates (backtracks) when they cannot lead to a valid solution.
- **Strategy:** Try → Check → Backtrack if invalid → Try next option
- **Applications:** Puzzle solving, game AI, optimization problems.

**Key Steps:**
1. Place queens row by row starting from the first row
2. For each row, try placing queen in each column
3. Check if current placement is safe (no conflicts)
4. If safe, move to next row recursively
5. If not safe or no solution found, backtrack and try next column

**Algorithm:**
```
N_QUEENS(n):
1. Initialize board[n] = [-1, -1, ..., -1]
2. Initialize solutions = empty list
3. Call BACKTRACK(0)

BACKTRACK(row):
1. IF row == n:
   Add current board configuration to solutions
   RETURN

2. FOR col = 0 to n-1:
   IF IS_SAFE(board, row, col):
     Place queen at board[row] = col
     BACKTRACK(row + 1)
     // Implicit backtrack when function returns

IS_SAFE(board, row, col):
1. FOR i = 0 to row-1:
   IF board[i] == col:           // Same column
     RETURN FALSE
   IF board[i] - i == col - row: // Main diagonal
     RETURN FALSE  
   IF board[i] + i == col + row: // Anti-diagonal
     RETURN FALSE
2. RETURN TRUE
```

---

## 💻 Python Code

```python
# N-Queens Problem Implementation using Backtracking

def is_safe(board, row, col):
    # Check if no queens threaten the current cell in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * n  # Initialize an empty chessboard
    solutions = []
    backtrack(0)
    return solutions

def print_solution(board):
    for row in board:
        line = ['.'] * len(board)
        line[row] = 'Q'
        print(' '.join(line))
    print()

def main():
    try:
        n = int(input("Enter the number of queens (e.g., 4): "))
        if n < 4:
            print("The number of queens must be at least 4.")
            return
        solutions = solve_n_queens(n)
        if solutions:
            print(f"Found {len(solutions)} solution(s) for {n}-queens problem:")
            for i, solution in enumerate(solutions):
                print(f"Solution {i + 1}:")
                print_solution(solution)
        else:
            print(f"No solution found for {n}-queens problem.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
```

---

## 🧾 Sample Output

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

Enter the number of queens (e.g., 4): 8
Found 92 solution(s) for 8-queens problem:
Solution 1:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
...
```

---

## 🧠 Viva Tips

* **Backtracking** systematically explores solution space and **backtracks** when constraints are violated.
* **Constraint checking** happens in three directions: **column**, **main diagonal**, **anti-diagonal**.
* **1D array representation**: `board[row] = col` saves space and simplifies logic.
* **Time complexity**: O(N!) due to factorial permutations, but **pruning** significantly reduces actual searches.
* **Space complexity**: O(N) for board storage and recursion stack.
* **Diagonal formulas**: Main diagonal: `row - col = constant`, Anti-diagonal: `row + col = constant`.
* **Applications**: VLSI design, task scheduling, constraint satisfaction problems.

---

## ✅ Conclusion

The **N-Queens problem** demonstrates the power of **backtracking algorithms** in solving constraint satisfaction problems.
It showcases systematic search with intelligent pruning, making it efficient for practical problem sizes.
Widely used to teach **recursive problem solving** and **constraint satisfaction techniques** in AI and computer science.