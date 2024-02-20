import random

board = ['-', '-', '-',
         '-', '-', '-',
        '-', '-', '-']

current_player = 'X'
winner = None
game_running = True




#function to print game board
def print_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])

#function to take player input
def player_input(board):
    input_funct = int(input('Enter a number 1-9: '))

    if input_funct >= 1 and input_funct <= 9 and board[input_funct - 1] == '-':
        board[input_funct - 1] = current_player
    else:
        print("Invalid move, please try again.")

#function to check for win or draw
def check_horizontal(board):
    global winner

    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    
def check_draw(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print('There is no winner! The game is a draw.')
        game_running = False

def check_win():
    global game_running
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print(f"Congratulations, {winner} wins!")
        game_running = False


#function to switch players
def switch_players():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    else:   #current player must be 'O', so set it to 'X'
        current_player = 'X'

def computer(board):
    while current_player == 'O':
        position = random.randint(0, 8)

        if board[position] == '-':
            board[position] = 'O'
            switch_players()


while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_draw(board)
    switch_players()
    computer(board)
    check_win()
    check_draw(board)

