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