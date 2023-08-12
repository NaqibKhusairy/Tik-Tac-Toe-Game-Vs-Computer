import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def draw_board(board):
    print("+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print("\n+---+---+---+")

def check_win_horizontal(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    return '-'

def check_win_vertical(board):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    return '-'

def check_win_diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return '-'

def get_input(player, board):
    try:
        if player == 1:
            input_text = input("CHOOSE BOX: ")
            input_value = int(input_text) - 1

            row = input_value // 3
            col = input_value % 3

            if board[row][col] != ' ':
                print("Box already taken. Please try again.")
                return False

            board[row][col] = 'X'
        else:
            available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
            if not available_moves:
                return False
            
            row, col = random.choice(available_moves)
            print("Computer Is Thiking")
            board[row][col] = 'O'
        
        return True
    except ValueError:
        print("Invalid input. Please enter a number from [ 1 - 9 ].")
        return False

board = initialize_board()
player = 1
winner = '-'
print("TIC TAC TOE GAME")

while winner == '-':
    print()
    draw_board(board)
        
    if player == 1:
        print("TURN: X")
    else:
        print("TURN: O")
    
    while not get_input(player, board):
        pass

    winner = check_win_horizontal(board)
    if winner == '-':
        winner = check_win_vertical(board)
    if winner == '-':
        winner = check_win_diagonal(board)

    player *= -1

print("WINNER IS", winner)
draw_board(board)
