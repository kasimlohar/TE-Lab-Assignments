# AI Lab Practical - Complete Code Guide

## 📋 Table of Contents
1. [Lab 1: Tic-Tac-Toe with Minimax](#lab-1)
2. [Lab 2: 8-Queens Problem (CSP)](#lab-2)
3. [Lab 3: Greedy Best First Search](#lab-3)
4. [Lab 4: A* Algorithm](#lab-4)
5. [Lab 6: Expert System](#lab-6)
6. [Quick Viva Guide](#viva)

---

## Lab 1: Tic-Tac-Toe with Minimax Algorithm {#lab-1}

### Complete Working Code

```python
import math

# Initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("-----------")
    print("\n")

# Check if there are moves left
def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False

# Evaluate the board
def evaluate(board):
    # Check rows for victory
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10
    
    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    
    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    
    # No winner
    return 0

# Minimax algorithm
def minimax(board, depth, is_max):
    score = evaluate(board)
    
    # If Maximizer has won
    if score == 10:
        return score - depth
    
    # If Minimizer has won
    if score == -10:
        return score + depth
    
    # If no moves left (draw)
    if not is_moves_left(board):
        return 0
    
    # Maximizer's move
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    
    # Minimizer's move
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

# Find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    print("Tic-Tac-Toe Game: You are 'O', AI is 'X'")
    print_board(board)
    
    while is_moves_left(board) and evaluate(board) == 0:
        # Player's move
        print("Your turn (O):")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        
        board[row][col] = 'O'
        print_board(board)
        
        if evaluate(board) == -10:
            print("You win!")
            break
        
        if not is_moves_left(board):
            print("It's a draw!")
            break
        
        # AI's move
        print("AI's turn (X):")
        move = find_best_move(board)
        board[move[0]][move[1]] = 'X'
        print(f"AI placed X at ({move[0]}, {move[1]})")
        print_board(board)
        
        if evaluate(board) == 10:
            print("AI wins!")
            break
        
        if not is_moves_left(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
```

### Key Concepts
- **Minimax**: Recursively evaluates all possible moves
- **Depth**: Used to prefer quicker wins
- **Pruning**: Can add alpha-beta pruning for optimization

---

## Lab 2: 8-Queens Problem (Constraint Satisfaction) {#lab-2}

### Complete Working Code

```python
# N-Queens Problem using Backtracking

def print_solution(board, n):
    """Print the board configuration"""
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n")

def is_safe(board, row, col, n):
    """Check if placing queen at (row, col) is safe"""
    
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, n):
    """Use backtracking to solve N-Queens"""
    
    # Base case: all queens placed
    if col >= n:
        return True
    
    # Try placing queen in all rows for current column
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen
            board[i][col] = 1
            
            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True
            
            # If placing queen doesn't lead to solution, backtrack
            board[i][col] = 0
    
    # If queen can't be placed in any row, return False
    return False

def solve_n_queens(n=8):
    """Main function to solve N-Queens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve_n_queens_util(board, 0, n):
        print(f"Solution does not exist for {n}-Queens")
        return False
    
    print(f"Solution for {n}-Queens Problem:")
    print_solution(board, n)
    return True

def solve_all_solutions(board, col, n, solutions):
    """Find all possible solutions"""
    if col >= n:
        # Save current solution
        solution = [row[:] for row in board]
        solutions.append(solution)
        return
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_all_solutions(board, col + 1, n, solutions)
            board[i][col] = 0

def find_all_solutions(n=8):
    """Find and print all solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_all_solutions(board, 0, n, solutions)
    
    print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
    
    # Print first 3 solutions
    for idx, sol in enumerate(solutions[:3]):
        print(f"Solution {idx + 1}:")
        print_solution(sol, n)

# Run the program
if __name__ == "__main__":
    # Find one solution
    solve_n_queens(8)
    
    # Find all solutions (optional)
    print("\n" + "="*30 + "\n")
    find_all_solutions(4)  # 4-Queens for demonstration
```

### Key Concepts
- **Backtracking**: Try placing queens column by column
- **Constraint Checking**: No two queens in same row, column, or diagonal
- **Pruning**: Abandon paths that violate constraints early

---

## Lab 3: Greedy Best First Search {#lab-3}

### Complete Working Code

```python
import heapq
import math

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  # Heuristic value
    
    def __lt__(self, other):
        return self.h < other.h
    
    def __eq__(self, other):
        return self.position == other.position

def heuristic(current, goal):
    """Calculate Manhattan distance"""
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def euclidean_heuristic(current, goal):
    """Calculate Euclidean distance"""
    return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

def get_neighbors(position, grid):
    """Get valid neighboring positions"""
    neighbors = []
    x, y = position
    rows, cols = len(grid), len(grid[0])
    
    # 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 1:
            neighbors.append((new_x, new_y))
    
    return neighbors

def greedy_best_first_search(grid, start, goal):
    """Implement Greedy Best First Search"""
    
    # Create start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)
    
    # Initialize open and closed lists
    open_list = []
    closed_set = set()
    
    # Add start node to open list
    heapq.heappush(open_list, start_node)
    
    nodes_explored = 0
    
    while open_list:
        # Get node with lowest heuristic value
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)
        nodes_explored += 1
        
        # Check if we reached the goal
        if current_node.position == goal_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            print(f"Nodes explored: {nodes_explored}")
            return path[::-1]  # Return reversed path
        
        # Generate children
        neighbors = get_neighbors(current_node.position, grid)
        
        for neighbor_pos in neighbors:
            # Skip if already visited
            if neighbor_pos in closed_set:
                continue
            
            # Create neighbor node
            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.h = heuristic(neighbor_pos, goal)
            
            # Check if neighbor is already in open list
            in_open = False
            for node in open_list:
                if node.position == neighbor_pos:
                    in_open = True
                    break
            
            if not in_open:
                heapq.heappush(open_list, neighbor_node)
    
    print("No path found!")
    return None

def print_grid_with_path(grid, path, start, goal):
    """Visualize the grid with the path"""
    rows, cols = len(grid), len(grid[0])
    display = [row[:] for row in grid]
    
    # Mark path
    for pos in path:
        if pos != start and pos != goal:
            display[pos[0]][pos[1]] = 2
    
    # Mark start and goal
    display[start[0]][start[1]] = 'S'
    display[goal[0]][goal[1]] = 'G'
    
    print("\nGrid (0=free, 1=obstacle, 2=path, S=start, G=goal):")
    for row in display:
        print(' '.join(str(cell) for cell in row))
    print()

# Example usage
if __name__ == "__main__":
    # Define grid (0 = free, 1 = obstacle)
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (7, 7)
    
    print("Greedy Best First Search")
    print(f"Start: {start}, Goal: {goal}\n")
    
    path = greedy_best_first_search(grid, start, goal)
    
    if path:
        print(f"Path found: {path}")
        print(f"Path length: {len(path)}")
        print_grid_with_path(grid, path, start, goal)
```

### Key Concepts
- **Heuristic Function**: Guides search toward goal
- **Priority Queue**: Explores most promising nodes first
- **Not Optimal**: May not find shortest path

---

## Lab 4: A* Search Algorithm {#lab-4}

### Complete Working Code

```python
import heapq
import math

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current to goal
        self.f = 0  # Total cost (g + h)
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.position == other.position

def heuristic(current, goal):
    """Manhattan distance heuristic"""
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def euclidean_heuristic(current, goal):
    """Euclidean distance heuristic"""
    return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

def get_neighbors(position, grid):
    """Get valid neighboring positions"""
    neighbors = []
    x, y = position
    rows, cols = len(grid), len(grid[0])
    
    # 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 1:
            neighbors.append((new_x, new_y))
    
    return neighbors

def a_star_search(grid, start, goal):
    """Implement A* Search Algorithm"""
    
    # Create start and goal nodes
    start_node = Node(start)
    start_node.g = start_node.h = start_node.f = 0
    goal_node = Node(goal)
    
    # Initialize open and closed lists
    open_list = []
    closed_set = set()
    
    # Add start node
    heapq.heappush(open_list, start_node)
    
    nodes_explored = 0
    
    while open_list:
        # Get node with lowest f value
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)
        nodes_explored += 1
        
        # Check if we reached the goal
        if current_node.position == goal_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            print(f"Nodes explored: {nodes_explored}")
            print(f"Path cost: {current_node.g}")
            return path[::-1]  # Return reversed path
        
        # Generate children
        neighbors = get_neighbors(current_node.position, grid)
        
        for neighbor_pos in neighbors:
            # Skip if already visited
            if neighbor_pos in closed_set:
                continue
            
            # Create neighbor node
            neighbor_node = Node(neighbor_pos, current_node)
            
            # Calculate g, h, and f values
            neighbor_node.g = current_node.g + 1  # Assuming cost = 1 for each move
            neighbor_node.h = heuristic(neighbor_pos, goal)
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            
            # Check if neighbor is in open list with higher g value
            add_to_open = True
            for idx, node in enumerate(open_list):
                if node.position == neighbor_pos and neighbor_node.g >= node.g:
                    add_to_open = False
                    break
            
            if add_to_open:
                heapq.heappush(open_list, neighbor_node)
    
    print("No path found!")
    return None

def print_grid_with_path(grid, path, start, goal):
    """Visualize the grid with the path"""
    rows, cols = len(grid), len(grid[0])
    display = [row[:] for row in grid]
    
    # Mark path
    for pos in path:
        if pos != start and pos != goal:
            display[pos[0]][pos[1]] = 2
    
    # Mark start and goal
    display[start[0]][start[1]] = 'S'
    display[goal[0]][goal[1]] = 'G'
    
    print("\nGrid (0=free, 1=obstacle, 2=path, S=start, G=goal):")
    for row in display:
        print(' '.join(str(cell) for cell in row))
    print()

# Example usage
if __name__ == "__main__":
    # Define grid (0 = free, 1 = obstacle)
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (7, 7)
    
    print("A* Search Algorithm")
    print(f"Start: {start}, Goal: {goal}\n")
    
    path = a_star_search(grid, start, goal)
    
    if path:
        print(f"Path found: {path}")
        print(f"Path length: {len(path)}")
        print_grid_with_path(grid, path, start, goal)
```

### Key Concepts
- **f(n) = g(n) + h(n)**: Total cost function
- **Optimal**: Always finds shortest path (with admissible heuristic)
- **Complete**: Always finds solution if one exists

---

## Lab 6: Expert System (Medical Diagnosis) {#lab-6}

### Complete Working Code

```python
class MedicalExpertSystem:
    def __init__(self):
        # Knowledge Base: Disease -> Symptoms mapping
        self.knowledge_base = {
            'Flu': ['fever', 'cough', 'sore_throat', 'body_ache', 'fatigue', 'headache'],
            'Common Cold': ['runny_nose', 'sneezing', 'sore_throat', 'cough', 'mild_fever'],
            'COVID-19': ['fever', 'cough', 'breathing_difficulty', 'fatigue', 'loss_of_taste', 'loss_of_smell'],
            'Malaria': ['high_fever', 'chills', 'sweating', 'headache', 'nausea', 'vomiting'],
            'Typhoid': ['sustained_fever', 'weakness', 'abdominal_pain', 'headache', 'loss_of_appetite'],
            'Dengue': ['high_fever', 'severe_headache', 'pain_behind_eyes', 'joint_pain', 'rash', 'nausea'],
            'Migraine': ['severe_headache', 'nausea', 'sensitivity_to_light', 'visual_disturbances'],
            'Pneumonia': ['fever', 'cough', 'chest_pain', 'breathing_difficulty', 'fatigue'],
            'Asthma': ['breathing_difficulty', 'wheezing', 'chest_tightness', 'cough'],
            'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'abdominal_pain', 'fever']
        }
        
        # Treatment advice
        self.treatments = {
            'Flu': 'Rest, drink plenty of fluids, take antiviral medications if prescribed.',
            'Common Cold': 'Rest, stay hydrated, use decongestants if needed.',
            'COVID-19': 'Isolate immediately, consult a doctor, get tested, monitor oxygen levels.',
            'Malaria': 'Seek immediate medical attention, antimalarial medications required.',
            'Typhoid': 'Consult a doctor immediately, antibiotics required.',
            'Dengue': 'Seek medical attention, stay hydrated, monitor platelet count.',
            'Migraine': 'Rest in dark room, pain relievers, avoid triggers.',
            'Pneumonia': 'Seek medical attention, antibiotics or antivirals may be needed.',
            'Asthma': 'Use inhaler, avoid triggers, consult pulmonologist.',
            'Food Poisoning': 'Stay hydrated, rest, seek medical help if severe.'
        }
    
    def get_symptoms_from_user(self):
        """Collect symptoms from user"""
        print("\n" + "="*60)
        print("MEDICAL EXPERT SYSTEM - SYMPTOM CHECKER")
        print("="*60)
        print("\nAvailable symptoms:")
        
        all_symptoms = set()
        for symptoms in self.knowledge_base.values():
            all_symptoms.update(symptoms)
        
        symptoms_list = sorted(list(all_symptoms))
        for idx, symptom in enumerate(symptoms_list, 1):
            print(f"{idx}. {symptom.replace('_', ' ').title()}")
        
        print("\nEnter the numbers of symptoms you are experiencing (comma-separated):")
        print("Example: 1,3,5")
        
        try:
            user_input = input("\nYour symptoms: ")
            indices = [int(x.strip()) - 1 for x in user_input.split(',')]
            user_symptoms = [symptoms_list[i] for i in indices if 0 <= i < len(symptoms_list)]
            return user_symptoms
        except:
            print("Invalid input!")
            return []
    
    def diagnose(self, user_symptoms):
        """Diagnose based on symptoms using forward chaining"""
        if not user_symptoms:
            print("No symptoms provided!")
            return None
        
        print(f"\nAnalyzing symptoms: {', '.join([s.replace('_', ' ').title() for s in user_symptoms])}")
        print("\n" + "-"*60)
        
        # Calculate match percentage for each disease
        disease_scores = {}
        
        for disease, disease_symptoms in self.knowledge_base.items():
            matching_symptoms = set(user_symptoms) & set(disease_symptoms)
            match_count = len(matching_symptoms)
            
            if match_count > 0:
                # Calculate confidence: (matching symptoms / total disease symptoms) * 100
                confidence = (match_count / len(disease_symptoms)) * 100
                disease_scores[disease] = {
                    'confidence': confidence,
                    'matching_count': match_count,
                    'total_symptoms': len(disease_symptoms),
                    'matching_symptoms': matching_symptoms
                }
        
        return disease_scores
    
    def display_diagnosis(self, disease_scores):
        """Display diagnosis results"""
        if not disease_scores:
            print("\nNo matching diseases found.")
            print("Recommendation: Consult a general physician for proper diagnosis.")
            return
        
        # Sort by confidence
        sorted_diseases = sorted(disease_scores.items(), 
                                key=lambda x: x[1]['confidence'], 
                                reverse=True)
        
        print("\nDIAGNOSIS RESULTS:")
        print("="*60)
        
        for rank, (disease, scores) in enumerate(sorted_diseases, 1):
            print(f"\n{rank}. {disease}")
            print(f"   Confidence: {scores['confidence']:.1f}%")
            print(f"   Matching symptoms: {scores['matching_count']}/{scores['total_symptoms']}")
            print(f"   Symptoms matched: {', '.join([s.replace('_', ' ').title() for s in scores['matching_symptoms']])}")
            
            if rank == 1:
                print(f"\n   RECOMMENDED ACTION:")
                print(f"   {self.treatments[disease]}")
        
        print("\n" + "="*60)
        print("⚠️  DISCLAIMER: This is a basic expert system for educational purposes.")
        print("   Always consult a qualified healthcare professional for proper diagnosis.")
        print("="*60)
    
    def run(self):
        """Main execution method"""
        while True:
            user_symptoms = self.get_symptoms_from_user()
            
            if user_symptoms:
                disease_scores = self.diagnose(user_symptoms)
                self.display_diagnosis(disease_scores)
            
            print("\n" + "-"*60)
            another = input("Would you like to check another diagnosis? (yes/no): ")
            if another.lower() != 'yes':
                print("\nThank you for using Medical Expert System!")
                break

# Alternative: Rule-based Expert System with explicit IF-THEN rules
class RuleBasedExpertSystem:
    def __init__(self):
        self.rules = []
        self.setup_rules()
    
    def setup_rules(self):
        """Define IF-THEN rules"""
        # Rule format: (conditions, conclusion, confidence)
        self.rules = [
            (['fever', 'cough', 'breathing_difficulty'], 'COVID-19 or Pneumonia', 0.8),
            (['high_fever', 'chills', 'sweating'], 'Malaria', 0.9),
            (['sustained_fever', 'weakness', 'abdominal_pain'], 'Typhoid', 0.85),
            (['fever', 'cough', 'body_ache'], 'Flu', 0.7),
            (['runny_nose', 'sneezing', 'sore_throat'], 'Common Cold', 0.75),
            (['severe_headache', 'sensitivity_to_light'], 'Migraine', 0.8),
        ]
    
    def apply_rules(self, symptoms):
        """Apply rules using forward chaining"""
        conclusions = []
        
        for conditions, conclusion, confidence in self.rules:
            if all(symptom in symptoms for symptom in conditions):
                conclusions.append((conclusion, confidence))
        
        return conclusions

# Run the expert system
if __name__ == "__main__":
    expert_system = MedicalExpertSystem()
    expert_system.run()
```

### Key Concepts
- **Knowledge Base**: IF-THEN rules mapping symptoms to diseases
- **Inference Engine**: Forward chaining to match symptoms
- **Confidence Score**: Percentage match of symptoms

---

## Quick Viva Questions & Answers {#viva}

### Lab 1: Minimax
**Q: What is Minimax?**
A: Algorithm for two-player games where one maximizes and other minimizes score.

**Q: Time complexity?**
A: O(b^d) where b=branching factor, d=depth

**Q: What is alpha-beta pruning?**
A: Optimization that eliminates branches that won't affect final decision.

### Lab 2: 8-Queens
**Q: What is CSP?**
A: Problem with variables, domains, and constraints to satisfy.

**Q: How does backtracking work?**
A: Build solution incrementally, backtrack when constraint violated.

**Q: Time complexity?**
A: O(N!) worst case, but pruning helps significantly.

### Lab 3: GBFS
**Q: How does GBFS work?**
A: Uses heuristic h(n) to select most promising node.

**Q: Is GBFS optimal?**
A: No, it may not find shortest path. Only considers heuristic, not actual cost.

**Q: Common heuristics?**
A: Manhattan distance, Euclidean distance, Chebyshev distance.

### Lab 4: A*
**Q: What is A* formula?**
A: f(n) = g(n) + h(n), where g=actual cost, h=heuristic estimate.

**Q: When is A* optimal?**
A: When heuristic is admissible (never overestimates).

**Q: Difference from Dijkstra?**
A: Dijkstra is A* with h(n)=0. A* is faster with good heuristic.

**Q: What is admissible heuristic?**
A: Heuristic that never overestimates actual cost to goal.

### Lab 6: Expert System
**Q: What is Expert System?**
A: AI that mimics human expert decision-making using knowledge base and rules.

**Q: Components?**
A: Knowledge Base, Inference Engine, User Interface, Explanation Facility.

**Q: Forward vs Backward chaining?**
A: Forward: data-driven (facts→conclusion). Backward: goal-driven (hypothesis→verify).

**Q: Advantages?**
A: Preserves expertise, consistent decisions, explains reasoning, available 24/7.

---

## 🎯 Quick Exam Tips

### Before Exam
1. **Practice typing** these programs at least once
2. **Understand logic** - don't just memorize
3. **Test with different inputs** to understand behavior
4. **Know time/space complexity** of each algorithm

### During Exam
1. **Read problem carefully** - note any modifications needed
2. **Write comments** - shows understanding
3. **Test incrementally** - don't write everything then test
4. **Handle edge cases** - empty inputs, invalid data
5. **Explain while coding** if examiner is watching

### Common Modifications Asked
- **Minimax**: Add alpha-beta pruning, change evaluation function
- **8-Queens**: Solve for N-Queens, find all solutions
- **GBFS/A***: Use different heuristics, diagonal movement, weighted edges
- **Expert System**: Add new diseases, implement backward chaining

---

## 📊 Algorithm Comparison Table

| Algorithm | Time Complexity | Space | Optimal | Complete | When to Use |
|-----------|----------------|-------|---------|----------|-------------|
| Minimax | O(b^d) | O(d) | Yes | Yes | Two-player games |
| Backtracking | O(N!) | O(N) | Yes | Yes | CSP, puzzles |
| GBFS | O(b^d) | O(b^d) | No | No | Fast solutions |
| A* | O(b^d) | O(b^d) | Yes* | Yes | Optimal pathfinding |

*A* is optimal only with admissible heuristic

---

## 🔑 Important Formulas

```
Minimax Score:
- Win: +10
- Loss: -10
- Draw: 0

A* Algorithm:
f(n) = g(n) + h(n)
- g(n) = actual cost from start
- h(n) = estimated cost to goal
- f(n) = total estimated cost

Manhattan Distance:
h = |x1 - x2| + |y1 - y2|

Euclidean Distance:
h = √[(x1-x2)² + (y1-y2)²]

Expert System Confidence:
confidence = (matching_symptoms / total_symptoms) × 100
```

---

## 💡 Common Errors to Avoid

### 1. Index Out of Bounds
```python
# Wrong
if board[i][j]:  # might go out of bounds

# Right
if 0 <= i < len(board) and 0 <= j < len(board[0]):
```

### 2. Infinite Loops in Search
```python
# Wrong - no visited check
def search(node):
    for neighbor in node.neighbors:
        search(neighbor)  # may revisit

# Right
visited = set()
def search(node):
    if node in visited:
        return
    visited.add(node)
```

### 3. Heuristic Not Admissible
```python
# Wrong - overestimates
def heuristic(current, goal):
    return (abs(current[0]-goal[0]) + abs(current[1]-goal[1])) * 2

# Right - admissible
def heuristic(current, goal):
    return abs(current[0]-goal[0]) + abs(current[1]-goal[1])
```

### 4. Forgetting Backtracking
```python
# Wrong - no backtrack
board[i][j] = 'Q'
if solve(board, col+1):
    return True
# Missing: board[i][j] = '.'

# Right
board[i][j] = 'Q'
if solve(board, col+1):
    return True
board[i][j] = '.'  # Backtrack
```

---

## 📝 Sample Viva Scenarios

### Scenario 1: Code Modification
**Examiner**: "Modify A* to allow diagonal movement."

**Answer**: 
```python
# Add diagonal directions to get_neighbors
directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),  # original 4
    (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonals
]

# Adjust cost for diagonal moves
if abs(dx) + abs(dy) == 2:  # diagonal
    neighbor_node.g = current_node.g + 1.414  # √2
else:
    neighbor_node.g = current_node.g + 1
```

### Scenario 2: Algorithm Comparison
**Examiner**: "Why use A* instead of GBFS?"

**Answer**: "A* guarantees optimal path while GBFS doesn't. A* considers both actual cost g(n) and heuristic h(n), so it finds shortest path. GBFS only uses h(n), so it's faster but may miss shorter routes. Use A* when optimality matters (GPS navigation), use GBFS when speed matters (game AI with limited time)."

### Scenario 3: Debugging
**Examiner**: "This Minimax code returns wrong results. Why?"

**Answer**: Check these common issues:
1. Evaluation function returning wrong scores
2. Not alternating between max and min players
3. Terminal condition not properly checked
4. Board state not properly restored after recursive call
5. Depth parameter causing premature cutoff

### Scenario 4: Complexity Analysis
**Examiner**: "Calculate time complexity for 8-Queens with N=8."

**Answer**: "Without pruning, it's O(8^8) as we try 8 positions in each of 8 columns. But backtracking prunes invalid branches early, reducing it significantly to around O(N!) in practice, which is about O(40,320) for N=8, much better than O(16,777,216)."

---

## 🎓 Final Checklist

### Knowledge Checklist
- [ ] Can explain Minimax algorithm and trace example
- [ ] Know how backtracking works with 8-Queens
- [ ] Understand difference between GBFS and A*
- [ ] Can calculate h(n), g(n), f(n) for A*
- [ ] Know what makes heuristic admissible
- [ ] Understand forward/backward chaining in Expert Systems
- [ ] Can write and explain each algorithm's pseudocode

### Coding Checklist
- [ ] Can code Minimax from scratch
- [ ] Can implement backtracking for N-Queens
- [ ] Can write GBFS with priority queue
- [ ] Can implement A* with proper f(n) calculation
- [ ] Can create basic Expert System with rules
- [ ] Know how to handle edge cases in each

### Viva Preparation Checklist
- [ ] Know time/space complexity of all algorithms
- [ ] Can compare algorithms (when to use which)
- [ ] Understand trade-offs (optimal vs fast)
- [ ] Can explain real-world applications
- [ ] Ready to modify code as requested
- [ ] Can debug common errors

---

## 🚀 Last Minute Revision (30 minutes before exam)

### Minute 1-10: Algorithms
- Minimax: Max/min alternation, terminal states
- Backtracking: Try, check, recurse, backtrack
- GBFS: h(n) only, priority queue
- A*: f(n) = g(n) + h(n), optimal with admissible h

### Minute 11-20: Key Concepts
- Admissible heuristic: never overestimates
- Manhattan: |x1-x2| + |y1-y2|
- Forward chaining: data → conclusion
- Alpha-beta: prune min-max tree

### Minute 21-30: Code Patterns
- Always check bounds: `0 <= i < len(array)`
- Use visited set in searches
- Restore state in backtracking
- Priority queue for GBFS/A*
- Parent pointer for path reconstruction

---

**Best of luck for your practical exam! 🌟**

**Remember**: Understanding > Memorization. If you understand the logic, you can write any variation of the code!