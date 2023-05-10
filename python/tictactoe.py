#!/usr/bin/python3

#IA = "O"
#todo
#clean un peu le code
#transférer line column dans l'objet et peut être d'autres éléments ?
#transformer des fonctions en méthode, load (@staticmethod), 
#dimension n - 5 gagnants : revoir la fonction segment_all_equal
#IA - fonction qui pour checker si on peut gagner ou si l'adversaire peut gagner
#IA2 - prévoir 2 coups plus tard - mode arbre descendant

import os
import pickle
import random

def print_board(game):
    _ = os.system('clear')
    print()
    for line in range(game.size):
        for column in range(game.size):
            if column > 0:
                print(" ", end='')
            print(game.board[line][column], end='')
        print()
    print()

#IA - fonction pour checker si on peut gagner ou si l'adversaire peut gagner
#mettre free_box (free square) dans l'objet puis le mettre à jour au fur et à mesure
#et le mettre dans une fonction à part
def ask_ia(game):
    #jouer dans un copie du board ?
    for line, column in game.free_squares():
       for player in "OX":
        game.board[line][column] = player
        if winner(game) == player:
                #attribuer un score à cette position, où ?
                #print("O va gagner, je joue à cette place")
                #temp = input("pausewinner")
                score = 10
                game.board[line][column] = "*"
                return line, column
        #regarde -1 +1 dans tous les sens
        else:
                #attribuer 0
                #continuer à chercher un bon emplacement, comment ?
                #jouer autour d'un de ses pions
                #jouer sur une ligne deja bien avancée
                score = 0
                game.board[line][column] = "*"

    return random.choice(game.free_squares())

def ask_user(game):
    if ia and user == "O":
        line, column = ask_ia(game)
    else:
        line, column = ask_ia(game)
        #line, column = input(user + " line column ? ").split()

    while check_in(int(line), int(column), game):
        if ia and user == "O":
            line, column = ask_ia(game)
        else:
            #line, column = ask_ia(size)
            line, column = input(user + " line column ?").split()

    return int(line), int(column)

#check si on est dans le board
#ou a implementer dans le check_occupied
def check_in(positionX, positionY, game):
    if positionX < 0 or positionX >= game.size or positionY < 0 or positionY >= game.size:
        print("out of the game !")
        return True
    return False

#check si la case est occupee
def check_occupied(game, line, column):
    if game.board[line][column] == "X" or game.board[line][column] == "O":
        print("occupied" + str(line) + str(column))
        temp = input("pause")
        return True
    return False

# best fonction pour check un alignement
def is_segment_all_equal(game, initial_line, initial_column, moveline, movecolumn):
    segment_all_equal = True
    line = initial_line
    column = initial_column
    #range avec start=1 plus elegant, a voir
    for move in range(game.size - 1):
        if game.board[line][column] != game.board[line+moveline][column+movecolumn]:
            segment_all_equal = False
            break
        line += moveline
        column += movecolumn
    if segment_all_equal and game.board[line][column] != "*":
        return game.board[line][column]
    return ""

# fonction pour check si y'a un gagnant
def winner(game):
    #check lines
    for line in range(game.size):
        check_line = is_segment_all_equal(game, line, 0, 0, 1)
        if check_line != "":
            return check_line
    
    #check column
    for column in range(game.size):
        check_column = is_segment_all_equal(game, 0, column, 1, 0)
        if check_column != "":
            return check_column

    #check diagonal \
    check_diag_backslash = is_segment_all_equal(game, 0, 0, 1, 1)
    if check_diag_backslash != "":
        return check_diag_backslash
    
    #check diagonal /
    #pas très beau le game.size -1 ?
    check_diag_slash = is_segment_all_equal(game, 0, (game.size - 1), 1, -1)
    if check_diag_slash != "":
        return check_diag_slash

    #check board full
    #parcourir le board a la recherche d'un *
    #to do with a comprehension list ?
    for line in range(game.size):
        for column in range(game.size):
            if game.board[line][column] == "*":
                return ""

    #no winner and no more "*"
    return "tie"
    
# fonction pour loader une partie
def load():
    if os.path.exists("ttt.pickle"):
        with open('ttt.pickle', 'rb') as handle:
            return pickle.load(handle)
    else:
        game = Game(None, "undef", size_board, ia)
        game.user = random.choice(['X', 'O'])
        game.board = [ ['*' for x in range(game.size)] for y in range(game.size) ]
        return game

# fonction pour sauvegarder la partie dans un fichier
def backup(game):
    with open('ttt.pickle', 'wb') as handle:
        pickle.dump(game, handle, protocol=pickle.HIGHEST_PROTOCOL)

class Game:
    def free_squares(self):
        free_squares = []
        for line in range(game.size):
            for column in range(game.size):
                if game.board[line][column] == "*":
                    #on est dans une case libre
                    #on enregistre cette position dans la liste
                    free_squares.append([line, column])
        return free_squares

    def __init__(self, board, user, size, ia):
        self.board = board
        self.user = user
        self.size = size
        self.ia = ia

if __name__ == "__main__":

    ia = False
    size_board = int(input("Taille du jeu : "))
    nb_players = int(input("Nombre de joueur(s) (1 ou 2): "))
    # on pourrait stocker le nb de joueur dans l'objet et si == 1, on fait appel à l'IA
    if nb_players == 1:
        ia = True

    #load an existing game or initialyze one
    game = load()

    while True:

        #print the board
        print_board(game)
        user = game.user

        #ask user to play in a box
        line, column = ask_user(game)
        while check_occupied(game, line, column):
            line, column = ask_user(game)
        game.board[line][column] = game.user
        game.user = ("O" if user == "X" else "X")

        #check_in and check_occupied
        #plutot que de tout faire au-dessus, pas beau

        #check if there is a winner
        winner_user = winner(game)
        if winner_user == "X" or winner_user == "O":
            print_board(game)
            print("winner is " + winner_user)
            print()
            os.remove("ttt.pickle")         
            break
        elif winner_user == "tie":
            print_board(game)
            print("tie game")
            print()
            os.remove("ttt.pickle")         
            break
        
        #backup
        backup(game)