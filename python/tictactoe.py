#!/usr/bin/python3

board=[
    ["*","*","*"],
    ["*","*","*"],
    ["*","*","*"]
]

def print_board(board):
    print("")
    for line in range(3):
        for column in range(3):
            if column > 0:
                print("|", end='')
            print(board[line][column], end='')
        print("")
        if line < 2:
            print("-----")
    print("")

def ask_user(user):
    line = int(input(user + " line ?"))
    while check_in(line):
        line = int(input(user + " line ?"))
    column = int(input(user + " column ?"))
    while check_in(column):
        column = int(input(user + " column ?"))
    return line, column

#check si on est dans le board
#ou a implementer dans le check_occupied
def check_in(position):
    if position < 0 or position > 2:
        print("out of the game !")
        return True
    return False

def check_occupied(line,column):
    if board[line][column] == "X" or board[line][column] == "O":
        print("occupied")
        return True
    return False

# fonction pour check si y'a un gagnant
def winner(board):
    #check lines
    if board[0][0] == board[0][1] == board[0][2]: winner() & exit
    elif board[1][0] == board[1][1] == board[1][2]: winner() & exit
    elif board[2][0] == board[2][1] == board[2][2]: winner() & exit
    #column
    elif board[0][0] == board[1][0] == board[2][0]: winner() & exit
    elif board[0][1] == board[1][1] == board[2][1]: winner() & exit
    elif board[0][2] == board[1][2] == board[2][2]: winner() & exit

    for line in range(3):
        for column in range(3):
            if board[line][column] != board[line][column+1]: return
            #on continue avec le suivant, de proche en proche
            #inconvénient on lit 2 fois le même element



            if board[line][column] == board[line][column] == board[line][column]:
                print("winner is " + user)
                return
    #check columns
    for column in range(3):
        for line in range(3):
            if board[column][line] == board[column][line] == board[column][line]:
                print("winner is " + user)
                return
    #check diagonale
    if board[0][0] == board[1][1] == board[2][2]:
        print("winner is " + user)
        return
    elif board[2][0] == board[1][1] == board[0][2]:
        print("winner is " + user)
        return

# fonction pour sauvegarder la partie dans un fichier
def backup():
    return

tour = 0

while tour < 9:
    if tour % 2 == 0:
        user = "X"
    else:
        user = "O"

    line, column = ask_user(user)
    while check_occupied(line, column):
        line, column = ask_user(user)
    board[line][column] = user
    print_board(board)
    winner(board)
    tour += 1