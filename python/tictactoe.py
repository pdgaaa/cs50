#!/usr/bin/python3

import os
import pickle

board=[
    ["*","*","*"],
    ["*","*","*"],
    ["*","*","*"]
]

def print_board(board):
    _=os.system('clear')
    print()
    for line in range(3):
        for column in range(3):
            if column > 0:
                print("|", end='')
            print(board[line][column], end='')
        print()
        if line < 2:
            print("-----")
    print()

def ask_user(user):
    line, column = input(user + " line column ?").split()
    while check_in(int(line), int(column)):
        line, column = input(user + " line column ?").split()
    #column = int(input(user + " column ?"))
    #while check_in(column):
        #column = int(input(user + " column ?"))
    return int(line), int(column)

#check si on est dans le board
#ou a implementer dans le check_occupied
def check_in(positionX, positionY):
    if positionX < 0 or positionX > 2 or positionY < 0 or positionY > 2:
        print("out of the game !")
        return True
    return False

def check_occupied(line, column):
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
    
# fonction pour loader une partie
def load():
    with open('ttt.pickle', 'rb') as handle:
        return pickle.load(handle)

# fonction pour sauvegarder la partie dans un fichier
def backup(board):
    #open file in write mode
    #write the board
    #close file
    with open('ttt.pickle', 'wb') as handle:
        pickle.dump(board, handle, protocol=pickle.HIGHEST_PROTOCOL)

    f = open("ttt.txt", "w")
    for line in range(3):
        for column in range(3):
            f.write(board[line][column])
    f.close()

#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read()) 
    #return

if __name__ == "__main__":
    tour = 0
    while True:
        if tour > 9:
            break
        if tour % 2 == 0:
            user = "X"
        else:
            user = "O"
        
        #write a function ou ameliore une pour sortir du programme quand le jeu est fini
        #if toutes les cases sont occupées, on sort
        #a qui c'est le tour

        board = load()
        print_board(board)

        #ask user to play in a box
        line, column = ask_user(user)
        while check_occupied(line, column):
            line, column = ask_user(user)
        board[line][column] = user

        print_board(board)
        winner_user = winner(board)
        if winner_user != "":
            print("winner is " + winner_user)
            break
        if tour == 8:
            print("match nul")
        backup(board)
        tour += 1