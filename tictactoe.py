import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
winner = None 
current_player = "X"
game_running = True


#print the board 
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take the player input 
def player_input(board):
    inp = int(input("select a number 1-9:"))
    if board[inp - 1] == "-":
        board[inp - 1] = current_player
    else:
        print("Stupid")



#check if it is a win or tie 
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[2] != "-":
        winner = current_player
        return True
    elif board[3] == board[4] == board[5] and board[5] != "-":
        winner = current_player
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = current_player
        return True  


def check_vertical(board):
    global winner 
    if board[0] == board[3] == board[6] and board[6] != "-":
        winner = current_player
        return True
    elif board[1] == board[4] == board[7] and board[7] != "-":
        winner = current_player
        return True
    elif board[2] == board[5] == board[8] and board[8] != "-":
        winner = current_player
        return True  
    

def check_diag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[8] != "-":
        winner = current_player
        return True
    elif board[4] == board[2] == board[6] and board[6] != "-":
        winner = current_player
        return True
    

def check_win():
    global game_running
    if check_diag(board) or check_horizontal(board) or check_vertical(board):
        print_board(board)
        print(f"the winner is {winner}")
        game_running = False


def check_tie(board):
    global game_running
    if "-" not in board:
        print("it is a tie!")
        game_running = False

#switch the player 
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def computer(board):
    pos = random.randint(0 , 8)
    while board[pos] != "-":
        pos = random.randint(0 , 8)
    board[pos] = current_player


#check if it is a win or tie again 
while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    switch_player()