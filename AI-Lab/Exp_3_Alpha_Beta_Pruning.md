# 🧠 Experiment 3: Alpha-Beta Pruning Algorithm for Game AI

## 🎯 Aim
To implement the **Alpha-Beta Pruning algorithm** as an optimization technique for the **Minimax algorithm** in a **Tic-Tac-Toe game** to demonstrate efficient game tree search and AI decision making.

---

## 📘 Theory (For Viva)

### 🎮 Alpha-Beta Pruning Overview
- **Concept:**  
  Alpha-Beta pruning is an optimization technique for the **Minimax algorithm** that eliminates branches in the game tree that cannot possibly influence the final decision.
- **Key Feature:** Maintains optimality while significantly reducing computation time
- **Applications:** Game AI (Chess, Checkers, Tic-Tac-Toe), decision trees, strategic planning.

### 🔢 Alpha-Beta Values
The algorithm maintains two crucial values:
- **Alpha (α)**: The best value that the **maximizing player** can guarantee so far
- **Beta (β)**: The best value that the **minimizing player** can guarantee so far

**Key Steps:**
1. Initialize α = -∞ and β = +∞
2. For each node, update α (for maximizing) or β (for minimizing)
3. If α ≥ β at any point, prune remaining branches
4. Return the optimal value without exploring pruned branches

**Algorithm:**
```
ALPHA_BETA(node, depth, alpha, beta, maximizing_player):
1. IF depth == 0 OR node is terminal:
   RETURN evaluate(node)

2. IF maximizing_player:
   max_eval = -∞
   FOR each child of node:
     eval = ALPHA_BETA(child, depth-1, alpha, beta, FALSE)
     max_eval = max(max_eval, eval)
     alpha = max(alpha, eval)
     IF beta <= alpha:
       BREAK  // β cutoff (prune)
   RETURN max_eval

3. ELSE: // minimizing player
   min_eval = +∞
   FOR each child of node:
     eval = ALPHA_BETA(child, depth-1, alpha, beta, TRUE)
     min_eval = min(min_eval, eval)
     beta = min(beta, eval)
     IF beta <= alpha:
       BREAK  // α cutoff (prune)
   RETURN min_eval
```

---

### 🎯 Minimax with Alpha-Beta in Tic-Tac-Toe
- **Game Representation:** 3×3 grid with values: 1 (Player X), -1 (Computer O), 0 (Empty)
- **Evaluation Function:** 
  - Player wins: +10 - depth (prefer faster wins)
  - Computer wins: depth - 10 (prefer delayed losses)
  - Draw: 0

**Pruning Condition:**
**If α ≥ β, prune remaining branches** because no better solution exists.

---

## 🧩 Algorithm Summary

| Aspect | Minimax | Alpha-Beta | Pure Search |
|--------|---------|------------|-------------|
| Data Structure | Game Tree | Game Tree (Pruned) | Full Exploration |
| Approach | Complete tree search | Intelligent pruning | Brute force |
| Uses | Game AI, Decision trees | Optimized game AI | Simple games |
| Time Complexity | O(b^d) | O(b^(d/2)) best case | O(b^d) |
| Space Complexity | O(d) | O(d) | O(d) |
| Optimality | ✅ | ✅ | ✅ |

**b** = branching factor, **d** = maximum depth

## Pruning Efficiency

#---

## 💻 Python Code

```python
from random import choice
from math import inf

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def print_board():
    chars = {1: 'X', -1: 'O', 0: ' '}
    for row in board:
        print('|'.join(f' {chars[cell]} ' for cell in row))
        print('-' * 11)

def check_winner():
    # Check rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0

def get_empty_cells():
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def minimax(depth, player, alpha, beta):
    winner = check_winner()
    
    if winner == 1: return 10 - depth
    if winner == -1: return depth - 10
    if not get_empty_cells(): return 0
    
    if player == 1:  # Maximizing
        max_eval = -inf
        for i, j in get_empty_cells():
            board[i][j] = 1
            eval = minimax(depth + 1, -1, alpha, beta)
            board[i][j] = 0
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break  # Pruning
        return max_eval
    else:  # Minimizing
        min_eval = inf
        for i, j in get_empty_cells():
            board[i][j] = -1
            eval = minimax(depth + 1, 1, alpha, beta)
            board[i][j] = 0
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: break  # Pruning
        return min_eval

def computer_move():
    best_score = inf
    best_move = None
    
    for i, j in get_empty_cells():
        board[i][j] = -1
        score = minimax(0, 1, -inf, inf)
        board[i][j] = 0
        
        if score < best_score:
            best_score = score
            best_move = (i, j)
    
    if best_move:
        board[best_move[0]][best_move[1]] = -1

def player_move():
    while True:
        try:
            pos = int(input('Enter position (1-9): ')) - 1
            row, col = pos // 3, pos % 3
            if 0 <= pos <= 8 and board[row][col] == 0:
                board[row][col] = 1
                break
            else:
                print('Invalid move!')
        except:
            print('Enter a number 1-9!')

def play_game():
    print("Tic-Tac-Toe (You: X, Computer: O)")
    print("Positions: 1-9 (left to right, top to bottom)")
    
    current_player = 1 if input('Play first? (y/n): ').lower() == 'y' else -1
    
    while True:
        print_board()
        
        if current_player == 1:
            player_move()
        else:
            computer_move()
            print("Computer's move:")
        
        winner = check_winner()
        if winner or not get_empty_cells():
            print_board()
            if winner == 1: print("You win!")
            elif winner == -1: print("Computer wins!")
            else: print("It's a draw!")
            break
        
        current_player *= -1

# Driver Code
if __name__ == "__main__":
    play_game()
```

---

## 🧾 Sample Output

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

|   |   |   |
-----------
|   | X |   |
-----------
|   |   |   |
-----------
Computer's move:
|   |   |   |
-----------
|   | X |   |
-----------
| O |   |   |
-----------
Enter position (1-9): 1

| X |   |   |
-----------
|   | X |   |
-----------
| O |   |   |
-----------
Computer's move:
| X |   |   |
-----------
|   | X | O |
-----------
| O |   |   |
-----------
```

---

## 🧠 Viva Tips

* Alpha-Beta pruning **maintains optimality** while dramatically reducing search time.
* **α (alpha)** tracks the best score for the **maximizing player**.
* **β (beta)** tracks the best score for the **minimizing player**.
* **Pruning condition:** If α ≥ β, eliminate remaining branches.
* **Best case improvement:** Time complexity reduces from O(b^d) to O(b^(d/2)).
* **Evaluation function** considers both win/loss and **depth** for strategic play.
* **Space complexity** remains O(d) same as regular Minimax.

---

## ✅ Conclusion

**Alpha-Beta pruning** is a crucial optimization that makes game-playing algorithms practical for real-world applications.
It demonstrates how intelligent pruning strategies can dramatically improve algorithm efficiency without compromising optimality.
Widely used in **game AI**, **decision trees**, and **strategic planning systems**.