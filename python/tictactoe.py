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

# best fonction pour check si y'a un gagnant
def is_segment_all_equal(board, initial_line, initial_column, moveline, movecolumn):
    segment_all_equal = True
    line = initial_line
    column = initial_column
    for move in range(2):
        if board[line][column] != board[line+moveline][column+movecolumn]:
            segment_all_equal = False
            break
        line += moveline
        column += movecolumn
    if segment_all_equal and board[line][column] != "*":
        return board[line][column]
    return ""

# fonction pour check si y'a un gagnant
def winner(board):
    #check lines
    for line in range(3):
        check_line = is_segment_all_equal(board, line, 0, 0, 1)
        if check_line != "":
            return check_line
    
    #check column
    for column in range(3):
        check_column = is_segment_all_equal(board, 0, column, 1, 0)
        if check_column != "":
            return check_column

    #check diagonal \
    check_diag_backslash = is_segment_all_equal(board, 0, 0, 1, 1)
    if check_diag_backslash != "":
        return check_diag_backslash
    
    #check diagonal /
    check_diag_slash = is_segment_all_equal(board, 0, 2, 1, -1)
    if check_diag_slash != "":
        return check_diag_slash

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