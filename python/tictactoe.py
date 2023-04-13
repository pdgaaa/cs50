#!/usr/bin/python3

#todo
#on devrait passer game en variable...
#stocker size dans game
#dimension n - 5 gagnants : revoir la fonction segment_all_equal
#IA - fonction qui pour checker si on peut gagner ou si l'adversaire peut gagner
#IA = "O"
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
            print(size*"--")
    print()

#IA - fonction pour checker si on peut gagner ou si l'adversaire peut gagner
def ask_ia(size):
    #todo
    #tester toutes les possibilités de jeu (toutes les cases libres) et pour
    #chaque possibilité check_winner mais sans modifier le board
    #random line and column
    #test avec is_segment_all_equal si on gagne

    line_temp, column_temp = random.randrange(size), random.randrange(size)
    while(check_occupied(game["board"], line_temp, column_temp))
        line_temp, column_temp = random.randrange(size), random.randrange(size)

    game["board"][line_temp][column_temp] = "O"
    if winner(game["board"], size) == "O":
        return line_temp, column_temp
    else:
        #on remet * dans le board
        #on recommence avec un autre random
        #ou bien on test toutes les possibilités et si rien ne gagne, on renvoie
        #un random
        #ca va boucler si on gagne pas, faudra un compteur de possibilités
        #FAUT TESTER TOUT, 1 par 1


    #return random.randrange(size), random.randrange(size)

def ask_user(user, size, ia):
    if ia and user == "O":
        line, column = ask_ia(size)
    else:
        #line, column = ask_ia(size)
        line, column = input(user + " line column ?").split()

    while check_in(int(line), int(column), size):
        if ia and user == "O":
            line, column = ask_ia(size)
        else:
            #line, column = ask_ia(size)
            line, column = input(user + " line column ?").split()

    return int(line), int(column)

#check si on est dans le board
#ou a implementer dans le check_occupied
def check_in(positionX, positionY, size):
    if positionX < 0 or positionX >= size or positionY < 0 or positionY >= size:
        print("out of the game !")
        return True
    return False

#check si la case est occupee
def check_occupied(board, line, column):
    if board[line][column] == "X" or board[line][column] == "O":
        print("occupied" + str(line) + str(column))
        return True
    return False

# best fonction pour check un alignement
def is_segment_all_equal(board, size, initial_line, initial_column, moveline, movecolumn):
    segment_all_equal = True
    line = initial_line
    column = initial_column
    #range avec start=1 plus elegant, a voir
    for move in range(size - 1):
        if board[line][column] != board[line+moveline][column+movecolumn]:
            segment_all_equal = False
            break
        line += moveline
        column += movecolumn
    if segment_all_equal and board[line][column] != "*":
        return board[line][column]
    return ""

# fonction pour check si y'a un gagnant
def winner(board, size):
    #check lines
    for line in range(size):
        check_line = is_segment_all_equal(board, size, line, 0, 0, 1)
        if check_line != "":
            return check_line
    
    #check column
    for column in range(size):
        check_column = is_segment_all_equal(board, size, 0, column, 1, 0)
        if check_column != "":
            return check_column

    #check diagonal \
    check_diag_backslash = is_segment_all_equal(board, size, 0, 0, 1, 1)
    if check_diag_backslash != "":
        return check_diag_backslash
    
    #check diagonal /
    check_diag_slash = is_segment_all_equal(board, size, 0, (size - 1), 1, -1)
    if check_diag_slash != "":
        return check_diag_slash

    #check board full
    #parcourir le board a la recherche d'un *
    #to do with a comprehension list ?
    for line in range(size):
        for column in range(size):
            if board[line][column] == "*":
                return ""

    #no winner and no more "*"
    return "tie"
    
# fonction pour loader une partie
def load(size):
    board = []
    if os.path.exists("ttt.pickle"):
        with open('ttt.pickle', 'rb') as handle:
            return pickle.load(handle)
    else:
        user = random.choice(['X', 'O'])
        board = [ ['*' for x in range(size)] for y in range(size) ]
        return { "board": board, "user": user }

# fonction pour sauvegarder la partie dans un fichier
def backup(board):
    with open('ttt.pickle', 'wb') as handle:
        pickle.dump(board, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":

    ia = False
    size_board = int(input("Taille du jeu : "))
    nb_players = int(input("Nombre de joueur(s) (1 ou 2): "))
    if nb_players == 1:
        ia = True

    #load an existing game or initialyze one
    game = { "board": None, "user": "undef", "size": 0, "IA": ia }
    game = load(size_board)

    while True:

        #print the board
        print_board(game["board"], size_board)
        user = game["user"]

        #ask user to play in a box
        line, column = ask_user(user, size_board, ia)
        while check_occupied(game["board"], line, column):
            line, column = ask_user(user, size_board, ia)
        game["board"][line][column] = user
        game["user"] = ("O" if user == "X" else "X")

        #check_in and check_occupied
        #plutot que de tout faire au-dessus, pas beau

        #check if there is a winner
        winner_user = winner(game["board"], size_board)
        if winner_user == "X" or winner_user == "O":
            print_board(game["board"], size_board)
            print("winner is " + winner_user)
            os.remove("ttt.pickle")         
            break
        elif winner_user == "tie":
            print_board(game["board"], size_board)
            print("tie game")
            os.remove("ttt.pickle")         
            break
        
        #backup
        backup(game)
