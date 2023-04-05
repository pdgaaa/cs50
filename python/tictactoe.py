#!/usr/bin/python3

#todo
#dimension n < 10
#dimension n - 5 gagnants
#IA - fonction qui pour checker si on peut gagner ou si l'adversaire peut gagner
#IA2 - prévoir 2 coups plus tard - mode arbre descendant

import os
import pickle
import random

def print_board(board, size):
    _ = os.system('clear')
    print()
    for line in range(size):
        for column in range(size):
            if column > 0:
                print("|", end='')
            print(board[line][column], end='')
        print()
        if line < size-1:
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

#check si la case est occupee
def check_occupied(board, line, column):
    if board[line][column] == "X" or board[line][column] == "O":
        print("occupied")
        return True
    return False

# best fonction pour check un alignement
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

    #check board full
    #parcourir le board a la recherche d'un *
    #ou compter les X et O et si somme = 9
    for line in range(3):
        for column in range(3):
            if board[line][column] == "*":
                return ""

    #no winner and no more "*"
    return "tie"
    
# fonction pour loader une partie
def load():
    if os.path.exists("ttt.pickle"):
        with open('ttt.pickle', 'rb') as handle:
            return pickle.load(handle)
    else:
        user = random.choice(['X', 'O'])
        return { "board": [ ["*","*","*"], ["*","*","*"], ["*","*","*"] ], "user": user }

# fonction pour sauvegarder la partie dans un fichier
def backup(board):
    #open file in write mode
    #write the board
    #close file
    with open('ttt.pickle', 'wb') as handle:
        pickle.dump(board, handle, protocol=pickle.HIGHEST_PROTOCOL)

    #f = open("ttt.txt", "w")
    #for line in range(3):
        #for column in range(3):
            #f.write(board[line][column])
    #f.close()

if __name__ == "__main__":
    #load an existing game or initialyze one and print it
    game = { "board": None, "user": "undef" }
    game = load()

    while True:

        size_board = int(input("Taille du jeu : "))
        print_board(game["board"], size_board)
        user = game["user"]

        #ask user to play in a box
        line, column = ask_user(user)
        while check_occupied(game["board"], line, column):
            line, column = ask_user(user)
        game["board"][line][column] = user
        game["user"] = ("O" if user == "X" else "X")

        #check if there is a winner
        winner_user = winner(game["board"])
        if winner_user == "X" or winner_user == "O":
            print_board(game["board"])
            print("winner is " + winner_user)
            os.remove("ttt.pickle")         
            break
        elif winner_user == "tie":
            print_board(game["board"])
            print("tie game")
            os.remove("ttt.pickle")         
            break
        
        #backup
        backup(game)
