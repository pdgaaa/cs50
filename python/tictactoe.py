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
# pb : dans mon board initialise à *, * va être gagnant !
def winner(board):
    #check lines
    for line in range(3):
        line_all_equal = True
        for column in range(2):
            if board[line][column] != board[line][column+1]:
                line_all_equal = False
                break
        if line_all_equal and board[line][column] != "*":
            return board[line][column]

    #check column
    for column in range(3):
        column_all_equal = True
        for line in range(2):
            if board[line][column] != board[line+1][column]:
                column_all_equal = False
                break
        if column_all_equal and board[line][column] != "*":
            return board[line][column]

    #check diagonal \
    diagonal_all_equal = True
    for column in range(2):
        line = column
        if board[line][column] != board[line+1][column+1]:
            diagonal_all_equal = False
            break
    if diagonal_all_equal and board[line][column] != "*":
        return board[line][column]

    #check diagonal /
    diagonal_all_equal = True
    for line in range(2):
        column = 2-line
        if board[line][column] != board[line+1][column-1]:
            diagonal_all_equal = False
            break
    if diagonal_all_equal and board[line][column] != "*":
        return board[line][column]

    #no winner
    return ""

# fonction pour sauvegarder la partie dans un fichier
def backup():
    return

tour = 0

if __name__ == "__main__":
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
        winner_user = winner(board)
        if winner_user != "":
            print("winner is " + winner_user)
            break
        tour += 1